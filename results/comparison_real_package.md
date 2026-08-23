# TuneMyBG LLM reproducibility — plain-English summary

Package generated 2026-08-21 covering 2026-08-07 to 2026-08-21 (14 days). Glucose: mean 121.6 mg/dL, time in range 86.0%, below range 5.1%, CV 32.6%. Carb entries logged: 0.

Each run is a brand-new conversation: package attached with Prompt 1, then Prompts 2, 3 and 4 in turn, then the app's correction prompt once if the JSON failed the app's checks. AAPS defaults are from nightscout/AndroidAPS master @ 598e2eb (2026-08-02).

## gemini-3.6-flash — 50 runs (`real_gemini36flash_50`)

### At a glance

- App outcome over 50 completed runs: accepted first time 50; accepted after the repair prompt 0; invalid JSON with no prompt offered 0; schema stop with no prompt offered 0; still rejected after repair 0. Dead ends (no way forward in the app): 0.
- Strict compliance with Prompt 4's own rules (which the app does not fully check): 46/50 (92%) of runs first time.
- Settings changed per run: 1–6 of 23 (most runs: 3).
- 26 settings were left unchanged in every single run; 10 were changed in at least one run, of which 4 were changed in more than half the runs.
- Headline profile recommendation focus: target in 39/50 (78%), basal in 11/50 (22%).
- Profile recommendation decision: change ×44, keep ×6.

### Changed in at least one run

Frequency is how many of the runs suggested a different value for that setting. Range is the spread of the suggested values across those runs.

| Setting | Current | AAPS default | Suggested change in | Suggested values | Direction |
|---|---|---|---|---|---|
| AAPS / max basal and max IOB limits / max_iob_units | 25 U | 3.0 U (Simple Mode recalculates this from the profile) | 49/50 (98%) | 4–15 U; most often 7 U (27 of 49); 7 distinct values | lower |
| AAPS / max basal and max IOB limits / max_basal_u_per_hour | 12 U/h | 1.0 U/h (Simple Mode recalculates this from the profile) | 48/50 (96%) | 2.5–4 U/h; most often 3.5 U/h (19 of 48); 5 distinct values | lower |
| Profile / target 00:00 | 90 mg/dL | — | 39/50 (78%) | always 100 mg/dL | higher |
| Profile / target 23:00 | 90 mg/dL | — | 39/50 (78%) | always 100 mg/dL | higher |
| AAPS / Autosens and Dynamic ISF / dynamic_isf_adjustment_factor_percent | 70 % | 100 % | 13/50 (26%) | always 50 % | lower |
| Profile / basal 00:00 | 0.6 U/h | — | 11/50 (22%) | always 0.5 U/h | lower |
| AAPS / SMB strength and frequency / max_uam_smb_basal_minutes | 20 min | 30 min | 4/50 (8%) | always 15 min | lower |
| Profile / basal 19:00 | 0.7 U/h | — | 3/50 (6%) | 0.5–0.6 U/h; most often 0.5 U/h (2 of 3); 2 distinct values | lower |
| AAPS / carbohydrate absorption model / min_5m_carbimpact | 8 mg/dL/5 min | 8 mg/dL/5 min | 1/50 (2%) | always 4 mg/dL/5 min | lower |
| Profile / basal 18:00 | 0.6 U/h | — | 1/50 (2%) | always 0.5 U/h | lower |

### Kept unchanged in every run

