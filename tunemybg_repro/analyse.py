"""Aggregate per-run outputs into comparable tables and a Markdown report."""

from __future__ import annotations

import json
import math
from collections import Counter
from difflib import SequenceMatcher
from itertools import combinations
from pathlib import Path
from typing import Any

import pandas as pd


def _load_runs(exp_dir: Path) -> list[dict[str, Any]]:
    runs = []
    for run_dir in sorted(exp_dir.glob("run_*")):
        meta_path = run_dir / "meta.json"
        if not meta_path.exists():
            continue
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        final = None
        if (run_dir / "final.json").exists():
            final = json.loads((run_dir / "final.json").read_text(encoding="utf-8"))
        runs.append({"experiment": exp_dir.name, "run_id": meta["run_id"], "meta": meta,
                     "final": final, "dir": run_dir})
    return runs


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """Wilson score 95% interval for a proportion."""
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return (round(max(0.0, centre - half), 3), round(min(1.0, centre + half), 3))


def _entropy(counter: Counter) -> float:
    n = sum(counter.values())
    return round(-sum(c / n * math.log2(c / n) for c in counter.values() if c), 4) if n else 0.0


def _norm(s: Any) -> str:
    return " ".join(str(s or "").lower().split())


def _sum_usage(meta: dict, keys: tuple[str, ...]) -> int | None:
    total, seen = 0, False
    for t in meta.get("turns", []):
        for k in keys:
            val = (t.get("usage") or {}).get(k)
            if isinstance(val, (int, float)):
                total += int(val)
                seen = True
                break
    return total if seen else None


# USD per million tokens: (input, cache write, cache read, output). Output includes thinking.
PRICING = {
    "claude-opus-5": (5.0, 6.25, 0.5, 25.0),
    "claude-sonnet-5": (3.0, 3.75, 0.3, 15.0),
    "claude-haiku-4-5": (1.0, 1.25, 0.1, 5.0),
}


def _est_cost(meta: dict) -> float | None:
    price = PRICING.get(str(meta.get("backend", {}).get("model")))
    if not price:
        return None
    inp = cw = cr = out = 0
    for t in meta.get("turns", []):
        u = t.get("usage") or {}
        inp += u.get("input_tokens") or 0
        cw += u.get("cache_creation_input_tokens") or 0
        cr += u.get("cache_read_input_tokens") or 0
        out += u.get("output_tokens") or 0
    return round((inp * price[0] + cw * price[1] + cr * price[2] + out * price[3]) / 1e6, 4)


