#!/usr/bin/env python3
"""How each model handled a package with no carbohydrate entries: recognition, CR decisions and
their stated reasons, inference of meals from glucose shape, advice to log, and how honestly the
meal steps were scored. One table across experiments plus representative CR rationales.

Usage: python3 carb_handling.py results/real_* --out results/carb_handling.md
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

from tunemybg_repro.reasoning import _text, cluster_texts

NO_CARB = re.compile(r"(no|zero|0|absent|absence of|without|not|never|un)[- ]?(logged|announced|recorded|entered)?\s*"
                     r"(carb|carbohydrate|meal entr|carb entr)|carb(ohydrate)?s? (were|was|are|is) (not|never)|"
                     r"(zero|0|no) (logged )?carb", re.I)
CR_UNTESTABLE = re.compile(r"(cannot|can't|could not|unable|no way|not possible|impossible|untest|unverif|"
                           r"not (be )?(evaluat|assess|verif|test|validat)|insufficient|lack of|absence of|"
                           r"pending|until .*log)", re.I)
INFER_MEALS = re.compile(r"(unannounced|unlogged|undeclared) (meal|carb|intake|eating)|UAM|meal-shaped|"
                         r"(likely|probable|presumed|apparent|inferred) (meal|eating|breakfast|lunch|dinner)|"
                         r"postprandial|post-meal", re.I)
ADVISE_LOG = re.compile(r"(log|record|enter|announce|declar)\w*\s+(all |your |the |some |accurate |consistent )?"
                        r"(carb|meal|carbohydrate)", re.I)


def analyse(exp: Path) -> dict | None:
    rows = []
    for d in sorted(exp.glob("run_*")):
        mp, fp = d / "meta.json", d / "final.json"
        if not (mp.exists() and fp.exists()):
            continue
        m = json.loads(mp.read_text(encoding="utf-8"))
        if m.get("status") != "completed" or not (m.get("validation") or {}).get("app_accepted"):
            continue
        o = json.loads(fp.read_text(encoding="utf-8"))
        whole = json.dumps(o, ensure_ascii=False)
        cr_rows = [x for x in o.get("parameter_decisions", []) if isinstance(x, dict)
                   and str(x.get("parameter_key", "")).startswith("profile.cr.")]
        cr_changed = [x for x in cr_rows if x.get("decision") == "change"]
        cr_rat = " ".join(_text(x.get("rationale")) for x in cr_rows)
        steps = {s.get("key"): s for s in o.get("analysis_steps", []) if isinstance(s, dict)}
        mb = steps.get("meal_bolus_strategy", {}) or {}
        ms = o.get("meal_strategy_summary") or {}
        recs = [x for x in o.get("recommendations", []) if isinstance(x, dict)]
        advice_text = " ".join([_text(x.get("title")) + " " + _text(x.get("description")) for x in recs]
                               + [_text(o.get("implementation_steps")), _text(ms.get("suggestion")),
                                  _text(ms.get("next_observation")), _text(o.get("profile_recommendation"))])
        rows.append({
            "run": d.name,
            "notices_no_carbs": bool(NO_CARB.search(whole)),
            "cr_changed": bool(cr_changed),
            "cr_changed_keys": [x.get("parameter_key") for x in cr_changed],
            "cr_rationale_untestable": bool(CR_UNTESTABLE.search(cr_rat)) and bool(NO_CARB.search(cr_rat)),
            "cr_rationale_mentions_no_carbs": bool(NO_CARB.search(cr_rat)),
            "infers_meals": bool(INFER_MEALS.search(whole)),
            "advises_logging": bool(ADVISE_LOG.search(advice_text)),
            "first_rec_is_logging": bool(recs) and bool(ADVISE_LOG.search(_text(recs[0].get("title")) + " " + _text(recs[0].get("description")))),
            "meal_step_status": mb.get("status"), "meal_step_confidence": mb.get("confidence"),
            "meal_summary_confidence": ms.get("confidence"),
            "cr_rationales": [(d.name, _text(x.get("rationale"))) for x in cr_rows],
        })
    if not rows:
        return None
    n = len(rows)
    meta = json.loads((exp / "experiment.json").read_text(encoding="utf-8"))
    return {"experiment": exp.name, "model": meta.get("backend", {}).get("model"), "n": n, "rows": rows}


def pct(k, n):
    return f"{k}/{n} ({round(100 * k / n)}%)"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("experiments", nargs="+", type=Path)
    ap.add_argument("--out", type=Path, default=Path("results/carb_handling.md"))
    args = ap.parse_args()
    res = [r for r in (analyse(e) for e in args.experiments) if r]
    L = ["# Handling of a package with no carbohydrate entries", "",
         "The real package has 0 carbohydrate entries in 14 days, 655 insulin entries and an empty declared "
         "meal strategy, so carb ratios were never exercised. Counts are over runs the app accepted.", "",
         "| Model | Runs | Notices no carbs | Changes a CR | CR rationale cites missing carbs | CR called untestable | Infers meals from glucose | Advises carb logging | First recommendation is logging | meal_bolus_strategy status | meal confidence |",
         "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in res:
        rows, n = r["rows"], r["n"]
        c = lambda k: sum(1 for x in rows if x[k])  # noqa: E731
        st = Counter(x["meal_step_status"] for x in rows)
        mc = Counter(x["meal_summary_confidence"] for x in rows)
        L.append(f"| {r['model']} | {n} | {pct(c('notices_no_carbs'), n)} | {pct(c('cr_changed'), n)} | "
                 f"{pct(c('cr_rationale_mentions_no_carbs'), n)} | {pct(c('cr_rationale_untestable'), n)} | "
                 f"{pct(c('infers_meals'), n)} | {pct(c('advises_logging'), n)} | {pct(c('first_rec_is_logging'), n)} | "
                 f"{', '.join(f'{k} ×{v}' for k, v in st.most_common())} | {', '.join(f'{k} ×{v}' for k, v in mc.most_common())} |")
    L += ["", "## What the models said about the carb ratios", "",
          "Sentences from the CR-row rationales, grouped across runs; the count is runs making the point.", ""]
    for r in res:
        items = [(rid, t) for x in r["rows"] for rid, t in x["cr_rationales"]]
        cl = cluster_texts(items, 0.25)
        L += [f"### {r['model']}", ""]
        for cc in cl[:5]:
            L.append(f"- ({cc['n_runs']}/{r['n']}) {cc['representative']}")
        changed = [(x['run'], x['cr_changed_keys']) for x in r["rows"] if x["cr_changed"]]
        if changed:
            L.append(f"- CR changes made despite no carb data: {changed}")
        L.append("")
    args.out.write_text("\n".join(L), encoding="utf-8")
    print(f"wrote {args.out}")
    print("\n".join(L[4:4 + len(res) + 2]))


if __name__ == "__main__":
    main()