- **Basal rates**: 05:00 0.7 U/h; 06:00 0.8 U/h; 10:00 0.7 U/h; 16:00 0.5 U/h
- **Carb ratios**: 00:00 13 g/U; 04:00 11.1 g/U; 08:00 13.2 g/U; 16:00 10.5 g/U; 20:00 12.6 g/U
- **Insulin sensitivity**: 00:00 56 mg/dL/U
- **Targets**: 08:00 100 mg/dL
- **DIA**: 10 h
- **AAPS smb_uam**: smb_enabled = true; uam_enabled = true
- **AAPS smb_activation**: smb_always_enabled = true; smb_with_cob_enabled = false; smb_after_carbs_enabled = false; smb_with_temp_target_enabled = true; smb_with_high_temp_target_enabled = false
- **AAPS smb_delivery**: smb_interval_minutes = 3 min; max_smb_basal_minutes = 15 min
- **AAPS sensitivity**: autosens_enabled = false; dynamic_sensitivity_enabled = true; autosens_raises_target = false; autosens_lowers_target = false
- **AAPS carb_absorption**: meal_max_absorption_hours = 7 h

### Primary recommendation (first item the model listed)

By area: smb ×22, target ×16, safety_limits ×5, basal ×3, aaps ×3, safety ×1.

- Reduce AAPS Max IOB and Max Basal Safety Limits ×9
- Raise Overnight Target to 100 mg/dL ×7
- Reduce Max IOB and Max Basal Safety Limits ×5
- Tighten AAPS Max IOB and Max Basal Safety Limits ×4
- Raise Overnight Target to Reduce Nocturnal Hypoglycemia ×2
- Reduce Overnight Basal Rate ×2
- Raise Overnight Glucose Target ×2
- Reduce AAPS Automation Safety Caps ×1
- … and 18 other titles

## gemini-3.1-pro-preview — 50 runs (`real_gemini31pro_50`)

### At a glance

- App outcome over 50 completed runs: accepted first time 50; accepted after the repair prompt 0; invalid JSON with no prompt offered 0; schema stop with no prompt offered 0; still rejected after repair 0. Dead ends (no way forward in the app): 0.
- Strict compliance with Prompt 4's own rules (which the app does not fully check): 47/50 (94%) of runs first time.
- Settings changed per run: 1–4 of 23 (most runs: 3).
- 29 settings were left unchanged in every single run; 7 were changed in at least one run, of which 4 were changed in more than half the runs.
- Headline profile recommendation focus: target in 46/50 (92%), basal in 4/50 (8%).
- Profile recommendation decision: change ×45, keep ×5.

### Changed in at least one run

Frequency is how many of the runs suggested a different value for that setting. Range is the spread of the suggested values across those runs.

| Setting | Current | AAPS default | Suggested change in | Suggested values | Direction |
|---|---|---|---|---|---|
| AAPS / max basal and max IOB limits / max_iob_units | 25 U | 3.0 U (Simple Mode recalculates this from the profile) | 45/50 (90%) | 3–10 U; most often 7 U (16 of 45); 7 distinct values | lower |
| Profile / target 00:00 | 90 mg/dL | — | 45/50 (90%) | 100–110 mg/dL; most often 100 mg/dL (24 of 45); 2 distinct values | higher |
| Profile / target 23:00 | 90 mg/dL | — | 45/50 (90%) | 100–110 mg/dL; most often 100 mg/dL (24 of 45); 2 distinct values | higher |
| AAPS / max basal and max IOB limits / max_basal_u_per_hour | 12 U/h | 1.0 U/h (Simple Mode recalculates this from the profile) | 41/50 (82%) | 2.5–4 U/h; most often 3 U/h (29 of 41); 5 distinct values | lower |
| AAPS / SMB strength and frequency / smb_interval_minutes | 3 min | 3 min | 3/50 (6%) | 5–15 min; most often 15 min (2 of 3); 2 distinct values | higher |
| Profile / basal 00:00 | 0.6 U/h | — | 1/50 (2%) | always 0.5 U/h | lower |
| Profile / target 08:00 | 100 mg/dL | — | 1/50 (2%) | always 110 mg/dL | higher |

### Kept unchanged in every run

