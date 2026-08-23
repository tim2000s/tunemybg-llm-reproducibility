# TuneMyBG LLM reproducibility — plain-English summary

Package generated 2026-08-21 covering 2026-08-07 to 2026-08-21 (14 days). Glucose: mean 117.0 mg/dL, time in range 99.7%, below range 0.0%, CV 12.9%. Carb entries logged: 28.

Each run is a brand-new conversation: package attached with Prompt 1, then Prompts 2, 3 and 4 in turn, then the app's correction prompt once if the JSON failed the app's checks. AAPS defaults are from nightscout/AndroidAPS master @ 598e2eb (2026-08-02).

## gemini-3.6-flash — 50 runs (`gemini36flash_50`)

### At a glance

- App outcome over 50 completed runs: accepted first time 50; accepted after the repair prompt 0; invalid JSON with no prompt offered 0; schema stop with no prompt offered 0; still rejected after repair 0. Dead ends (no way forward in the app): 0.
- Strict compliance with Prompt 4's own rules (which the app does not fully check): 49/50 (98%) of runs first time.
- Settings changed per run: 0–0 of 22 (most runs: 0).
- 35 settings were left unchanged in every single run; 0 were changed in at least one run, of which 0 were changed in more than half the runs.
- Headline profile recommendation focus: basal in 40/50 (80%), cr in 10/50 (20%).
- Profile recommendation decision: keep ×50.

### Changed in at least one run

Frequency is how many of the runs suggested a different value for that setting. Range is the spread of the suggested values across those runs.

| Setting | Current | AAPS default | Suggested change in | Suggested values | Direction |
|---|---|---|---|---|---|

### Kept unchanged in every run

- **Basal rates**: 00:00 0.85 U/h; 06:00 0.95 U/h; 12:00 0.9 U/h; 18:00 1.05 U/h
- **Carb ratios**: 00:00 12 g/U; 06:00 10 g/U; 12:00 11 g/U; 18:00 9 g/U
- **Insulin sensitivity**: 00:00 48 mg/dL/U; 06:00 42 mg/dL/U; 12:00 45 mg/dL/U; 18:00 40 mg/dL/U
- **Targets**: 00:00 95-110 mg/dL; 06:00 90-105 mg/dL; 22:00 100-115 mg/dL
- **DIA**: 5.5 h
- **AAPS smb_uam**: smb_enabled = true; uam_enabled = true
- **AAPS smb_activation**: smb_always_enabled = None; smb_with_cob_enabled = None; smb_after_carbs_enabled = None; smb_with_temp_target_enabled = None; smb_with_high_temp_target_enabled = None
- **AAPS smb_delivery**: smb_interval_minutes = 3 min; max_smb_basal_minutes = 45 min; max_uam_smb_basal_minutes = 30 min
- **AAPS safety_limits**: max_basal_u_per_hour = 2.4 U/h; max_iob_units = 8 U
- **AAPS sensitivity**: autosens_enabled = None; dynamic_sensitivity_enabled = None; autosens_raises_target = None; autosens_lowers_target = None; dynamic_isf_adjustment_factor_percent = 100 %
- **AAPS carb_absorption**: min_5m_carbimpact = 3 mg/dL/5 min; meal_max_absorption_hours = 6 h

### Primary recommendation (first item the model listed)

By area: meal_strategy ×21, meal_bolus ×7, smb ×5, profile ×4, basal ×4, meal_timing ×3, aaps ×3, cr ×2, meal ×1.

- Optimize Prebolus Timing for Weekend Brunch ×5
- Optimize Weekend Brunch Prebolus Timing ×5
- Extend Prebolus Timing for Weekend Brunch ×5
- Maintain Current Profile Parameters ×2
- Maintain Current Profile and Automation Settings ×2
- Test Slightly Extended Prebolus for Weekend Brunch ×2
- Extend Prebolus Time for Weekday Breakfast ×1
- Optimize prebolus timing for weekend brunch ×1
- … and 27 other titles