def build_tables(exp_dirs: list[Path], package: dict[str, Any]) -> dict[str, pd.DataFrame]:
    inv = {i["parameter_key"]: i for i in package["decision_inventory"]["items"]}
    step_keys = [s["key"] for s in package["analysis_workflow"]["steps"]]

    run_rows, dec_rows, step_rows, rec_rows = [], [], [], []
    for exp_dir in exp_dirs:
        for r in _load_runs(exp_dir):
            meta, final = r["meta"], r["final"]
            val = meta.get("validation") or {}
            # The app holds nothing for a rejected conversation, so its JSON is not analysed.
            if not val.get("app_accepted"):
                final = None
            fp = meta.get("first_pass") or {   # runs recorded before the correction loop existed
                "json_extracted": meta.get("json_extracted"),
                "extraction_method": meta.get("extraction_method"),
                "fully_compliant": val.get("fully_compliant"), "sections": val.get("sections")}
            # Compare first pass with the accepted version only when both parsed; an unparseable
            # first pass has no decisions to compare and must not count as "changed".
            rd: dict[str, Any] = {}
            fp_path = r["dir"] / "final_firstpass.json"
            if meta.get("n_repairs") and fp_path.exists() and final is not None:
                from .extract import decision_diff
                rd = decision_diff(json.loads(fp_path.read_text(encoding="utf-8")), final)
            row: dict[str, Any] = {
                "experiment": r["experiment"], "run_id": r["run_id"], "status": meta.get("status"),
                "error": meta.get("error"), "model": meta.get("backend", {}).get("model"),
                "wall_time_s": meta.get("wall_time_s"),
                "est_cost_usd": _est_cost(meta),
                "input_tokens_total": _sum_usage(meta, ("prompt_tokens", "input_tokens",
                                                        "promptTokenCount", "prompt_eval_count")),
                "output_tokens_total": _sum_usage(meta, ("completion_tokens", "output_tokens",
                                                         "candidatesTokenCount", "eval_count")),
                "json_extracted": meta.get("json_extracted"),
                "extraction_method": meta.get("extraction_method"),
                "fully_compliant": val.get("fully_compliant"),
                "schema_score": val.get("schema_score"),
                "n_violations": len(val.get("violations", [])) if val else None,
                "violations": " | ".join(val.get("violations", [])) if val else None,
                "first_pass_json": fp.get("json_extracted"),
                "first_pass_method": fp.get("extraction_method"),
                "first_pass_compliant": fp.get("fully_compliant"),
                "first_pass_sections": ", ".join(fp.get("sections") or []) if fp else None,
                "n_repairs": meta.get("n_repairs", 0),
                # What the real app does: invalid JSON gets "Paste a valid JSON response from AI."
                # and no correction prompt, so it is a dead end regardless of any harness repair.
                "app_outcome": meta.get("app_outcome") if meta.get("status") == "completed" else None,
                "app_accepted": val.get("app_accepted"),
                "prompt_only_violations": " | ".join(val.get("prompt_only_violations") or []) if val else None,
                "n_prompt_only_violations": len(val.get("prompt_only_violations") or []) if val else None,
                "repair_rows_changed": rd.get("n_rows_changed"),
                "repair_decisions_changed": rd.get("n_decision_changed"),
                "repair_decisions_changed_keys": ";".join(rd.get("decision_changed") or []),
                "repair_profile_focus_changed": rd.get("profile_focus_changed"),
            }
            if final:
                decs = [d for d in final.get("parameter_decisions", []) if isinstance(d, dict)]
                dc = Counter(d.get("decision") for d in decs)
                pr = final.get("profile_recommendation") or {}
                ms = final.get("meal_strategy_summary") or {}
                recs = [x for x in final.get("recommendations", []) if isinstance(x, dict)]
                primary = recs[0] if recs else {}
                row.update({
                    "n_change": dc.get("change", 0), "n_keep": dc.get("keep", 0),
                    "n_verify": dc.get("verify", 0),
                    "changed_keys": ";".join(sorted(d["parameter_key"] for d in decs
                                                    if d.get("decision") == "change"
                                                    and d.get("parameter_key"))),
                    "profile_rec_focus": pr.get("focus"), "profile_rec_decision": pr.get("decision"),
                    "profile_rec_confidence": pr.get("confidence"),
                    "profile_rec_text": pr.get("recommendation"),
                    "meal_confidence": ms.get("confidence"),
                    "meal_n_exceptions": len(ms.get("exceptions") or [])
                    if isinstance(ms.get("exceptions"), list) else None,
                    "meal_suggestion": ms.get("suggestion"),
                    "n_recommendations": len(recs),
                    "primary_rec_area": primary.get("area"), "primary_rec_title": primary.get("title"),
                    "primary_rec_priority": primary.get("priority"),
                    "rec_areas": ";".join(str(x.get("area")) for x in recs),
                    "n_issues": len(final.get("issues") or []),
                    "n_strengths": len(final.get("strengths") or []),
                    "n_implementation_steps": len(final.get("implementation_steps") or []),
                    "summary": final.get("summary"),
                    "summary_chars": len(str(final.get("summary") or "")),
                })
                for d in decs:
                    key = d.get("parameter_key")
                    dec_rows.append({"experiment": r["experiment"], "run_id": r["run_id"],
                                     "parameter_key": key,
                                     "category": inv.get(key, {}).get("category"),
                                     "in_inventory": key in inv,
                                     "current_value": d.get("current_value"),
                                     "decision": d.get("decision"),
                                     "suggested_value": d.get("suggested_value"),
                                     "rationale": d.get("rationale")})
                for s in final.get("analysis_steps", []):
                    if isinstance(s, dict):
                        step_rows.append({"experiment": r["experiment"], "run_id": r["run_id"],
                                          "step": s.get("key"), "status": s.get("status"),
                                          "confidence": s.get("confidence"),
                                          "in_workflow": s.get("key") in step_keys})
                for rank, x in enumerate(recs, start=1):
                    rec_rows.append({"experiment": r["experiment"], "run_id": r["run_id"],
                                     "rank": rank, "area": x.get("area"), "title": x.get("title"),
                                     "priority": x.get("priority"),
                                     "suggested_change": json.dumps(x.get("suggested_change"),
                                                                    ensure_ascii=False)})
            run_rows.append(row)

    runs = pd.DataFrame(run_rows)
    decisions = pd.DataFrame(dec_rows)
    steps = pd.DataFrame(step_rows)
    recs = pd.DataFrame(rec_rows)

    # Per-parameter agreement across runs (within each experiment)
    agree_rows = []
    if not decisions.empty:
        for (exp, key), g in decisions.groupby(["experiment", "parameter_key"], sort=False):
            c = Counter(g["decision"])
            modal, modal_n = c.most_common(1)[0]
            sugg = Counter(_norm(s) for s, d in zip(g["suggested_value"], g["decision"])
                           if d == "change")
            lo, hi = wilson(c.get("change", 0), len(g))
            agree_rows.append({"experiment": exp, "parameter_key": key,
                               "category": inv.get(key, {}).get("category"),
                               "current_value": inv.get(key, {}).get("current_value"),
                               "n_runs": len(g), "modal_decision": modal,
                               "agreement": round(modal_n / len(g), 3),
                               "change_rate": round(c.get("change", 0) / len(g), 3),
                               "change_rate_ci95": f"{lo}–{hi}",
                               "entropy_bits": _entropy(c),
                               "n_change": c.get("change", 0), "n_keep": c.get("keep", 0),
                               "n_verify": c.get("verify", 0),
                               "distinct_suggested_values": len(sugg),
                               "suggested_values": " | ".join(f"{v} x{n}" for v, n in sugg.most_common())})
    agreement = pd.DataFrame(agree_rows)

    step_agree_rows = []
    if not steps.empty:
        for (exp, step), g in steps.groupby(["experiment", "step"], sort=False):
            sc, cc = Counter(g["status"]), Counter(g["confidence"])
            step_agree_rows.append({"experiment": exp, "step": step, "n_runs": len(g),
                                    "modal_status": sc.most_common(1)[0][0],
                                    "status_agreement": round(sc.most_common(1)[0][1] / len(g), 3),
                                    "modal_confidence": cc.most_common(1)[0][0],
                                    "confidence_agreement": round(cc.most_common(1)[0][1] / len(g), 3),
                                    "status_counts": dict(sc), "confidence_counts": dict(cc)})
    step_agreement = pd.DataFrame(step_agree_rows)

    # Pairwise similarity of free text and of the change-set between runs
    sim_rows = []
    if not runs.empty:
        for exp, g in runs[runs["json_extracted"] == True].groupby("experiment"):  # noqa: E712
            recs_g = g.to_dict("records")
            for a, b in combinations(recs_g, 2):
                set_a = set(filter(None, str(a.get("changed_keys") or "").split(";")))
                set_b = set(filter(None, str(b.get("changed_keys") or "").split(";")))
                union = set_a | set_b
                sim_rows.append({
                    "experiment": exp, "run_a": a["run_id"], "run_b": b["run_id"],
                    "summary_similarity": round(SequenceMatcher(None, _norm(a.get("summary")),
                                                                _norm(b.get("summary"))).ratio(), 3),
                    "profile_rec_similarity": round(SequenceMatcher(
                        None, _norm(a.get("profile_rec_text")),
                        _norm(b.get("profile_rec_text"))).ratio(), 3),
                    "meal_suggestion_similarity": round(SequenceMatcher(
                        None, _norm(a.get("meal_suggestion")),
                        _norm(b.get("meal_suggestion"))).ratio(), 3),
                    "change_set_jaccard": round(len(set_a & set_b) / len(union), 3) if union else 1.0,
                    "same_primary_rec_area": a.get("primary_rec_area") == b.get("primary_rec_area"),
                    "same_profile_focus": a.get("profile_rec_focus") == b.get("profile_rec_focus"),
                })
    similarity = pd.DataFrame(sim_rows)

    # Between-model agreement on the modal decision per setting (only meaningful with >1 experiment)
    bm_rows = []
    if not agreement.empty and agreement["experiment"].nunique() > 1:
        for key, g in agreement.groupby("parameter_key", sort=False):
            modes = Counter(g["modal_decision"])
            rates = {r["experiment"]: r["change_rate"] for _, r in g.iterrows()}
            bm_rows.append({"parameter_key": key, "n_models": len(g),
                            "models_modal_change": int((g["modal_decision"] == "change").sum()),
                            "models_modal_keep": int((g["modal_decision"] == "keep").sum()),
                            "models_modal_verify": int((g["modal_decision"] == "verify").sum()),
                            "modal_agreement_across_models": round(modes.most_common(1)[0][1] / len(g), 3),
                            "change_rate_min": float(g["change_rate"].min()),
                            "change_rate_max": float(g["change_rate"].max()),
                            "change_rate_by_model": json.dumps(rates)})
    between_models = pd.DataFrame(bm_rows)

    # App outcome proportions with Wilson intervals, per experiment
    oc_rows = []
    if not runs.empty and "app_outcome" in runs:
        for exp, g in runs.groupby("experiment"):
            done = g[g["app_outcome"].notna()]
            n = len(done)
            for outcome in ("accepted_first_pass", "accepted_after_correction", "rejected_no_prompt",
                            "rejected_schema_stop", "rejected_after_correction"):
                k = int((done["app_outcome"] == outcome).sum())
                lo, hi = wilson(k, n)
                oc_rows.append({"experiment": exp, "outcome": outcome, "k": k, "n": n,
                                "proportion": round(k / n, 3) if n else None, "ci95_low": lo, "ci95_high": hi})
    outcome_ci = pd.DataFrame(oc_rows)

    return {"runs": runs, "decisions_long": decisions, "decision_agreement": agreement,
            "steps_long": steps, "step_agreement": step_agreement,
            "recommendations_long": recs, "pairwise_similarity": similarity,
            "between_models": between_models, "app_outcome_ci": outcome_ci}