- **Basal rates**: 05:00 0.7 U/h; 06:00 0.8 U/h; 10:00 0.7 U/h; 16:00 0.5 U/h; 18:00 0.6 U/h; 19:00 0.7 U/h
- **Carb ratios**: 00:00 13 g/U; 04:00 11.1 g/U; 08:00 13.2 g/U; 16:00 10.5 g/U; 20:00 12.6 g/U
- **Insulin sensitivity**: 00:00 56 mg/dL/U
- **DIA**: 10 h
- **AAPS smb_uam**: smb_enabled = true; uam_enabled = true
- **AAPS smb_activation**: smb_always_enabled = true; smb_with_cob_enabled = false; smb_after_carbs_enabled = false; smb_with_temp_target_enabled = true; smb_with_high_temp_target_enabled = false
- **AAPS smb_delivery**: max_smb_basal_minutes = 15 min; max_uam_smb_basal_minutes = 20 min
- **AAPS sensitivity**: autosens_enabled = false; dynamic_sensitivity_enabled = true; autosens_raises_target = false; autosens_lowers_target = false; dynamic_isf_adjustment_factor_percent = 70 %
- **AAPS carb_absorption**: min_5m_carbimpact = 8 mg/dL/5 min; meal_max_absorption_hours = 7 h

### Primary recommendation (first item the model listed)

By area: target ×17, automation ×9, safety_limits ×8, aaps.core.safety_limits ×6, aaps ×4, safety ×3, automation_safety ×1, automation_sensitivity_limits ×1, limits ×1.

- Reduce AAPS Safety Limits ×3
- Reduce Max IOB and Max Basal Limits ×3
- Reduce Max IOB and Max Basal limits ×2
- Raise Overnight Target for Safety ×2
- Raise Overnight Glucose Targets ×2
- Restrict Max IOB and Max Basal ×2
- Create a safety buffer against overnight lows ×1
- Raise overnight glucose target for safety ×1
- … and 34 other titles

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

## gpt-5.4-mini — 50 runs (`real_gpt54mini_med_50`)

Reasoning effort: medium.

### At a glance

- App outcome over 50 completed runs: accepted first time 48; accepted after the repair prompt 0; invalid JSON with no prompt offered 1; schema stop with no prompt offered 0; still rejected after repair 1. Dead ends (no way forward in the app): 1.
- Strict compliance with Prompt 4's own rules (which the app does not fully check): 23/50 (46%) of runs first time.
- Settings changed per run: 0–1 of 23 (most runs: 0).
- 35 settings were left unchanged in every single run; 1 were changed in at least one run, of which 0 were changed in more than half the runs.
- Headline profile recommendation focus: basal in 49/50 (98%), cr in 1/50 (2%).
- Profile recommendation decision: keep ×48, change ×2.

### Changed in at least one run

Frequency is how many of the runs suggested a different value for that setting. Range is the spread of the suggested values across those runs.

| Setting | Current | AAPS default | Suggested change in | Suggested values | Direction |
|---|---|---|---|---|---|
| Profile / basal 00:00 | 0.6 U/h | — | 2/50 (4%) | always 0.55 U/h | lower |

### Kept unchanged in every run

- **Basal rates**: 05:00 0.7 U/h; 06:00 0.8 U/h; 10:00 0.7 U/h; 16:00 0.5 U/h; 18:00 0.6 U/h; 19:00 0.7 U/h
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

By area: basal ×34, profile ×13, basal_and_targets ×1, meal ×1, profile_and_data ×1.

- Keep the current profile unchanged and verify with fasting data first ×1
- Keep the current profile unchanged and verify with separated no-meal observations ×1
- Keep profile unchanged pending one fasting verification ×1
- Keep the current profile and verify with one focused test ×1
- Keep the current profile and verify with meal-linked observation first ×1
- Keep the current profile unchanged and verify with one clean fasting-like block ×1
- Keep the current profile unchanged and verify with a meal-logged day before any basal, CR, ISF, target, or DIA revision ×1
- Keep the current profile unchanged for now ×1
- … and 42 other titles

## claude-opus-5 — 19 runs (`real_opus5`)

### At a glance

