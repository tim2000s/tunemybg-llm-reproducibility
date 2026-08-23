# TuneMyBG LLM reproducibility — plain-English summary

Package generated 2026-08-21 covering 2026-08-07 to 2026-08-21 (14 days). Glucose: mean 121.6 mg/dL, time in range 86.0%, below range 5.1%, CV 32.6%. Carb entries logged: 0.

Each run is a brand-new conversation: package attached with Prompt 1, then Prompts 2, 3 and 4 in turn, then the app's correction prompt once if the JSON failed the app's checks. AAPS defaults are from nightscout/AndroidAPS master @ 598e2eb (2026-08-02).

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
