# TuneMyBG LLM reproducibility — plain-English summary

Package generated 2026-08-21 covering 2026-08-07 to 2026-08-21 (14 days). Glucose: mean 121.6 mg/dL, time in range 86.0%, below range 5.1%, CV 32.6%. Carb entries logged: 0.

Each run is a brand-new conversation: package attached with Prompt 1, then Prompts 2, 3 and 4 in turn, then the app's correction prompt once if the JSON failed the app's checks. AAPS defaults are from nightscout/AndroidAPS master @ 598e2eb (2026-08-02).

## claude-haiku-4-5 — 49 runs (`real_haiku45_50`)

### At a glance

- App outcome over 50 completed runs: accepted first time 17; accepted after the repair prompt 3; invalid JSON with no prompt offered 2; schema stop with no prompt offered 1; still rejected after repair 27. Dead ends (no way forward in the app): 3.
- Strict compliance with Prompt 4's own rules (which the app does not fully check): 2/49 (4%) of runs first time.
- Settings changed per run: 0–5 of 23 (most runs: 1).
- 18 settings were left unchanged in every single run; 18 were changed in at least one run, of which 0 were changed in more than half the runs.
- Headline profile recommendation focus: basal in 18/49 (37%), meal_bolus_and_carb_logging in 2/49 (4%), isf in 2/49 (4%), meal_bolus_strategy in 2/49 (4%), ISF in 1/49 (2%), overall_profile_sequencing in 1/49 (2%), basal, carb ratio, ISF, and DIA collectively in 1/49 (2%), carb logging, then isf verification in 1/49 (2%), carbohydrate_ratio_and_meal_strategy in 1/49 (2%), DIA (insulin duration) in 1/49 (2%), DIA shortening (safety priority), basal timing adjustment (safety priority), basal increase at 10:00 segment (medium priority, conditional on ISF verification) in 1/49 (2%), basal_and_targets_and_cr_and_isf_and_dia in 1/49 (2%), carb_ratio in 1/49 (2%), basal_and_meal_strategy_interaction in 1/49 (2%), meal_bolus_timing in 1/49 (2%), Basal, ISF, CR, and target settings. ISF inadequacy drives Dynamic ISF compensation and overcorrection lows; overnight basal excess drives hour 1 lows; afternoon CR looseness combined with GLP-1 absorption delay drives sustained highs. Overnight target too tight buffers low risk when ISF and basal adjusted. in 1/49 (2%), insulin_sensitivity_and_action_duration in 1/49 (2%), basal_and_isf in 1/49 (2%), None in 1/49 (2%), meal_bolus_strategy_and_afternoon_basal in 1/49 (2%), basal_carb_ratios_isf_dia in 1/49 (2%), DIA and meal_max_absorption_hours (carb and insulin absorption model parameters) in 1/49 (2%), basal and max_iob in 1/49 (2%), DIA (Duration of Insulin Action) in 1/49 (2%), basal_cr_isf_target in 1/49 (2%), meal_strategy_and_meal_absorption in 1/49 (2%), carb_ratio_daytime in 1/49 (2%), basal_target_cr_isf_dia in 1/49 (2%), basal and target at 00:00 in 1/49 (2%).
- Profile recommendation decision: change ×30, keep ×18, None ×1.

### Changed in at least one run

Frequency is how many of the runs suggested a different value for that setting. Range is the spread of the suggested values across those runs.