- App outcome over 20 completed runs: accepted first time 10; accepted after the repair prompt 1; invalid JSON with no prompt offered 9; schema stop with no prompt offered 0; still rejected after repair 0. Dead ends (no way forward in the app): 9.
- Strict compliance with Prompt 4's own rules (which the app does not fully check): 5/19 (26%) of runs first time.
- Settings changed per run: 1–3 of 23 (most runs: 1).
- 31 settings were left unchanged in every single run; 5 were changed in at least one run, of which 1 were changed in more than half the runs.
- Headline profile recommendation focus: basal in 13/19 (68%), dia in 3/19 (16%), isf in 3/19 (16%).
- Profile recommendation decision: keep ×19.

### Changed in at least one run

Frequency is how many of the runs suggested a different value for that setting. Range is the spread of the suggested values across those runs.

| Setting | Current | AAPS default | Suggested change in | Suggested values | Direction |
|---|---|---|---|---|---|
| AAPS / max basal and max IOB limits / max_iob_units | 25 U | 3.0 U (Simple Mode recalculates this from the profile) | 15/19 (79%) | 6–10 U; most often 8 U (8 of 15); 4 distinct values; a reachable backstop with clear headroom above the observed peak of 5.94 u, for example 8-10 u, to be confirmed with the care team ×1 | lower |
| AAPS / Autosens and Dynamic ISF / dynamic_isf_adjustment_factor_percent | 70 % | 100 % | 6/19 (32%) | 55–60 %; most often 60 % (5 of 6); 2 distinct values | lower |
| AAPS / SMB strength and frequency / max_uam_smb_basal_minutes | 20 min | 30 min | 4/19 (21%) | always 15 min | lower |
| AAPS / max basal and max IOB limits / max_basal_u_per_hour | 12 U/h | 1.0 U/h (Simple Mode recalculates this from the profile) | 2/19 (11%) | 4–5 U/h; most often 4 U/h (1 of 2); 2 distinct values | lower |
| AAPS / SMB strength and frequency / smb_interval_minutes | 3 min | 3 min | 1/19 (5%) | always 5 min | higher |

### Kept unchanged in every run

- **Basal rates**: 00:00 0.6 U/h; 05:00 0.7 U/h; 06:00 0.8 U/h; 10:00 0.7 U/h; 16:00 0.5 U/h; 18:00 0.6 U/h; 19:00 0.7 U/h
- **Carb ratios**: 00:00 13 g/U; 04:00 11.1 g/U; 08:00 13.2 g/U; 16:00 10.5 g/U; 20:00 12.6 g/U
- **Insulin sensitivity**: 00:00 56 mg/dL/U
- **Targets**: 00:00 90 mg/dL; 08:00 100 mg/dL; 23:00 90 mg/dL
- **DIA**: 10 h
- **AAPS smb_uam**: smb_enabled = true; uam_enabled = true
- **AAPS smb_activation**: smb_always_enabled = true; smb_with_cob_enabled = false; smb_after_carbs_enabled = false; smb_with_temp_target_enabled = true; smb_with_high_temp_target_enabled = false
- **AAPS smb_delivery**: max_smb_basal_minutes = 15 min
- **AAPS sensitivity**: autosens_enabled = false; dynamic_sensitivity_enabled = true; autosens_raises_target = false; autosens_lowers_target = false
- **AAPS carb_absorption**: min_5m_carbimpact = 8 mg/dL/5 min; meal_max_absorption_hours = 7 h

### Primary recommendation (first item the model listed)

By area: smb ×14, isf ×3, safety_limits ×1, meal ×1.

- Primary: review the max IOB ceiling as the first and only change this cycle ×1
- Reduce the maximum insulin-on-board ceiling as the single first change ×1
- Primary: discuss reducing the unannounced-meal microbolus ceiling as the single first change ×1
- Discuss reducing max IOB as the first, independent step ×1
- Reduce the maximum insulin-on-board ceiling to a value that can actually act ×1
- Discuss tightening the maximum insulin on board ceiling as the single primary change ×1
- Primary: reduce the dynamic ISF adjustment factor as the single first change ×1
- Primary: discuss aligning the UAM microbolus basal-minutes cap with the non-UAM cap ×1
- … and 11 other titles

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

