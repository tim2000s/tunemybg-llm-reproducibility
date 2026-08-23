"""Plain-English per-model summary: what every run kept, what was changed, how often,
the range of suggested values, and how they compare with AndroidAPS code defaults."""

from __future__ import annotations

import json
import re
import statistics
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from .aaps_defaults import AAPS_SOURCE, COMPONENT_DEFAULTS, PROFILE_NOTES, default_for, note_for

_NUM = re.compile(r"^\s*(-?\d+(?:\.\d+)?)\s*(.*?)\s*$")


def parse_value(s: Any) -> tuple[float | None, str]:
    """'0.6 U/h' -> (0.6, 'U/h'); 'true' -> (None, 'true'); '95-110 mg/dL' -> (None, text)."""
    if s is None:
        return None, "null"
    s = str(s).strip()
    m = _NUM.match(s)
    if m and not re.match(r"^\d+\s*-\s*\d+", s):
        return float(m.group(1)), m.group(2)
    return None, s


def parse_composite(s: Any) -> dict[str, str]:
    """'a=1 U/h; b=2 U' -> {'a': '1 U/h', 'b': '2 U'}; a non-composite string -> {'': s}."""
    if s is None:
        return {}
    s = str(s)
    if "=" not in s:
        return {"": s.strip()}
    out = {}
    for part in s.split(";"):
        if "=" in part:
            k, v = part.split("=", 1)
            out[k.strip()] = v.strip()
    return out


def _same(a: str, b: str) -> bool:
    na, ua = parse_value(a)
    nb, ub = parse_value(b)
    if na is not None and nb is not None:
        return abs(na - nb) < 1e-9
    return a.strip().lower() == b.strip().lower()


def _fmt(v: float) -> str:
    return f"{v:g}"


def _load(exp_dir: Path) -> list[dict[str, Any]]:
    runs = []
    for d in sorted(exp_dir.glob("run_*")):
        if (d / "meta.json").exists() and (d / "final.json").exists():
            meta = json.loads((d / "meta.json").read_text(encoding="utf-8"))
            if meta.get("status") != "completed":
                continue
            runs.append({"meta": meta, "final": json.loads((d / "final.json").read_text(encoding="utf-8"))})
    return runs


