# TuneMyBG LLM reproducibility — plain-English summary

Package generated 2026-08-21 covering 2026-08-07 to 2026-08-21 (14 days). Glucose: mean 121.6 mg/dL, time in range 86.0%, below range 5.1%, CV 32.6%. Carb entries logged: 0.

Each run is a brand-new conversation: package attached with Prompt 1, then Prompts 2, 3 and 4 in turn, then the app's correction prompt once if the JSON failed the app's checks. AAPS defaults are from nightscout/AndroidAPS master @ 598e2eb (2026-08-02).

## gemini-3.5-flash-lite — 49 runs (`real_gemini35flashlite_50`)

### At a glance

- App outcome over 50 completed runs: accepted first time 38; accepted after the repair prompt 1; invalid JSON with no prompt offered 10; schema stop with no prompt offered 1; still rejected after repair 0. Dead ends (no way forward in the app): 11.
- Strict compliance with Prompt 4's own rules (which the app does not fully check): 32/49 (65%) of runs first time.
- Settings changed per run: 0–2 of 23 (most runs: 0).
- 33 settings were left unchanged in every single run; 3 were changed in at least one run, of which 0 were changed in more than half the runs.
- Headline profile recommendation focus: basal in 41/49 (84%), isf in 3/49 (6%), dia in 2/49 (4%), cr in 2/49 (4%), target in 1/49 (2%).
- Profile recommendation decision: keep ×43, change ×6.

### Changed in at least one run

Frequency is how many of the runs suggested a different value for that setting. Range is the spread of the suggested values across those runs.

| Setting | Current | AAPS default | Suggested change in | Suggested values | Direction |
|---|---|---|---|---|---|
| AAPS / max basal and max IOB limits / max_iob_units | 25 U | 3.0 U (Simple Mode recalculates this from the profile) | 8/49 (16%) | 6–15 U; most often 6 U (5 of 8); 4 distinct values | lower |
| Profile / basal 00:00 | 0.6 U/h | — | 5/49 (10%) | always 0.5 U/h | lower |
| Profile / target 00:00 | 90 mg/dL | — | 1/49 (2%) | always 95 mg/dL | higher |

### Kept unchanged in every run

- **Basal rates**: 05:00 0.7 U/h; 06:00 0.8 U/h; 10:00 0.7 U/h; 16:00 0.5 U/h; 18:00 0.6 U/h; 19:00 0.7 U/h
- **Carb ratios**: 00:00 13 g/U; 04:00 11.1 g/U; 08:00 13.2 g/U; 16:00 10.5 g/U; 20:00 12.6 g/U
- **Insulin sensitivity**: 00:00 56 mg/dL/U
- **Targets**: 08:00 100 mg/dL; 23:00 90 mg/dL
- **DIA**: 10 h
- **AAPS smb_uam**: smb_enabled = true; uam_enabled = true
- **AAPS smb_activation**: smb_always_enabled = true; smb_with_cob_enabled = false; smb_after_carbs_enabled = false; smb_with_temp_target_enabled = true; smb_with_high_temp_target_enabled = false
- **AAPS smb_delivery**: smb_interval_minutes = 3 min; max_smb_basal_minutes = 15 min; max_uam_smb_basal_minutes = 20 min
- **AAPS safety_limits**: max_basal_u_per_hour = 12 U/h
- **AAPS sensitivity**: autosens_enabled = false; dynamic_sensitivity_enabled = true; autosens_raises_target = false; autosens_lowers_target = false; dynamic_isf_adjustment_factor_percent = 70 %
- **AAPS carb_absorption**: min_5m_carbimpact = 8 mg/dL/5 min; meal_max_absorption_hours = 7 h

### Primary recommendation (first item the model listed)

By area: basal ×22, meal ×7, cr ×6, smb ×5, aaps ×5, meal_strategy ×1, profile ×1, target ×1, safety ×1.

- Review Max IOB Safety Limit ×4
- Verify Overnight Basal Rates ×3
- Initiate Carbohydrate Logging ×3
- Introduce Manual Carbohydrate Logging ×3
- Verify Overnight Basal and Fasting Stability ×3
- Reduce Overnight Basal Rates ×2
- Reduce Max IOB Safety Limit ×2
- Reduce Max IOB Limit for Safety ×2
- … and 27 other titles
