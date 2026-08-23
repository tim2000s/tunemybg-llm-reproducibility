#!/usr/bin/env python3
"""Re-validate every completed run against the current (app-faithful) validator and rewrite
meta.json / final.json accordingly. Safe to re-run. Raw responses are never touched.

Usage: python3 revalidate.py results/real_*
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from tunemybg_repro.extract import decision_diff, extract_json, validate
from tunemybg_repro.runner import classify_attempts

DEFAULT_PACKAGE = Path.home() / "Downloads" / "TuneMyBG-analysis.json"


def revalidate_run(run_dir: Path, package: dict) -> str | None:
    meta_path = run_dir / "meta.json"
    if not meta_path.exists():
        return None
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    if meta.get("status") != "completed":
        return None
    attempts = []
    i = 0
    while True:
        raw = run_dir / ("final_raw.txt" if i == 0 else f"final_raw_attempt{i}.txt")
        if not raw.exists():
            break
        obj, method = extract_json(raw.read_text(encoding="utf-8"))
        attempts.append({"attempt": i, "json_extracted": obj is not None, "extraction_method": method,
                         "validation": validate(obj, package) if obj is not None else None, "obj": obj})
        i += 1
    if not attempts:
        return None
    first = attempts[0]
    accepted, outcome = classify_attempts(attempts)
    meta["attempts"] = [{k: v for k, v in a.items() if k != "obj"} for a in attempts]
    meta["n_repairs"] = len(attempts) - 1
    meta["first_pass"] = {"json_extracted": first["json_extracted"] and first["extraction_method"] != "raw_decode_prefix",
                          "extraction_method": first["extraction_method"],
                          "fully_compliant": bool(first["validation"] and first["validation"]["fully_compliant"]),
                          "app_accepted": bool(first["validation"] and first["validation"]["app_accepted"]),
                          "sections": (first["validation"] or {}).get("sections") if first["validation"] else None,
                          "failed_by_tier": (first["validation"] or {}).get("failed_by_tier") if first["validation"] else None}
    meta["app_outcome"] = outcome
    meta["accepted_attempt"] = accepted["attempt"] if accepted else None
    meta["json_extracted"] = bool(accepted and accepted["obj"] is not None)
    meta["extraction_method"] = accepted["extraction_method"] if accepted else None
    # The app never holds a rejected response, so app_accepted must follow the outcome even
    # when the last attempt's JSON parsed and would otherwise pass on its own.
    meta["validation"] = dict(accepted["validation"]) if accepted and accepted["validation"] else None
    if meta["validation"] is not None and not outcome.startswith("accepted"):
        meta["validation"]["app_accepted"] = False
    meta["repair_diff"] = (decision_diff(first["obj"], accepted["obj"])
                           if first["obj"] is not None and accepted is not None and accepted is not first
                           and accepted["obj"] is not None else None)
    if accepted and accepted["obj"] is not None:
        (run_dir / "final.json").write_text(json.dumps(accepted["obj"], indent=2, ensure_ascii=False), encoding="utf-8")
    elif (run_dir / "final.json").exists():
        (run_dir / "final.json").unlink()
    if first["obj"] is not None:
        (run_dir / "final_firstpass.json").write_text(json.dumps(first["obj"], indent=2, ensure_ascii=False), encoding="utf-8")
    # keep per-attempt JSON files in step with the raw responses
    for a in attempts[1:]:
        p = run_dir / f"final_attempt{a['attempt']}.json"
        if a["obj"] is not None:
            p.write_text(json.dumps(a["obj"], indent=2, ensure_ascii=False), encoding="utf-8")
        elif p.exists():
            p.unlink()
    for stale in run_dir.glob("final_attempt*.json"):
        n = int(stale.stem.replace("final_attempt", "") or 0)
        if n >= len(attempts):
            stale.unlink()
    meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    return outcome


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("experiments", nargs="+", type=Path)
    ap.add_argument("--package", type=Path, default=DEFAULT_PACKAGE)
    args = ap.parse_args()
    package = json.loads(Path(args.package).read_text(encoding="utf-8"))
    for exp in args.experiments:
        from collections import Counter
        c = Counter()
        for run_dir in sorted(exp.glob("run_*")):
            o = revalidate_run(run_dir, package)
            if o:
                c[o] += 1
        print(f"{exp.name}: {dict(c)}")


if __name__ == "__main__":
    main()