def analyse_experiment(exp_dir: Path, package: dict[str, Any]) -> dict[str, Any]:
    runs = _load(exp_dir)
    n = len(runs)
    inv = package["decision_inventory"]["items"]
    exp_meta = json.loads((exp_dir / "experiment.json").read_text(encoding="utf-8"))

    # component-level records: (parameter_key, component_key) -> {"current", "unit", "changes": [values]}
    comp: dict[tuple[str, str], dict[str, Any]] = {}
    for item in inv:
        if item["category"] == "profile":
            comp[(item["parameter_key"], "")] = {"label": item["label"], "current": item["current_value"],
                                                  "changes": [], "runs_changed": set()}
        else:
            for c in item.get("components", []):
                comp[(item["parameter_key"], c["key"])] = {
                    "label": f"{item['label']} / {c['key']}", "current": c["current_value"],
                    "changes": [], "runs_changed": set()}
    row_changed: dict[str, int] = Counter()
    for run in runs:
        rid = run["meta"]["run_id"]
        for d in run["final"].get("parameter_decisions", []):
            if not isinstance(d, dict) or d.get("decision") != "change":
                continue
            pk = d.get("parameter_key")
            row_changed[pk] += 1
            item = next((i for i in inv if i["parameter_key"] == pk), None)
            if item is None:
                continue
            if item["category"] == "profile":
                rec = comp[(pk, "")]
                sv = str(d.get("suggested_value"))
                if not _same(sv, str(rec["current"])):
                    rec["changes"].append(sv)
                    rec["runs_changed"].add(rid)
            else:
                sugg = parse_composite(d.get("suggested_value"))
                for c in item.get("components", []):
                    rec = comp[(pk, c["key"])]
                    sv = sugg.get(c["key"])
                    if sv is None or rec["current"] is None:
                        continue
                    if not _same(sv, str(rec["current"])):
                        rec["changes"].append(sv)
                        rec["runs_changed"].add(rid)

    changed_rows, kept_rows = [], []
    for (pk, ck), rec in comp.items():
        k = len(rec["runs_changed"])
        cur_num, unit = parse_value(rec["current"])
        nums = [parse_value(v)[0] for v in rec["changes"]]
        nums = [x for x in nums if x is not None]
        texts = Counter(v.strip().lower() for v in rec["changes"] if parse_value(v)[0] is None)
        entry = {"parameter_key": pk, "component": ck, "label": rec["label"], "current": rec["current"],
                 "unit": unit, "default": default_for(ck) if ck else "—", "note": note_for(ck) if ck
                 else PROFILE_NOTES.get(pk, ""), "n_changed": k, "pct": round(100 * k / n) if n else 0,
                 "n_runs": n}
        if k == 0:
            kept_rows.append(entry)
            continue
        if nums:
            c = Counter(nums)
            mode, mode_n = c.most_common(1)[0]
            entry.update({"min": min(nums), "max": max(nums), "median": statistics.median(nums),
                          "mode": mode, "mode_n": mode_n, "distinct": len(c),
                          "direction": ("lower" if cur_num is not None and max(nums) < cur_num else
                                        "higher" if cur_num is not None and min(nums) > cur_num else
                                        "mixed")})
        if texts:
            entry["text_values"] = dict(texts)
        changed_rows.append(entry)
    changed_rows.sort(key=lambda e: (-e["n_changed"], e["parameter_key"]))

    # headline
    focus = Counter(r["final"].get("profile_recommendation", {}).get("focus") for r in runs)
    pdec = Counter(r["final"].get("profile_recommendation", {}).get("decision") for r in runs)
    primary = Counter()
    primary_area = Counter()
    for r in runs:
        recs = [x for x in r["final"].get("recommendations", []) if isinstance(x, dict)]
        if recs:
            primary[recs[0].get("title")] += 1
            primary_area[recs[0].get("area")] += 1
    first_ok = sum(1 for r in runs if (r["meta"].get("first_pass") or {}).get("fully_compliant"))
    repaired = sum(1 for r in runs if r["meta"].get("n_repairs"))
    final_ok = sum(1 for r in runs if (r["meta"].get("validation") or {}).get("fully_compliant"))
    # app-faithful outcomes from meta (set by the runner or revalidate.py)
    outcomes = Counter()
    for d in sorted(exp_dir.glob("run_*")):
        mp = d / "meta.json"
        if mp.exists():
            m = json.loads(mp.read_text(encoding="utf-8"))
            if m.get("status") == "completed":
                outcomes[m.get("app_outcome")] += 1
    dead_end = outcomes.get("rejected_no_prompt", 0) + outcomes.get("rejected_schema_stop", 0)
    n_change_per_run = [sum(1 for d in r["final"].get("parameter_decisions", [])
                            if isinstance(d, dict) and d.get("decision") == "change") for r in runs]
    return {"experiment": exp_dir.name, "model": exp_meta.get("backend", {}).get("model"),
            "backend": exp_meta.get("backend", {}), "n": n, "first_ok": first_ok, "repaired": repaired,
            "final_ok": final_ok, "dead_end": dead_end, "outcomes": outcomes,
            "changed": changed_rows, "kept": kept_rows,
            "row_changed": row_changed, "focus": focus, "pdec": pdec, "primary": primary,
            "primary_area": primary_area, "n_change_per_run": n_change_per_run,
            "n_inventory": len(inv)}


def _pct(k: int, n: int) -> str:
    return f"{k}/{n} ({round(100 * k / n) if n else 0}%)"


def _range_text(e: dict[str, Any]) -> str:
    parts = []
    if "min" in e:
        u = f" {e['unit']}" if e["unit"] else ""
        if e["min"] == e["max"]:
            parts.append(f"always {_fmt(e['min'])}{u}")
        else:
            parts.append(f"{_fmt(e['min'])}–{_fmt(e['max'])}{u}; most often {_fmt(e['mode'])}{u} "
                         f"({e['mode_n']} of {e['n_changed']}); {e['distinct']} distinct values")
    if e.get("text_values"):
        parts.append(", ".join(f"{v} ×{c}" for v, c in e["text_values"].items()))
    return "; ".join(parts) or "—"


def _group_kept(kept: list[dict[str, Any]]) -> list[str]:
    groups: dict[str, list[str]] = defaultdict(list)
    for e in kept:
        pk = e["parameter_key"]
        if pk.startswith("profile."):
            area = pk.split(".")[1]
            seg = pk.split(".")[2].replace("_", ":") if pk.count(".") == 2 else ""
            groups[area].append(f"{seg} {e['current']}".strip())
        else:
            groups["AAPS " + pk.split(".")[-1]].append(f"{e['component']} = {e['current']}")
    names = {"basal": "Basal rates", "cr": "Carb ratios", "isf": "Insulin sensitivity", "target": "Targets",
             "dia": "DIA"}
    return [f"**{names.get(g, g)}**: " + "; ".join(v) for g, v in groups.items()]


