"""Pull the final JSON out of the prompt-4 response and validate it.

Validation has three tiers, established by pasting 25 real outputs into the app (2026-08-22):

* app_prompt  - the app rejects and composes a repair prompt: decision rows missing from or not
                in decision_inventory, current_value not copied exactly, profile_recommendation.focus
                outside basal/target/cr/isf/dia.
* app_schema  - the app hard-stops with "The AI response does not match the TuneMyBG schema."
                and offers no prompt: a required string field is absent (observed: a decision row
                without `rationale`, profile_recommendation without `recommendation`). Fields
                observed to be optional: suggested_value, data_gaps. Others are assumed.
* prompt_only - demanded by Prompt 4 / required_output_schema but NOT enforced by the app
                (observed accepted: extra keys, invalid status/confidence/priority words, a missing
                `issues` section, a trailing ``` fence). Reported as instruction compliance.
"""

from __future__ import annotations

import json
import re
from typing import Any

_FENCE_RE = re.compile(r"```(?:json)?\s*(.*?)```", re.DOTALL)
_THINK_RE = re.compile(r"<think>.*?</think>", re.DOTALL)

TOP_LEVEL = ["summary", "analysis_steps", "strengths", "issues", "recommendations",
             "profile_recommendation", "parameter_decisions", "meal_strategy_summary",
             "implementation_steps", "education", "safety_notes"]
ARRAY_SECTIONS = ["analysis_steps", "strengths", "issues", "recommendations",
                  "parameter_decisions", "implementation_steps", "education", "safety_notes"]
STEP_FIELDS = ["key", "status", "confidence", "findings", "evidence", "dependencies", "data_gaps"]
DECISION_FIELDS = ["parameter_key", "parameter", "current_value", "suggested_value", "decision",
                   "rationale"]
PROFILE_REC_FIELDS = ["focus", "decision", "recommendation", "rationale", "confidence", "next_check"]
MEAL_FIELDS = ["suggestion", "rationale", "confidence", "next_observation", "exceptions"]
STATUS_VALUES = {"completed", "partial", "blocked"}
CONFIDENCE_VALUES = {"low", "medium", "high"}
FOCUS_VALUES = {"basal", "target", "cr", "isf", "dia"}
PRIORITY_VALUES = {"low", "medium", "high", "safety"}

# Required (non-null string) fields for the app's typed schema. Observed: rationale and
# recommendation required; suggested_value and data_gaps optional. The rest is assumption.
APP_REQUIRED_DECISION_FIELDS = ["parameter_key", "decision", "rationale"]
APP_REQUIRED_PROFILE_REC_FIELDS = ["focus", "decision", "recommendation", "rationale"]
APP_REQUIRED_TOP_LEVEL = ["parameter_decisions", "profile_recommendation"]


def extract_json(text: str) -> tuple[dict | None, str]:
    """Return (object, method). The app strips ```json fences (observed), so 'fenced' and a
    trailing-fence 'brace_slice' count as parseable; 'raw_decode_prefix' (several top-level
    objects) does not: the app rejects it as invalid JSON."""
    text = _THINK_RE.sub("", text).strip()
    candidates: list[tuple[str, str]] = [("strict", text)]
    for m in _FENCE_RE.finditer(text):
        candidates.append(("fenced", m.group(1).strip()))
    first, last = text.find("{"), text.rfind("}")
    if first != -1 and last > first:
        candidates.append(("brace_slice", text[first:last + 1]))
    for method, cand in candidates:
        try:
            obj = json.loads(cand)
            if isinstance(obj, dict):
                return obj, method
        except json.JSONDecodeError:
            continue
    if first != -1:
        try:
            obj, _ = json.JSONDecoder().raw_decode(text[first:])
            if isinstance(obj, dict):
                return obj, "raw_decode_prefix"
        except json.JSONDecodeError:
            pass
    return None, "failed"


APP_PARSEABLE_METHODS = {"strict", "fenced", "brace_slice"}