## x-ai/grok-4.6 — 50 runs (`real_grok46_50`)

### At a glance

- App outcome over 50 completed runs: accepted first time 50; accepted after the repair prompt 0; invalid JSON with no prompt offered 0; schema stop with no prompt offered 0; still rejected after repair 0. Dead ends (no way forward in the app): 0.
- Strict compliance with Prompt 4's own rules (which the app does not fully check): 49/50 (98%) of runs first time.
- Settings changed per run: 0–2 of 23 (most runs: 0).
- 34 settings were left unchanged in every single run; 2 were changed in at least one run, of which 0 were changed in more than half the runs.
- Headline profile recommendation focus: target in 33/50 (66%), basal in 17/50 (34%).
- Profile recommendation decision: keep ×40, change ×10.

### Changed in at least one run

Frequency is how many of the runs suggested a different value for that setting. Range is the spread of the suggested values across those runs.

| Setting | Current | AAPS default | Suggested change in | Suggested values | Direction |
|---|---|---|---|---|---|
| Profile / target 00:00 | 90 mg/dL | — | 10/50 (20%) | always 100 mg/dL | higher |
| Profile / target 23:00 | 90 mg/dL | — | 6/50 (12%) | always 100 mg/dL | higher |

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

By area: target ×33, basal ×16, profile ×1.

- Keep the profile and first separate overnight lows from leftover IOB ×2
- Keep the profile and do not add insulin for afternoon highs ×1
- Review raising only the 00:00 target from 90 to 100 mg/dL ×1
- Keep the profile and first separate overnight IOB from target and basal ×1
- Keep the profile and separate leftover IOB from overnight landing ×1
- Keep the current profile and verify nights without leftover meal IOB ×1
- Keep the overnight profile and compare midnight IOB with overnight lows ×1
- Keep the profile and verify overnight lows against leftover IOB ×1
- … and 41 other titles

## meta-llama/llama-4-maverick — 49 runs (`real_llama4maverick_50`)

### At a glance

- App outcome over 50 completed runs: accepted first time 19; accepted after the repair prompt 25; invalid JSON with no prompt offered 2; schema stop with no prompt offered 0; still rejected after repair 4. Dead ends (no way forward in the app): 2.
- Strict compliance with Prompt 4's own rules (which the app does not fully check): 19/49 (39%) of runs first time.
- Settings changed per run: 0–4 of 23 (most runs: 1).
- 28 settings were left unchanged in every single run; 8 were changed in at least one run, of which 1 were changed in more than half the runs.
- Headline profile recommendation focus: basal in 43/49 (88%), isf in 4/49 (8%), cr in 1/49 (2%), max_iob_units in 1/49 (2%).
- Profile recommendation decision: change ×32, keep ×17.

### Changed in at least one run

Frequency is how many of the runs suggested a different value for that setting. Range is the spread of the suggested values across those runs.

| Setting | Current | AAPS default | Suggested change in | Suggested values | Direction |
|---|---|---|---|---|---|
| Profile / basal 00:00 | 0.6 U/h | — | 27/49 (55%) | 0.55–0.65 U/h; most often 0.65 U/h (19 of 27); 2 distinct values | mixed |
| AAPS / max basal and max IOB limits / max_iob_units | 25 U | 3.0 U (Simple Mode recalculates this from the profile) | 19/49 (39%) | 15–20 U; most often 15 U (12 of 19); 2 distinct values | lower |
| Profile / ISF 00:00 | 56 mg/dL/U | — | 4/49 (8%) | 50–55 mg/dL/U; most often 50 mg/dL/U (3 of 4); 2 distinct values | lower |
| Profile / basal 16:00 | 0.5 U/h | — | 2/49 (4%) | 0.55–0.6 U/h; most often 0.55 U/h (1 of 2); 2 distinct values | higher |
| Profile / CR 00:00 | 13 g/U | — | 2/49 (4%) | always 12.5 g/U | lower |
| AAPS / max basal and max IOB limits / max_basal_u_per_hour | 12 U/h | 1.0 U/h (Simple Mode recalculates this from the profile) | 1/49 (2%) | always 10 U/h | lower |
| Profile / basal 05:00 | 0.7 U/h | — | 1/49 (2%) | always 0.65 U/h | lower |
| Profile / basal 06:00 | 0.8 U/h | — | 1/49 (2%) | always 0.75 U/h | lower |

