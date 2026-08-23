#!/usr/bin/env python3
"""Supplementary Table S3: for every change and keep decision in accepted conversations, does the
rationale cite at least one figure with a unit that is present in the package? Appends or
replaces the S3 section in paper/SUPPLEMENT.md.

Usage: python3 decision_citations.py
"""
from __future__ import annotations

import glob
import json
import re
from collections import defaultdict
from pathlib import Path

from tunemybg_repro.analyse import wilson
from tunemybg_repro.citations import package_numbers, verify_text

ORDER = [("real_gemini36flash_50", "Gemini 3.6 Flash"), ("real_gemini31pro_50", "Gemini 3.1 Pro Preview"),
         ("real_gemini35flashlite_50", "Gemini 3.5 Flash-Lite"), ("real_gpt56sol_med_50", "GPT-5.6-sol"),
         ("real_gpt54mini_med_50", "GPT-5.4-mini"), ("real_opus5", "Claude Opus 5"),
         ("real_sonnet5_20", "Claude Sonnet 5"), ("real_haiku45_50", "Claude Haiku 4.5"),
         ("real_deepseek_v4pro_50", "DeepSeek V4 Pro"), ("real_grok46_50", "Grok 4.6"),
         ("real_llama4maverick_50", "Llama 4 Maverick")]


def main() -> None:
    pkg = json.load(open("paper/study_package.json"))
    nums = package_numbers(pkg)
    rows = []
    for exp, name in ORDER:
        c: dict[str, int] = defaultdict(int)
        for p in sorted(glob.glob(f"results/{exp}/run_*/meta.json")):
            m = json.load(open(p))
            if not (m.get("validation") or {}).get("app_accepted"):
                continue
            o = json.load(open(p.replace("meta.json", "final.json")))
            for r in o.get("parameter_decisions", []):
                if not isinstance(r, dict):
                    continue
                key = "chg" if r.get("decision") == "change" else "keep"
                v, t, _ = verify_text(str(r.get("rationale") or ""), nums)
                c[key + "_n"] += 1
                if t == 0:
                    c[key + "_nofig"] += 1
                elif v > 0:
                    c[key + "_ver"] += 1
                else:
                    c[key + "_unver"] += 1
        n, k = c["chg_n"], c["keep_n"]
        lo, hi = wilson(c["chg_ver"], n) if n else (0, 0)
        pct = f"{c['chg_ver']} ({100 * c['chg_ver'] / n:.0f}; {100 * lo:.0f} to {100 * hi:.0f})" if n else "no changes"
        rows.append(f"| {name} | {n} | {pct} | {c['chg_unver']} | {c['chg_nofig']} | {k} | "
                    f"{c['keep_ver']} ({100 * c['keep_ver'] / k:.0f}) |")
    section = ["## Table S3. Whether the rationale for each decision cites a figure from the record", "",
               "Post hoc analysis over accepted conversations. For each decision row the rationale text was searched for figures "
               "with a unit (the same extraction as the citation check) and each figure was checked against the numbers in the "
               "package. A change decision is counted as cited when at least one such figure is present in the package. Wilson 95 "
               "per cent intervals, with the decision row as the unit, are given for the cited proportion; rows are not independent "
               "within a conversation, so the intervals are indicative.", "",
               "| Model | Change decisions | Cited a verified figure, n (per cent; 95 per cent interval) | Cited figures, none verified | No figure in rationale | Keep decisions | Keep decisions citing a verified figure, n (per cent) |",
               "|---|---|---|---|---|---|---|"] + rows
    sup = Path("paper/SUPPLEMENT.md")
    text = sup.read_text(encoding="utf-8")
    text = re.sub(r"\n## Table S3\..*", "", text, flags=re.S).rstrip() + "\n\n" + "\n".join(section) + "\n"
    sup.write_text(text, encoding="utf-8")
    print("\n".join(rows))


if __name__ == "__main__":
    main()
