#!/usr/bin/env python3
"""Write a plain-English summary (and PDF) for one or more experiments.

Examples:
  python3 summarise_runs.py results/real_gemini36flash_50
  python3 summarise_runs.py results/real_gemini36flash_50 results/real_opus5 results/real_gpt56sol_med_50 \
      --out ~/Downloads/TuneMyBG-model-comparison.md
"""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

from tunemybg_repro.summary import analyse_experiment, write_summary

HERE = Path(__file__).resolve().parent
DEFAULT_PACKAGE = Path.home() / "Downloads" / "TuneMyBG-analysis.json"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("experiments", nargs="+", type=Path)
    ap.add_argument("--package", type=Path, default=None)
    ap.add_argument("--out", type=Path, default=None, help="output .md path (PDF written alongside)")
    ap.add_argument("--no-pdf", action="store_true")
    args = ap.parse_args()

    exp_dirs = [p.resolve() for p in args.experiments]
    package_path = args.package
    if package_path is None:
        recorded = json.loads((exp_dirs[0] / "experiment.json").read_text()).get("package_path")
        package_path = Path(recorded) if recorded and Path(recorded).exists() else DEFAULT_PACKAGE
    package = json.loads(Path(package_path).read_text(encoding="utf-8"))

    results = [analyse_experiment(d, package) for d in exp_dirs]
    out = args.out or (exp_dirs[0] / "analysis" / "summary.md" if len(exp_dirs) == 1
                       else exp_dirs[0].parent / ("summary_" + "_".join(d.name for d in exp_dirs) + ".md"))
    out.parent.mkdir(parents=True, exist_ok=True)
    write_summary(results, package, out)
    print(f"wrote {out}")
    if not args.no_pdf:
        subprocess.run([str(HERE / "report_to_pdf.sh"), str(out)], check=True)


if __name__ == "__main__":
    main()