| Setting | Current | AAPS default | Suggested change in | Suggested values | Direction |
|---|---|---|---|---|---|
| Profile / basal 10:00 | 0.7 U/h | — | 11/49 (22%) | 0.8–0.9 U/h; most often 0.8 U/h (6 of 11); 3 distinct values | higher |
| Profile / basal 16:00 | 0.5 U/h | — | 11/49 (22%) | 0.6–0.8 U/h; most often 0.6 U/h (5 of 11); 4 distinct values | higher |
| Profile / basal 00:00 | 0.6 U/h | — | 7/49 (14%) | 0.5–0.55 U/h; most often 0.5 U/h (6 of 7); 2 distinct values | lower |
| Profile / ISF 00:00 | 56 mg/dL/U | — | 7/49 (14%) | 40–110 mg/dL/U; most often 40 mg/dL/U (2 of 7); 5 distinct values; 80-100 mg/dl/u ×1 | mixed |
| Profile / DIA | 10 h | — (AAPS defaultDIA = 5.0 h (Constants.kt)) | 6/49 (12%) | 5.5–8 h; most often 5.5 h (2 of 6); 4 distinct values; 5-6 h ×1 | lower |
| AAPS / carbohydrate absorption model / min_5m_carbimpact | 8 mg/dL/5 min | 8 mg/dL/5 min | 4/49 (8%) | 5–12 mg/dL/5 min; most often 12 mg/dL/5 min (2 of 4); 3 distinct values | mixed |
| AAPS / carbohydrate absorption model / meal_max_absorption_hours | 7 h | 6 h | 3/49 (6%) | 8–10 h; most often 8 h (1 of 3); 2 distinct values; 3-4 h ×1 | higher |
| AAPS / max basal and max IOB limits / max_iob_units | 25 U | 3.0 U (Simple Mode recalculates this from the profile) | 3/49 (6%) | 8–20 U; most often 8 U (1 of 3); 3 distinct values | lower |
| AAPS / Autosens and Dynamic ISF / dynamic_isf_adjustment_factor_percent | 70 % | 100 % | 3/49 (6%) | 50–85 %; most often 50 % (2 of 3); 2 distinct values | mixed |
| Profile / CR 08:00 | 13.2 g/U | — | 2/49 (4%) | 11.5–12.5 g/U; most often 11.5 g/U (1 of 2); 2 distinct values | lower |
| Profile / target 00:00 | 90 mg/dL | — | 2/49 (4%) | 95–100 mg/dL; most often 100 mg/dL (1 of 2); 2 distinct values | higher |
| AAPS / SMB activation conditions / smb_after_carbs_enabled | false | true | 1/49 (2%) | true ×1 | — |
| AAPS / SMB strength and frequency / max_smb_basal_minutes | 15 min | 30 min | 1/49 (2%) | always 10 min | lower |
| AAPS / SMB strength and frequency / max_uam_smb_basal_minutes | 20 min | 30 min | 1/49 (2%) | always 15 min | lower |
| Profile / basal 18:00 | 0.6 U/h | — | 1/49 (2%) | always 0.5 U/h | lower |
| Profile / basal 19:00 | 0.7 U/h | — | 1/49 (2%) | always 0.6 U/h | lower |
| Profile / CR 16:00 | 10.5 g/U | — | 1/49 (2%) | always 9.5 g/U | lower |
| Profile / target 23:00 | 90 mg/dL | — | 1/49 (2%) | always 100 mg/dL | higher |

### Kept unchanged in every run

- **Basal rates**: 05:00 0.7 U/h; 06:00 0.8 U/h
- **Carb ratios**: 00:00 13 g/U; 04:00 11.1 g/U; 20:00 12.6 g/U
- **Targets**: 08:00 100 mg/dL
- **AAPS smb_uam**: smb_enabled = true; uam_enabled = true
- **AAPS smb_activation**: smb_always_enabled = true; smb_with_cob_enabled = false; smb_with_temp_target_enabled = true; smb_with_high_temp_target_enabled = false
- **AAPS smb_delivery**: smb_interval_minutes = 3 min
- **AAPS safety_limits**: max_basal_u_per_hour = 12 U/h
- **AAPS sensitivity**: autosens_enabled = false; dynamic_sensitivity_enabled = true; autosens_raises_target = false; autosens_lowers_target = false

### Primary recommendation (first item the model listed)

By area: basal ×13, meal_bolus_strategy ×7, meal_strategy ×5, profile ×3, safety ×2, meal_logging ×2, carb_logging ×2, ISF ×1, Data and meal strategy ×1, meal strategy ×1, Carbohydrate logging (highest-leverage behavior change) ×1, dia ×1, behavioral_and_logging ×1, Data Integrity – ISF Verification ×1, isf ×1, meal_carbs ×1, profile_isf ×1, meal_detection_threshold ×1, profile_dia ×1, data_and_meal_documentation ×1, automation ×1, carbohydrate_logging_and_meal_strategy ×1.

- Correct ISF underestimation from 56 to 90 mg/dL/U ×1
- Restart carb logging immediately for 3 complete days ×1
- Reduce max_iob from 25 U to 6-8 U immediately ×1
- Enable carb logging (Nightscout treatment entries) immediately for all meals and snacks; log carb amount (grams) and meal time. Continue for minimum 7 days to establish baseline. ×1
- Reduce basal 00:00 from 0.6 U/h to 0.55 U/h or 0.5 U/h to address hour 1 lows (18.5% TBR, nadir 42–55 mg/dL). ×1
- Raise basal in 10:00–16:00 afternoon window to address persistent hyperglycemia. ×1
- Implement meal carbohydrate logging ×1
- Reduce overnight and evening basal segments to address recurrent hypoglycemia ×1
- … and 41 other titles
