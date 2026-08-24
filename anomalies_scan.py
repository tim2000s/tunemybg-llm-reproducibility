#!/usr/bin/env python3
"""Supplementary Table S5: further package-inherited splits in the accepted conversations.

Three smaller anomalies share the shape of the bolus-only insulin total (Table S4):
1. Hour of the lows. The package carries hourly glucose keyed in UTC (peak time below range
   18.5 per cent at hour 0) and in local time (the same peak at 01:00, BST). Responses are
   classed by where they place the 18.5 per cent peak: 01:00 only, 00:00 or midnight only
   (the UTC array read as clock time), both, or neither.
2. Diluted insulin. The only disclosure that the user runs diluted insulin is the free-text
   profile name ("u200 dilute basal - 16-2u per day FLAT ISF") in Profile Switch events.
   Responses are classed by whether they mention it and whether they engage with its kinetics.
3. mmol/L reason strings. The AAPS reason strings in the loop statuses are denominated in
   mmol/L inside an otherwise mg/dl package; responses quoting those ISF values are counted.

Appends or replaces the S5 section of paper/SUPPLEMENT.md.

Usage: python3 anomalies_scan.py
"""
from __future__ import annotations

import glob
import json
import re
from pathlib import Path

ORDER = [("real_gemini36flash_50", "Gemini 3.6 Flash"), ("real_gemini31pro_50", "Gemini 3.1 Pro Preview"),
         ("real_gemini35flashlite_50", "Gemini 3.5 Flash-Lite"), ("real_gpt56sol_med_50", "GPT-5.6-sol"),
         ("real_gpt54mini_med_50", "GPT-5.4-mini"), ("real_opus5", "Claude Opus 5"),
         ("real_sonnet5_20", "Claude Sonnet 5"), ("real_haiku45_50", "Claude Haiku 4.5"),
         ("real_deepseek_v4pro_50", "DeepSeek V4 Pro"), ("real_grok46_50", "Grok 4.6"),
         ("real_llama4maverick_50", "Llama 4 Maverick")]

AT00 = re.compile(r'(00:00|midnight)[^"]{0,40}(18\.5|highest|worst|peak)|18\.5[^"]{0,50}(00:00|midnight)')
AT01 = re.compile(r'01:00[^"]{0,40}(18\.5|highest|worst|peak)|18\.5[^"]{0,50}01:00')
DIL = re.compile(r"u-?200|dilut", re.I)
DIL_K = re.compile(r"(unknown|uncertain|cannot|non-standard|custom)[^\"]{0,60}(u-?200|dilut|kinetic|peak)|"
                   r"(u-?200|dilut\w*)[^\"]{0,80}(unknown|uncertain|cannot|kinetic|peak|absorption)", re.I)
MMOL = re.compile(r"ISF[ :]{0,3}[2-9]\.\d\b")


def main() -> None:
    rows = []
    for exp, name in ORDER:
        n = a01 = a00 = both = dil = dilk = mmol = 0
        for p in sorted(glob.glob(f"results/{exp}/run_*/meta.json")):
            m = json.load(open(p))
            if not (m.get("validation") or {}).get("app_accepted"):
                continue
            t = Path(p.replace("meta.json", "final.json")).read_text(encoding="utf-8")
            n += 1
            h0, h1 = bool(AT00.search(t)), bool(AT01.search(t))
            if h0 and h1:
                both += 1
            elif h1:
                a01 += 1
            elif h0:
                a00 += 1
            if DIL.search(t):
                dil += 1
                if DIL_K.search(t):
                    dilk += 1
            if MMOL.search(t):
                mmol += 1
        rows.append(f"| {name} | {n} | {a01} | {a00} | {both} | {dil} | {dilk} | {mmol} |")
    section = ["## Table S5. Further package-inherited splits", "",
               "Post hoc analysis over accepted conversations. Hour of the lows: the package's hourly glucose is keyed both in UTC "
               "(time below range peaks at 18.5 per cent at hour 0) and in local time (the same peak at 01:00, BST); responses are "
               "classed by where they place the peak, with '00:00 or midnight only' indicating the UTC array read as clock time. "
               "Diluted insulin: the record's use of diluted insulin is disclosed only in a free-text profile name inside Profile "
               "Switch events; counts give responses mentioning it and responses engaging with its kinetics or absorption. mmol/L: "
               "responses quoting the mmol-denominated ISF values from the loop reason strings inside the otherwise mg/dl package.", "",
               "| Model | Accepted | Peak at 01:00 only | Peak at 00:00 or midnight only | Both hours cited | Mentions diluted insulin | Engages with its kinetics | Quotes mmol ISF values |",
               "|---|---|---|---|---|---|---|---|"] + rows
    sup = Path("paper/SUPPLEMENT.md")
    text = re.sub(r"\n## Table S5\..*", "", sup.read_text(encoding="utf-8"), flags=re.S).rstrip()
    sup.write_text(text + "\n\n" + "\n".join(section) + "\n", encoding="utf-8")
    print("\n".join(rows))


if __name__ == "__main__":
    main()