def write_summary(results: list[dict[str, Any]], package: dict[str, Any], out_path: Path) -> Path:
    meta = package["metadata"]
    tl = package["telemetry"]
    gs = tl["glucose_summary"]
    L = ["# TuneMyBG LLM reproducibility — plain-English summary", "",
         f"Package generated {meta['generated_at'][:10]} covering {tl['period_start'][:10]} to "
         f"{tl['period_end'][:10]} ({meta['range_days']} days). Glucose: mean {gs['average_glucose']} mg/dL, "
         f"time in range {gs['time_in_range_percent']}%, below range {gs['time_below_range_percent']}%, "
         f"CV {gs['coefficient_of_variation_percent']}%. Carb entries logged: "
         f"{tl['treatment_summary']['carb_entries']}.", "",
         f"Each run is a brand-new conversation: package attached with Prompt 1, then Prompts 2, 3 and 4 "
         f"in turn, then the app's correction prompt once if the JSON failed the app's checks. "
         f"AAPS defaults are from {AAPS_SOURCE}.", ""]
    for r in results:
        n = r["n"]
        L += [f"## {r['model']} — {n} runs (`{r['experiment']}`)", ""]
        eff = r["backend"].get("reasoning_effort") or r["backend"].get("effort")
        if eff:
            L += [f"Reasoning effort: {eff}.", ""]
        L += ["### At a glance", "",
              f"- App outcome over {sum(r['outcomes'].values())} completed runs: accepted first time "
              f"{r['outcomes'].get('accepted_first_pass', 0)}; accepted after the repair prompt "
              f"{r['outcomes'].get('accepted_after_correction', 0)}; invalid JSON with no prompt offered "
              f"{r['outcomes'].get('rejected_no_prompt', 0)}; schema stop with no prompt offered "
              f"{r['outcomes'].get('rejected_schema_stop', 0)}; still rejected after repair "
              f"{r['outcomes'].get('rejected_after_correction', 0)}. Dead ends (no way forward in the app): "
              f"{r['dead_end']}.",
              f"- Strict compliance with Prompt 4's own rules (which the app does not fully check): "
              f"{_pct(r['first_ok'], n)} of runs first time.",
              f"- Settings changed per run: {min(r['n_change_per_run']) if n else 0}–"
              f"{max(r['n_change_per_run']) if n else 0} of {r['n_inventory']} "
              f"(most runs: {Counter(r['n_change_per_run']).most_common(1)[0][0] if n else 0}).",
              f"- {len(r['kept'])} settings were left unchanged in every single run; "
              f"{len(r['changed'])} were changed in at least one run, of which "
              f"{sum(1 for e in r['changed'] if e['pct'] > 50)} were changed in more than half the runs.",
              f"- Headline profile recommendation focus: "
              + ", ".join(f"{k} in {_pct(v, n)}" for k, v in r["focus"].most_common()) + ".",
              f"- Profile recommendation decision: "
              + ", ".join(f"{k} ×{v}" for k, v in r["pdec"].most_common()) + ".", ""]
        L += ["### Changed in at least one run", "",
              "Frequency is how many of the runs suggested a different value for that setting. "
              "Range is the spread of the suggested values across those runs.", "",
              "| Setting | Current | AAPS default | Suggested change in | Suggested values | Direction |",
              "|---|---|---|---|---|---|"]
        for e in r["changed"]:
            default = e["default"] + (f" ({e['note']})" if e["note"] else "")
            L.append(f"| {e['label']} | {e['current']} | {default} | {_pct(e['n_changed'], n)} | "
                     f"{_range_text(e)} | {e.get('direction', '—')} |")
        L += ["", "### Kept unchanged in every run", ""]
        L += [f"- {line}" for line in _group_kept(r["kept"])]
        L += ["", "### Primary recommendation (first item the model listed)", "",
              "By area: " + ", ".join(f"{k} ×{v}" for k, v in r["primary_area"].most_common()) + ".", ""]
        L += [f"- {t} ×{c}" for t, c in r["primary"].most_common(8)]
        if len(r["primary"]) > 8:
            L.append(f"- … and {len(r['primary']) - 8} other titles")
        L.append("")

    if len(results) > 1:
        L += ["## Model comparison — how often each setting was changed", "",
              "| Setting | Current | AAPS default | " + " | ".join(r["model"] for r in results) + " |",
              "|---|---|---|" + "---|" * len(results)]
        keys: list[tuple[str, str]] = []
        for r in results:
            for e in r["changed"]:
                if (e["parameter_key"], e["component"]) not in keys:
                    keys.append((e["parameter_key"], e["component"]))
        for pk, ck in keys:
            cells, label, cur, dflt = [], "", "", ""
            for r in results:
                e = next((x for x in r["changed"] if (x["parameter_key"], x["component"]) == (pk, ck)), None)
                if e is None:
                    cells.append("never")
                else:
                    label, cur, dflt = e["label"], e["current"], e["default"]
                    rng = (f"{_fmt(e['min'])}–{_fmt(e['max'])}" if "min" in e and e["min"] != e["max"]
                           else _fmt(e["min"]) if "min" in e else ", ".join(e.get("text_values", {})))
                    cells.append(f"{e['pct']}% ({rng})")
            L.append(f"| {label} | {cur} | {dflt} | " + " | ".join(cells) + " |")
        L.append("")
    out_path.write_text("\n".join(L), encoding="utf-8")
    return out_path