### Kept unchanged in every run

- **Basal rates**: 10:00 0.7 U/h; 18:00 0.6 U/h; 19:00 0.7 U/h
- **Carb ratios**: 04:00 11.1 g/U; 08:00 13.2 g/U; 16:00 10.5 g/U; 20:00 12.6 g/U
- **Targets**: 00:00 90 mg/dL; 08:00 100 mg/dL; 23:00 90 mg/dL
- **DIA**: 10 h
- **AAPS smb_uam**: smb_enabled = true; uam_enabled = true
- **AAPS smb_activation**: smb_always_enabled = true; smb_with_cob_enabled = false; smb_after_carbs_enabled = false; smb_with_temp_target_enabled = true; smb_with_high_temp_target_enabled = false
- **AAPS smb_delivery**: smb_interval_minutes = 3 min; max_smb_basal_minutes = 15 min; max_uam_smb_basal_minutes = 20 min
- **AAPS sensitivity**: autosens_enabled = false; dynamic_sensitivity_enabled = true; autosens_raises_target = false; autosens_lowers_target = false; dynamic_isf_adjustment_factor_percent = 70 %
- **AAPS carb_absorption**: min_5m_carbimpact = 8 mg/dL/5 min; meal_max_absorption_hours = 7 h

### Primary recommendation (first item the model listed)

By area: basal ×26, AAPS safety limits ×6, AAPS ×5, profile ×5, meal strategy ×3, Meal Logging ×1, meal logging ×1, Meal Strategy ×1.

- Adjust basal rates ×6
- Adjust max IOB ×5
- Verify basal rates ×4
- Review basal rates ×3
- Verify and adjust basal rates ×2
- Start logging meal data ×2
- Reduce max IOB ×2
- Adjust max IOB to a safer limit ×2
- … and 20 other titles

## Model comparison — how often each setting was changed

