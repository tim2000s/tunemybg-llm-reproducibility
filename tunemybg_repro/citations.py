"""Citation verification: do the numbers the models quote exist in the package?

Following the settings preprint's exact-match check, every figure with a glucose-type unit
(mg/dL, %, U/h, U, h, min, g/U) quoted in the accepted JSON is checked against the set of
numbers that actually appear in the package's telemetry, profile and inventory. A quoted
figure counts as verified if it matches a package number to the precision quoted (after
rounding the package value to the same number of decimals). Clock times are checked against
the hourly tables. Derived statistics the model may legitimately compute (for example a
ratio of two package numbers) are not in the package and will count as unverified, so the
rate is a lower bound; it is nevertheless comparable across models on the same package."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

from .reasoning import _text

_NUM_UNIT = re.compile(r"(?<![\w.])(\d+(?:\.\d+)?)\s?(%|percent|mg/dl|mg/dL|U/h|u/h|g/U|g/u|\bU\b|\bu\b|\bh\b|\bhours?\b|\bmin\b|\bminutes?\b)",
                       re.I)
UNITLESS_SKIP = {"%": False}


def package_numbers(package: dict[str, Any]) -> set[float]:
    nums: set[float] = set()

    def walk(o):
        if isinstance(o, bool):
            return
        if isinstance(o, (int, float)):
            nums.add(float(o))
        elif isinstance(o, str):
            for m in re.finditer(r"-?\d+(?:\.\d+)?", o):
                try:
                    nums.add(float(m.group()))
                except ValueError:
                    pass
        elif isinstance(o, dict):
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(package.get("telemetry", {}))
    walk(package.get("aaps_profile", {}))
    walk(package.get("decision_inventory", {}))
    # obvious derived quantities a careful reader would also compute
    ts = package.get("telemetry", {}).get("treatment_summary", {}) or {}
    days = package.get("metadata", {}).get("range_days") or 1
    if ts.get("total_insulin_u"):
        nums.add(ts["total_insulin_u"] / days)
        if ts.get("insulin_entries"):
            nums.add(ts["total_insulin_u"] / ts["insulin_entries"])
    nums.update({60.0, 120.0, 180.0, 240.0, 300.0, 360.0})   # response-window offsets in minutes
    return nums


def verify_text(text: str, pkg_nums: set[float]) -> tuple[int, int, list[str]]:
    """Return (verified, total, unverified_examples) for numeric citations in text."""
    verified = total = 0
    missing: list[str] = []
    for m in _NUM_UNIT.finditer(text):
        raw = m.group(1)
        val = float(raw)
        decimals = len(raw.split(".")[1]) if "." in raw else 0
        total += 1
        tol = 0.5 * 10 ** (-decimals) + 1e-9
        ok = any(abs(p - val) <= tol for p in pkg_nums)
        if ok:
            verified += 1
        else:
            missing.append(m.group(0))
    return verified, total, missing


def analyse_citations(exp_dir: Path, package: dict[str, Any]) -> dict[str, Any]:
    pkg_nums = package_numbers(package)
    runs = []
    for d in sorted(exp_dir.glob("run_*")):
        mp, fp = d / "meta.json", d / "final.json"
        if not (mp.exists() and fp.exists()):
            continue
        m = json.loads(mp.read_text(encoding="utf-8"))
        if m.get("status") != "completed" or not (m.get("validation") or {}).get("app_accepted"):
            continue
        o = json.loads(fp.read_text(encoding="utf-8"))
        parts = [_text(o.get("summary")), _text(o.get("issues")), _text(o.get("strengths"))]
        for s in o.get("analysis_steps", []) or []:
            if isinstance(s, dict):
                parts += [_text(s.get("findings")), _text(s.get("evidence"))]
        for dd in o.get("parameter_decisions", []) or []:
            if isinstance(dd, dict):
                parts.append(_text(dd.get("rationale")))
        parts.append(_text(o.get("profile_recommendation")))
        v, t, miss = verify_text(" ".join(parts), pkg_nums)
        runs.append({"run": d.name, "verified": v, "total": t, "missing": miss})
    meta = json.loads((exp_dir / "experiment.json").read_text(encoding="utf-8"))
    tot_v = sum(r["verified"] for r in runs)
    tot_t = sum(r["total"] for r in runs)
    miss = Counter(x.lower().replace(" ", "") for r in runs for x in r["missing"])
    return {"experiment": exp_dir.name, "model": meta.get("backend", {}).get("model"), "n_runs": len(runs),
            "citations_total": tot_t, "citations_verified": tot_v,
            "rate": round(tot_v / tot_t, 3) if tot_t else None,
            "per_run_rates": [round(r["verified"] / r["total"], 3) for r in runs if r["total"]],
            "commonest_unverified": miss.most_common(10)}
