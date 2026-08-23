"""AndroidAPS code defaults for the settings that appear in the TuneMyBG decision inventory.

Source: github.com/nightscout/AndroidAPS, master branch, commit 598e2eb (2026-08-02),
core/keys/src/main/kotlin/app/aaps/core/keys/{DoubleKey,IntKey,BooleanKey}.kt.
Profile rows (basal, CR, ISF, targets) are user-entered and have no code default.
"""

AAPS_SOURCE = "nightscout/AndroidAPS master @ 598e2eb (2026-08-02)"

# package component key -> (AAPS preference key, default, allowed range, note)
COMPONENT_DEFAULTS: dict[str, tuple[str, str, str, str]] = {
    "max_basal_u_per_hour": ("openapsma_max_basal", "1.0 U/h", "0.1–25",
                             "Simple Mode recalculates this from the profile"),
    "max_iob_units": ("openapsmb_max_iob", "3.0 U", "0–70",
                      "Simple Mode recalculates this from the profile"),
    "smb_interval_minutes": ("smbinterval", "3 min", "1–10", ""),
    "max_smb_basal_minutes": ("smbmaxminutes", "30 min", "15–120", ""),
    "max_uam_smb_basal_minutes": ("uamsmbmaxminutes", "30 min", "15–120", ""),
    "autosens_enabled": ("openapsama_useautosens", "true", "", "ignored when dynamic sensitivity is on"),
    "dynamic_sensitivity_enabled": ("use_dynamic_sensitivity", "false", "", ""),
    "autosens_raises_target": ("sensitivity_raises_target", "true", "", ""),
    "autosens_lowers_target": ("resistance_lowers_target", "true", "", ""),
    "dynamic_isf_adjustment_factor_percent": ("DynISFAdjust", "100 %", "1–300", ""),
    "smb_enabled": ("use_smb", "true", "", ""),
    "uam_enabled": ("use_uam", "true", "", ""),
    "smb_always_enabled": ("enableSMB_always", "true", "", ""),
    "smb_with_cob_enabled": ("enableSMB_with_COB", "true", "", ""),
    "smb_after_carbs_enabled": ("enableSMB_after_carbs", "true", "", ""),
    "smb_with_temp_target_enabled": ("enableSMB_with_temptarget", "true", "", ""),
    "smb_with_high_temp_target_enabled": ("enableSMB_with_high_temptarget", "false", "", ""),
    "min_5m_carbimpact": ("openaps_smb_min_5m_carbimpact", "8 mg/dL/5 min", "1–12", ""),
    "meal_max_absorption_hours": ("absorption_maxtime", "6 h", "4–10", ""),
}

# whole-parameter notes for profile rows
PROFILE_NOTES: dict[str, str] = {
    "profile.dia": "AAPS defaultDIA = 5.0 h (Constants.kt)",
}
# Temp-target limits (Constants.kt): MIN_TT_MGDL = 72, MAX_TT_MGDL = 180


def default_for(component_key: str) -> str:
    d = COMPONENT_DEFAULTS.get(component_key)
    return d[1] if d else "—"


def note_for(component_key: str) -> str:
    d = COMPONENT_DEFAULTS.get(component_key)
    return d[3] if d else ""
