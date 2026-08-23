# TuneMyBG LLM reproducibility — plain-English summary

Package generated 2026-08-21 covering 2026-08-07 to 2026-08-21 (14 days). Glucose: mean 121.6 mg/dL, time in range 86.0%, below range 5.1%, CV 32.6%. Carb entries logged: 0.

Each run is a brand-new conversation: package attached with Prompt 1, then Prompts 2, 3 and 4 in turn, then the app's correction prompt once if the JSON failed the app's checks. AAPS defaults are from nightscout/AndroidAPS master @ 598e2eb (2026-08-02).

## gpt-5.6-sol — 50 runs (`real_gpt56sol_med_50`)

Reasoning effort: medium.

### At a glance

- App outcome over 50 completed runs: accepted first time 50; accepted after the repair prompt 0; invalid JSON with no prompt offered 0; schema stop with no prompt offered 0; still rejected after repair 0. Dead ends (no way forward in the app): 0.
- Strict compliance with Prompt 4's own rules (which the app does not fully check): 50/50 (100%) of runs first time.
- Settings changed per run: 0–2 of 23 (most runs: 0).
- 34 settings were left unchanged in every single run; 2 were changed in at least one run, of which 0 were changed in more than half the runs.
- Headline profile recommendation focus: target in 39/50 (78%), basal in 11/50 (22%).
- Profile recommendation decision: keep ×32, change ×18.

### Changed in at least one run

Frequency is how many of the runs suggested a different value for that setting. Range is the spread of the suggested values across those runs.

| Setting | Current | AAPS default | Suggested change in | Suggested values | Direction |
|---|---|---|---|---|---|
| Profile / target 00:00 | 90 mg/dL | — | 18/50 (36%) | always 100 mg/dL | higher |
| Profile / target 23:00 | 90 mg/dL | — | 2/50 (4%) | always 100 mg/dL | higher |

### Kept unchanged in every run

- **Basal rates**: 00:00 0.6 U/h; 05:00 0.7 U/h; 06:00 0.8 U/h; 10:00 0.7 U/h; 16:00 0.5 U/h; 18:00 0.6 U/h; 19:00 0.7 U/h
- **Carb ratios**: 00:00 13 g/U; 04:00 11.1 g/U; 08:00 13.2 g/U; 16:00 10.5 g/U; 20:00 12.6 g/U
- **Insulin sensitivity**: 00:00 56 mg/dL/U
- **Targets**: 08:00 100 mg/dL
- **DIA**: 10 h
- **AAPS smb_uam**: smb_enabled = true; uam_enabled = true
- **AAPS smb_activation**: smb_always_enabled = true; smb_with_cob_enabled = false; smb_after_carbs_enabled = false; smb_with_temp_target_enabled = true; smb_with_high_temp_target_enabled = false
- **AAPS smb_delivery**: smb_interval_minutes = 3 min; max_smb_basal_minutes = 15 min; max_uam_smb_basal_minutes = 20 min
- **AAPS safety_limits**: max_basal_u_per_hour = 12 U/h; max_iob_units = 25 U
- **AAPS sensitivity**: autosens_enabled = false; dynamic_sensitivity_enabled = true; autosens_raises_target = false; autosens_lowers_target = false; dynamic_isf_adjustment_factor_percent = 70 %
- **AAPS carb_absorption**: min_5m_carbimpact = 8 mg/dL/5 min; meal_max_absorption_hours = 7 h

### Primary recommendation (first item the model listed)

By area: target ×28, basal ×9, profile ×8, safety_and_data ×2, data_and_profile ×2, safety ×1.

- Primary: review a higher 00:00 target ×3
- Keep the profile while verifying the overnight low pattern ×2
- Verify the overnight low pattern before changing the profile ×2
- Primary: keep the profile stable and verify the low pattern first ×1
- Review the 00:00 glucose target first ×1
- Primary: verify the context of recurrent lows before changing the profile ×1
- Primary: review the midnight target ×1
- Keep the profile and verify the overnight pattern first ×1
- … and 38 other titles
