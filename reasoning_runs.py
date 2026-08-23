#!/usr/bin/env python3
"""Natural-language analysis of the reasoning in an experiment's final JSONs.

Examples:
  python3 reasoning_runs.py results/real_gemini36flash_50
  python3 reasoning_runs.py results/real_opus5 --threshold 0.35
"""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

from tunemybg_repro.reasoning import analyse_reasoning, write_reasoning_report

HERE = Path(__file__).resolve().parent
DEFAULT_PACKAGE = Path.home() / "Downloads" / "TuneMyBG-analysis.json"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("experiment", type=Path)
    ap.add_argument("--package", type=Path, default=None)
    ap.add_argument("--threshold", type=float, default=0.25, help="cosine similarity to merge sentences")
    ap.add_argument("--no-pdf", action="store_true")
    args = ap.parse_args()

    exp_dir = args.experiment.resolve()
    package_path = args.package
    if package_path is None:
        recorded = json.loads((exp_dir / "experiment.json").read_text()).get("package_path")
        package_path = Path(recorded) if recorded and Path(recorded).exists() else DEFAULT_PACKAGE
    package = json.loads(Path(package_path).read_text(encoding="utf-8"))

    out_dir = exp_dir / "analysis"
    out_dir.mkdir(exist_ok=True)
    res = analyse_reasoning(exp_dir, package, threshold=args.threshold)
    md = write_reasoning_report(res, out_dir / "reasoning.md", out_dir / "reasoning_clusters.csv")
    print(f"wrote {md}")
    if not args.no_pdf:
        subprocess.run([str(HERE / "report_to_pdf.sh"), str(md)], check=True)


if __name__ == "__main__":
    main()
