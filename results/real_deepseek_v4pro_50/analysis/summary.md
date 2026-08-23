# TuneMyBG LLM reproducibility — plain-English summary

Package generated 2026-08-21 covering 2026-08-07 to 2026-08-21 (14 days). Glucose: mean 121.6 mg/dL, time in range 86.0%, below range 5.1%, CV 32.6%. Carb entries logged: 0.

Each run is a brand-new conversation: package attached with Prompt 1, then Prompts 2, 3 and 4 in turn, then the app's correction prompt once if the JSON failed the app's checks. AAPS defaults are from nightscout/AndroidAPS master @ 598e2eb (2026-08-02).

## deepseek/deepseek-v4-pro — 50 runs (`real_deepseek_v4pro_50`)

### At a glance

- App outcome over 50 completed runs: accepted first time 45; accepted after the repair prompt 3; invalid JSON with no prompt offered 0; schema stop with no prompt offered 2; still rejected after repair 0. Dead ends (no way forward in the app): 2.
- Strict compliance with Prompt 4's own rules (which the app does not fully check): 33/50 (66%) of runs first time.
- Settings changed per run: 0–6 of 23 (most runs: 2).
- 18 settings were left unchanged in every single run; 18 were changed in at least one run, of which 0 were changed in more than half the runs.
- Headline profile recommendation focus: basal in 28/50 (56%), isf in 17/50 (34%), dia in 4/50 (8%), target in 1/50 (2%).
- Profile recommendation decision: change ×39, keep ×11.

### Changed in at least one run

Frequency is how many of the runs suggested a different value for that setting. Range is the spread of the suggested values across those runs.

| Setting | Current | AAPS default | Suggested change in | Suggested values | Direction |
|---|---|---|---|---|---|
| AAPS / max basal and max IOB limits / max_iob_units | 25 U | 3.0 U (Simple Mode recalculates this from the profile) | 22/50 (44%) | 2–12 U; most often 5 U (7 of 22); 7 distinct values | lower |
| Profile / basal 00:00 | 0.6 U/h | — | 22/50 (44%) | 0.5–0.55 U/h; most often 0.5 U/h (20 of 22); 2 distinct values | lower |
| Profile / ISF 00:00 | 56 mg/dL/U | — | 20/50 (40%) | 30–180 mg/dL/U; most often 70 mg/dL/U (5 of 20); 14 distinct values | mixed |
| AAPS / max basal and max IOB limits / max_basal_u_per_hour | 12 U/h | 1.0 U/h (Simple Mode recalculates this from the profile) | 9/50 (18%) | 2–4 U/h; most often 4 U/h (4 of 9); 3 distinct values | lower |
| AAPS / Autosens and Dynamic ISF / dynamic_isf_adjustment_factor_percent | 70 % | 100 % | 9/50 (18%) | 0–100 %; most often 100 % (4 of 9); 5 distinct values | mixed |
| Profile / DIA | 10 h | — (AAPS defaultDIA = 5.0 h (Constants.kt)) | 8/50 (16%) | 5–8 h; most often 6 h (4 of 8); 4 distinct values | lower |
| AAPS / SMB strength and frequency / max_uam_smb_basal_minutes | 20 min | 30 min | 5/50 (10%) | 10–15 min; most often 15 min (3 of 5); 2 distinct values | lower |
| AAPS / carbohydrate absorption model / min_5m_carbimpact | 8 mg/dL/5 min | 8 mg/dL/5 min | 3/50 (6%) | 3–5 mg/dL/5 min; most often 5 mg/dL/5 min (2 of 3); 2 distinct values | lower |
| Profile / basal 19:00 | 0.7 U/h | — | 2/50 (4%) | always 0.6 U/h | lower |
| AAPS / carbohydrate absorption model / meal_max_absorption_hours | 7 h | 6 h | 1/50 (2%) | always 5 h | lower |
| AAPS / SMB activation conditions / smb_always_enabled | true | true | 1/50 (2%) | false ×1 | — |
| AAPS / SMB activation conditions / smb_with_temp_target_enabled | true | true | 1/50 (2%) | false ×1 | — |
| AAPS / SMB strength and frequency / smb_interval_minutes | 3 min | 3 min | 1/50 (2%) | always 10 min | higher |
| AAPS / SMB strength and frequency / max_smb_basal_minutes | 15 min | 30 min | 1/50 (2%) | always 10 min | lower |
| AAPS / SMB and UAM / uam_enabled | true | true | 1/50 (2%) | false ×1 | — |
| Profile / basal 05:00 | 0.7 U/h | — | 1/50 (2%) | always 0.6 U/h | lower |
| Profile / target 00:00 | 90 mg/dL | — | 1/50 (2%) | always 100 mg/dL | higher |
| Profile / target 23:00 | 90 mg/dL | — | 1/50 (2%) | always 100 mg/dL | higher |

### Kept unchanged in every run

- **Basal rates**: 06:00 0.8 U/h; 10:00 0.7 U/h; 16:00 0.5 U/h; 18:00 0.6 U/h
- **Carb ratios**: 00:00 13 g/U; 04:00 11.1 g/U; 08:00 13.2 g/U; 16:00 10.5 g/U; 20:00 12.6 g/U
- **Targets**: 08:00 100 mg/dL
- **AAPS smb_uam**: smb_enabled = true
- **AAPS smb_activation**: smb_with_cob_enabled = false; smb_after_carbs_enabled = false; smb_with_high_temp_target_enabled = false
- **AAPS sensitivity**: autosens_enabled = false; dynamic_sensitivity_enabled = true; autosens_raises_target = false; autosens_lowers_target = false

### Primary recommendation (first item the model listed)

By area: basal ×18, isf ×16, aaps_safety_limits ×2, dia ×2, meal_strategy ×1, data_foundation ×1, aaps_safety ×1, aaps ×1, automation_sensitivity_limits ×1, uam_aggressiveness ×1, UAM SMB delivery ×1, automation_sensitivity ×1, meal ×1, target ×1, aaps_uam ×1.

- Reduce overnight basal rate ×6
- Increase Insulin Sensitivity Factor (ISF) ×2
- Reduce overnight basal rate 00:00-05:00 ×2
- Begin carbohydrate entries for all meals ×1
- Reduce overnight basal (00:00–05:00) ×1
- Record all carbohydrate intake consistently ×1
- Correct Insulin Sensitivity Factor (ISF) ×1
- Reduce overnight basal rate (00:00–05:00) ×1
- … and 34 other titles
