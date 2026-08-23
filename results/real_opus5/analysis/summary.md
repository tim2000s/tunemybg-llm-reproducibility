# TuneMyBG LLM reproducibility — plain-English summary

Package generated 2026-08-21 covering 2026-08-07 to 2026-08-21 (14 days). Glucose: mean 121.6 mg/dL, time in range 86.0%, below range 5.1%, CV 32.6%. Carb entries logged: 0.

Each run is a brand-new conversation: package attached with Prompt 1, then Prompts 2, 3 and 4 in turn, then the app's correction prompt once if the JSON failed the app's checks. AAPS defaults are from nightscout/AndroidAPS master @ 598e2eb (2026-08-02).

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
