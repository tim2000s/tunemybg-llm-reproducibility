# TuneMyBG LLM reproducibility — plain-English summary

Package generated 2026-08-21 covering 2026-08-07 to 2026-08-21 (14 days). Glucose: mean 121.6 mg/dL, time in range 86.0%, below range 5.1%, CV 32.6%. Carb entries logged: 0.

Each run is a brand-new conversation: package attached with Prompt 1, then Prompts 2, 3 and 4 in turn, then the app's correction prompt once if the JSON failed the app's checks. AAPS defaults are from nightscout/AndroidAPS master @ 598e2eb (2026-08-02).

## claude-sonnet-5 — 20 runs (`real_sonnet5_20`)

### At a glance

- App outcome over 20 completed runs: accepted first time 18; accepted after the repair prompt 1; invalid JSON with no prompt offered 1; schema stop with no prompt offered 0; still rejected after repair 0. Dead ends (no way forward in the app): 1.
- Strict compliance with Prompt 4's own rules (which the app does not fully check): 16/20 (80%) of runs first time.
- Settings changed per run: 0–1 of 23 (most runs: 0).
- 35 settings were left unchanged in every single run; 1 were changed in at least one run, of which 0 were changed in more than half the runs.
- Headline profile recommendation focus: basal in 14/20 (70%), target in 3/20 (15%), dia in 2/20 (10%), cr in 1/20 (5%).
- Profile recommendation decision: keep ×19, change ×1.

### Changed in at least one run

Frequency is how many of the runs suggested a different value for that setting. Range is the spread of the suggested values across those runs.

| Setting | Current | AAPS default | Suggested change in | Suggested values | Direction |
|---|---|---|---|---|---|
| Profile / basal 16:00 | 0.5 U/h | — | 1/20 (5%) | approximately 0.6 u/h (modest increase, verify stepwise) ×1 | — |

### Kept unchanged in every run

- **Basal rates**: 00:00 0.6 U/h; 05:00 0.7 U/h; 06:00 0.8 U/h; 10:00 0.7 U/h; 18:00 0.6 U/h; 19:00 0.7 U/h
- **Carb ratios**: 00:00 13 g/U; 04:00 11.1 g/U; 08:00 13.2 g/U; 16:00 10.5 g/U; 20:00 12.6 g/U
- **Insulin sensitivity**: 00:00 56 mg/dL/U
- **Targets**: 00:00 90 mg/dL; 08:00 100 mg/dL; 23:00 90 mg/dL
- **DIA**: 10 h
- **AAPS smb_uam**: smb_enabled = true; uam_enabled = true
- **AAPS smb_activation**: smb_always_enabled = true; smb_with_cob_enabled = false; smb_after_carbs_enabled = false; smb_with_temp_target_enabled = true; smb_with_high_temp_target_enabled = false
- **AAPS smb_delivery**: smb_interval_minutes = 3 min; max_smb_basal_minutes = 15 min; max_uam_smb_basal_minutes = 20 min
- **AAPS safety_limits**: max_basal_u_per_hour = 12 U/h; max_iob_units = 25 U
- **AAPS sensitivity**: autosens_enabled = false; dynamic_sensitivity_enabled = true; autosens_raises_target = false; autosens_lowers_target = false; dynamic_isf_adjustment_factor_percent = 70 %
- **AAPS carb_absorption**: min_5m_carbimpact = 8 mg/dL/5 min; meal_max_absorption_hours = 7 h

### Primary recommendation (first item the model listed)

By area: meal ×6, safety ×3, data ×2, basal ×2, dia ×2, target ×1, cr ×1, data_quality ×1, safety_iob ×1, data_logging ×1.

- Prioritize understanding recurrent overnight hypoglycemia before any other change ×1
- Begin logging carbohydrate and e-carb entries ×1
- Begin logging carbohydrate intake to resolve competing explanations ×1
- Establish basic carbohydrate logging before further profile or automation changes ×1
- Clarify the effective maximum basal ceiling before any basal change ×1
- Establish carbohydrate logging before further profile or automation changes ×1
- Investigate the recurring correction-then-delayed-hypoglycemia pattern before any other change ×1
- Establish basic carbohydrate logging at recurring meal windows ×1
- … and 12 other titles
