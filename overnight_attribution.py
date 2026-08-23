#!/usr/bin/env python3
"""Did the models trace the overnight lows to earlier insulin, and did that stop them changing
the overnight target or basal?

The record's time below 70 mg/dL peaks at 01:00 local (18.5 per cent) and has fallen to low
single figures by 04:00 to 07:00 with the same basal segment running, under a 10-hour DIA; the
pattern is consistent with the tail of insulin delivered in the evening rather than with the
overnight basal or target. For each accepted response the text about the overnight settings
(rationales for target 00:00, target 23:00 and basal 00:00, the basal_targets step findings and
the profile recommendation rationale) is searched for explicit causal attribution to earlier
insulin (tail, stacking, carry-over, residual IOB, evening correction dosing) and for attribution
to the setting itself, and cross-tabulated with whether the response changed the target or the
midnight basal.

Usage: python3 overnight_attribution.py results/real_* --out results/overnight_attribution.md
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from tunemybg_repro.analyse import wilson
from tunemybg_repro.reasoning import _text

PRIOR_INSULIN = re.compile(
    r"insulin tail|\btail\b.{0,40}(insulin|evening|dos|bolus)|"
    r"(evening|earlier|prior|late|dinner).{0,40}(insulin|bolus|dos|correction|microbolus|SMB).{0,80}(overnight|night|00:00|01:00|midnight|early.hours|low)|"
    r"stack|carry.?over|residual insulin|(decay|wan|tail).{0,30}(insulin|IOB)|overcorrection|over-correction|"
    r"insulin (delivered|given|dosed) (earlier|in the evening|before)|IOB (from|carried|remaining|tail|still)", re.I)
SETTING_CAUSE = re.compile(
    r"(target|basal).{0,60}(too (high|low|tight|aggressive)|excess|insufficient|contribut|driv|caus|responsib)|"
    r"(caus|driv|due to|attribut).{0,60}(basal|target)", re.I)
OVERNIGHT_KEYS = ("profile.target.00_00", "profile.target.23_00", "profile.basal.00_00")


def analyse(exp: Path) -> dict | None:
    n = prior = setting = changed = changed_prior = changed_no_cause = 0
    for d in sorted(exp.glob("run_*")):
        mp, fp = d / "meta.json", d / "final.json"
        if not (mp.exists() and fp.exists()):
            continue
        m = json.loads(mp.read_text(encoding="utf-8"))
        if m.get("status") != "completed" or not (m.get("validation") or {}).get("app_accepted"):
            continue
        o = json.loads(fp.read_text(encoding="utf-8"))
        rows = {r.get("parameter_key"): r for r in o.get("parameter_decisions", []) if isinstance(r, dict)}
        steps = {s.get("key"): s for s in o.get("analysis_steps", []) if isinstance(s, dict)}
        txt = " ".join(_text(rows.get(k, {}).get("rationale")) for k in OVERNIGHT_KEYS)
        txt += " " + _text((steps.get("basal_targets") or {}).get("findings"))
        txt += " " + _text((o.get("profile_recommendation") or {}).get("rationale"))
        n += 1
        a = bool(PRIOR_INSULIN.search(txt))
        b = bool(SETTING_CAUSE.search(txt))
        c = any(rows.get(k, {}).get("decision") == "change" for k in OVERNIGHT_KEYS)
        prior += a
        setting += b
        changed += c
        changed_prior += a and c
        changed_no_cause += c and not a and not b
    if not n:
        return None
    model = json.loads((exp / "experiment.json").read_text(encoding="utf-8")).get("backend", {}).get("model")
    return {"model": model, "n": n, "prior": prior, "setting": setting, "changed": changed,
            "changed_prior": changed_prior, "changed_no_cause": changed_no_cause}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("experiments", nargs="+", type=Path)
    ap.add_argument("--out", type=Path, default=Path("results/overnight_attribution.md"))
    args = ap.parse_args()
    res = [r for r in (analyse(e) for e in args.experiments) if r]
    L = ["# Attribution of the overnight lows and changes to the overnight settings", "",
         "Counts are accepted conversations. 'Earlier insulin' means an explicit causal attribution of the overnight "
         "lows to the tail of evening dosing, stacking, carry-over or residual IOB in the text about the overnight "
         "settings; 'setting' means attribution to the target or basal itself. A conversation may do both. Wilson 95 "
         "per cent intervals in brackets.", "",
         "| Model | n | Attributes lows to earlier insulin | Attributes lows to target or basal | Changed target 00:00, target 23:00 or basal 00:00 | Changed despite attributing to earlier insulin | Changed with no causal attribution |",
         "|---|---|---|---|---|---|---|"]
    for r in res:
        n = r["n"]
        f = lambda k: f"{r[k]} ({r[k] / n:.0%}; {wilson(r[k], n)[0]:.2f} to {wilson(r[k], n)[1]:.2f})"  # noqa: E731
        L.append(f"| {r['model']} | {n} | {f('prior')} | {f('setting')} | {f('changed')} | {r['changed_prior']} | {r['changed_no_cause']} |")
    args.out.write_text("\n".join(L), encoding="utf-8")
    print("\n".join(L[5:]))


if __name__ == "__main__":
    main()