| Setting | Current | AAPS default | gemini-3.6-flash | gemini-3.1-pro-preview | gemini-3.5-flash-lite | gpt-5.6-sol | gpt-5.4-mini | claude-opus-5 | claude-sonnet-5 | claude-haiku-4-5 | deepseek/deepseek-v4-pro | x-ai/grok-4.6 | meta-llama/llama-4-maverick |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AAPS / max basal and max IOB limits / max_iob_units | 25 U | 3.0 U | 98% (4–15) | 90% (3–10) | 16% (6–15) | never | never | 79% (6–10) | never | 6% (8–20) | 44% (2–12) | never | 39% (15–20) |
| AAPS / max basal and max IOB limits / max_basal_u_per_hour | 12 U/h | 1.0 U/h | 96% (2.5–4) | 82% (2.5–4) | never | never | never | 11% (4–5) | never | never | 18% (2–4) | never | 2% (10) |
| Profile / target 00:00 | 90 mg/dL | — | 78% (100) | 90% (100–110) | 2% (95) | 36% (100) | never | never | never | 4% (95–100) | 2% (100) | 20% (100) | never |
| Profile / target 23:00 | 90 mg/dL | — | 78% (100) | 90% (100–110) | never | 4% (100) | never | never | never | 2% (100) | 2% (100) | 12% (100) | never |
| AAPS / Autosens and Dynamic ISF / dynamic_isf_adjustment_factor_percent | 70 % | 100 % | 26% (50) | never | never | never | never | 32% (55–60) | never | 6% (50–85) | 18% (0–100) | never | never |
| Profile / basal 00:00 | 0.6 U/h | — | 22% (0.5) | 2% (0.5) | 10% (0.5) | never | 4% (0.55) | never | never | 14% (0.5–0.55) | 44% (0.5–0.55) | never | 55% (0.55–0.65) |
| AAPS / SMB strength and frequency / max_uam_smb_basal_minutes | 20 min | 30 min | 8% (15) | never | never | never | never | 21% (15) | never | 2% (15) | 10% (10–15) | never | never |
| Profile / basal 19:00 | 0.7 U/h | — | 6% (0.5–0.6) | never | never | never | never | never | never | 2% (0.6) | 4% (0.6) | never | never |
| AAPS / carbohydrate absorption model / min_5m_carbimpact | 8 mg/dL/5 min | 8 mg/dL/5 min | 2% (4) | never | never | never | never | never | never | 8% (5–12) | 6% (3–5) | never | never |
| Profile / basal 18:00 | 0.6 U/h | — | 2% (0.5) | never | never | never | never | never | never | 2% (0.5) | never | never | never |
| AAPS / SMB strength and frequency / smb_interval_minutes | 3 min | 3 min | never | 6% (5–15) | never | never | never | 5% (5) | never | never | 2% (10) | never | never |
| Profile / target 08:00 | 100 mg/dL | — | never | 2% (110) | never | never | never | never | never | never | never | never | never |
| Profile / basal 16:00 | 0.5 U/h | — | never | never | never | never | never | never | 5% (approximately 0.6 u/h (modest increase, verify stepwise)) | 22% (0.6–0.8) | never | never | 4% (0.55–0.6) |
| Profile / basal 10:00 | 0.7 U/h | — | never | never | never | never | never | never | never | 22% (0.8–0.9) | never | never | never |
| Profile / ISF 00:00 | 56 mg/dL/U | — | never | never | never | never | never | never | never | 14% (40–110) | 40% (30–180) | never | 8% (50–55) |
| Profile / DIA | 10 h | — | never | never | never | never | never | never | never | 12% (5.5–8) | 16% (5–8) | never | never |
| AAPS / carbohydrate absorption model / meal_max_absorption_hours | 7 h | 6 h | never | never | never | never | never | never | never | 6% (8–10) | 2% (5) | never | never |
| Profile / CR 08:00 | 13.2 g/U | — | never | never | never | never | never | never | never | 4% (11.5–12.5) | never | never | never |
| AAPS / SMB activation conditions / smb_after_carbs_enabled | false | true | never | never | never | never | never | never | never | 2% (true) | never | never | never |
| AAPS / SMB strength and frequency / max_smb_basal_minutes | 15 min | 30 min | never | never | never | never | never | never | never | 2% (10) | 2% (10) | never | never |
| Profile / CR 16:00 | 10.5 g/U | — | never | never | never | never | never | never | never | 2% (9.5) | never | never | never |
| AAPS / SMB activation conditions / smb_always_enabled | true | true | never | never | never | never | never | never | never | never | 2% (false) | never | never |
| AAPS / SMB activation conditions / smb_with_temp_target_enabled | true | true | never | never | never | never | never | never | never | never | 2% (false) | never | never |
| AAPS / SMB and UAM / uam_enabled | true | true | never | never | never | never | never | never | never | never | 2% (false) | never | never |
| Profile / basal 05:00 | 0.7 U/h | — | never | never | never | never | never | never | never | never | 2% (0.6) | never | 2% (0.65) |
| Profile / CR 00:00 | 13 g/U | — | never | never | never | never | never | never | never | never | never | never | 4% (12.5) |
| Profile / basal 06:00 | 0.8 U/h | — | never | never | never | never | never | never | never | never | never | never | 2% (0.75) |