def _sub(df: pd.DataFrame, exp: str) -> pd.DataFrame:
    """Rows for one experiment; tolerates an empty table with no columns."""
    return df[df["experiment"] == exp] if "experiment" in df.columns else df


def _dist(series: pd.Series) -> str:
    c = Counter(series.dropna().astype(str))
    return ", ".join(f"{k} ×{n}" for k, n in c.most_common()) or "—"


def write_report(tables: dict[str, pd.DataFrame], out_dir: Path) -> Path:
    runs, agreement = tables["runs"], tables["decision_agreement"]
    sim, steps_agree = tables["pairwise_similarity"], tables["step_agreement"]
    lines = ["# TuneMyBG reproducibility report", ""]
    for exp, g in runs.groupby("experiment"):
        n = len(g)
        ok = g[g["json_extracted"] == True]  # noqa: E712
        ag = _sub(agreement, exp)
        sg = _sub(sim, exp)
        model = g["model"].dropna().iloc[0] if g["model"].notna().any() else "?"
        lines += [f"## Experiment `{exp}` — model `{model}`", "",
                  f"- Runs: {n} (completed {int((g['status'] == 'completed').sum())}, "
                  f"failed {int((g['status'] == 'failed').sum())})",
                  f"- Final JSON extracted: {len(ok)}/{n} "
                  f"(methods: {_dist(g['extraction_method'])})",
                  f"- Fully schema-compliant: {int(ok['fully_compliant'].fillna(False).sum())}/{len(ok)}; "
                  f"mean schema score {ok['schema_score'].mean():.3f}" if len(ok) else
                  "- Fully schema-compliant: n/a",
                  f"- Mean wall time per run: {g['wall_time_s'].mean():.0f}s"]
        if g["est_cost_usd"].notna().any():
            lines += [f"- Estimated API cost: ${g['est_cost_usd'].sum():.2f} total, "
                      f"${g['est_cost_usd'].mean():.2f} per run (list prices; output includes thinking)"]
        if "app_outcome" in g:
            oc = Counter(g["app_outcome"].dropna())
            nc = int(sum(oc.values()))
            lines += [f"- **App outcome (as the app behaves), over {nc} completed runs:** accepted first time {oc.get('accepted_first_pass', 0)}; "
                      f"accepted after the repair prompt {oc.get('accepted_after_correction', 0)}; "
                      f"invalid JSON, no prompt offered {oc.get('rejected_no_prompt', 0)}; "
                      f"schema stop, no prompt offered {oc.get('rejected_schema_stop', 0)}; "
                      f"still rejected after repair {oc.get('rejected_after_correction', 0)}"]
            acc = g[g["app_accepted"] == True]  # noqa: E712
            if len(acc):
                npo = int((acc["n_prompt_only_violations"].fillna(0) > 0).sum())
                pov = Counter(x.split(":")[0].strip() for v in acc["prompt_only_violations"].dropna()
                              for x in str(v).split(" | ") if x.strip())
                lines += [f"- **Accepted by the app but breaking Prompt 4's own rules:** {npo}/{len(acc)} accepted runs; "
                          f"commonest: " + (", ".join(f"{k} ×{c}" for k, c in pov.most_common(5)) or "—")]
        if "first_pass_compliant" in g:
            fp_ok = int(g["first_pass_compliant"].fillna(False).astype(bool).sum())
            fp_json = int(g["first_pass_json"].fillna(False).astype(bool).sum())
            repaired = g[g["n_repairs"].fillna(0) > 0]
            lines += [f"- **App loop:** first pass parseable {fp_json}/{n}, first pass compliant "
                      f"{fp_ok}/{n}; correction prompt sent in {len(repaired)} run(s); compliant "
                      f"after correction {int(g['fully_compliant'].fillna(False).astype(bool).sum())}/{n}"]
            if len(repaired):
                secs = Counter(s.strip() for v in repaired["first_pass_sections"].dropna()
                               for s in str(v).split(",") if s.strip())
                comparable = repaired[repaired["repair_decisions_changed"].notna()]
                n_unparse = int((repaired["first_pass_json"].fillna(False).astype(bool) == False).sum())  # noqa: E712
                lines += [f"- Sections the app would flag: "
                          + (", ".join(f"{k} ×{c}" for k, c in secs.most_common(12)) or "—")
                          + (f"; first pass not valid JSON at all ×{n_unparse}" if n_unparse else ""),
                          f"- Corrections that changed a decision (not just format): "
                          f"{int((comparable['repair_decisions_changed'] > 0).sum())}/{len(comparable)} comparable; "
                          f"changed profile focus: "
                          f"{int(comparable['repair_profile_focus_changed'].fillna(False).astype(bool).sum())}/{len(comparable)}"
                          + (f" ({n_unparse} unparseable first pass(es) not comparable)" if n_unparse else "")]
        if len(ok):
            lines += [f"- Decisions per run — change: {_dist(ok['n_change'])}; "
                      f"keep: {_dist(ok['n_keep'])}; verify: {_dist(ok['n_verify'])}",
                      f"- profile_recommendation focus: {_dist(ok['profile_rec_focus'])}",
                      f"- profile_recommendation decision: {_dist(ok['profile_rec_decision'])}; "
                      f"confidence: {_dist(ok['profile_rec_confidence'])}",
                      f"- Primary recommendation area: {_dist(ok['primary_rec_area'])}; "
                      f"priority: {_dist(ok['primary_rec_priority'])}",
                      f"- Meal strategy confidence: {_dist(ok['meal_confidence'])}; "
                      f"exceptions: {_dist(ok['meal_n_exceptions'])}"]
        if len(ag):
            lines += [f"- **Decision stability index** (mean per-parameter agreement): "
                      f"{ag['agreement'].mean():.3f}; parameters with unanimous decisions: "
                      f"{int((ag['agreement'] == 1.0).sum())}/{len(ag)}"]
        if len(sg):
            lines += [f"- Pairwise change-set Jaccard: mean {sg['change_set_jaccard'].mean():.3f}; "
                      f"same primary area {sg['same_primary_rec_area'].mean():.0%}; "
                      f"same profile focus {sg['same_profile_focus'].mean():.0%}",
                      f"- Pairwise text similarity — summary {sg['summary_similarity'].mean():.3f}, "
                      f"profile recommendation {sg['profile_rec_similarity'].mean():.3f}, "
                      f"meal suggestion {sg['meal_suggestion_similarity'].mean():.3f}"]
        lines.append("")
        if len(ag):
            lines += ["### Parameter decision agreement", "",
                      "| parameter_key | current | modal | agreement | change | keep | verify | suggested values (when change) |",
                      "|---|---|---|---|---|---|---|---|"]
            for _, a in ag.sort_values(["agreement", "parameter_key"]).iterrows():
                lines.append(f"| {a['parameter_key']} | {a['current_value']} | {a['modal_decision']} | "
                             f"{a['agreement']:.2f} | {a['n_change']} | {a['n_keep']} | {a['n_verify']} | "
                             f"{a['suggested_values'] or ''} |")
            lines.append("")
        sa = _sub(steps_agree, exp)
        if len(sa):
            lines += ["### Analysis step status / confidence agreement", "",
                      "| step | modal status | agreement | modal confidence | agreement |",
                      "|---|---|---|---|---|"]
            for _, s in sa.iterrows():
                lines.append(f"| {s['step']} | {s['modal_status']} | {s['status_agreement']:.2f} | "
                             f"{s['modal_confidence']} | {s['confidence_agreement']:.2f} |")
            lines.append("")
        lines += ["### Per-run overview", "",
                  "| run | status | 1st pass JSON | 1st pass OK | repairs | final OK | score | change/keep/verify | profile focus | primary rec | time (s) |",
                  "|---|---|---|---|---|---|---|---|---|---|---|"]
        for _, r in g.iterrows():
            ckv = (f"{int(r['n_change'])}/{int(r['n_keep'])}/{int(r['n_verify'])}"
                   if pd.notna(r.get("n_change")) else "—")
            score = f"{r['schema_score']:.2f}" if pd.notna(r.get("schema_score")) else "—"
            nrep = int(r["n_repairs"]) if pd.notna(r.get("n_repairs")) else 0
            lines.append(f"| {r['run_id']} | {r['status']} | {r.get('first_pass_method') or '—'} | "
                         f"{r.get('first_pass_compliant')} | {nrep} | {r['fully_compliant']} | {score} | "
                         f"{ckv} | {r.get('profile_rec_focus') or '—'} | "
                         f"{(r.get('primary_rec_title') or '—')} | {r['wall_time_s']} |")
        lines.append("")
        failed = g[g["status"] == "failed"]
        if len(failed):
            lines += ["### Failures", ""] + [f"- {r['run_id']}: {r['error']}" for _, r in failed.iterrows()] + [""]
        bad = ok[ok["fully_compliant"] == False]  # noqa: E712
        if len(bad):
            lines += ["### Schema violations remaining after correction", ""] + [
                f"- {r['run_id']}: {r['violations']}" for _, r in bad.iterrows()] + [""]
    report = out_dir / "report.md"
    report.write_text("\n".join(lines), encoding="utf-8")
    return report


def analyse(exp_dirs: list[Path], package: dict[str, Any], out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    tables = build_tables(exp_dirs, package)
    for name, df in tables.items():
        df.to_csv(out_dir / f"{name}.csv", index=False)
    return write_report(tables, out_dir)
