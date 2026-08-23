# TuneMyBG LLM reproducibility — plain-English summary

Package generated 2026-08-21 covering 2026-08-07 to 2026-08-21 (14 days). Glucose: mean 121.6 mg/dL, time in range 86.0%, below range 5.1%, CV 32.6%. Carb entries logged: 0.

Each run is a brand-new conversation: package attached with Prompt 1, then Prompts 2, 3 and 4 in turn, then the app's correction prompt once if the JSON failed the app's checks. AAPS defaults are from nightscout/AndroidAPS master @ 598e2eb (2026-08-02).

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
