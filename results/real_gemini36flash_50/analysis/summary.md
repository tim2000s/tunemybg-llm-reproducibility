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