def validate(obj: dict, package: dict) -> dict[str, Any]:
    v: list[str] = []
    checks: dict[str, bool] = {}
    tiers: dict[str, str] = {}
    sections: list[str] = []

    def check(name: str, tier: str, ok: bool, msg: str = "", secs: list[str] | None = None):
        checks[name] = bool(ok)
        tiers[name] = tier
        if not ok:
            v.append(msg or name)
            for s in secs or []:
                if s not in sections:
                    sections.append(s)

    keys = list(obj.keys())
    missing, extra = sorted(set(TOP_LEVEL) - set(keys)), sorted(set(keys) - set(TOP_LEVEL))
    check("top_level_exact", "prompt_only", not missing and not extra,
          f"top-level keys differ: missing={missing} extra={extra}", missing + extra)
    app_missing = [k for k in APP_REQUIRED_TOP_LEVEL if not isinstance(obj.get(k), (list, dict))]
    check("app_required_sections_present", "app_schema", not app_missing,
          f"required sections absent or wrong type: {app_missing}", app_missing)
    for k in ARRAY_SECTIONS:
        check(f"{k}_is_array", "prompt_only", k not in obj or isinstance(obj.get(k), list),
              f"{k} is not an array", [k])
    check("profile_recommendation_is_object", "app_schema", isinstance(obj.get("profile_recommendation"), dict),
          "profile_recommendation is not an object", ["profile_recommendation"])
    check("meal_strategy_summary_is_object", "prompt_only",
          "meal_strategy_summary" not in obj or isinstance(obj.get("meal_strategy_summary"), dict),
          "meal_strategy_summary is not an object", ["meal_strategy_summary"])

    # analysis_steps (prompt-only: the app accepted missing data_gaps and bad enum words)
    wf_keys = [s["key"] for s in package["analysis_workflow"]["steps"]]
    steps = obj.get("analysis_steps") if isinstance(obj.get("analysis_steps"), list) else []
    step_keys = [s.get("key") if isinstance(s, dict) else None for s in steps]
    check("steps_keys_match_order", "prompt_only", step_keys == wf_keys,
          f"analysis_steps keys {step_keys} != workflow {wf_keys}", ["analysis_steps"])
    bad_fields = [s.get("key") for s in steps if isinstance(s, dict) and set(s.keys()) != set(STEP_FIELDS)]
    check("steps_fields_exact", "prompt_only", not bad_fields, f"steps with wrong field set: {bad_fields}",
          [f"analysis_steps.{k}" for k in bad_fields])
    bad_status = [s.get("key") for s in steps if isinstance(s, dict) and s.get("status") not in STATUS_VALUES]
    bad_conf = [s.get("key") for s in steps if isinstance(s, dict) and s.get("confidence") not in CONFIDENCE_VALUES]
    check("steps_enums_valid", "prompt_only", not bad_status and not bad_conf,
          f"steps with invalid status {bad_status} / confidence {bad_conf}",
          [f"analysis_steps.{k}.status" for k in bad_status] + [f"analysis_steps.{k}.confidence" for k in bad_conf])

    # parameter_decisions
    inv = {i["parameter_key"]: i for i in package["decision_inventory"]["items"]}
    decs = obj.get("parameter_decisions") if isinstance(obj.get("parameter_decisions"), list) else []
    dec_keys = [d.get("parameter_key") for d in decs if isinstance(d, dict)]
    expected_total = package["decision_inventory"]["expected_total"]
    missing_keys = sorted(set(inv) - set(dec_keys))
    extra_keys = sorted(set(dec_keys) - set(inv))
    dup_keys = sorted({k for k in dec_keys if dec_keys.count(k) > 1})
    check("decisions_count", "prompt_only", len(decs) == expected_total,
          f"parameter_decisions has {len(decs)} items, expected {expected_total}", ["parameter_decisions"])
    check("decisions_no_duplicates", "app_prompt", not dup_keys, f"duplicate parameter_key: {dup_keys}",
          ["parameter_decisions"])
    check("decisions_keys_match_inventory", "app_prompt", not missing_keys and not extra_keys,
          f"missing={missing_keys} extra={extra_keys}", ["parameter_decisions"])
    rows_missing_required = [d.get("parameter_key") for d in decs if isinstance(d, dict)
                             and any(not isinstance(d.get(f), str) for f in APP_REQUIRED_DECISION_FIELDS)]
    check("decisions_required_fields", "app_schema", not rows_missing_required,
          f"decision rows missing a required field ({APP_REQUIRED_DECISION_FIELDS}): {rows_missing_required}",
          [f"parameter_decisions.{k}" for k in rows_missing_required])
    wrong_fields = [d.get("parameter_key") for d in decs if isinstance(d, dict) and set(d.keys()) != set(DECISION_FIELDS)]
    check("decisions_fields_exact", "prompt_only", not wrong_fields, f"decisions with wrong field set: {wrong_fields}",
          [f"parameter_decisions.{k}" for k in wrong_fields])
    cv_mismatch, bad_dec, bad_verify, change_no_value = [], [], [], []
    for d in decs:
        if not isinstance(d, dict) or d.get("parameter_key") not in inv:
            continue
        item = inv[d["parameter_key"]]
        if d.get("current_value") != item["current_value"]:
            cv_mismatch.append(d["parameter_key"])
        dec = d.get("decision")
        allowed = {"change", "keep"} if item["category"] == "profile" else {"change", "keep", "verify"}
        if dec not in allowed:
            bad_dec.append(d["parameter_key"])
        if dec == "verify" and not any(c.get("current_value") is None for c in item.get("components", [])):
            bad_verify.append(d["parameter_key"])
        if dec == "change" and (d.get("suggested_value") in (None, "", item["current_value"])):
            change_no_value.append(d["parameter_key"])
    check("decisions_current_value_copied", "app_prompt", not cv_mismatch,
          f"current_value not copied exactly: {cv_mismatch}",
          [f"parameter_decisions.{k}.current_value" for k in cv_mismatch])
    check("decisions_values_valid", "prompt_only", not bad_dec, f"invalid decision value: {bad_dec}",
          [f"parameter_decisions.{k}.decision" for k in bad_dec])
    check("decisions_verify_rule", "prompt_only", not bad_verify, f"verify without null component: {bad_verify}",
          [f"parameter_decisions.{k}.decision" for k in bad_verify])
    check("decisions_change_has_value", "prompt_only", not change_no_value,
          f"change without a distinct suggested_value: {change_no_value}",
          [f"parameter_decisions.{k}.suggested_value" for k in change_no_value])

    # profile_recommendation
    pr = obj.get("profile_recommendation") if isinstance(obj.get("profile_recommendation"), dict) else {}
    pr_missing_required = [f for f in APP_REQUIRED_PROFILE_REC_FIELDS if not isinstance(pr.get(f), str)]
    check("profile_rec_required_fields", "app_schema", not pr_missing_required,
          f"profile_recommendation missing required field(s): {pr_missing_required}", ["profile_recommendation"])
    check("profile_rec_fields_exact", "prompt_only", set(pr.keys()) == set(PROFILE_REC_FIELDS),
          f"profile_recommendation fields: {sorted(pr.keys())}", ["profile_recommendation"])
    check("profile_rec_focus_valid", "app_prompt", pr.get("focus") in FOCUS_VALUES,
          f"profile_recommendation.focus={pr.get('focus')}", ["profile_recommendation.focus"])
    check("profile_rec_decision_valid", "prompt_only", pr.get("decision") in {"change", "keep"},
          f"profile_recommendation.decision={pr.get('decision')}", ["profile_recommendation.decision"])
    check("profile_rec_confidence_valid", "prompt_only", pr.get("confidence") in CONFIDENCE_VALUES,
          f"profile_recommendation.confidence={pr.get('confidence')}", ["profile_recommendation.confidence"])
    any_profile_change = any(isinstance(d, dict) and d.get("decision") == "change"
                             and inv.get(d.get("parameter_key"), {}).get("category") == "profile" for d in decs)
    expected_pr = "change" if any_profile_change else "keep"
    check("profile_rec_decision_consistent", "prompt_only", pr.get("decision") == expected_pr,
          f"profile_recommendation.decision={pr.get('decision')} but profile rows imply {expected_pr}",
          ["profile_recommendation.decision"])

    # meal_strategy_summary and recommendations (prompt-only)
    ms = obj.get("meal_strategy_summary") if isinstance(obj.get("meal_strategy_summary"), dict) else {}
    check("meal_fields_exact", "prompt_only", set(ms.keys()) == set(MEAL_FIELDS),
          f"meal_strategy_summary fields: {sorted(ms.keys())}", ["meal_strategy_summary"])
    exc = ms.get("exceptions")
    check("meal_exceptions_0_to_2", "prompt_only", isinstance(exc, list) and len(exc) <= 2,
          f"meal exceptions = {exc if not isinstance(exc, list) else len(exc)}", ["meal_strategy_summary.exceptions"])
    check("meal_confidence_valid", "prompt_only", ms.get("confidence") in CONFIDENCE_VALUES,
          f"meal_strategy_summary.confidence={ms.get('confidence')}", ["meal_strategy_summary.confidence"])
    recs = obj.get("recommendations") if isinstance(obj.get("recommendations"), list) else []
    bad_prio = [r.get("title") for r in recs if isinstance(r, dict) and r.get("priority") not in PRIORITY_VALUES]
    check("recommendations_priority_valid", "prompt_only", not bad_prio, f"bad priority: {bad_prio}",
          ["recommendations.priority"])

    by_tier = {t: [c for c, ok in checks.items() if not ok and tiers[c] == t]
               for t in ("app_prompt", "app_schema", "prompt_only")}
    passed = sum(checks.values())
    details = {"missing_keys": missing_keys, "extra_keys": extra_keys, "duplicate_keys": dup_keys,
               "current_value_mismatch": cv_mismatch,
               "focus_invalid": pr.get("focus") not in FOCUS_VALUES}
    return {"violations": v, "sections": sections, "details": details, "checks": checks, "tiers": tiers,
            "failed_by_tier": by_tier, "n_checks": len(checks), "n_passed": passed,
            "schema_score": round(passed / len(checks), 4) if checks else 0.0,
            "fully_compliant": not v,
            "app_schema_stop": bool(by_tier["app_schema"]),
            "app_needs_repair": bool(by_tier["app_prompt"]) and not by_tier["app_schema"],
            "app_accepted": not by_tier["app_prompt"] and not by_tier["app_schema"],
            "prompt_only_violations": by_tier["prompt_only"]}


def decision_diff(a: dict | None, b: dict | None) -> dict[str, Any]:
    """Compare parameter_decisions between two extracted outputs (first pass vs corrected)."""
    def table(o):
        if not o or not isinstance(o.get("parameter_decisions"), list):
            return {}
        return {d.get("parameter_key"): (d.get("decision"), str(d.get("suggested_value")))
                for d in o["parameter_decisions"] if isinstance(d, dict)}
    ta, tb = table(a), table(b)
    changed = sorted((k for k in set(ta) | set(tb) if ta.get(k) != tb.get(k)), key=str)
    decision_changed = sorted((k for k in changed
                               if (ta.get(k) or (None,))[0] != (tb.get(k) or (None,))[0]), key=str)
    pa = (a or {}).get("profile_recommendation") or {}
    pb = (b or {}).get("profile_recommendation") or {}
    return {"n_rows_changed": len(changed), "rows_changed": changed,
            "n_decision_changed": len(decision_changed), "decision_changed": decision_changed,
            "profile_focus_changed": pa.get("focus") != pb.get("focus"),
            "profile_decision_changed": pa.get("decision") != pb.get("decision")}
