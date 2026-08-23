#!/usr/bin/env python3
"""Analyse one or more experiment directories and write CSV tables plus report.md.

Examples:
  python3 analyse_runs.py results/qwen9b
  python3 analyse_runs.py results/qwen9b results/gemini25pro --out results/compare_qwen_gemini
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from tunemybg_repro.analyse import analyse

DEFAULT_PACKAGE = Path.home() / "Downloads" / "TuneMyBG-analysis.json"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("experiments", nargs="+", type=Path, help="results/<experiment> directories")
    ap.add_argument("--package", type=Path, default=None,
                    help="analysis package (defaults to the path recorded in experiment.json)")
    ap.add_argument("--out", type=Path, default=None,
                    help="output directory (default: <experiment>/analysis, or results/compare_* for several)")
    args = ap.parse_args()

    exp_dirs = [p.resolve() for p in args.experiments]
    for p in exp_dirs:
        if not (p / "experiment.json").exists():
            raise SystemExit(f"{p} has no experiment.json")
    package_path = args.package
    if package_path is None:
        recorded = json.loads((exp_dirs[0] / "experiment.json").read_text()).get("package_path")
        package_path = Path(recorded) if recorded and Path(recorded).exists() else DEFAULT_PACKAGE
    package = json.loads(Path(package_path).read_text(encoding="utf-8"))

    out = args.out
    if out is None:
        out = exp_dirs[0] / "analysis" if len(exp_dirs) == 1 else \
            exp_dirs[0].parent / ("compare_" + "_".join(p.name for p in exp_dirs))
    report = analyse(exp_dirs, package, out)
    print(f"Wrote tables to {out}/*.csv and report to {report}\n")
    print(report.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
