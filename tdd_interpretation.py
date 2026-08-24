#!/usr/bin/env python3
"""Supplementary Table S4: how accepted conversations read the package's bolus-only insulin
total (treatment_summary.total_insulin_u, 275.95 U over 14 days, 19.7 U/day). The package
carries no basal delivery, so the total omits roughly the basal share of insulin; the
scheduled basal in the package integrates to 16.2 U/day. Per model, over accepted
conversations: treated 19.7 U (or the 275.95 total) as a daily insulin total or TDD; noted
that the total excludes basal or is bolus or SMB only; reconstructed a TDD near 36 U/day by
adding the scheduled basal; and lowered the maximum IOB limit while calling 19.7 a daily
total. Appends or replaces the S4 section of paper/SUPPLEMENT.md.

Usage: python3 tdd_interpretation.py
"""
from __future__ import annotations

import glob
import json
import re
from pathlib import Path

from tunemybg_repro.analyse import wilson
from tunemybg_repro.summary import parse_composite, parse_value

ORDER = [("real_gemini36flash_50", "Gemini 3.6 Flash"), ("real_gemini31pro_50", "Gemini 3.1 Pro Preview"),
         ("real_gemini35flashlite_50", "Gemini 3.5 Flash-Lite"), ("real_gpt56sol_med_50", "GPT-5.6-sol"),
         ("real_gpt54mini_med_50", "GPT-5.4-mini"), ("real_opus5", "Claude Opus 5"),
         ("real_sonnet5_20", "Claude Sonnet 5"), ("real_haiku45_50", "Claude Haiku 4.5"),
         ("real_deepseek_v4pro_50", "DeepSeek V4 Pro"), ("real_grok46_50", "Grok 4.6"),
         ("real_llama4maverick_50", "Llama 4 Maverick")]

TDD_NEAR = re.compile(r"TDD|total daily|daily insulin|/day|per day", re.I)
EXCLUDES = re.compile(r"(excludes?|not includ\w*|without|omits?|only\s+captures?)[^.\"]{0,60}basal|"
                      r"basal[^.\"]{0,50}(excluded|not included|not captured|not counted|missing|absent)|"
                      r"bolus[- /]?(and SMB |SMB[- ]?)?only|SMB[- ]only", re.I)
RECON = re.compile(r"35\.9|~ ?36 ?U|36 ?U/day|around 36|approximately 36|roughly 36|16\.2[^.\"]{0,50}(basal|/day)|"
                   r"basal[^.\"]{0,40}16\.2", re.I)


def lowered_iob(o: dict) -> bool:
    for r in o.get("parameter_decisions", []):
        if isinstance(r, dict) and r.get("parameter_key") == "aaps.core.safety_limits" and r.get("decision") == "change":
            v = parse_value(parse_composite(r.get("suggested_value")).get("max_iob_units"))[0]
            return v is not None and v != 25
    return False


def main() -> None:
    rows = []
    for exp, name in ORDER:
        n = tdd = ex = rec = both = 0
        for p in sorted(glob.glob(f"results/{exp}/run_*/meta.json")):
            m = json.load(open(p))
            if not (m.get("validation") or {}).get("app_accepted"):
                continue
            t = Path(p.replace("meta.json", "final.json")).read_text(encoding="utf-8")
            n += 1
            as_tdd = any(TDD_NEAR.search(w.group()) for w in re.finditer(r'[^"]{0,90}(19\.7|275\.95)[^"]{0,60}', t))
            tdd += as_tdd
            ex += bool(EXCLUDES.search(t))
            rec += bool(RECON.search(t))
            if as_tdd and lowered_iob(json.loads(t)):
                both += 1
        lo, hi = wilson(tdd, n)
        rows.append(f"| {name} | {n} | {tdd} ({100 * tdd / n:.0f}; {100 * lo:.0f} to {100 * hi:.0f}) | "
                    f"{ex} ({100 * ex / n:.0f}) | {rec} ({100 * rec / n:.0f}) | {both} |")
    section = ["## Table S4. How accepted conversations read the package's bolus-only insulin total", "",
               "Post hoc analysis. The package's treatment_summary gives total_insulin_u 275.95 over 14 days (19.7 U/day), a sum "
               "of the bolus and SMB treatment records only: the package carries no basal delivery data, and its scheduled basal "
               "profile integrates to 16.2 U/day. Response text was searched for the derived figure (19.7 or 275.95) in a daily "
               "total or TDD context, for statements that the total excludes basal or is bolus only, and for a reconstructed "
               "total near 36 U/day. Wilson 95 per cent intervals over accepted conversations.", "",
               "| Model | Accepted | Treated 19.7 U as a daily total or TDD, n (per cent; 95 per cent interval) | Noted the total excludes basal, n (per cent) | Reconstructed about 36 U/day, n (per cent) | Lowered max IOB while calling 19.7 a daily total |",
               "|---|---|---|---|---|---|"] + rows
    sup = Path("paper/SUPPLEMENT.md")
    text = re.sub(r"\n## Table S4\..*", "", sup.read_text(encoding="utf-8"), flags=re.S).rstrip()
    sup.write_text(text + "\n\n" + "\n".join(section) + "\n", encoding="utf-8")
    print("\n".join(rows))


if __name__ == "__main__":
    main()
