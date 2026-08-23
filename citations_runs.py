#!/usr/bin/env python3
"""Citation verification across experiments: fraction of quoted figures that exist in the package.

Usage: python3 citations_runs.py results/real_* --out results/citations.md
"""

from __future__ import annotations

import argparse
import json
import statistics
from pathlib import Path

from tunemybg_repro.citations import analyse_citations

DEFAULT_PACKAGE = Path.home() / "Downloads" / "TuneMyBG-analysis.json"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("experiments", nargs="+", type=Path)
    ap.add_argument("--package", type=Path, default=DEFAULT_PACKAGE)
    ap.add_argument("--out", type=Path, default=Path("results/citations.md"))
    args = ap.parse_args()
    package = json.loads(Path(args.package).read_text(encoding="utf-8"))
    res = [analyse_citations(e, package) for e in args.experiments]
    L = ["# Citation verification — do the quoted figures exist in the package?", "",
         "Every number with a unit (mg/dL, %, U/h, U, h, min, g/U) quoted in the accepted JSON's summary, "
         "issues, strengths, step findings and evidence, decision rationales and profile recommendation is "
         "checked against the numbers present in the package (telemetry, profile, inventory), to the "
         "precision quoted. Derived figures the model computes itself count as unverified, so rates are lower "
         "bounds but comparable across models.", "",
         "| Model | Runs | Figures quoted | Verified | Rate | Per-run median (min–max) | Commonest unverified figures |",
         "|---|---|---|---|---|---|---|"]
    for r in res:
        pr = r["per_run_rates"]
        med = f"{statistics.median(pr):.2f} ({min(pr):.2f}–{max(pr):.2f})" if pr else "—"
        L.append(f"| {r['model']} | {r['n_runs']} | {r['citations_total']} | {r['citations_verified']} | "
                 f"{r['rate']} | {med} | " + ", ".join(f"{k} ×{c}" for k, c in r["commonest_unverified"][:6]) + " |")
    args.out.write_text("\n".join(L), encoding="utf-8")
    print("\n".join(L[6:]))


if __name__ == "__main__":
    main()
