# TuneMyBG reproducibility report

## Experiment `real_deepseek_v4pro_50` — model `deepseek/deepseek-v4-pro`

- Runs: 50 (completed 50, failed 0)
- Final JSON extracted: 50/50 (methods: strict ×50)
- Fully schema-compliant: 36/50; mean schema score 0.991
- Mean wall time per run: 360s
- **App outcome (as the app behaves), over 50 completed runs:** accepted first time 45; accepted after the repair prompt 3; invalid JSON, no prompt offered 0; schema stop, no prompt offered 2; still rejected after repair 0
- **Accepted by the app but breaking Prompt 4's own rules:** 14/48 accepted runs; commonest: steps_enums_valid ×11, top_level_exact ×1, profile_rec_confidence_valid ×1, decisions_fields_exact ×1, decisions_verify_rule ×1
- **App loop:** first pass parseable 50/50, first pass compliant 33/50; correction prompt sent in 17 run(s); compliant after correction 36/50
- Sections the app would flag: analysis_steps.profile_cr_isf_dia.confidence ×7, analysis_steps.automation_sensitivity_limits.confidence ×4, parameter_decisions.profile.cr.00_00 ×2, profile_recommendation.focus ×2, parameter_decisions.profile.basal.10_00 ×1, parameter_decisions.profile.basal.16_00 ×1, education ×1, eduction ×1, profile_recommendation.confidence ×1, analysis_steps.automation_smb_uam.confidence ×1, parameter_decisions.profile.basal.00_00.current_value ×1, parameter_decisions.profile.basal.05_00.current_value ×1
- Corrections that changed a decision (not just format): 0/15 comparable; changed profile focus: 2/15
- Decisions per run — change: 2.0 ×19, 1.0 ×17, 3.0 ×6, 0.0 ×2, 5.0 ×2, 4.0 ×1, 6.0 ×1; keep: 21.0 ×19, 22.0 ×17, 20.0 ×5, 23.0 ×2, 19.0 ×2, 18.0 ×2, 17.0 ×1; verify: 0.0 ×47, 1.0 ×1
- profile_recommendation focus: basal ×26, isf ×17, dia ×4, target ×1
- profile_recommendation decision: change ×37, keep ×11; confidence: medium ×38, high ×7, low ×2, medium-high ×1
- Primary recommendation area: basal ×16, isf ×16, aaps_safety_limits ×2, dia ×2, meal_strategy ×1, data_foundation ×1, aaps_safety ×1, aaps ×1, automation_sensitivity_limits ×1, uam_aggressiveness ×1, UAM SMB delivery ×1, automation_sensitivity ×1, meal ×1, target ×1, aaps_uam ×1; priority: high ×30, safety ×16, medium ×1
- Meal strategy confidence: low ×43, medium ×5; exceptions: 0.0 ×44, 2.0 ×4
- **Decision stability index** (mean per-parameter agreement): 0.915; parameters with unanimous decisions: 10/23
- Pairwise change-set Jaccard: mean 0.195; same primary area 20%; same profile focus 38%
- Pairwise text similarity — summary 0.062, profile recommendation 0.284, meal suggestion 0.078

### Parameter decision agreement

| parameter_key | current | modal | agreement | change | keep | verify | suggested values (when change) |
|---|---|---|---|---|---|---|---|
| aaps.core.safety_limits | max_basal_u_per_hour=12 U/h; max_iob_units=25 U | keep | 0.56 | 21 | 27 | 0 | max_basal_u_per_hour=12 u/h; max_iob_units=10 u x3 | max_basal_u_per_hour=12 u/h; max_iob_units=5 u x3 | max_basal_u_per_hour=3 u/h; max_iob_units=8 u x2 | max_basal_u_per_hour=4 u/h; max_iob_units=5 u x2 | max_basal_u_per_hour=12 u/h; max_iob_units=8 u x2 | max_basal_u_per_hour=4 u/h; max_iob_units=8 u x1 | max_basal_u_per_hour=2 u/h; max_iob_units=5 u x1 | max_basal_u_per_hour=12 u/h; max_iob_units=6 u x1 | max_basal_u_per_hour=12 u/h; max_iob_units=7 u x1 | max_basal_u_per_hour=3 u/h; max_iob_units=5 u x1 | max_basal_u_per_hour=2 u/h; max_iob_units=10 u x1 | max_basal_u_per_hour=12 u/h; max_iob_units=2.0 u x1 | max_basal_u_per_hour=12 u/h; max_iob_units=12 u x1 | max_basal_u_per_hour=4 u/h; max_iob_units=7 u x1 |
| profile.basal.00_00 | 0.6 U/h | keep | 0.58 | 20 | 28 | 0 | 0.5 u/h x18 | 0.55 u/h x2 |
| profile.isf.00_00 | 56 mg/dL/U | keep | 0.58 | 20 | 28 | 0 | 70 mg/dl/u x5 | 80 mg/dl/u x2 | 40 mg/dl/u x2 | 30 mg/dl/u x1 | 150 mg/dl/u x1 | 36 mg/dl/u x1 | 110 mg/dl/u x1 | 100 mg/dl/u x1 | 38 mg/dl/u x1 | 90 mg/dl/u x1 | 75 mg/dl/u x1 | 50 mg/dl/u x1 | 35 mg/dl/u x1 | 180 mg/dl/u x1 |
| aaps.core.sensitivity | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=70 % | keep | 0.81 | 9 | 39 | 0 | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=100 % x4 | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=50 % x2 | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=60 % x1 | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=85 % x1 | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=0 % x1 |
| profile.dia | 10 h | keep | 0.83 | 8 | 40 | 0 | 6 h x4 | 5 h x2 | 8 h x1 | 7 h x1 |
| aaps.core.smb_delivery | smb_interval_minutes=3 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=20 min | keep | 0.90 | 5 | 43 | 0 | smb_interval_minutes=3 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=10 min x2 | smb_interval_minutes=3 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=15 min x2 | smb_interval_minutes=10 min; max_smb_basal_minutes=10 min; max_uam_smb_basal_minutes=15 min x1 |
| aaps.core.carb_absorption | min_5m_carbimpact=8 mg/dL/5 min; meal_max_absorption_hours=7 h | keep | 0.92 | 3 | 44 | 1 | min_5m_carbimpact=5 mg/dl/5 min; meal_max_absorption_hours=7 h x2 | min_5m_carbimpact=3 mg/dl/5 min; meal_max_absorption_hours=5 h x1 |
| aaps.core.smb_activation | smb_always_enabled=true; smb_with_cob_enabled=false; smb_after_carbs_enabled=false; smb_with_temp_target_enabled=true; smb_with_high_temp_target_enabled=false | keep | 0.96 | 2 | 46 | 0 | smb_always_enabled=true; smb_with_cob_enabled=false; smb_after_carbs_enabled=false; smb_with_temp_target_enabled=false; smb_with_high_temp_target_enabled=false x1 | smb_always_enabled=false; smb_with_cob_enabled=false; smb_after_carbs_enabled=false; smb_with_temp_target_enabled=true; smb_with_high_temp_target_enabled=false x1 |
| aaps.core.smb_uam | smb_enabled=true; uam_enabled=true | keep | 0.98 | 1 | 47 | 0 | smb_enabled=true; uam_enabled=false x1 |
| profile.basal.05_00 | 0.7 U/h | keep | 0.98 | 1 | 47 | 0 | 0.6 u/h x1 |
| profile.basal.19_00 | 0.7 U/h | keep | 0.98 | 1 | 47 | 0 | 0.6 u/h x1 |
| profile.target.00_00 | 90 mg/dL | keep | 0.98 | 1 | 47 | 0 | 100 mg/dl x1 |
| profile.target.23_00 | 90 mg/dL | keep | 0.98 | 1 | 47 | 0 | 100 mg/dl x1 |
| profile.basal.06_00 | 0.8 U/h | keep | 1.00 | 0 | 48 | 0 |  |
| profile.basal.10_00 | 0.7 U/h | keep | 1.00 | 0 | 48 | 0 |  |
| profile.basal.16_00 | 0.5 U/h | keep | 1.00 | 0 | 48 | 0 |  |
| profile.basal.18_00 | 0.6 U/h | keep | 1.00 | 0 | 48 | 0 |  |
| profile.cr.00_00 | 13 g/U | keep | 1.00 | 0 | 48 | 0 |  |
| profile.cr.04_00 | 11.1 g/U | keep | 1.00 | 0 | 48 | 0 |  |
| profile.cr.08_00 | 13.2 g/U | keep | 1.00 | 0 | 48 | 0 |  |
| profile.cr.16_00 | 10.5 g/U | keep | 1.00 | 0 | 48 | 0 |  |
| profile.cr.20_00 | 12.6 g/U | keep | 1.00 | 0 | 48 | 0 |  |
| profile.target.08_00 | 100 mg/dL | keep | 1.00 | 0 | 48 | 0 |  |

### Analysis step status / confidence agreement

| step | modal status | agreement | modal confidence | agreement |
|---|---|---|---|---|
| data_quality | completed | 1.00 | high | 0.98 |
| safety_overview | completed | 0.98 | high | 0.88 |
| basal_targets | completed | 0.58 | medium | 0.98 |
| profile_cr_isf_dia | partial | 0.71 | low | 0.46 |
| automation_smb_uam | completed | 0.92 | medium | 0.54 |
| automation_sensitivity_limits | completed | 0.94 | medium | 0.46 |
| meal_bolus_strategy | blocked | 0.60 | low | 0.98 |
| meal_ecarbs_absorption | blocked | 0.67 | low | 0.94 |
| synthesis_plan | completed | 1.00 | medium | 0.54 |

### Per-run overview

| run | status | 1st pass JSON | 1st pass OK | repairs | final OK | score | change/keep/verify | profile focus | primary rec | time (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| run_001 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | isf | Begin carbohydrate entries for all meals | 339.41 |
| run_002 | completed | strict | False | 1 | True | 1.00 | — | nan | nan | 459.95 |
| run_003 | completed | strict | False | 1 | False | 0.97 | 2/21/0 | basal | Reduce overnight basal (00:00–05:00) | 489.89 |
| run_004 | completed | strict | False | 1 | False | 0.97 | 3/20/0 | basal | Record all carbohydrate intake consistently | 401.71 |
| run_005 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | isf | Correct Insulin Sensitivity Factor (ISF) | 388.77 |
| run_006 | completed | strict | False | 1 | False | 0.97 | 1/22/0 | isf | Increase Insulin Sensitivity Factor (ISF) | 395.24 |
| run_007 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | basal | Reduce overnight basal rate (00:00–05:00) | 412.65 |
| run_008 | completed | strict | False | 1 | False | 0.94 | 1/22/0 | isf | Lower ISF to reduce hypoglycaemia risk | 433.42 |
| run_009 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Overnight basal verification | 287.55 |
| run_010 | completed | strict | False | 1 | True | 1.00 | — | nan | nan | 434.94 |
| run_011 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | isf | Increase Insulin Sensitivity Factor (ISF) to reduce hypoglycemia risk | 407.31 |
| run_012 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | basal | Reduce max IOB and max basal rate limits | 331.53 |
| run_013 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | isf | Increase Insulin Sensitivity Factor (ISF) | 391.13 |
| run_014 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | basal | Reduce max IOB and max basal limits | 320.4 |
| run_015 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | basal | Reduce overnight basal rate to reduce hypoglycemia | 275.51 |
| run_016 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | basal | Reduce overnight basal rate | 388.74 |
| run_017 | completed | strict | False | 1 | False | 0.97 | 4/19/0 | basal | Reduce max IOB from 25 U to 10 U | 417.85 |
| run_018 | completed | strict | False | 1 | False | 0.97 | 3/20/0 | dia | Immediately disable dynamic ISF by setting adjustment factor to 0% | 461.32 |
| run_019 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | basal | Reduce early overnight basal rate | 269.33 |
| run_020 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | basal | Reduce overnight basal from 0.6 U/h to 0.55 U/h (00:00-05:00) | 301.9 |
| run_021 | completed | strict | False | 1 | False | 0.97 | 1/22/0 | basal | Reduce overnight basal rate 00:00-05:00 | 350.75 |
| run_022 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | basal | Reduce overnight basal 00:00-05:00 | 317.1 |
| run_023 | completed | strict | False | 1 | False | 0.97 | 2/21/0 | basal | Reduce UAM‑driven bolus size | 372.32 |
| run_024 | completed | strict | False | 1 | False | 0.97 | 5/18/0 | dia | Reduce DIA to prevent IOB accumulation | 411.71 |
| run_025 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | isf | Increase profile ISF | 300.3 |
| run_026 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | basal | Reduce UAM SMB aggression temporarily | 328.84 |
| run_027 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | isf | Lower ISF to reduce hypoglycemia from corrections | 356.35 |
| run_028 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | isf | Increase profile ISF to reduce correction aggressiveness | 347.08 |
| run_029 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | dia | Reduce Duration of Insulin Action (DIA) to 5 hours | 235.03 |
| run_030 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | basal | Reduce overnight basal rate | 261.22 |
| run_031 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | isf | Increase ISF to reflect actual insulin sensitivity | 265.16 |
| run_032 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | basal | Reduce dynamic ISF adjustment factor to 100% | 377.49 |
| run_033 | completed | strict | False | 1 | False | 0.97 | 3/20/0 | isf | Raise profile ISF and disable Dynamic ISF amplification | 429.24 |
| run_034 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | isf | Reduce Insulin Sensitivity Factor (ISF) | 304.19 |
| run_035 | completed | strict | False | 1 | False | 0.97 | 1/22/0 | basal | Begin logging all carbohydrates and declare a meal strategy | 365.42 |
| run_036 | completed | strict | False | 1 | False | 0.97 | 5/18/0 | isf | Increase base ISF from 56 to 70 mg/dL/U | 492.69 |
| run_037 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | basal | Reduce overnight basal from 00:00 to 05:00 | 312.47 |
| run_038 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | basal | nan | 328.22 |
| run_039 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | basal | Reduce overnight basal rate | 370.83 |
| run_040 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Evaluate overnight basal rate after a fasting test | 335.31 |
| run_041 | completed | strict | False | 1 | True | 1.00 | 6/17/0 | target | Raise overnight glucose targets to reduce hypoglycemia risk | 404.21 |
| run_042 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | basal | Reduce UAM‑driven meal detection sensitivity | 334.91 |
| run_043 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | isf | Correct the ISF: raise from 56 to 180 mg/dL/U as a safe initial step | 292.4 |
| run_044 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | isf | Increase Insulin Sensitivity Factor (ISF) to reduce over-insulinization | 324.57 |
| run_045 | completed | strict | False | 1 | False | 0.97 | 2/21/0 | isf | Reduce ISF to improve safety | 446.15 |
| run_046 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | dia | Immediately reduce max IOB to a safe level | 343.87 |
| run_047 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | isf | Raise static ISF to 80 mg/dL/U | 366.73 |
| run_048 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | basal | Reduce overnight basal rate 00:00-05:00 | 312.76 |
| run_049 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | basal | Reduce overnight basal rate | 279.44 |
| run_050 | completed | strict | False | 1 | False | 0.97 | 3/19/1 | basal | Reduce overnight basal rate | 442.23 |

### Schema violations remaining after correction

- run_003: top-level keys differ: missing=['education'] extra=['eduction']
- run_004: steps with invalid status [] / confidence ['profile_cr_isf_dia']
- run_006: steps with invalid status [] / confidence ['profile_cr_isf_dia']
- run_008: steps with invalid status [] / confidence ['automation_sensitivity_limits'] | profile_recommendation.confidence=medium-high
- run_017: steps with invalid status [] / confidence ['profile_cr_isf_dia']
- run_018: steps with invalid status [] / confidence ['profile_cr_isf_dia']
- run_021: steps with invalid status [] / confidence ['automation_sensitivity_limits']
- run_023: steps with invalid status [] / confidence ['automation_smb_uam']
- run_024: steps with invalid status [] / confidence ['automation_sensitivity_limits']
- run_033: steps with invalid status [] / confidence ['profile_cr_isf_dia']
- run_035: decisions with wrong field set: ['profile.cr.00_00']
- run_036: steps with invalid status [] / confidence ['safety_overview', 'profile_cr_isf_dia', 'automation_sensitivity_limits']
- run_045: steps with invalid status [] / confidence ['profile_cr_isf_dia']
- run_050: verify without null component: ['aaps.core.carb_absorption']

## Experiment `real_gemini31pro_50` — model `gemini-3.1-pro-preview`

- Runs: 50 (completed 50, failed 0)
- Final JSON extracted: 50/50 (methods: strict ×50)
- Fully schema-compliant: 47/50; mean schema score 0.998
- Mean wall time per run: 137s
- **App outcome (as the app behaves), over 50 completed runs:** accepted first time 50; accepted after the repair prompt 0; invalid JSON, no prompt offered 0; schema stop, no prompt offered 0; still rejected after repair 0
- **Accepted by the app but breaking Prompt 4's own rules:** 3/50 accepted runs; commonest: top_level_exact ×3
- **App loop:** first pass parseable 50/50, first pass compliant 47/50; correction prompt sent in 3 run(s); compliant after correction 47/50
- Sections the app would flag: issues ×3
- Corrections that changed a decision (not just format): 0/3 comparable; changed profile focus: 0/3
- Decisions per run — change: 3.0 ×36, 1.0 ×5, 4.0 ×5, 2.0 ×4; keep: 20.0 ×36, 22.0 ×5, 19.0 ×5, 21.0 ×4; verify: 0.0 ×50
- profile_recommendation focus: target ×46, basal ×4
- profile_recommendation decision: change ×45, keep ×5; confidence: high ×50
- Primary recommendation area: target ×17, automation ×9, safety_limits ×8, aaps.core.safety_limits ×6, aaps ×4, safety ×3, automation_safety ×1, automation_sensitivity_limits ×1, limits ×1; priority: safety ×45, high ×5
- Meal strategy confidence: high ×24, medium ×21, low ×5; exceptions: 0.0 ×50
- **Decision stability index** (mean per-parameter agreement): 0.983; parameters with unanimous decisions: 17/23
- Pairwise change-set Jaccard: mean 0.784; same primary area 18%; same profile focus 85%
- Pairwise text similarity — summary 0.085, profile recommendation 0.624, meal suggestion 0.239

### Parameter decision agreement

| parameter_key | current | modal | agreement | change | keep | verify | suggested values (when change) |
|---|---|---|---|---|---|---|---|
| profile.target.00_00 | 90 mg/dL | change | 0.90 | 45 | 5 | 0 | 100 mg/dl x24 | 110 mg/dl x21 |
| profile.target.23_00 | 90 mg/dL | change | 0.90 | 45 | 5 | 0 | 100 mg/dl x24 | 110 mg/dl x21 |
| aaps.core.safety_limits | max_basal_u_per_hour=12 U/h; max_iob_units=25 U | change | 0.92 | 46 | 4 | 0 | max_basal_u_per_hour=3 u/h; max_iob_units=5 u x10 | max_basal_u_per_hour=3 u/h; max_iob_units=7 u x7 | max_basal_u_per_hour=3 u/h; max_iob_units=6 u x6 | max_basal_u_per_hour=12 u/h; max_iob_units=7 u x4 | max_basal_u_per_hour=4 u/h; max_iob_units=7 u x2 | max_basal_u_per_hour=4 u/h; max_iob_units=8 u x2 | max_basal_u_per_hour=3.0 u/h; max_iob_units=5.0 u x2 | max_basal_u_per_hour=3 u/h; max_iob_units=3 u x2 | max_basal_u_per_hour=2.5 u/h; max_iob_units=5 u x2 | max_basal_u_per_hour=3 u/h; max_iob_units=25 u x1 | max_basal_u_per_hour=3 u/h; max_iob_units=8 u x1 | max_basal_u_per_hour=3.5 u/h; max_iob_units=7 u x1 | max_basal_u_per_hour=2.5 u/h; max_iob_units=7 u x1 | max_basal_u_per_hour=3.2 u/h; max_iob_units=7 u x1 | max_basal_u_per_hour=4 u/h; max_iob_units=10 u x1 | max_basal_u_per_hour=2.5 u/h; max_iob_units=4.0 u x1 | max_basal_u_per_hour=12 u/h; max_iob_units=6 u x1 | max_basal_u_per_hour=4 u/h; max_iob_units=5 u x1 |
| aaps.core.smb_delivery | smb_interval_minutes=3 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=20 min | keep | 0.94 | 3 | 47 | 0 | smb_interval_minutes=15 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=20 min x2 | smb_interval_minutes=5 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=20 min x1 |
| profile.basal.00_00 | 0.6 U/h | keep | 0.98 | 1 | 49 | 0 | 0.5 u/h x1 |
| profile.target.08_00 | 100 mg/dL | keep | 0.98 | 1 | 49 | 0 | 110 mg/dl x1 |
| aaps.core.carb_absorption | min_5m_carbimpact=8 mg/dL/5 min; meal_max_absorption_hours=7 h | keep | 1.00 | 0 | 50 | 0 |  |
| aaps.core.sensitivity | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=70 % | keep | 1.00 | 0 | 50 | 0 |  |
| aaps.core.smb_activation | smb_always_enabled=true; smb_with_cob_enabled=false; smb_after_carbs_enabled=false; smb_with_temp_target_enabled=true; smb_with_high_temp_target_enabled=false | keep | 1.00 | 0 | 50 | 0 |  |
| aaps.core.smb_uam | smb_enabled=true; uam_enabled=true | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.05_00 | 0.7 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.06_00 | 0.8 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.10_00 | 0.7 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.16_00 | 0.5 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.18_00 | 0.6 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.19_00 | 0.7 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.00_00 | 13 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.04_00 | 11.1 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.08_00 | 13.2 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.16_00 | 10.5 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.20_00 | 12.6 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.dia | 10 h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.isf.00_00 | 56 mg/dL/U | keep | 1.00 | 0 | 50 | 0 |  |

### Analysis step status / confidence agreement

| step | modal status | agreement | modal confidence | agreement |
|---|---|---|---|---|
| data_quality | completed | 0.54 | high | 0.82 |
| safety_overview | completed | 1.00 | high | 0.98 |
| basal_targets | completed | 0.88 | medium | 0.60 |
| profile_cr_isf_dia | partial | 0.66 | medium | 0.64 |
| automation_smb_uam | completed | 1.00 | high | 1.00 |
| automation_sensitivity_limits | completed | 1.00 | high | 1.00 |
| meal_bolus_strategy | completed | 0.80 | high | 0.66 |
| meal_ecarbs_absorption | completed | 0.78 | high | 0.78 |
| synthesis_plan | completed | 1.00 | high | 0.98 |

### Per-run overview

| run | status | 1st pass JSON | 1st pass OK | repairs | final OK | score | change/keep/verify | profile focus | primary rec | time (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| run_001 | completed | strict | False | 1 | False | 0.97 | 3/20/0 | target | Create a safety buffer against overnight lows | 169.34 |
| run_002 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | target | Raise overnight glucose target for safety | 141.89 |
| run_003 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Restrict Max IOB and Max Basal Limits | 125.02 |
| run_004 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Reduce Max IOB and Max Basal limits | 149.56 |
| run_005 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | basal | Constrain AAPS Maximum Safety Limits | 126.59 |
| run_006 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Restrict Maximum IOB and Max Basal | 119.53 |
| run_007 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Raise Overnight Target for Safety | 142.94 |
| run_008 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Raise Overnight Glucose Targets | 115.84 |
| run_009 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Raise Overnight Target to Build Safety Buffer | 131.56 |
| run_010 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Constrain Safety Limits | 129.68 |
| run_011 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | basal | Reduce Max IOB safely | 131.9 |
| run_012 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Drastically Reduce Max IOB and Max Basal | 136.39 |
| run_013 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Reduce AAPS Safety Limits | 142.27 |
| run_014 | completed | strict | True | 0 | True | 1.00 | 4/19/0 | target | Restore Max IOB and Max Basal limits | 131.19 |
| run_015 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Reduce Automation Safety Limits | 157.02 |
| run_016 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Reduce AAPS Safety Limits | 139.61 |
| run_017 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Reduce Maximum IOB and Maximum Basal Limits | 123.1 |
| run_018 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | target | Raise overnight target for safety | 138.24 |
| run_019 | completed | strict | False | 1 | False | 0.97 | 3/20/0 | target | Tighten Safety Limits | 180.6 |
| run_020 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Restrict Max IOB and Max Basal | 145.54 |
| run_021 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Reduce Maximum IOB and Basal Limits | 143.1 |
| run_022 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Reduce Max IOB and Max Basal Limits | 152.63 |
| run_023 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Reduce Max IOB and Max Basal Limits | 141.78 |
| run_024 | completed | strict | False | 1 | False | 0.97 | 3/20/0 | target | Raise Overnight Target for Safety | 164.75 |
| run_025 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | basal | Urgently reduce Max IOB and Max Basal | 144.87 |
| run_026 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Constrain AAPS Safety Limits | 145.16 |
| run_027 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Raise Overnight Targets | 146.65 |
| run_028 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Raise overnight targets to establish a safety buffer | 138.27 |
| run_029 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Reduce maximum safety limits immediately | 131.61 |
| run_030 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Reduce Max IOB and Max Basal | 125.05 |
| run_031 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | target | Raise Overnight Glucose Targets | 155.14 |
| run_032 | completed | strict | True | 0 | True | 1.00 | 4/19/0 | target | Reduce Dangerous Safety Limits | 135.8 |
| run_033 | completed | strict | True | 0 | True | 1.00 | 4/19/0 | target | Raise glucose targets to build a safety buffer | 131.47 |
| run_034 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Reduce Max IOB and Max Basal Limits | 124.03 |
| run_035 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Reduce max_iob_units immediately | 119.7 |
| run_036 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | basal | Tighten Max IOB and Max Basal limits | 139.91 |
| run_037 | completed | strict | True | 0 | True | 1.00 | 4/19/0 | target | Raise overnight targets to prevent fasting lows | 137.88 |
| run_038 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Reduce AAPS Safety Limits | 133.82 |
| run_039 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Relax Overnight Target | 140.27 |
| run_040 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Urgently restrict Max IOB and Max Basal | 138.59 |
| run_041 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Enforce Safety Limits | 136.44 |
| run_042 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Lower Max IOB Limit | 136.58 |
| run_043 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Reduce Max IOB for Safety | 127.25 |
| run_044 | completed | strict | True | 0 | True | 1.00 | 4/19/0 | target | Tighten Max IOB and Max Basal Limits | 128.96 |
| run_045 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | target | Raise overnight target | 140.5 |
| run_046 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Raise Overnight Target | 125.4 |
| run_047 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Raise overnight and fasting targets to 100 mg/dL | 131.61 |
| run_048 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Restrict Max IOB and Max Basal | 124.13 |
| run_049 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Reduce Max IOB and Max Basal limits | 118.02 |
| run_050 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Raise overnight targets to provide a safety buffer | 135.74 |

### Schema violations remaining after correction

- run_001: top-level keys differ: missing=['issues'] extra=[]
- run_019: top-level keys differ: missing=['issues'] extra=[]
- run_024: top-level keys differ: missing=['issues'] extra=[]

## Experiment `real_gemini35flashlite_50` — model `gemini-3.5-flash-lite`

- Runs: 50 (completed 50, failed 0)
- Final JSON extracted: 49/50 (methods: strict ×48, brace_slice ×1, failed ×1)
- Fully schema-compliant: 41/49; mean schema score 0.994
- Mean wall time per run: 34s
- **App outcome (as the app behaves), over 50 completed runs:** accepted first time 38; accepted after the repair prompt 1; invalid JSON, no prompt offered 10; schema stop, no prompt offered 1; still rejected after repair 0
- **Accepted by the app but breaking Prompt 4's own rules:** 6/39 accepted runs; commonest: steps_enums_valid ×3, top_level_exact ×2, decisions_fields_exact ×1
- **App loop:** first pass parseable 40/50, first pass compliant 32/50; correction prompt sent in 18 run(s); compliant after correction 41/50
- Sections the app would flag: analysis_steps.basal_targets.confidence ×3, issues ×2, strengths ×2, analysis_steps.automation_sensitivity_limits.confidence ×2, analysis_steps.synthesis_plan.confidence ×2, parameter_decisions.aaps.core.carb_absorption ×1, analysis_steps.meal_ecarbs_absorption.confidence ×1, parameter_decisions ×1, profile_recommendation ×1; first pass not valid JSON at all ×10
- Corrections that changed a decision (not just format): 1/7 comparable; changed profile focus: 0/7 (10 unparseable first pass(es) not comparable)
- Decisions per run — change: 0.0 ×32, 1.0 ×4, 2.0 ×3; keep: 23.0 ×32, 22.0 ×4, 21.0 ×3; verify: 0.0 ×39
- profile_recommendation focus: basal ×32, isf ×3, cr ×2, dia ×1, target ×1
- profile_recommendation decision: keep ×34, change ×5; confidence: medium ×37, high ×2
- Primary recommendation area: basal ×16, meal ×6, cr ×6, smb ×4, aaps ×3, meal_strategy ×1, profile ×1, target ×1, safety ×1; priority: high ×20, medium ×13, safety ×6
- Meal strategy confidence: medium ×38, low ×1; exceptions: 1.0 ×15, 2.0 ×13, 0.0 ×11
- **Decision stability index** (mean per-parameter agreement): 0.989; parameters with unanimous decisions: 20/23
- Pairwise change-set Jaccard: mean 0.467; same primary area 14%; same profile focus 43%
- Pairwise text similarity — summary 0.133, profile recommendation 0.367, meal suggestion 0.143

### Parameter decision agreement

| parameter_key | current | modal | agreement | change | keep | verify | suggested values (when change) |
|---|---|---|---|---|---|---|---|
| aaps.core.safety_limits | max_basal_u_per_hour=12 U/h; max_iob_units=25 U | keep | 0.87 | 5 | 34 | 0 | max_basal_u_per_hour=12 u/h; max_iob_units=6 u x4 | max_basal_u_per_hour=12 u/h; max_iob_units=15 u x1 |
| profile.basal.00_00 | 0.6 U/h | keep | 0.90 | 4 | 35 | 0 | 0.5 u/h x4 |
| profile.target.00_00 | 90 mg/dL | keep | 0.97 | 1 | 38 | 0 | 95 mg/dl x1 |
| aaps.core.carb_absorption | min_5m_carbimpact=8 mg/dL/5 min; meal_max_absorption_hours=7 h | keep | 1.00 | 0 | 39 | 0 |  |
| aaps.core.sensitivity | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=70 % | keep | 1.00 | 0 | 39 | 0 |  |
| aaps.core.smb_activation | smb_always_enabled=true; smb_with_cob_enabled=false; smb_after_carbs_enabled=false; smb_with_temp_target_enabled=true; smb_with_high_temp_target_enabled=false | keep | 1.00 | 0 | 39 | 0 |  |
| aaps.core.smb_delivery | smb_interval_minutes=3 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=20 min | keep | 1.00 | 0 | 39 | 0 |  |
| aaps.core.smb_uam | smb_enabled=true; uam_enabled=true | keep | 1.00 | 0 | 39 | 0 |  |
| profile.basal.05_00 | 0.7 U/h | keep | 1.00 | 0 | 39 | 0 |  |
| profile.basal.06_00 | 0.8 U/h | keep | 1.00 | 0 | 39 | 0 |  |
| profile.basal.10_00 | 0.7 U/h | keep | 1.00 | 0 | 39 | 0 |  |
| profile.basal.16_00 | 0.5 U/h | keep | 1.00 | 0 | 39 | 0 |  |
| profile.basal.18_00 | 0.6 U/h | keep | 1.00 | 0 | 39 | 0 |  |
| profile.basal.19_00 | 0.7 U/h | keep | 1.00 | 0 | 39 | 0 |  |
| profile.cr.00_00 | 13 g/U | keep | 1.00 | 0 | 39 | 0 |  |
| profile.cr.04_00 | 11.1 g/U | keep | 1.00 | 0 | 39 | 0 |  |
| profile.cr.08_00 | 13.2 g/U | keep | 1.00 | 0 | 39 | 0 |  |
| profile.cr.16_00 | 10.5 g/U | keep | 1.00 | 0 | 39 | 0 |  |
| profile.cr.20_00 | 12.6 g/U | keep | 1.00 | 0 | 39 | 0 |  |
| profile.dia | 10 h | keep | 1.00 | 0 | 39 | 0 |  |
| profile.isf.00_00 | 56 mg/dL/U | keep | 1.00 | 0 | 39 | 0 |  |
| profile.target.08_00 | 100 mg/dL | keep | 1.00 | 0 | 39 | 0 |  |
| profile.target.23_00 | 90 mg/dL | keep | 1.00 | 0 | 39 | 0 |  |

### Analysis step status / confidence agreement

| step | modal status | agreement | modal confidence | agreement |
|---|---|---|---|---|
| data_quality | completed | 1.00 | high | 1.00 |
| safety_overview | completed | 1.00 | high | 1.00 |
| basal_targets | completed | 1.00 | medium | 0.95 |
| profile_cr_isf_dia | completed | 1.00 | medium | 1.00 |
| automation_smb_uam | completed | 1.00 | high | 1.00 |
| automation_sensitivity_limits | completed | 1.00 | high | 0.74 |
| meal_bolus_strategy | completed | 1.00 | medium | 0.97 |
| meal_ecarbs_absorption | completed | 1.00 | medium | 0.80 |
| synthesis_plan | completed | 1.00 | medium | 0.64 |

### Per-run overview

| run | status | 1st pass JSON | 1st pass OK | repairs | final OK | score | change/keep/verify | profile focus | primary rec | time (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| run_001 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Monitor Early Nocturnal Basal Delivery | 31.33 |
| run_002 | completed | failed | False | 1 | True | 1.00 | — | nan | nan | 44.25 |
| run_003 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | isf | Introduce Carbohydrate Logging | 28.78 |
| run_004 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Establish Consistent Meal Logging | 30.62 |
| run_005 | completed | failed | False | 1 | True | 1.00 | — | nan | nan | 41.41 |
| run_006 | completed | failed | False | 1 | False | 0.91 | — | nan | nan | 37.09 |
| run_007 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Verify Overnight Basal Rates | 28.21 |
| run_008 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Review Max IOB Safety Limit | 28.94 |
| run_009 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Verify Overnight Basal Rates for Nocturnal Dips | 28.45 |
| run_010 | completed | strict | False | 1 | False | 0.97 | 0/23/0 | dia | Initiate Carbohydrate Logging | 44.23 |
| run_011 | completed | failed | False | 1 | True | 1.00 | — | nan | nan | 41.58 |
| run_012 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Pilot Manual Carb Logging | 29.32 |
| run_013 | completed | strict | False | 1 | False | 0.97 | 0/23/0 | isf | Maintain Profile Baselines and Verify Meal Logging | 42.67 |
| run_014 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Begin Consistent Carbohydrate Logging | 29.75 |
| run_015 | completed | strict | False | 1 | False | 0.97 | 1/22/0 | target | Adjust Overnight Target | 45.07 |
| run_016 | completed | failed | False | 1 | True | 1.00 | — | nan | nan | 36.89 |
| run_017 | completed | brace_slice | True | 0 | True | 1.00 | 0/23/0 | basal | Initiate Carbohydrate Logging | 32.44 |
| run_018 | completed | strict | False | 1 | False | 0.97 | 0/23/0 | basal | Evaluate Nocturnal Basal Rates | 42.53 |
| run_019 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Review Max IOB Safety Limit | 30.62 |
| run_020 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Begin Structured Carbohydrate Logging | 28.31 |
| run_021 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Verify Overnight Basal Rates | 29.73 |
| run_022 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Monitor Overnight Basal and Hypoglycemia | 28.2 |
| run_023 | completed | strict | False | 1 | False | 0.97 | 1/22/0 | basal | Tighten Maximum IOB Safety Limit | 40.81 |
| run_024 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Log Carbohydrates for Trial Period | 29.99 |
| run_025 | completed | failed | False | 1 | None | — | — | nan | nan | 45.23 |
| run_026 | completed | strict | False | 1 | False | 0.97 | 2/21/0 | basal | Reduce Max IOB Safety Limit | 35.7 |
| run_027 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Verify Overnight Basal and Fasting Stability | 27.5 |
| run_028 | completed | failed | False | 1 | True | 1.00 | — | nan | nan | 43.79 |
| run_029 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Introduce Manual Carbohydrate Logging | 31.69 |
| run_030 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | basal | Reduce Max IOB Limit for Safety | 31.27 |
| run_031 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | isf | Initiate Carbohydrate Logging | 32.32 |
| run_032 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Reduce Overnight Basal Rates | 29.9 |
| run_033 | completed | strict | False | 1 | True | 1.00 | 2/21/0 | basal | Reduce Overnight Basal Rate | 43.37 |
| run_034 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Monitor Overnight Low Trends | 32.02 |
| run_035 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Review overnight and late-afternoon basal rates | 30.38 |
| run_036 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Verify Overnight Basal Rates | 29.18 |
| run_037 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Introduce Manual Carbohydrate Logging | 26.3 |
| run_038 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Verify Overnight Basal and Fasting Stability | 26.98 |
| run_039 | completed | failed | False | 1 | True | 1.00 | — | nan | nan | 39.71 |
| run_040 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | basal | Reduce Max IOB Limit for Safety | 29.83 |
| run_041 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | cr | Initiate Manual Carb Logging for Verification | 29.39 |
| run_042 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | cr | Begin Recording Manual Carbohydrate Entries | 26.15 |
| run_043 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Begin Recording Carbohydrate Entries | 28.29 |
| run_044 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Evaluate Carbohydrate Logging for Complex Meals | 32.23 |
| run_045 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Review Max IOB Safety Limit | 33.47 |
| run_046 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Verify Overnight Basal and Fasting Stability | 30.41 |
| run_047 | completed | failed | False | 1 | False | 0.97 | — | nan | nan | 42.84 |
| run_048 | completed | failed | False | 1 | True | 1.00 | — | nan | nan | 38.76 |
| run_049 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | basal | Reduce Early-Night Basal Rate | 30.69 |
| run_050 | completed | strict | False | 1 | True | 1.00 | — | nan | nan | 37.78 |

### Schema violations remaining after correction

- run_006: invalid decision value: ['profile.isf.00_00'] | verify without null component: ['profile.isf.00_00'] | meal_strategy_summary fields: ['confidence', 'exceptions', 'next_observation', 'rationale']
- run_010: top-level keys differ: missing=['issues', 'strengths'] extra=[]
- run_013: steps with invalid status [] / confidence ['basal_targets', 'automation_sensitivity_limits', 'synthesis_plan']
- run_015: decisions with wrong field set: ['aaps.core.carb_absorption']
- run_018: steps with invalid status [] / confidence ['basal_targets', 'automation_sensitivity_limits']
- run_023: top-level keys differ: missing=['issues', 'strengths'] extra=[]
- run_026: steps with invalid status [] / confidence ['meal_ecarbs_absorption']
- run_047: top-level keys differ: missing=['issues', 'strengths'] extra=[]

## Experiment `real_gemini36flash_50` — model `gemini-3.6-flash`

- Runs: 50 (completed 50, failed 0)
- Final JSON extracted: 50/50 (methods: strict ×50)
- Fully schema-compliant: 46/50; mean schema score 0.997
- Mean wall time per run: 107s
- **App outcome (as the app behaves), over 50 completed runs:** accepted first time 50; accepted after the repair prompt 0; invalid JSON, no prompt offered 0; schema stop, no prompt offered 0; still rejected after repair 0
- **Accepted by the app but breaking Prompt 4's own rules:** 4/50 accepted runs; commonest: steps_enums_valid ×3, meal_confidence_valid ×1, decisions_fields_exact ×1
- **App loop:** first pass parseable 50/50, first pass compliant 46/50; correction prompt sent in 4 run(s); compliant after correction 46/50
- Sections the app would flag: analysis_steps.meal_ecarbs_absorption.confidence ×2, analysis_steps.meal_bolus_strategy.confidence ×1, analysis_steps.profile_cr_isf_dia.confidence ×1, meal_strategy_summary.confidence ×1, parameter_decisions.profile.dia ×1
- Corrections that changed a decision (not just format): 0/4 comparable; changed profile focus: 0/4
- Decisions per run — change: 3.0 ×19, 4.0 ×13, 2.0 ×7, 1.0 ×5, 5.0 ×4, 6.0 ×2; keep: 20.0 ×19, 19.0 ×13, 21.0 ×7, 22.0 ×5, 18.0 ×4, 17.0 ×2; verify: 0.0 ×50
- profile_recommendation focus: target ×39, basal ×11
- profile_recommendation decision: change ×44, keep ×6; confidence: high ×49, medium ×1
- Primary recommendation area: smb ×22, target ×16, safety_limits ×5, basal ×3, aaps ×3, safety ×1; priority: safety ×49, high ×1
- Meal strategy confidence: medium ×39, high ×5, low ×5, medium-high ×1; exceptions: 1.0 ×27, 2.0 ×23
- **Decision stability index** (mean per-parameter agreement): 0.951; parameters with unanimous decisions: 14/23
- Pairwise change-set Jaccard: mean 0.580; same primary area 30%; same profile focus 65%
- Pairwise text similarity — summary 0.156, profile recommendation 0.485, meal suggestion 0.181

### Parameter decision agreement

| parameter_key | current | modal | agreement | change | keep | verify | suggested values (when change) |
|---|---|---|---|---|---|---|---|
| aaps.core.sensitivity | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=70 % | keep | 0.74 | 13 | 37 | 0 | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=50 % x13 |
| profile.basal.00_00 | 0.6 U/h | keep | 0.78 | 11 | 39 | 0 | 0.5 u/h x11 |
| profile.target.00_00 | 90 mg/dL | change | 0.78 | 39 | 11 | 0 | 100 mg/dl x39 |
| profile.target.23_00 | 90 mg/dL | change | 0.78 | 39 | 11 | 0 | 100 mg/dl x39 |
| aaps.core.smb_delivery | smb_interval_minutes=3 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=20 min | keep | 0.92 | 4 | 46 | 0 | smb_interval_minutes=3 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=15 min x4 |
| profile.basal.19_00 | 0.7 U/h | keep | 0.94 | 3 | 47 | 0 | 0.5 u/h x2 | 0.6 u/h x1 |
| aaps.core.carb_absorption | min_5m_carbimpact=8 mg/dL/5 min; meal_max_absorption_hours=7 h | keep | 0.98 | 1 | 49 | 0 | min_5m_carbimpact=4 mg/dl/5 min; meal_max_absorption_hours=7 h x1 |
| aaps.core.safety_limits | max_basal_u_per_hour=12 U/h; max_iob_units=25 U | change | 0.98 | 49 | 1 | 0 | max_basal_u_per_hour=3.0 u/h; max_iob_units=7.0 u x8 | max_basal_u_per_hour=3.5 u/h; max_iob_units=7.0 u x6 | max_basal_u_per_hour=3.5 u/h; max_iob_units=6 u x4 | max_basal_u_per_hour=3 u/h; max_iob_units=7 u x3 | max_basal_u_per_hour=3.0 u/h; max_iob_units=6.0 u x3 | max_basal_u_per_hour=3.5 u/h; max_iob_units=7 u x3 | max_basal_u_per_hour=3.5 u/h; max_iob_units=5.0 u x2 | max_basal_u_per_hour=4 u/h; max_iob_units=7 u x2 | max_basal_u_per_hour=2.5 u/h; max_iob_units=7 u x1 | max_basal_u_per_hour=3 u/h; max_iob_units=4 u x1 | max_basal_u_per_hour=3.5 u/h; max_iob_units=8 u x1 | max_basal_u_per_hour=3.5 u/h; max_iob_units=8.0 u x1 | max_basal_u_per_hour=3.0 u/h; max_iob_units=7 u x1 | max_basal_u_per_hour=4.0 u/h; max_iob_units=7.0 u x1 | max_basal_u_per_hour=4.0 u/h; max_iob_units=8.0 u x1 | max_basal_u_per_hour=3.5 u/h; max_iob_units=15 u x1 | max_basal_u_per_hour=3.2 u/h; max_iob_units=7.0 u x1 | max_basal_u_per_hour=3.0 u/h; max_iob_units=5.0 u x1 | max_basal_u_per_hour=3.2 u/h; max_iob_units=8.0 u x1 | max_basal_u_per_hour=4 u/h; max_iob_units=10 u x1 | max_basal_u_per_hour=4 u/h; max_iob_units=8 u x1 | max_basal_u_per_hour=3.2 u/h; max_iob_units=7 u x1 | max_basal_u_per_hour=12 u/h; max_iob_units=10 u x1 | max_basal_u_per_hour=3.2 u/h; max_iob_units=6 u x1 | max_basal_u_per_hour=3 u/h; max_iob_units=5 u x1 | max_basal_u_per_hour=3.5 u/h; max_iob_units=10 u x1 |
| profile.basal.18_00 | 0.6 U/h | keep | 0.98 | 1 | 49 | 0 | 0.5 u/h x1 |
| aaps.core.smb_activation | smb_always_enabled=true; smb_with_cob_enabled=false; smb_after_carbs_enabled=false; smb_with_temp_target_enabled=true; smb_with_high_temp_target_enabled=false | keep | 1.00 | 0 | 50 | 0 |  |
| aaps.core.smb_uam | smb_enabled=true; uam_enabled=true | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.05_00 | 0.7 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.06_00 | 0.8 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.10_00 | 0.7 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.16_00 | 0.5 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.00_00 | 13 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.04_00 | 11.1 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.08_00 | 13.2 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.16_00 | 10.5 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.20_00 | 12.6 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.dia | 10 h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.isf.00_00 | 56 mg/dL/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.target.08_00 | 100 mg/dL | keep | 1.00 | 0 | 50 | 0 |  |

### Analysis step status / confidence agreement

| step | modal status | agreement | modal confidence | agreement |
|---|---|---|---|---|
| data_quality | completed | 0.94 | high | 0.98 |
| safety_overview | completed | 1.00 | high | 1.00 |
| basal_targets | completed | 0.96 | medium | 0.56 |
| profile_cr_isf_dia | completed | 0.86 | medium | 0.98 |
| automation_smb_uam | completed | 1.00 | high | 1.00 |
| automation_sensitivity_limits | completed | 1.00 | high | 1.00 |
| meal_bolus_strategy | completed | 0.82 | medium | 0.76 |
| meal_ecarbs_absorption | completed | 0.82 | medium | 0.62 |
| synthesis_plan | completed | 1.00 | high | 0.96 |

### Per-run overview

| run | status | 1st pass JSON | 1st pass OK | repairs | final OK | score | change/keep/verify | profile focus | primary rec | time (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| run_001 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Reduce AAPS Max IOB and Max Basal Safety Limits | 102.27 |
| run_002 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Reduce AAPS Max IOB and Max Basal Safety Limits | 130.89 |
| run_003 | completed | strict | False | 1 | False | 0.97 | 5/18/0 | target | Reduce AAPS Max IOB and Max Basal Safety Limits | 132.92 |
| run_004 | completed | strict | True | 0 | True | 1.00 | 5/18/0 | target | Raise Overnight Target to 100 mg/dL | 120.52 |
| run_005 | completed | strict | False | 1 | False | 0.94 | 4/19/0 | target | Reduce Max IOB and Max Basal Safety Limits | 141.22 |
| run_006 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | basal | Reduce AAPS Max IOB and Max Basal Safety Limits | 113.94 |
| run_007 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Reduce AAPS Automation Safety Caps | 96.26 |
| run_008 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Reduce AAPS Max Basal and Max IOB Safety Ceilings | 93.41 |
| run_009 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Raise Overnight Target to Reduce Nocturnal Hypoglycemia | 107.59 |
| run_010 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | basal | Reduce AAPS Max IOB Safety Limit | 99.06 |
| run_011 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Raise Overnight Target to 100 mg/dL | 108.51 |
| run_012 | completed | strict | True | 0 | True | 1.00 | 5/18/0 | basal | Reduce AAPS Safety Limits (Max IOB and Max Basal) | 95.47 |
| run_013 | completed | strict | True | 0 | True | 1.00 | 4/19/0 | target | Reduce Max IOB and Max Basal Safety Limits | 120.67 |
| run_014 | completed | strict | True | 0 | True | 1.00 | 4/19/0 | basal | Reduce Overnight Basal Rate | 103.07 |
| run_015 | completed | strict | True | 0 | True | 1.00 | 5/18/0 | basal | Reduce AAPS Max IOB and Max Basal Safety Limits | 97.79 |
| run_016 | completed | strict | False | 1 | False | 0.97 | 4/19/0 | target | Reduce Max IOB and Max Basal Safety Limits | 138.77 |
| run_017 | completed | strict | True | 0 | True | 1.00 | 4/19/0 | target | Raise Overnight Target to 100 mg/dL | 119.69 |
| run_018 | completed | strict | True | 0 | True | 1.00 | 4/19/0 | target | Reduce Maximum IOB Safety Cap | 108.78 |
| run_019 | completed | strict | True | 0 | True | 1.00 | 6/17/0 | basal | Reduce Overnight Basal Rate | 101.27 |
| run_020 | completed | strict | True | 0 | True | 1.00 | 4/19/0 | target | Raise Overnight Target to 100 mg/dL | 101.61 |
| run_021 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Raise Overnight Target to Reduce Nocturnal Hypoglycemia | 89.47 |
| run_022 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Reduce Max IOB and Max Basal Safety Limits | 105.46 |
| run_023 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Reduce AAPS Max IOB and Max Basal Safety Ceilings | 96.98 |
| run_024 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Lower Max IOB and Max Basal Ceilings in AAPS | 102.42 |
| run_025 | completed | strict | True | 0 | True | 1.00 | 4/19/0 | target | Reduce AAPS Max IOB and Max Basal Safety Limits | 115.98 |
| run_026 | completed | strict | True | 0 | True | 1.00 | 4/19/0 | target | Raise Overnight Target to Reduce Nocturnal Lows | 104.37 |
| run_027 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Reduce AAPS Max IOB and Max Basal Safety Limits | 96.39 |
| run_028 | completed | strict | True | 0 | True | 1.00 | 4/19/0 | target | Raise Overnight Target to 100 mg/dL | 98.56 |
| run_029 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Raise Overnight Glucose Target | 101.68 |
| run_030 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | basal | Tighten AAPS Max Basal and Max IOB Safety Limits | 106.28 |
| run_031 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Reduce Maximum IOB and Maximum Basal Safety Limits | 108.38 |
| run_032 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Raise Overnight Target Setting | 96.95 |
| run_033 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Tighten AAPS Max IOB and Max Basal Safety Limits | 101.86 |
| run_034 | completed | strict | True | 0 | True | 1.00 | 4/19/0 | target | Reduce Max IOB and Max Basal Safety Limits | 102.45 |
| run_035 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Reduce Max IOB Safety Limit | 108.21 |
| run_036 | completed | strict | True | 0 | True | 1.00 | 6/17/0 | target | Raise Overnight Target to Reduce Hypoglycemia | 97.86 |
| run_037 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | basal | Reduce Midnight Basal Rate (00:00–05:00) | 101.96 |
| run_038 | completed | strict | True | 0 | True | 1.00 | 4/19/0 | target | Tighten AAPS Safety Limits (Max IOB & Max Basal) | 110.88 |
| run_039 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | basal | Tighten AAPS Max IOB and Max Basal Safety Limits | 114.7 |
| run_040 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Raise Overnight Target Segment to 100 mg/dL | 116.62 |
| run_041 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Tighten AAPS Max IOB and Max Basal Safety Limits | 102.35 |
| run_042 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Raise Overnight Target to 100 mg/dL | 109.93 |
| run_043 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Tighten AAPS Max IOB and Max Basal Safety Limits | 97.28 |
| run_044 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Reduce AAPS Max IOB and Max Basal Safety Limits | 89.61 |
| run_045 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Raise Overnight Target to Reduce Night-time Hypoglycemia | 102.24 |
| run_046 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | basal | Reduce Max IOB and Max Basal safety limits to match Total Daily Dose | 90.37 |
| run_047 | completed | strict | False | 1 | False | 0.97 | 4/19/0 | target | Raise Overnight Glucose Target | 138.25 |
| run_048 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | basal | Restrict Max Basal and Max IOB Safety Guardrails | 100.34 |
| run_049 | completed | strict | True | 0 | True | 1.00 | 3/20/0 | target | Reduce AAPS Max IOB and Max Basal Safety Limits | 112.19 |
| run_050 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | target | Raise Overnight Target to 100 mg/dL | 108.58 |

### Schema violations remaining after correction

- run_003: steps with invalid status [] / confidence ['meal_bolus_strategy', 'meal_ecarbs_absorption']
- run_005: steps with invalid status [] / confidence ['profile_cr_isf_dia'] | meal_strategy_summary.confidence=medium-high
- run_016: decisions with wrong field set: ['profile.dia']
- run_047: steps with invalid status [] / confidence ['meal_ecarbs_absorption']

## Experiment `real_gpt54mini_med_50` — model `gpt-5.4-mini`

- Runs: 50 (completed 50, failed 0)
- Final JSON extracted: 50/50 (methods: strict ×50)
- Fully schema-compliant: 23/50; mean schema score 0.979
- Mean wall time per run: 123s
- **App outcome (as the app behaves), over 50 completed runs:** accepted first time 48; accepted after the repair prompt 0; invalid JSON, no prompt offered 1; schema stop, no prompt offered 0; still rejected after repair 1
- **Accepted by the app but breaking Prompt 4's own rules:** 25/48 accepted runs; commonest: steps_enums_valid ×22, meal_confidence_valid ×5, profile_rec_confidence_valid ×3, meal_fields_exact ×2, profile_rec_fields_exact ×1
- **App loop:** first pass parseable 49/50, first pass compliant 23/50; correction prompt sent in 27 run(s); compliant after correction 23/50
- Sections the app would flag: analysis_steps.automation_smb_uam.confidence ×15, analysis_steps.profile_cr_isf_dia.confidence ×12, meal_strategy_summary.confidence ×5, analysis_steps.automation_sensitivity_limits.confidence ×5, analysis_steps.meal_bolus_strategy.confidence ×4, profile_recommendation.confidence ×3, analysis_steps.synthesis_plan.confidence ×2, meal_strategy_summary ×2, parameter_decisions.aaps.core.carb_absorption.current_value ×1, analysis_steps.safety_overview.confidence ×1, analysis_steps.basal_targets.confidence ×1, profile_recommendation ×1; first pass not valid JSON at all ×1
- Corrections that changed a decision (not just format): 0/25 comparable; changed profile focus: 0/25 (1 unparseable first pass(es) not comparable)
- Decisions per run — change: 0.0 ×46, 1.0 ×2; keep: 23.0 ×46, 22.0 ×2; verify: 0.0 ×48
- profile_recommendation focus: basal ×47, cr ×1
- profile_recommendation decision: keep ×46, change ×2; confidence: medium ×44, medium-low ×3, low ×1
- Primary recommendation area: basal ×33, profile ×12, basal_and_targets ×1, meal ×1, profile_and_data ×1; priority: high ×44, medium ×3, safety ×1
- Meal strategy confidence: low ×43, low-to-medium ×2, low-medium ×2, low_medium ×1; exceptions: 2.0 ×42, 1.0 ×3, 0.0 ×3
- **Decision stability index** (mean per-parameter agreement): 0.998; parameters with unanimous decisions: 22/23
- Pairwise change-set Jaccard: mean 0.847; same primary area 48%; same profile focus 88%
- Pairwise text similarity — summary 0.046, profile recommendation 0.561, meal suggestion 0.103

### Parameter decision agreement

| parameter_key | current | modal | agreement | change | keep | verify | suggested values (when change) |
|---|---|---|---|---|---|---|---|
| profile.basal.00_00 | 0.6 U/h | keep | 0.96 | 2 | 46 | 0 | 0.55 u/h x2 |
| aaps.core.carb_absorption | min_5m_carbimpact=8 mg/dL/5 min; meal_max_absorption_hours=7 h | keep | 1.00 | 0 | 48 | 0 |  |
| aaps.core.safety_limits | max_basal_u_per_hour=12 U/h; max_iob_units=25 U | keep | 1.00 | 0 | 48 | 0 |  |
| aaps.core.sensitivity | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=70 % | keep | 1.00 | 0 | 48 | 0 |  |
| aaps.core.smb_activation | smb_always_enabled=true; smb_with_cob_enabled=false; smb_after_carbs_enabled=false; smb_with_temp_target_enabled=true; smb_with_high_temp_target_enabled=false | keep | 1.00 | 0 | 48 | 0 |  |
| aaps.core.smb_delivery | smb_interval_minutes=3 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=20 min | keep | 1.00 | 0 | 48 | 0 |  |
| aaps.core.smb_uam | smb_enabled=true; uam_enabled=true | keep | 1.00 | 0 | 48 | 0 |  |
| profile.basal.05_00 | 0.7 U/h | keep | 1.00 | 0 | 48 | 0 |  |
| profile.basal.06_00 | 0.8 U/h | keep | 1.00 | 0 | 48 | 0 |  |
| profile.basal.10_00 | 0.7 U/h | keep | 1.00 | 0 | 48 | 0 |  |
| profile.basal.16_00 | 0.5 U/h | keep | 1.00 | 0 | 48 | 0 |  |
| profile.basal.18_00 | 0.6 U/h | keep | 1.00 | 0 | 48 | 0 |  |
| profile.basal.19_00 | 0.7 U/h | keep | 1.00 | 0 | 48 | 0 |  |
| profile.cr.00_00 | 13 g/U | keep | 1.00 | 0 | 48 | 0 |  |
| profile.cr.04_00 | 11.1 g/U | keep | 1.00 | 0 | 48 | 0 |  |
| profile.cr.08_00 | 13.2 g/U | keep | 1.00 | 0 | 48 | 0 |  |
| profile.cr.16_00 | 10.5 g/U | keep | 1.00 | 0 | 48 | 0 |  |
| profile.cr.20_00 | 12.6 g/U | keep | 1.00 | 0 | 48 | 0 |  |
| profile.dia | 10 h | keep | 1.00 | 0 | 48 | 0 |  |
| profile.isf.00_00 | 56 mg/dL/U | keep | 1.00 | 0 | 48 | 0 |  |
| profile.target.00_00 | 90 mg/dL | keep | 1.00 | 0 | 48 | 0 |  |
| profile.target.08_00 | 100 mg/dL | keep | 1.00 | 0 | 48 | 0 |  |
| profile.target.23_00 | 90 mg/dL | keep | 1.00 | 0 | 48 | 0 |  |

### Analysis step status / confidence agreement

| step | modal status | agreement | modal confidence | agreement |
|---|---|---|---|---|
| data_quality | completed | 1.00 | high | 1.00 |
| safety_overview | completed | 1.00 | high | 0.94 |
| basal_targets | partial | 0.83 | medium | 0.98 |
| profile_cr_isf_dia | partial | 0.85 | low | 0.42 |
| automation_smb_uam | completed | 1.00 | medium | 0.42 |
| automation_sensitivity_limits | completed | 0.98 | medium | 0.85 |
| meal_bolus_strategy | partial | 0.67 | low | 0.92 |
| meal_ecarbs_absorption | partial | 0.33 | low | 1.00 |
| synthesis_plan | completed | 1.00 | medium | 0.96 |

### Per-run overview

| run | status | 1st pass JSON | 1st pass OK | repairs | final OK | score | change/keep/verify | profile focus | primary rec | time (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| run_001 | completed | strict | False | 1 | False | 0.97 | 0/23/0 | basal | Keep the current profile unchanged and verify with fasting data first | 152.66 |
| run_002 | completed | strict | False | 1 | False | 0.97 | 0/23/0 | basal | Keep the current profile unchanged and verify with separated no-meal observations | 131.13 |
| run_003 | completed | strict | False | 1 | False | 0.97 | 0/23/0 | basal | Keep profile unchanged pending one fasting verification | 140.04 |
| run_004 | completed | strict | False | 1 | False | 0.97 | 0/23/0 | basal | Keep the current profile and verify with one focused test | 111.71 |
| run_005 | completed | strict | False | 1 | False | 0.97 | 0/23/0 | basal | Keep the current profile and verify with meal-linked observation first | 150.39 |
| run_006 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the current profile unchanged and verify with one clean fasting-like block | 98.66 |
| run_007 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | cr | Keep the current profile unchanged and verify with a meal-logged day before any basal, CR, ISF, target, or DIA revision | 126.29 |
| run_008 | completed | strict | False | 1 | False | 0.97 | 0/23/0 | basal | Keep the current profile unchanged for now | 132.08 |
| run_009 | completed | failed | False | 1 | False | 0.94 | — | nan | nan | 141.51 |
| run_010 | completed | strict | False | 1 | False | 0.94 | 0/23/0 | basal | Keep the current profile and verify fasting overnight behavior before any dependent edit | 133.16 |
| run_011 | completed | strict | False | 1 | False | 0.94 | 0/23/0 | basal | Keep the profile unchanged and separate the problem windows before considering any dependent edit | 155.06 |
| run_012 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the basal profile unchanged and verify the daytime rise with meal-logged observation | 118.95 |
| run_013 | completed | strict | False | 1 | False | 0.97 | 0/23/0 | basal | Keep the profile unchanged for now | 139.96 |
| run_014 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the profile unchanged and verify one quiet overnight block | 107.94 |
| run_015 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the basal profile unchanged and verify with one fasting-like window | 121.95 |
| run_016 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Log representative meals before changing bolus settings | 118.94 |
| run_017 | completed | strict | False | 1 | False | 0.97 | 0/23/0 | basal | Keep the current profile and verify one fasting-like window before any profile change | 130.35 |
| run_018 | completed | strict | False | 1 | False | 0.97 | — | nan | nan | 132.0 |
| run_019 | completed | strict | False | 1 | False | 0.97 | 0/23/0 | basal | Keep the current profile and verify with one structured observation window | 136.48 |
| run_020 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep basal unchanged and verify with one clean fasting-like window | 113.18 |
| run_021 | completed | strict | False | 1 | False | 0.97 | 0/23/0 | basal | Keep the current profile unchanged and verify with fasting and meal logs first | 142.25 |
| run_022 | completed | strict | False | 1 | False | 0.91 | 0/23/0 | basal | Keep the current basal profile and verify one clean daytime window first | 134.68 |
| run_023 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Hold basal steady and verify with a clean fasting window | 150.79 |
| run_024 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep basal unchanged and verify one controlled window first | 135.52 |
| run_025 | completed | strict | False | 1 | False | 0.97 | 1/22/0 | basal | Trial a small overnight basal reduction only | 157.82 |
| run_026 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the basal profile unchanged and verify with one fasting-style observation | 114.56 |
| run_027 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the current profile unchanged and verify the overnight low window | 115.33 |
| run_028 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the basal profile unchanged and verify one daytime fasting-like window | 139.88 |
| run_029 | completed | strict | False | 1 | False | 0.94 | 0/23/0 | basal | Keep the current basal profile and verify overnight behavior first | 156.17 |
| run_030 | completed | strict | False | 1 | False | 0.97 | 0/23/0 | basal | Keep the current profile unchanged and verify the nocturnal pattern first | 132.2 |
| run_031 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Verify daytime basal before changing it | 118.29 |
| run_032 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the basal profile unchanged and verify the daytime pattern first | 111.48 |
| run_033 | completed | strict | False | 1 | False | 0.97 | 0/23/0 | basal | Keep the profile unchanged and verify with a controlled separated observation | 112.46 |
| run_034 | completed | strict | False | 1 | False | 0.91 | 0/23/0 | basal | Keep the profile unchanged and verify one clean observation | 151.2 |
| run_035 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the profile unchanged and validate with one fully logged meal day first | 97.93 |
| run_036 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the current profile unchanged and verify with meal-linked observation | 102.76 |
| run_037 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Verify one clean overnight and one afternoon window before changing basal | 98.16 |
| run_038 | completed | strict | False | 1 | False | 0.97 | 0/23/0 | basal | Keep the basal profile unchanged and verify overnight behavior first | 112.93 |
| run_039 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Verify one clean overnight fasting block before any profile change | 92.25 |
| run_040 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the current profile unchanged and verify one fasting-style window first | 97.57 |
| run_041 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the current basal and target profile unchanged for now | 94.46 |
| run_042 | completed | strict | False | 1 | False | 0.97 | 0/23/0 | basal | Verify the basal pattern before any profile change | 130.57 |
| run_043 | completed | strict | False | 1 | False | 0.94 | 0/23/0 | basal | Keep the basal profile unchanged and verify with a structured fasting-like daytime window | 112.76 |
| run_044 | completed | strict | False | 1 | False | 0.97 | 0/23/0 | basal | Hold basal profile and verify with a fasting-only window | 115.7 |
| run_045 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep basal unchanged and verify with one logged window | 93.77 |
| run_046 | completed | strict | False | 1 | False | 0.97 | 1/22/0 | basal | Review the 00:00 basal segment first | 121.63 |
| run_047 | completed | strict | False | 1 | False | 0.97 | 0/23/0 | basal | Keep the current profile and verify one normal overnight trace first | 111.07 |
| run_048 | completed | strict | False | 1 | False | 0.97 | 0/23/0 | basal | Keep basal and target profile unchanged pending one fasting verification | 124.6 |
| run_049 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the current profile and verify one quiet overnight period | 83.26 |
| run_050 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep basal and targets unchanged for now | 81.79 |

### Schema violations remaining after correction

- run_001: steps with invalid status [] / confidence ['automation_smb_uam', 'synthesis_plan']
- run_002: steps with invalid status [] / confidence ['profile_cr_isf_dia']
- run_003: meal_strategy_summary.confidence=low-to-medium
- run_004: steps with invalid status [] / confidence ['profile_cr_isf_dia', 'automation_sensitivity_limits']
- run_005: steps with invalid status [] / confidence ['profile_cr_isf_dia', 'automation_smb_uam']
- run_008: meal_strategy_summary fields: ['confidence', 'confidence_note', 'exceptions', 'next_observation', 'rationale', 'suggestion']
- run_009: profile_recommendation missing required field(s): ['recommendation'] | profile_recommendation fields: ['confidence', 'decision', 'focus', 'next_check', 'rationale']
- run_010: steps with invalid status [] / confidence ['automation_smb_uam', 'meal_bolus_strategy'] | meal_strategy_summary.confidence=low-medium
- run_011: steps with invalid status [] / confidence ['profile_cr_isf_dia', 'automation_smb_uam'] | profile_recommendation.confidence=medium-low
- run_013: steps with invalid status [] / confidence ['profile_cr_isf_dia', 'automation_sensitivity_limits']
- run_017: steps with invalid status [] / confidence ['automation_smb_uam']
- run_018: current_value not copied exactly: ['aaps.core.carb_absorption']
- run_019: steps with invalid status [] / confidence ['automation_sensitivity_limits']
- run_021: steps with invalid status [] / confidence ['automation_smb_uam']
- run_022: steps with invalid status [] / confidence ['profile_cr_isf_dia', 'automation_sensitivity_limits', 'meal_bolus_strategy'] | profile_recommendation.confidence=medium-low | meal_strategy_summary.confidence=low-to-medium
- run_025: steps with invalid status [] / confidence ['safety_overview', 'profile_cr_isf_dia', 'automation_smb_uam']
- run_029: steps with invalid status [] / confidence ['profile_cr_isf_dia', 'automation_smb_uam'] | meal_strategy_summary.confidence=low_medium
- run_030: steps with invalid status [] / confidence ['automation_smb_uam', 'meal_bolus_strategy']
- run_033: steps with invalid status [] / confidence ['profile_cr_isf_dia', 'automation_smb_uam', 'meal_bolus_strategy']
- run_034: steps with invalid status [] / confidence ['synthesis_plan'] | profile_recommendation.confidence=medium-low | meal_strategy_summary.confidence=low-medium
- run_038: steps with invalid status [] / confidence ['basal_targets', 'profile_cr_isf_dia', 'automation_smb_uam']
- run_042: profile_recommendation fields: ['confidence', 'confidence_note', 'decision', 'focus', 'next_check', 'rationale', 'recommendation']
- run_043: steps with invalid status [] / confidence ['automation_sensitivity_limits'] | meal_strategy_summary fields: ['confidence', 'e_carbs', 'exceptions', 'immediate_bolus_percent', 'next_observation', 'prebolus_minutes', 'rationale', 'suggestion']
- run_044: steps with invalid status [] / confidence ['profile_cr_isf_dia', 'automation_smb_uam']
- run_046: steps with invalid status [] / confidence ['automation_smb_uam']
- run_047: steps with invalid status [] / confidence ['profile_cr_isf_dia', 'automation_smb_uam']
- run_048: steps with invalid status [] / confidence ['automation_smb_uam']

## Experiment `real_gpt56sol_med_50` — model `gpt-5.6-sol`

- Runs: 50 (completed 50, failed 0)
- Final JSON extracted: 50/50 (methods: strict ×50)
- Fully schema-compliant: 50/50; mean schema score 1.000
- Mean wall time per run: 306s
- **App outcome (as the app behaves), over 50 completed runs:** accepted first time 50; accepted after the repair prompt 0; invalid JSON, no prompt offered 0; schema stop, no prompt offered 0; still rejected after repair 0
- **Accepted by the app but breaking Prompt 4's own rules:** 0/50 accepted runs; commonest: —
- **App loop:** first pass parseable 50/50, first pass compliant 50/50; correction prompt sent in 0 run(s); compliant after correction 50/50
- Decisions per run — change: 0.0 ×32, 1.0 ×16, 2.0 ×2; keep: 23.0 ×32, 22.0 ×16, 21.0 ×2; verify: 0.0 ×50
- profile_recommendation focus: target ×39, basal ×11
- profile_recommendation decision: keep ×32, change ×18; confidence: medium ×50
- Primary recommendation area: target ×28, basal ×9, profile ×8, safety_and_data ×2, data_and_profile ×2, safety ×1; priority: safety ×50
- Meal strategy confidence: low ×50; exceptions: 2.0 ×25, 0.0 ×13, 1.0 ×12
- **Decision stability index** (mean per-parameter agreement): 0.983; parameters with unanimous decisions: 21/23
- Pairwise change-set Jaccard: mean 0.517; same primary area 36%; same profile focus 65%
- Pairwise text similarity — summary 0.144, profile recommendation 0.341, meal suggestion 0.080

### Parameter decision agreement

| parameter_key | current | modal | agreement | change | keep | verify | suggested values (when change) |
|---|---|---|---|---|---|---|---|
| profile.target.00_00 | 90 mg/dL | keep | 0.64 | 18 | 32 | 0 | 100 mg/dl x18 |
| profile.target.23_00 | 90 mg/dL | keep | 0.96 | 2 | 48 | 0 | 100 mg/dl x2 |
| aaps.core.carb_absorption | min_5m_carbimpact=8 mg/dL/5 min; meal_max_absorption_hours=7 h | keep | 1.00 | 0 | 50 | 0 |  |
| aaps.core.safety_limits | max_basal_u_per_hour=12 U/h; max_iob_units=25 U | keep | 1.00 | 0 | 50 | 0 |  |
| aaps.core.sensitivity | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=70 % | keep | 1.00 | 0 | 50 | 0 |  |
| aaps.core.smb_activation | smb_always_enabled=true; smb_with_cob_enabled=false; smb_after_carbs_enabled=false; smb_with_temp_target_enabled=true; smb_with_high_temp_target_enabled=false | keep | 1.00 | 0 | 50 | 0 |  |
| aaps.core.smb_delivery | smb_interval_minutes=3 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=20 min | keep | 1.00 | 0 | 50 | 0 |  |
| aaps.core.smb_uam | smb_enabled=true; uam_enabled=true | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.00_00 | 0.6 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.05_00 | 0.7 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.06_00 | 0.8 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.10_00 | 0.7 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.16_00 | 0.5 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.18_00 | 0.6 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.19_00 | 0.7 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.00_00 | 13 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.04_00 | 11.1 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.08_00 | 13.2 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.16_00 | 10.5 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.20_00 | 12.6 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.dia | 10 h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.isf.00_00 | 56 mg/dL/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.target.08_00 | 100 mg/dL | keep | 1.00 | 0 | 50 | 0 |  |

### Analysis step status / confidence agreement

| step | modal status | agreement | modal confidence | agreement |
|---|---|---|---|---|
| data_quality | completed | 1.00 | high | 1.00 |
| safety_overview | completed | 1.00 | high | 1.00 |
| basal_targets | partial | 0.96 | medium | 1.00 |
| profile_cr_isf_dia | partial | 1.00 | low | 0.86 |
| automation_smb_uam | completed | 0.86 | medium | 1.00 |
| automation_sensitivity_limits | completed | 0.86 | medium | 1.00 |
| meal_bolus_strategy | partial | 1.00 | low | 1.00 |
| meal_ecarbs_absorption | partial | 0.64 | low | 0.96 |
| synthesis_plan | completed | 1.00 | medium | 1.00 |

### Per-run overview

| run | status | 1st pass JSON | 1st pass OK | repairs | final OK | score | change/keep/verify | profile focus | primary rec | time (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| run_001 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Primary: keep the profile stable and verify the low pattern first | 306.33 |
| run_002 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Review the 00:00 glucose target first | 295.55 |
| run_003 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the profile while verifying the overnight low pattern | 283.02 |
| run_004 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Primary: verify the context of recurrent lows before changing the profile | 321.76 |
| run_005 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Primary: review the midnight target | 305.87 |
| run_006 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the profile and verify the overnight pattern first | 302.41 |
| run_007 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the profile unchanged while verifying recurrent lows | 336.12 |
| run_008 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the profile unchanged while verifying the recurrent low pattern | 334.16 |
| run_009 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Prioritize overnight low attribution before changing the profile | 291.91 |
| run_010 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the profile and verify the overnight low pattern first | 324.26 |
| run_011 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | target | Increase the contiguous overnight target safety margin | 321.26 |
| run_012 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the profile unchanged while verifying the low patterns | 288.45 |
| run_013 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Reconstruct recurrent low-glucose sequences before changing settings | 320.74 |
| run_014 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Primary: test a less aggressive midnight target | 321.32 |
| run_015 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Characterize recurrent lows before changing settings | 314.54 |
| run_016 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Primary: reconstruct severe-low insulin sequences before changing settings | 293.48 |
| run_017 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Primary review: raise the midnight target | 290.85 |
| run_018 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Primary: review a higher 00:00 target | 319.99 |
| run_019 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Primary: keep the profile stable while isolating overnight lows | 324.49 |
| run_020 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Validate the overnight pattern before changing the profile | 280.94 |
| run_021 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Primary: review a higher 00:00 target | 309.68 |
| run_022 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Verify overnight profile behavior first | 292.43 |
| run_023 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Primary review: reduce overnight low pressure | 301.36 |
| run_024 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the selected profile while verifying the overnight low pattern | 325.18 |
| run_025 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the profile provisionally and verify the low pattern first | 303.87 |
| run_026 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Verify the overnight low pattern before changing the profile | 287.43 |
| run_027 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the profile unchanged while verifying overnight insulin exposure | 318.29 |
| run_028 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | target | Review one continuous overnight target change first | 313.38 |
| run_029 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the current profile while validating the recurrent low pattern | 304.17 |
| run_030 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Primary: review a higher 00:00 overnight target | 318.9 |
| run_031 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Verify the recurrent low pattern before changing the profile | 308.23 |
| run_032 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Primary: preserve the profile while verifying the recurrent overnight low pattern | 286.82 |
| run_033 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Primary review: raise the 00:00 target candidate | 324.32 |
| run_034 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Verify the overnight low pattern before changing the profile | 307.37 |
| run_035 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the profile unchanged while verifying low-IOB overnight behaviour | 284.71 |
| run_036 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the profile unchanged while verifying the overnight low pattern | 315.93 |
| run_037 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Review one conservative overnight target change first | 303.84 |
| run_038 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Validate the overnight low mechanism before changing the profile | 354.35 |
| run_039 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the profile stable while verifying the high-IOB-to-late-low pattern | 300.03 |
| run_040 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the profile while verifying the overnight low mechanism | 296.4 |
| run_041 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the profile while verifying the overnight low pattern | 292.08 |
| run_042 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Primary: review a higher 00:00 target | 308.57 |
| run_043 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Verify the recurrent overnight low pattern before changing the profile | 306.89 |
| run_044 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Primary: review a higher overnight target | 311.07 |
| run_045 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Review a higher midnight target first | 301.12 |
| run_046 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the profile unchanged while verifying overnight low exposure | 273.97 |
| run_047 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Primary review: increase the 00:00 target segment | 297.51 |
| run_048 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Primary review: raise the 00:00 target | 287.64 |
| run_049 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the profile stable while isolating overnight lows | 290.42 |
| run_050 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Primary: review a higher target after midnight | 320.62 |

## Experiment `real_grok46_50` — model `x-ai/grok-4.6`

- Runs: 50 (completed 50, failed 0)
- Final JSON extracted: 50/50 (methods: strict ×50)
- Fully schema-compliant: 49/50; mean schema score 0.999
- Mean wall time per run: 522s
- **App outcome (as the app behaves), over 50 completed runs:** accepted first time 50; accepted after the repair prompt 0; invalid JSON, no prompt offered 0; schema stop, no prompt offered 0; still rejected after repair 0
- **Accepted by the app but breaking Prompt 4's own rules:** 1/50 accepted runs; commonest: steps_fields_exact ×1
- **App loop:** first pass parseable 50/50, first pass compliant 49/50; correction prompt sent in 1 run(s); compliant after correction 49/50
- Sections the app would flag: analysis_steps.safety_overview ×1, analysis_steps.basal_targets ×1, analysis_steps.profile_cr_isf_dia ×1, analysis_steps.automation_smb_uam ×1, analysis_steps.automation_sensitivity_limits ×1, analysis_steps.meal_bolus_strategy ×1, analysis_steps.meal_ecarbs_absorption ×1, analysis_steps.synthesis_plan ×1
- Corrections that changed a decision (not just format): 0/1 comparable; changed profile focus: 0/1
- Decisions per run — change: 0.0 ×40, 2.0 ×6, 1.0 ×4; keep: 23.0 ×40, 21.0 ×6, 22.0 ×4; verify: 0.0 ×50
- profile_recommendation focus: target ×33, basal ×17
- profile_recommendation decision: keep ×40, change ×10; confidence: medium ×50
- Primary recommendation area: target ×33, basal ×16, profile ×1; priority: safety ×41, high ×9
- Meal strategy confidence: low ×44, medium ×6; exceptions: 2.0 ×38, 1.0 ×7, 0.0 ×5
- **Decision stability index** (mean per-parameter agreement): 0.986; parameters with unanimous decisions: 21/23
- Pairwise change-set Jaccard: mean 0.664; same primary area 53%; same profile focus 54%
- Pairwise text similarity — summary 0.108, profile recommendation 0.393, meal suggestion 0.117

### Parameter decision agreement

| parameter_key | current | modal | agreement | change | keep | verify | suggested values (when change) |
|---|---|---|---|---|---|---|---|
| profile.target.00_00 | 90 mg/dL | keep | 0.80 | 10 | 40 | 0 | 100 mg/dl x10 |
| profile.target.23_00 | 90 mg/dL | keep | 0.88 | 6 | 44 | 0 | 100 mg/dl x6 |
| aaps.core.carb_absorption | min_5m_carbimpact=8 mg/dL/5 min; meal_max_absorption_hours=7 h | keep | 1.00 | 0 | 50 | 0 |  |
| aaps.core.safety_limits | max_basal_u_per_hour=12 U/h; max_iob_units=25 U | keep | 1.00 | 0 | 50 | 0 |  |
| aaps.core.sensitivity | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=70 % | keep | 1.00 | 0 | 50 | 0 |  |
| aaps.core.smb_activation | smb_always_enabled=true; smb_with_cob_enabled=false; smb_after_carbs_enabled=false; smb_with_temp_target_enabled=true; smb_with_high_temp_target_enabled=false | keep | 1.00 | 0 | 50 | 0 |  |
| aaps.core.smb_delivery | smb_interval_minutes=3 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=20 min | keep | 1.00 | 0 | 50 | 0 |  |
| aaps.core.smb_uam | smb_enabled=true; uam_enabled=true | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.00_00 | 0.6 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.05_00 | 0.7 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.06_00 | 0.8 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.10_00 | 0.7 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.16_00 | 0.5 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.18_00 | 0.6 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.19_00 | 0.7 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.00_00 | 13 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.04_00 | 11.1 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.08_00 | 13.2 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.16_00 | 10.5 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.20_00 | 12.6 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.dia | 10 h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.isf.00_00 | 56 mg/dL/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.target.08_00 | 100 mg/dL | keep | 1.00 | 0 | 50 | 0 |  |

### Analysis step status / confidence agreement

| step | modal status | agreement | modal confidence | agreement |
|---|---|---|---|---|
| data_quality | completed | 1.00 | high | 1.00 |
| safety_overview | completed | 1.00 | high | 0.96 |
| basal_targets | partial | 0.86 | medium | 1.00 |
| profile_cr_isf_dia | partial | 1.00 | low | 0.92 |
| automation_smb_uam | completed | 0.96 | medium | 1.00 |
| automation_sensitivity_limits | completed | 0.94 | medium | 0.96 |
| meal_bolus_strategy | partial | 0.94 | low | 0.92 |
| meal_ecarbs_absorption | completed | 0.64 | high | 0.62 |
| synthesis_plan | completed | 1.00 | medium | 1.00 |

### Per-run overview

| run | status | 1st pass JSON | 1st pass OK | repairs | final OK | score | change/keep/verify | profile focus | primary rec | time (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| run_001 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the profile and do not add insulin for afternoon highs | 587.24 |
| run_002 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Review raising only the 00:00 target from 90 to 100 mg/dL | 567.95 |
| run_003 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the profile and first separate overnight IOB from target and basal | 548.25 |
| run_004 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the profile and separate leftover IOB from overnight landing | 568.21 |
| run_005 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the current profile and verify nights without leftover meal IOB | 530.92 |
| run_006 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the overnight profile and compare midnight IOB with overnight lows | 557.64 |
| run_007 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the profile and verify overnight lows against leftover IOB | 445.58 |
| run_008 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | target | Review overnight targets 23:00 and 00:00 first | 568.02 |
| run_009 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep overnight profile settings and separate evening IOB from overnight insulin | 496.62 |
| run_010 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the current profile and first separate overnight lows from leftover IOB | 512.2 |
| run_011 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Review a single overnight 00:00 target raise | 589.05 |
| run_012 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep overnight profile settings and split 00:00-03:00 lows by leftover IOB | 537.87 |
| run_013 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | target | Review a higher overnight target only | 570.5 |
| run_014 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the profile and verify early-night lows against leftover afternoon IOB | 490.83 |
| run_015 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep overnight target and basal; verify residual IOB first | 559.3 |
| run_016 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the current profile and treat overnight lows as the first review constraint | 537.84 |
| run_017 | completed | strict | False | 1 | False | 0.97 | 2/21/0 | target | Review raising overnight target from 90 to 100 mg/dL | 575.77 |
| run_018 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the current profile and separate leftover IOB from overnight basal and target | 573.84 |
| run_019 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the profile and verify overnight lows before any edit | 570.51 |
| run_020 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the profile and separate leftover IOB from overnight basal first | 438.57 |
| run_021 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the basal and target profile and separate leftover IOB from overnight basal | 462.25 |
| run_022 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep overnight target 90 mg/dL until lows are split from afternoon IOB | 490.89 |
| run_023 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the current basal profile and verify overnight lows against evening insulin | 430.84 |
| run_024 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the full profile and first separate overnight lows from residual IOB | 503.73 |
| run_025 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep overnight basal and target; classify evening IOB first | 496.23 |
| run_026 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep overnight basal and target and verify IOB at lows first | 491.35 |
| run_027 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep overnight settings and separate leftover IOB first | 563.08 |
| run_028 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the selected profile and verify overnight IOB before any basal or target edit | 535.02 |
| run_029 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the current profile and verify overnight residual insulin first | 505.94 |
| run_030 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the profile and separate overnight IOB from basal | 471.53 |
| run_031 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the current profile and separate evening IOB from the 19:00 basal step first | 536.59 |
| run_032 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the overnight profile and verify IOB tail first | 590.9 |
| run_033 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | target | Review raising the overnight target only | 513.15 |
| run_034 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the selected profile and separate overnight leftover IOB from target 90 mg/dL | 521.43 |
| run_035 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Raise the 00:00 overnight target before any insulin-adding change | 503.38 |
| run_036 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Hold the profile and verify overnight lows against residual IOB | 548.87 |
| run_037 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep overnight profile and verify low-IOB nights first | 483.44 |
| run_038 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Raise only the 00:00 target from 90 to 100 mg/dL | 557.05 |
| run_039 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the profile and verify overnight lows before any segment edit | 507.47 |
| run_040 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the profile and first test overnight lows against leftover IOB | 458.07 |
| run_041 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep night target 90 and separate overnight TBR sources first | 527.02 |
| run_042 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the profile and first separate overnight lows from leftover IOB | 503.29 |
| run_043 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the profile and first separate overnight lows from leftover IOB | 515.83 |
| run_044 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the basal profile and split overnight observation by evening IOB | 498.37 |
| run_045 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep overnight target and basal until IOB at lows is seen | 534.61 |
| run_046 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | target | Align overnight target with daytime 100 mg/dL | 504.91 |
| run_047 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the full profile and separate overnight lows from leftover IOB first | 530.05 |
| run_048 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the overnight profile and verify lows before any insulin-increasing edit | 414.04 |
| run_049 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the current profile and collect meal-timed observations first | 512.25 |
| run_050 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | target | Review overnight target 90 toward daytime 100 | 574.61 |

### Schema violations remaining after correction

- run_017: steps with wrong field set: ['safety_overview', 'basal_targets', 'profile_cr_isf_dia', 'automation_smb_uam', 'automation_sensitivity_limits', 'meal_bolus_strategy', 'meal_ecarbs_absorption', 'synthesis_plan']

## Experiment `real_haiku45_50` — model `claude-haiku-4-5`

- Runs: 50 (completed 50, failed 0)
- Final JSON extracted: 49/50 (methods: fenced ×49, failed ×1)
- Fully schema-compliant: 3/49; mean schema score 0.930
- Mean wall time per run: 737s
- Estimated API cost: $24.67 total, $0.49 per run (list prices; output includes thinking)
- **App outcome (as the app behaves), over 50 completed runs:** accepted first time 17; accepted after the repair prompt 3; invalid JSON, no prompt offered 2; schema stop, no prompt offered 1; still rejected after repair 27
- **Accepted by the app but breaking Prompt 4's own rules:** 17/20 accepted runs; commonest: steps_enums_valid ×9, decisions_verify_rule ×5, meal_confidence_valid ×4, steps_fields_exact ×4, profile_rec_confidence_valid ×3
- **App loop:** first pass parseable 48/50, first pass compliant 2/50; correction prompt sent in 44 run(s); compliant after correction 3/50
- Sections the app would flag: profile_recommendation.focus ×29, analysis_steps.basal_targets.confidence ×18, analysis_steps.automation_smb_uam.confidence ×12, analysis_steps.meal_bolus_strategy.confidence ×9, analysis_steps.automation_sensitivity_limits ×7, analysis_steps.meal_bolus_strategy ×7, analysis_steps.meal_ecarbs_absorption ×7, analysis_steps.synthesis_plan.confidence ×7, analysis_steps.automation_smb_uam ×6, analysis_steps.synthesis_plan ×6, parameter_decisions.aaps.core.sensitivity.current_value ×6, analysis_steps.meal_ecarbs_absorption.confidence ×6; first pass not valid JSON at all ×2
- Corrections that changed a decision (not just format): 0/15 comparable; changed profile focus: 2/15 (2 unparseable first pass(es) not comparable)
- Decisions per run — change: 1.0 ×10, 2.0 ×7, 0.0 ×2, 3.0 ×1; keep: 22.0 ×9, 21.0 ×6, 20.0 ×4, 23.0 ×1; verify: 0.0 ×15, 1.0 ×4, 2.0 ×1
- profile_recommendation focus: basal ×18, isf ×2
- profile_recommendation decision: change ×16, keep ×4; confidence: high ×10, medium ×7, medium-high ×3
- Primary recommendation area: basal ×11, meal_strategy ×3, meal_bolus_strategy ×3, Carbohydrate logging (highest-leverage behavior change) ×1, isf ×1, meal_carbs ×1; priority: high ×14, safety ×6
- Meal strategy confidence: medium ×12, low ×3, low-medium ×2, medium-high ×2, high ×1; exceptions: 2.0 ×19, 1.0 ×1
- **Decision stability index** (mean per-parameter agreement): 0.928; parameters with unanimous decisions: 13/23
- Pairwise change-set Jaccard: mean 0.376; same primary area 5%; same profile focus 13%
- Pairwise text similarity — summary 0.356, profile recommendation 0.360, meal suggestion 0.353

### Parameter decision agreement

| parameter_key | current | modal | agreement | change | keep | verify | suggested values (when change) |
|---|---|---|---|---|---|---|---|
| profile.basal.10_00 | 0.7 U/h | keep | 0.50 | 10 | 10 | 0 | 0.8 u/h x4 | 0.85 u/h x3 | 0.85–0.95 u/h x1 | 0.8–0.85 u/h x1 | 0.7 u/h x1 |
| profile.basal.16_00 | 0.5 U/h | keep | 0.65 | 7 | 13 | 0 | 0.6 u/h x3 | 0.7–0.75 u/h x1 | 0.65 x1 | 0.7 u/h x1 | 0.8 u/h x1 |
| aaps.core.carb_absorption | min_5m_carbimpact=8 mg/dL/5 min; meal_max_absorption_hours=7 h | keep | 0.80 | 2 | 16 | 2 | min_5m_carbimpact=12–15 mg/dl/5 min; meal_max_absorption_hours=7 h x1 | min_5m_carbimpact=5 mg/dl/5 min; meal_max_absorption_hours=7 h x1 |
| profile.basal.00_00 | 0.6 U/h | keep | 0.85 | 3 | 17 | 0 | 0.5 u/h x2 | 0.55 u/h x1 |
| aaps.core.safety_limits | max_basal_u_per_hour=12 U/h; max_iob_units=25 U | keep | 0.90 | 1 | 18 | 1 | max_basal_u_per_hour=12 u/h; max_iob_units=20 u x1 |
| aaps.core.sensitivity | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=70 % | keep | 0.90 | 0 | 18 | 2 |  |
| profile.isf.00_00 | 56 mg/dL/U | keep | 0.90 | 2 | 18 | 0 | 110 mg/dl/u x1 | 50 mg/dl/u x1 |
| aaps.core.smb_activation | smb_always_enabled=true; smb_with_cob_enabled=false; smb_after_carbs_enabled=false; smb_with_temp_target_enabled=true; smb_with_high_temp_target_enabled=false | keep | 0.95 | 0 | 19 | 1 |  |
| profile.basal.19_00 | 0.7 U/h | keep | 0.95 | 1 | 19 | 0 | 0.6 u/h x1 |
| profile.dia | 10 h | keep | 0.95 | 1 | 19 | 0 | 6.0–7.0 h x1 |
| aaps.core.smb_delivery | smb_interval_minutes=3 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=20 min | keep | 1.00 | 0 | 20 | 0 |  |
| aaps.core.smb_uam | smb_enabled=true; uam_enabled=true | keep | 1.00 | 0 | 20 | 0 |  |
| profile.basal.05_00 | 0.7 U/h | keep | 1.00 | 0 | 20 | 0 |  |
| profile.basal.06_00 | 0.8 U/h | keep | 1.00 | 0 | 20 | 0 |  |
| profile.basal.18_00 | 0.6 U/h | keep | 1.00 | 0 | 20 | 0 |  |
| profile.cr.00_00 | 13 g/U | keep | 1.00 | 0 | 20 | 0 |  |
| profile.cr.04_00 | 11.1 g/U | keep | 1.00 | 0 | 20 | 0 |  |
| profile.cr.08_00 | 13.2 g/U | keep | 1.00 | 0 | 20 | 0 |  |
| profile.cr.16_00 | 10.5 g/U | keep | 1.00 | 0 | 20 | 0 |  |
| profile.cr.20_00 | 12.6 g/U | keep | 1.00 | 0 | 20 | 0 |  |
| profile.target.00_00 | 90 mg/dL | keep | 1.00 | 0 | 20 | 0 |  |
| profile.target.08_00 | 100 mg/dL | keep | 1.00 | 0 | 20 | 0 |  |
| profile.target.23_00 | 90 mg/dL | keep | 1.00 | 0 | 20 | 0 |  |

### Analysis step status / confidence agreement

| step | modal status | agreement | modal confidence | agreement |
|---|---|---|---|---|
| data_quality | completed | 1.00 | high | 1.00 |
| safety_overview | completed | 1.00 | high | 0.95 |
| basal_targets | completed | 1.00 | high | 0.40 |
| profile_cr_isf_dia | completed | 1.00 | medium | 0.75 |
| automation_smb_uam | completed | 1.00 | high | 0.75 |
| automation_sensitivity_limits | completed | 1.00 | medium | 0.50 |
| meal_bolus_strategy | completed | 1.00 | medium | 0.55 |
| meal_ecarbs_absorption | completed | 1.00 | medium | 0.40 |
| synthesis_plan | completed | 1.00 | medium | 0.45 |

### Per-run overview

| run | status | 1st pass JSON | 1st pass OK | repairs | final OK | score | change/keep/verify | profile focus | primary rec | time (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| run_001 | completed | failed | False | 1 | None | — | — | nan | nan | 929.57 |
| run_002 | completed | fenced | False | 1 | False | 0.91 | — | nan | nan | 632.36 |
| run_003 | completed | fenced | False | 1 | False | 0.82 | — | nan | nan | 793.77 |
| run_004 | completed | fenced | False | 1 | False | 0.97 | — | nan | nan | 909.28 |
| run_005 | completed | failed | False | 1 | False | 0.85 | — | nan | nan | 905.72 |
| run_006 | completed | fenced | False | 1 | False | 0.97 | 1/22/0 | basal | Reduce basal 00:00 from 0.6 U/h to 0.55 U/h or 0.5 U/h to address hour 1 lows (18.5% TBR, nadir 42–55 mg/dL). | 703.18 |
| run_007 | completed | fenced | False | 1 | False | 0.91 | 2/21/0 | basal | Raise basal in 10:00–16:00 afternoon window to address persistent hyperglycemia. | 767.54 |
| run_008 | completed | fenced | False | 1 | False | 0.97 | 3/20/0 | basal | Implement meal carbohydrate logging | 838.02 |
| run_009 | completed | fenced | False | 1 | False | 0.97 | 2/20/1 | basal | Reduce overnight and evening basal segments to address recurrent hypoglycemia | 708.92 |
| run_010 | completed | fenced | False | 1 | False | 0.85 | — | nan | nan | 825.12 |
| run_011 | completed | fenced | False | 1 | False | 0.91 | — | nan | nan | 900.18 |
| run_012 | completed | fenced | False | 1 | False | 0.97 | 1/22/0 | basal | Increase afternoon basal conservatively (16:00 segment 0.5→0.65 U/h; 10:00–13:00 segment 0.7→0.80 U/h) and monitor for 2–3 days. | 640.85 |
| run_013 | completed | fenced | False | 1 | False | 0.97 | 2/21/0 | basal | Increase basal rate 10:00–16:00 window to address midday elevation | 872.31 |
| run_014 | completed | fenced | False | 1 | False | 0.94 | — | nan | nan | 788.18 |
| run_015 | completed | fenced | False | 1 | False | 0.91 | — | nan | nan | 776.69 |
| run_016 | completed | fenced | False | 1 | False | 0.97 | 1/22/0 | basal | Verify and increase basal in afternoon peak window (08:00–17:00 local) | 836.38 |
| run_017 | completed | fenced | False | 1 | False | 0.88 | — | nan | nan | 786.27 |
| run_018 | completed | fenced | False | 1 | False | 0.97 | 2/21/0 | basal | Strengthen afternoon basal (10:00–15:59) and eliminate evening basal valley (16:00–17:59) to address concurrent hyperglycemia and hypoglycemia clustering. | 704.72 |
| run_019 | completed | fenced | False | 1 | False | 0.91 | 1/22/0 | basal | Increase basal rate 10:00–16:00 window from 0.7 to 0.8 U/h to address primary afternoon hyperglycemia driver | 606.77 |
| run_020 | completed | fenced | False | 1 | False | 0.94 | — | nan | nan | 694.21 |
| run_021 | completed | fenced | True | 0 | True | 1.00 | 2/21/0 | isf | Raise ISF from 56 to 110 mg/dL/U | 436.96 |
| run_022 | completed | fenced | False | 1 | False | 0.97 | — | nan | nan | 717.72 |
| run_023 | completed | fenced | False | 1 | False | 0.97 | 1/22/0 | basal | Establish consistent meal bolus strategy: prebolus 0–15 min, immediate bolus 20–30% of total. | 801.35 |
| run_024 | completed | fenced | False | 1 | False | 0.88 | — | nan | nan | 739.63 |
| run_025 | completed | fenced | False | 1 | False | 0.94 | 1/22/0 | basal | Restore meal carbohydrate logging | 667.65 |
| run_026 | completed | fenced | False | 1 | False | 0.94 | 1/21/1 | basal | Implement carb logging immediately (prerequisite for all downstream optimizations) | 745.78 |
| run_027 | completed | fenced | False | 1 | False | 0.97 | 2/20/1 | basal | Increase midday basal 10:00–17:00 from 0.7 to 0.85 U/h; eliminate 16:00 step-down to 0.5 U/h | 944.08 |
| run_028 | completed | fenced | False | 1 | False | 0.97 | — | nan | nan | 710.84 |
| run_029 | completed | fenced | False | 1 | True | 1.00 | 1/22/0 | isf | Add explicit prebolus and at-meal bolus to replace SMB-only meal coverage | 792.93 |
| run_030 | completed | fenced | False | 1 | False | 0.97 | — | nan | nan | 686.03 |
| run_031 | completed | fenced | False | 0 | False | 0.97 | 1/22/0 | basal | Reduce early-morning basal 00:00 UTC from 0.6 U/h to 0.5 U/h | 426.54 |
| run_032 | completed | fenced | False | 1 | False | 0.91 | — | nan | nan | 764.49 |
| run_033 | completed | fenced | False | 0 | False | 0.68 | — | nan | nan | 577.34 |
| run_034 | completed | fenced | True | 0 | True | 1.00 | 1/22/0 | basal | Increase basal from 0.5 U/h to 0.8 U/h at 16:00 local segment. | 461.91 |
| run_035 | completed | fenced | False | 1 | False | 0.91 | — | nan | nan | 724.7 |
| run_036 | completed | fenced | False | 0 | False | 0.97 | 0/21/2 | basal | Adopt prebolus and meal logging to separate meal bolus from basal and SMB | 582.68 |
| run_037 | completed | fenced | False | 1 | False | 0.97 | — | nan | nan | 887.81 |
| run_038 | completed | fenced | False | 1 | False | 0.94 | — | nan | nan | 800.37 |
| run_039 | completed | fenced | False | 1 | False | 0.91 | — | nan | nan | 717.54 |
| run_040 | completed | fenced | False | 1 | False | 0.88 | — | nan | nan | 788.99 |
| run_041 | completed | fenced | False | 1 | False | 0.85 | — | nan | nan | 725.07 |
| run_042 | completed | fenced | False | 1 | False | 0.94 | — | nan | nan | 702.18 |
| run_043 | completed | fenced | False | 1 | False | 0.97 | — | nan | nan | 730.26 |
| run_044 | completed | fenced | False | 1 | False | 0.94 | — | nan | nan | 744.07 |
| run_045 | completed | fenced | False | 1 | False | 0.94 | 0/23/0 | basal | Obtain 3–5 day meal diary with carbohydrate amounts, timing, and macronutrient composition. | 907.66 |
| run_046 | completed | fenced | False | 1 | False | 0.88 | — | nan | nan | 681.6 |
| run_047 | completed | fenced | False | 1 | False | 0.94 | — | nan | nan | 747.28 |
| run_048 | completed | fenced | False | 0 | False | 0.91 | 2/20/1 | basal | Log all meals with estimated carbs; this is the primary change enabling all downstream improvements | 462.67 |
| run_049 | completed | fenced | False | 1 | False | 0.91 | — | nan | nan | 787.1 |
| run_050 | completed | fenced | False | 1 | False | 0.91 | — | nan | nan | 742.92 |

### Schema violations remaining after correction

- run_002: steps with wrong field set: ['data_quality', 'safety_overview', 'basal_targets', 'profile_cr_isf_dia', 'automation_smb_uam', 'automation_sensitivity_limits', 'meal_bolus_strategy', 'meal_ecarbs_absorption', 'synthesis_plan'] | steps with invalid status [] / confidence ['basal_targets', 'synthesis_plan'] | profile_recommendation.focus=ISF
- run_003: steps with invalid status [] / confidence ['basal_targets', 'automation_smb_uam', 'synthesis_plan'] | current_value not copied exactly: ['aaps.core.sensitivity'] | invalid decision value: ['profile.isf.00_00', 'profile.dia'] | verify without null component: ['profile.isf.00_00', 'profile.dia'] | profile_recommendation.focus=overall_profile_sequencing | profile_recommendation.decision=keep but profile rows imply change
- run_004: profile_recommendation.focus=basal, carb ratio, ISF, and DIA collectively
- run_005: steps with wrong field set: ['basal_targets', 'profile_cr_isf_dia', 'automation_smb_uam', 'automation_sensitivity_limits', 'meal_bolus_strategy', 'meal_ecarbs_absorption', 'synthesis_plan'] | steps with invalid status [] / confidence ['basal_targets', 'synthesis_plan'] | current_value not copied exactly: ['aaps.core.smb_activation'] | verify without null component: ['aaps.core.smb_activation', 'aaps.core.carb_absorption'] | profile_recommendation.focus=carb logging, then isf verification
- run_006: steps with invalid status [] / confidence ['basal_targets', 'profile_cr_isf_dia', 'meal_ecarbs_absorption']
- run_007: steps with invalid status [] / confidence ['profile_cr_isf_dia', 'automation_smb_uam', 'meal_bolus_strategy', 'synthesis_plan'] | profile_recommendation.confidence=medium-high | meal_strategy_summary.confidence=low-medium
- run_008: steps with invalid status [] / confidence ['basal_targets', 'automation_sensitivity_limits']
- run_009: verify without null component: ['aaps.core.sensitivity']
- run_010: steps with wrong field set: ['basal_targets', 'profile_cr_isf_dia', 'automation_smb_uam', 'automation_sensitivity_limits', 'meal_bolus_strategy', 'meal_ecarbs_absorption', 'synthesis_plan'] | steps with invalid status [] / confidence ['basal_targets', 'automation_smb_uam', 'meal_bolus_strategy'] | verify without null component: ['aaps.core.carb_absorption'] | profile_recommendation.focus=carbohydrate_ratio_and_meal_strategy | meal_strategy_summary.confidence=medium_high
- run_011: steps with wrong field set: ['automation_sensitivity_limits'] | steps with invalid status [] / confidence ['meal_ecarbs_absorption'] | profile_recommendation.focus=DIA (insulin duration)
- run_012: steps with wrong field set: ['meal_bolus_strategy']
- run_013: steps with wrong field set: ['automation_smb_uam', 'automation_sensitivity_limits', 'meal_bolus_strategy', 'meal_ecarbs_absorption']
- run_014: steps with invalid status [] / confidence ['basal_targets', 'automation_sensitivity_limits', 'meal_ecarbs_absorption'] | profile_recommendation.focus=meal_bolus_and_carb_logging
- run_015: invalid decision value: ['profile.isf.00_00'] | verify without null component: ['profile.isf.00_00'] | profile_recommendation.focus=DIA shortening (safety priority), basal timing adjustment (safety priority), basal increase at 10:00 segment (medium priority, conditional on ISF verification)
- run_016: meal_strategy_summary.confidence=medium-high
- run_017: analysis_steps keys ['data_quality', 'safety_overview', 'basal_targets', 'profile_cr_isf_dia', 'automation_smb_uam', 'automation_sensitivity_limits', 'synthesis_plan'] != workflow ['data_quality', 'safety_overview', 'basal_targets', 'profile_cr_isf_dia', 'automation_smb_uam', 'automation_sensitivity_limits', 'meal_bolus_strategy', 'meal_ecarbs_absorption', 'synthesis_plan'] | steps with invalid status [] / confidence ['profile_cr_isf_dia'] | current_value not copied exactly: ['aaps.core.sensitivity'] | profile_recommendation.focus=basal_and_targets_and_cr_and_isf_and_dia
- run_018: steps with wrong field set: ['basal_targets', 'profile_cr_isf_dia', 'automation_smb_uam', 'automation_sensitivity_limits', 'meal_bolus_strategy', 'meal_ecarbs_absorption', 'synthesis_plan']
- run_019: steps with invalid status [] / confidence ['basal_targets', 'automation_smb_uam', 'automation_sensitivity_limits', 'meal_bolus_strategy'] | profile_recommendation.confidence=medium-high | meal_strategy_summary.confidence=low-medium
- run_020: steps with invalid status [] / confidence ['automation_smb_uam'] | profile_recommendation.focus=carb_ratio
- run_022: profile_recommendation.focus=basal_and_meal_strategy_interaction
- run_023: steps with invalid status [] / confidence ['basal_targets', 'automation_smb_uam', 'automation_sensitivity_limits']
- run_024: steps with invalid status [] / confidence ['basal_targets'] | current_value not copied exactly: ['aaps.core.sensitivity'] | verify without null component: ['aaps.core.sensitivity'] | profile_recommendation.focus=meal_bolus_timing
- run_025: steps with invalid status [] / confidence ['basal_targets', 'meal_bolus_strategy', 'synthesis_plan'] | profile_recommendation.confidence=medium-high
- run_026: steps with invalid status [] / confidence ['safety_overview', 'profile_cr_isf_dia'] | verify without null component: ['aaps.core.smb_activation']
- run_027: verify without null component: ['aaps.core.carb_absorption']
- run_028: profile_recommendation.focus=Basal, ISF, CR, and target settings. ISF inadequacy drives Dynamic ISF compensation and overcorrection lows; overnight basal excess drives hour 1 lows; afternoon CR looseness combined with GLP-1 absorption delay drives sustained highs. Overnight target too tight buffers low risk when ISF and basal adjusted.
- run_030: profile_recommendation.focus=insulin_sensitivity_and_action_duration
- run_031: steps with invalid status [] / confidence ['profile_cr_isf_dia', 'meal_ecarbs_absorption', 'synthesis_plan']
- run_032: steps with invalid status [] / confidence ['basal_targets', 'automation_sensitivity_limits', 'meal_ecarbs_absorption', 'synthesis_plan'] | profile_recommendation.focus=basal_and_isf | profile_recommendation.confidence=medium-high
- run_033: top-level keys differ: missing=['profile_recommendation'] extra=[] | required sections absent or wrong type: ['profile_recommendation'] | profile_recommendation is not an object | steps with invalid status [] / confidence ['profile_cr_isf_dia', 'meal_bolus_strategy', 'meal_ecarbs_absorption', 'synthesis_plan'] | profile_recommendation missing required field(s): ['focus', 'decision', 'recommendation', 'rationale'] | profile_recommendation fields: [] | profile_recommendation.focus=None | profile_recommendation.decision=None | profile_recommendation.confidence=None | profile_recommendation.decision=None but profile rows imply change | meal_strategy_summary.confidence=medium (reactive strategy confirmed high confidence; carb-free approach valid). Low confidence in meal timing/size (inferred from glucose only; no logs). Medium confidence in GLP-1 effect quantification (absorption timing evident from telemetry, but effect magnitude not measured).
- run_035: steps with invalid status [] / confidence ['basal_targets'] | profile_recommendation.focus=meal_bolus_strategy_and_afternoon_basal | bad priority: ['No profile parameter changes indicated (CR, ISF, DIA, targets, non-afternoon basal remain stable)', 'Autosens remains disabled (intentional active tuning phase)', 'Dynamic ISF remains enabled at 70% (will operate at more moderate levels once meal bolusing is improved)']
- run_036: verify without null component: ['aaps.core.sensitivity', 'aaps.core.carb_absorption']
- run_037: profile_recommendation.focus=basal_carb_ratios_isf_dia
- run_038: current_value not copied exactly: ['aaps.core.carb_absorption'] | profile_recommendation.focus=DIA and meal_max_absorption_hours (carb and insulin absorption model parameters)
- run_039: steps with invalid status [] / confidence ['automation_smb_uam', 'automation_sensitivity_limits', 'meal_bolus_strategy', 'meal_ecarbs_absorption'] | profile_recommendation.focus=basal and max_iob | meal_strategy_summary.confidence=low-to-medium
- run_040: steps with invalid status [] / confidence ['meal_ecarbs_absorption'] | current_value not copied exactly: ['profile.dia', 'aaps.core.sensitivity', 'aaps.core.carb_absorption'] | verify without null component: ['aaps.core.carb_absorption'] | profile_recommendation.focus=DIA (Duration of Insulin Action)
- run_041: steps with wrong field set: ['profile_cr_isf_dia', 'automation_smb_uam', 'automation_sensitivity_limits', 'meal_bolus_strategy', 'meal_ecarbs_absorption', 'synthesis_plan'] | steps with invalid status [] / confidence ['profile_cr_isf_dia', 'meal_bolus_strategy'] | current_value not copied exactly: ['aaps.core.sensitivity'] | profile_recommendation.focus=meal_bolus_strategy | bad priority: ['Trial e-carbs for lunch meal if identified as slow-absorbing (high-fat, >40g carbs) during carb logging']
- run_042: steps with invalid status [] / confidence ['basal_targets', 'automation_smb_uam', 'meal_bolus_strategy'] | profile_recommendation.focus=basal_cr_isf_target
- run_043: profile_recommendation.focus=meal_bolus_and_carb_logging
- run_044: steps with wrong field set: ['meal_ecarbs_absorption', 'synthesis_plan'] | profile_recommendation.focus=meal_strategy_and_meal_absorption
- run_045: steps with invalid status [] / confidence ['basal_targets', 'automation_smb_uam', 'meal_bolus_strategy', 'synthesis_plan'] | meal_strategy_summary.confidence=medium-high
- run_046: steps with invalid status [] / confidence ['basal_targets', 'automation_smb_uam', 'synthesis_plan'] | verify without null component: ['aaps.core.sensitivity'] | profile_recommendation.focus=meal_bolus_strategy | profile_recommendation.decision=change but profile rows imply keep
- run_047: steps with invalid status [] / confidence ['basal_targets', 'automation_smb_uam', 'meal_bolus_strategy'] | profile_recommendation.focus=carb_ratio_daytime
- run_048: steps with wrong field set: ['safety_overview', 'basal_targets', 'profile_cr_isf_dia', 'automation_smb_uam', 'automation_sensitivity_limits', 'meal_bolus_strategy', 'meal_ecarbs_absorption', 'synthesis_plan'] | verify without null component: ['aaps.core.safety_limits'] | change without a distinct suggested_value: ['profile.basal.10_00']
- run_049: steps with invalid status [] / confidence ['basal_targets'] | decisions with wrong field set: ['profile.basal.00_00', 'profile.basal.05_00', 'profile.basal.06_00', 'profile.basal.10_00', 'profile.basal.16_00', 'profile.basal.18_00', 'profile.basal.19_00', 'profile.cr.00_00', 'profile.cr.04_00', 'profile.cr.08_00', 'profile.cr.16_00', 'profile.cr.20_00', 'profile.isf.00_00', 'profile.target.00_00', 'profile.target.08_00', 'profile.target.23_00', 'profile.dia', 'aaps.core.smb_uam', 'aaps.core.smb_activation', 'aaps.core.smb_delivery', 'aaps.core.safety_limits', 'aaps.core.sensitivity', 'aaps.core.carb_absorption'] | profile_recommendation.focus=basal_target_cr_isf_dia
- run_050: steps with invalid status [] / confidence ['basal_targets', 'automation_smb_uam'] | current_value not copied exactly: ['aaps.core.sensitivity'] | profile_recommendation.focus=basal and target at 00:00

## Experiment `real_llama4maverick_50` — model `meta-llama/llama-4-maverick`

- Runs: 50 (completed 50, failed 0)
- Final JSON extracted: 49/50 (methods: fenced ×44, brace_slice ×5, failed ×1)
- Fully schema-compliant: 41/49; mean schema score 0.990
- Mean wall time per run: 85s
- **App outcome (as the app behaves), over 50 completed runs:** accepted first time 19; accepted after the repair prompt 25; invalid JSON, no prompt offered 2; schema stop, no prompt offered 0; still rejected after repair 4
- **Accepted by the app but breaking Prompt 4's own rules:** 5/44 accepted runs; commonest: decisions_fields_exact ×4, steps_enums_valid ×1, meal_confidence_valid ×1
- **App loop:** first pass parseable 48/50, first pass compliant 19/50; correction prompt sent in 31 run(s); compliant after correction 41/50
- Sections the app would flag: parameter_decisions ×28, parameter_decisions.profile.basal.00_00.current_value ×4, parameter_decisions.profile.basal.05_00.current_value ×4, parameter_decisions.aaps.core.safety_limits.current_value ×2, profile_recommendation.focus ×2, profile_recommendation.decision ×2, parameter_decisions.profile.basal.06_00.current_value ×1, parameter_decisions.profile.basal.10_00.current_value ×1, parameter_decisions.profile.basal.16_00.current_value ×1, parameter_decisions.profile.basal.18_00.current_value ×1, parameter_decisions.profile.basal.19_00.current_value ×1, parameter_decisions.profile.cr.00_00.current_value ×1; first pass not valid JSON at all ×2
- Corrections that changed a decision (not just format): 24/25 comparable; changed profile focus: 1/25 (2 unparseable first pass(es) not comparable)
- Decisions per run — change: 1.0 ×31, 2.0 ×11, 0.0 ×1, 3.0 ×1; keep: 22.0 ×31, 21.0 ×11, 23.0 ×1, 20.0 ×1; verify: 0.0 ×44
- profile_recommendation focus: basal ×39, isf ×4, cr ×1
- profile_recommendation decision: change ×27, keep ×17; confidence: medium ×42, high ×1, low ×1
- Primary recommendation area: basal ×23, AAPS safety limits ×6, profile ×5, AAPS ×4, meal strategy ×3, Meal Logging ×1, meal logging ×1, Meal Strategy ×1; priority: medium ×23, high ×21
- Meal strategy confidence: low ×34, medium ×8, high ×1, low to medium ×1; exceptions: 1.0 ×30, 2.0 ×8, 0.0 ×6
- **Decision stability index** (mean per-parameter agreement): 0.953; parameters with unanimous decisions: 17/23
- Pairwise change-set Jaccard: mean 0.328; same primary area 24%; same profile focus 64%
- Pairwise text similarity — summary 0.289, profile recommendation 0.464, meal suggestion 0.410

### Parameter decision agreement

| parameter_key | current | modal | agreement | change | keep | verify | suggested values (when change) |
|---|---|---|---|---|---|---|---|
| profile.basal.00_00 | 0.6 U/h | change | 0.52 | 23 | 21 | 0 | 0.65 u/h x16 | 0.55 u/h x5 | 0.55 x2 |
| aaps.core.safety_limits | max_basal_u_per_hour=12 U/h; max_iob_units=25 U | change | 0.57 | 25 | 19 | 0 | max_basal_u_per_hour=12 u/h; max_iob_units=15 u x10 | max_basal_u_per_hour=12 u/h; max_iob_units=20 u x4 | {"max_iob_units": 15} x3 | {"max_basal_u_per_hour": 12, "max_iob_units": 15} x1 | max_iob_units=20 x1 | {"max_basal_u_per_hour": 6, "max_iob_units": 10} x1 | max_iob_units=20 u x1 | {"max_iob_units": 20} x1 | {"max_iob_units": 15, "max_basal_u_per_hour": 6} x1 | max_basal_u_per_hour=10 u/h; max_iob_units=25 u x1 | max_iob_units=15 u x1 |
| profile.isf.00_00 | 56 mg/dL/U | keep | 0.91 | 4 | 40 | 0 | 50 mg/dl/u x3 | 55 mg/dl/u x1 |
| profile.cr.00_00 | 13 g/U | keep | 0.95 | 2 | 42 | 0 | 12.5 g/u x2 |
| profile.basal.05_00 | 0.7 U/h | keep | 0.98 | 1 | 43 | 0 | 0.65 u/h x1 |
| profile.basal.16_00 | 0.5 U/h | keep | 0.98 | 1 | 43 | 0 | 0.6 u/h x1 |
| aaps.core.carb_absorption | min_5m_carbimpact=8 mg/dL/5 min; meal_max_absorption_hours=7 h | keep | 1.00 | 0 | 44 | 0 |  |
| aaps.core.sensitivity | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=70 % | keep | 1.00 | 0 | 44 | 0 |  |
| aaps.core.smb_activation | smb_always_enabled=true; smb_with_cob_enabled=false; smb_after_carbs_enabled=false; smb_with_temp_target_enabled=true; smb_with_high_temp_target_enabled=false | keep | 1.00 | 0 | 44 | 0 |  |
| aaps.core.smb_delivery | smb_interval_minutes=3 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=20 min | keep | 1.00 | 0 | 44 | 0 |  |
| aaps.core.smb_uam | smb_enabled=true; uam_enabled=true | keep | 1.00 | 0 | 44 | 0 |  |
| profile.basal.06_00 | 0.8 U/h | keep | 1.00 | 0 | 44 | 0 |  |
| profile.basal.10_00 | 0.7 U/h | keep | 1.00 | 0 | 44 | 0 |  |
| profile.basal.18_00 | 0.6 U/h | keep | 1.00 | 0 | 44 | 0 |  |
| profile.basal.19_00 | 0.7 U/h | keep | 1.00 | 0 | 44 | 0 |  |
| profile.cr.04_00 | 11.1 g/U | keep | 1.00 | 0 | 44 | 0 |  |
| profile.cr.08_00 | 13.2 g/U | keep | 1.00 | 0 | 44 | 0 |  |
| profile.cr.16_00 | 10.5 g/U | keep | 1.00 | 0 | 44 | 0 |  |
| profile.cr.20_00 | 12.6 g/U | keep | 1.00 | 0 | 44 | 0 |  |
| profile.dia | 10 h | keep | 1.00 | 0 | 44 | 0 |  |
| profile.target.00_00 | 90 mg/dL | keep | 1.00 | 0 | 44 | 0 |  |
| profile.target.08_00 | 100 mg/dL | keep | 1.00 | 0 | 44 | 0 |  |
| profile.target.23_00 | 90 mg/dL | keep | 1.00 | 0 | 44 | 0 |  |

### Analysis step status / confidence agreement

| step | modal status | agreement | modal confidence | agreement |
|---|---|---|---|---|
| data_quality | completed | 1.00 | high | 1.00 |
| safety_overview | completed | 1.00 | medium | 0.86 |
| basal_targets | completed | 0.98 | medium | 0.98 |
| profile_cr_isf_dia | completed | 0.95 | medium | 1.00 |
| automation_smb_uam | completed | 1.00 | medium | 0.50 |
| automation_sensitivity_limits | completed | 1.00 | medium | 0.91 |
| meal_bolus_strategy | completed | 0.98 | low | 0.82 |
| meal_ecarbs_absorption | completed | 0.98 | low | 0.84 |
| synthesis_plan | completed | 1.00 | medium | 0.95 |

### Per-run overview

| run | status | 1st pass JSON | 1st pass OK | repairs | final OK | score | change/keep/verify | profile focus | primary rec | time (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| run_001 | completed | fenced | False | 1 | True | 1.00 | 2/21/0 | basal | Verify basal rates | 141.12 |
| run_002 | completed | fenced | False | 1 | True | 1.00 | 2/21/0 | basal | Review basal profile | 135.81 |
| run_003 | completed | fenced | False | 1 | None | — | — | nan | nan | 165.23 |
| run_004 | completed | fenced | True | 0 | True | 1.00 | 1/22/0 | basal | Adjust basal profile | 66.09 |
| run_005 | completed | fenced | True | 0 | True | 1.00 | 1/22/0 | basal | Adjust max IOB | 72.49 |
| run_006 | completed | fenced | False | 1 | False | 0.76 | — | nan | nan | 88.94 |
| run_007 | completed | fenced | False | 1 | True | 1.00 | 2/21/0 | basal | Review basal rates and targets. | 95.75 |
| run_008 | completed | fenced | True | 0 | True | 1.00 | 1/22/0 | basal | Verify and adjust basal rates | 66.05 |
| run_009 | completed | fenced | False | 1 | True | 1.00 | 1/22/0 | basal | Review basal rates for potential adjustments | 90.61 |
| run_010 | completed | fenced | False | 1 | False | 0.97 | — | nan | nan | 90.36 |
| run_011 | completed | fenced | True | 0 | True | 1.00 | 2/21/0 | basal | Adjust basal rates | 63.89 |
| run_012 | completed | failed | False | 1 | True | 1.00 | — | nan | nan | 100.01 |
| run_013 | completed | fenced | True | 0 | True | 1.00 | 1/22/0 | basal | Start logging meals | 69.1 |
| run_014 | completed | fenced | False | 1 | False | 0.94 | 1/22/0 | basal | Start logging meal data. | 95.23 |
| run_015 | completed | fenced | False | 1 | False | 0.97 | 1/22/0 | basal | Adjust max IOB | 91.65 |
| run_016 | completed | fenced | True | 0 | True | 1.00 | 1/22/0 | basal | Verify basal rates | 63.32 |
| run_017 | completed | fenced | True | 0 | True | 1.00 | 1/22/0 | basal | Verify and adjust basal rates | 63.97 |
| run_018 | completed | fenced | False | 1 | True | 1.00 | 1/22/0 | basal | Start logging meal data | 85.13 |
| run_019 | completed | fenced | False | 1 | True | 1.00 | 1/22/0 | basal | Adjust basal rates | 89.4 |
| run_020 | completed | fenced | False | 1 | True | 1.00 | 1/22/0 | isf | Review and adjust ISF | 103.28 |
| run_021 | completed | fenced | False | 1 | False | 0.97 | 1/22/0 | isf | Reduce max IOB | 90.68 |
| run_022 | completed | fenced | True | 0 | True | 1.00 | 1/22/0 | cr | Start logging meal data | 68.51 |
| run_023 | completed | fenced | False | 1 | True | 1.00 | 1/22/0 | basal | Adjust max IOB to a safer limit | 85.66 |
| run_024 | completed | fenced | False | 1 | True | 1.00 | 1/22/0 | basal | Review basal rates for potential adjustments. | 91.26 |
| run_025 | completed | fenced | False | 1 | False | 0.94 | — | nan | nan | 78.69 |
| run_026 | completed | fenced | False | 1 | True | 1.00 | 1/22/0 | basal | Adjust max IOB to a safer limit | 87.87 |
| run_027 | completed | failed | False | 1 | True | 1.00 | — | nan | nan | 99.79 |
| run_028 | completed | fenced | False | 1 | True | 1.00 | 1/22/0 | basal | Review and adjust basal rates | 84.51 |
| run_029 | completed | fenced | True | 0 | True | 1.00 | 1/22/0 | basal | Adjust basal rate | 63.15 |
| run_030 | completed | fenced | True | 0 | True | 1.00 | 1/22/0 | basal | Review basal rates | 64.73 |
| run_031 | completed | fenced | False | 1 | True | 1.00 | 2/21/0 | basal | Adjust basal rates | 90.68 |
| run_032 | completed | fenced | True | 0 | True | 1.00 | 0/23/0 | basal | Verify basal rates | 63.77 |
| run_033 | completed | fenced | False | 1 | True | 1.00 | 1/22/0 | basal | Implement meal logging and bolusing | 82.29 |
| run_034 | completed | fenced | False | 1 | False | 0.97 | 2/21/0 | basal | Adjust basal rates | 90.37 |
| run_035 | completed | fenced | True | 0 | True | 1.00 | 1/22/0 | basal | Verify basal rates | 63.85 |
| run_036 | completed | fenced | False | 1 | True | 1.00 | 1/22/0 | basal | Adjust max IOB | 80.91 |
| run_037 | completed | fenced | False | 1 | True | 1.00 | 1/22/0 | basal | Adjust max IOB limit | 80.38 |
| run_038 | completed | fenced | True | 0 | True | 1.00 | 1/22/0 | basal | Review basal rates | 61.61 |
| run_039 | completed | fenced | True | 0 | True | 1.00 | 2/21/0 | basal | Review and adjust basal rates. | 66.03 |
| run_040 | completed | fenced | False | 1 | True | 1.00 | 2/21/0 | isf | Review ISF setting | 95.96 |
| run_041 | completed | fenced | True | 0 | True | 1.00 | 1/22/0 | basal | Implement a meal bolus strategy | 65.47 |
| run_042 | completed | fenced | False | 1 | True | 1.00 | 1/22/0 | basal | Adjust max IOB | 81.67 |
| run_043 | completed | fenced | True | 0 | True | 1.00 | 2/21/0 | basal | Adjust basal rates | 68.04 |
| run_044 | completed | fenced | True | 0 | True | 1.00 | 1/22/0 | basal | Review basal rates | 62.67 |
| run_045 | completed | fenced | False | 1 | False | 0.97 | 1/22/0 | basal | Adjust max IOB limit | 101.24 |
| run_046 | completed | fenced | False | 1 | True | 1.00 | 2/21/0 | isf | Review and adjust ISF settings. | 95.02 |
| run_047 | completed | fenced | True | 0 | True | 1.00 | 1/22/0 | basal | Review basal rates for potential adjustments. | 62.81 |
| run_048 | completed | fenced | False | 1 | True | 1.00 | 3/20/0 | basal | Adjust basal rates for better glucose control | 96.34 |
| run_049 | completed | fenced | True | 0 | True | 1.00 | 2/21/0 | basal | Adjust basal rates for better glucose control. | 70.57 |
| run_050 | completed | fenced | False | 1 | True | 1.00 | 1/22/0 | basal | Reduce max IOB | 93.85 |

### Schema violations remaining after correction

- run_006: top-level keys differ: missing=['education', 'implementation_steps', 'meal_strategy_summary', 'safety_notes'] extra=[] | parameter_decisions has 24 items, expected 23 | missing=[] extra=[None] | decision rows missing a required field (['parameter_key', 'decision', 'rationale']): [None] | decisions with wrong field set: ['profile.basal.00_00', 'profile.basal.05_00', 'profile.basal.06_00', 'profile.basal.10_00', 'profile.basal.16_00', 'profile.basal.18_00', 'profile.basal.19_00', 'profile.cr.00_00', 'profile.cr.04_00', 'profile.cr.08_00', 'profile.cr.16_00', 'profile.cr.20_00', 'profile.isf.00_00', 'profile.target.00_00', 'profile.target.08_00', 'profile.target.23_00', 'profile.dia', 'aaps.core.smb_uam', 'aaps.core.smb_activation', 'aaps.core.smb_delivery', 'aaps.core.safety_limits', 'aaps.core.sensitivity', 'aaps.core.carb_absorption', None] | meal_strategy_summary fields: [] | meal exceptions = None | meal_strategy_summary.confidence=None
- run_010: current_value not copied exactly: ['profile.basal.00_00', 'profile.basal.05_00', 'profile.basal.06_00', 'profile.basal.10_00', 'profile.basal.16_00', 'profile.basal.18_00', 'profile.basal.19_00', 'profile.cr.00_00', 'profile.cr.04_00', 'profile.cr.08_00', 'profile.cr.16_00', 'profile.cr.20_00', 'profile.isf.00_00', 'profile.target.00_00', 'profile.target.08_00', 'profile.target.23_00', 'profile.dia']
- run_014: steps with invalid status [] / confidence ['automation_smb_uam'] | meal_strategy_summary.confidence=low to medium
- run_015: decisions with wrong field set: ['profile.basal.00_00', 'profile.basal.05_00', 'profile.basal.06_00', 'profile.basal.10_00', 'profile.basal.16_00', 'profile.basal.18_00', 'profile.basal.19_00', 'profile.cr.00_00', 'profile.cr.04_00', 'profile.cr.08_00', 'profile.cr.16_00', 'profile.cr.20_00', 'profile.dia', 'profile.isf.00_00', 'profile.target.00_00', 'profile.target.08_00', 'profile.target.23_00', 'aaps.core.smb_uam', 'aaps.core.smb_activation', 'aaps.core.smb_delivery', 'aaps.core.safety_limits', 'aaps.core.sensitivity', 'aaps.core.carb_absorption']
- run_021: decisions with wrong field set: ['profile.basal.00_00', 'profile.basal.05_00', 'profile.basal.06_00', 'profile.basal.10_00', 'profile.basal.16_00', 'profile.basal.18_00', 'profile.basal.19_00', 'profile.cr.00_00', 'profile.cr.04_00', 'profile.cr.08_00', 'profile.cr.16_00', 'profile.cr.20_00', 'profile.dia', 'profile.isf.00_00', 'profile.target.00_00', 'profile.target.08_00', 'profile.target.23_00', 'aaps.core.carb_absorption', 'aaps.core.sensitivity', 'aaps.core.smb_activation', 'aaps.core.smb_delivery', 'aaps.core.smb_uam', 'aaps.core.safety_limits']
- run_025: profile_recommendation.focus=max_iob_units | profile_recommendation.decision=change but profile rows imply keep
- run_034: decisions with wrong field set: ['profile.basal.00_00', 'profile.basal.05_00', 'profile.basal.06_00', 'profile.basal.10_00', 'profile.basal.16_00', 'profile.basal.18_00', 'profile.basal.19_00', 'profile.cr.00_00', 'profile.cr.04_00', 'profile.cr.08_00', 'profile.cr.16_00', 'profile.cr.20_00', 'profile.dia', 'profile.isf.00_00', 'profile.target.00_00', 'profile.target.08_00', 'profile.target.23_00', 'aaps.core.smb_uam', 'aaps.core.smb_activation', 'aaps.core.smb_delivery', 'aaps.core.safety_limits', 'aaps.core.sensitivity', 'aaps.core.carb_absorption']
- run_045: decisions with wrong field set: ['profile.basal.00_00', 'profile.basal.05_00', 'profile.basal.06_00', 'profile.basal.10_00', 'profile.basal.16_00', 'profile.basal.18_00', 'profile.basal.19_00', 'profile.cr.00_00', 'profile.cr.04_00', 'profile.cr.08_00', 'profile.cr.16_00', 'profile.cr.20_00', 'profile.dia', 'profile.isf.00_00', 'profile.target.00_00', 'profile.target.08_00', 'profile.target.23_00', 'aaps.core.carb_absorption', 'aaps.core.sensitivity', 'aaps.core.smb_activation', 'aaps.core.smb_delivery', 'aaps.core.smb_uam', 'aaps.core.safety_limits']

## Experiment `real_opus5` — model `claude-opus-5`

- Runs: 20 (completed 20, failed 0)
- Final JSON extracted: 19/20 (methods: strict ×19, failed ×1)
- Fully schema-compliant: 14/19; mean schema score 0.992
- Mean wall time per run: 1025s
- Estimated API cost: $56.64 total, $2.83 per run (list prices; output includes thinking)
- **App outcome (as the app behaves), over 20 completed runs:** accepted first time 10; accepted after the repair prompt 1; invalid JSON, no prompt offered 9; schema stop, no prompt offered 0; still rejected after repair 0
- **Accepted by the app but breaking Prompt 4's own rules:** 5/11 accepted runs; commonest: meal_fields_exact ×4, recommendations_priority_valid ×1
- **App loop:** first pass parseable 11/20, first pass compliant 5/20; correction prompt sent in 15 run(s); compliant after correction 14/20
- Sections the app would flag: meal_strategy_summary ×5, analysis_steps ×1, education ×1, implementation_steps ×1, issues ×1, parameter_decisions ×1, profile_recommendation ×1, recommendations ×1, safety_notes ×1, strengths ×1, profile_recommendation.focus ×1, profile_recommendation.decision ×1; first pass not valid JSON at all ×9
- Corrections that changed a decision (not just format): 0/6 comparable; changed profile focus: 0/6 (9 unparseable first pass(es) not comparable)
- Decisions per run — change: 1.0 ×7, 2.0 ×3, 3.0 ×1; keep: 22.0 ×7, 21.0 ×3, 20.0 ×1; verify: 0.0 ×11
- profile_recommendation focus: basal ×8, dia ×2, isf ×1
- profile_recommendation decision: keep ×11; confidence: medium ×9, low ×2
- Primary recommendation area: smb ×8, safety_limits ×1, meal ×1, isf ×1; priority: safety ×9, high ×1
- Meal strategy confidence: low ×11; exceptions: 2.0 ×11
- **Decision stability index** (mean per-parameter agreement): 0.972; parameters with unanimous decisions: 20/23
- Pairwise change-set Jaccard: mean 0.345; same primary area 16%; same profile focus 17%
- Pairwise text similarity — summary 0.224, profile recommendation 0.216, meal suggestion 0.174

### Parameter decision agreement

| parameter_key | current | modal | agreement | change | keep | verify | suggested values (when change) |
|---|---|---|---|---|---|---|---|
| aaps.core.smb_delivery | smb_interval_minutes=3 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=20 min | keep | 0.64 | 4 | 7 | 0 | smb_interval_minutes=3 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=15 min x3 | smb_interval_minutes=5 to 8 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=20 min x1 |
| aaps.core.sensitivity | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=70 % | keep | 0.82 | 2 | 9 | 0 | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=55 to 60 % x1 | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=60 % x1 |
| aaps.core.safety_limits | max_basal_u_per_hour=12 U/h; max_iob_units=25 U | change | 0.91 | 10 | 1 | 0 | max_basal_u_per_hour=12 u/h; max_iob_units=8 u x3 | max_basal_u_per_hour=12 u/h; max_iob_units=7 u x1 | max_basal_u_per_hour=12 u/h; max_iob_units=8 to 10 u x1 | max_basal_u_per_hour=12 u/h; max_iob_units=6 to 8 u for review with the care team x1 | max_basal_u_per_hour=4 u/h; max_iob_units=8 u x1 | max_basal_u_per_hour=12 u/h unchanged; max_iob_units reduced from 25 u to a care-team-agreed ceiling clearly above routine operating iob and far below 25 u, for example in the region of 8 to 10 u if total daily dose is confirmed near 20 u per day x1 | max_basal_u_per_hour=5 u/h; max_iob_units=10 u x1 | max_basal_u_per_hour=12 u/h; max_iob_units in the region of 8 to 10 u, to be agreed with the care team x1 |
| aaps.core.carb_absorption | min_5m_carbimpact=8 mg/dL/5 min; meal_max_absorption_hours=7 h | keep | 1.00 | 0 | 11 | 0 |  |
| aaps.core.smb_activation | smb_always_enabled=true; smb_with_cob_enabled=false; smb_after_carbs_enabled=false; smb_with_temp_target_enabled=true; smb_with_high_temp_target_enabled=false | keep | 1.00 | 0 | 11 | 0 |  |
| aaps.core.smb_uam | smb_enabled=true; uam_enabled=true | keep | 1.00 | 0 | 11 | 0 |  |
| profile.basal.00_00 | 0.6 U/h | keep | 1.00 | 0 | 11 | 0 |  |
| profile.basal.05_00 | 0.7 U/h | keep | 1.00 | 0 | 11 | 0 |  |
| profile.basal.06_00 | 0.8 U/h | keep | 1.00 | 0 | 11 | 0 |  |
| profile.basal.10_00 | 0.7 U/h | keep | 1.00 | 0 | 11 | 0 |  |
| profile.basal.16_00 | 0.5 U/h | keep | 1.00 | 0 | 11 | 0 |  |
| profile.basal.18_00 | 0.6 U/h | keep | 1.00 | 0 | 11 | 0 |  |
| profile.basal.19_00 | 0.7 U/h | keep | 1.00 | 0 | 11 | 0 |  |
| profile.cr.00_00 | 13 g/U | keep | 1.00 | 0 | 11 | 0 |  |
| profile.cr.04_00 | 11.1 g/U | keep | 1.00 | 0 | 11 | 0 |  |
| profile.cr.08_00 | 13.2 g/U | keep | 1.00 | 0 | 11 | 0 |  |
| profile.cr.16_00 | 10.5 g/U | keep | 1.00 | 0 | 11 | 0 |  |
| profile.cr.20_00 | 12.6 g/U | keep | 1.00 | 0 | 11 | 0 |  |
| profile.dia | 10 h | keep | 1.00 | 0 | 11 | 0 |  |
| profile.isf.00_00 | 56 mg/dL/U | keep | 1.00 | 0 | 11 | 0 |  |
| profile.target.00_00 | 90 mg/dL | keep | 1.00 | 0 | 11 | 0 |  |
| profile.target.08_00 | 100 mg/dL | keep | 1.00 | 0 | 11 | 0 |  |
| profile.target.23_00 | 90 mg/dL | keep | 1.00 | 0 | 11 | 0 |  |

### Analysis step status / confidence agreement

| step | modal status | agreement | modal confidence | agreement |
|---|---|---|---|---|
| data_quality | completed | 1.00 | high | 1.00 |
| safety_overview | completed | 1.00 | high | 0.55 |
| basal_targets | partial | 1.00 | medium | 0.55 |
| profile_cr_isf_dia | partial | 1.00 | low | 1.00 |
| automation_smb_uam | completed | 1.00 | medium | 1.00 |
| automation_sensitivity_limits | completed | 0.82 | medium | 1.00 |
| meal_bolus_strategy | partial | 1.00 | low | 1.00 |
| meal_ecarbs_absorption | blocked | 1.00 | low | 1.00 |
| synthesis_plan | completed | 1.00 | medium | 1.00 |

### Per-run overview

| run | status | 1st pass JSON | 1st pass OK | repairs | final OK | score | change/keep/verify | profile focus | primary rec | time (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| run_001 | completed | failed | False | 1 | True | 1.00 | — | nan | nan | 1052.83 |
| run_002 | completed | strict | False | 1 | False | 0.97 | 1/22/0 | dia | Reduce the maximum insulin-on-board ceiling as the single first change | 1136.97 |
| run_003 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | basal | Primary: discuss reducing the unannounced-meal microbolus ceiling as the single first change | 831.17 |
| run_004 | completed | failed | False | 1 | True | 1.00 | — | nan | nan | 1036.08 |
| run_005 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | dia | Reduce the maximum insulin-on-board ceiling to a value that can actually act | 795.29 |
| run_006 | completed | failed | False | 1 | True | 1.00 | — | nan | nan | 1003.84 |
| run_007 | completed | failed | False | 1 | True | 1.00 | — | nan | nan | 1048.0 |
| run_008 | completed | failed | False | 1 | True | 1.00 | — | nan | nan | 1009.03 |
| run_009 | completed | strict | False | 1 | False | 0.97 | 3/20/0 | basal | Discuss lowering the maximum insulin-on-board limit toward observed usage | 1066.07 |
| run_010 | completed | failed | False | 1 | True | 1.00 | — | nan | nan | 1101.54 |
| run_011 | completed | raw_decode_prefix | False | 1 | True | 1.00 | — | nan | nan | 1196.14 |
| run_012 | completed | strict | False | 1 | True | 1.00 | 1/22/0 | basal | Begin logging one recurring daytime eating occasion before changing any insulin setting | 958.94 |
| run_013 | completed | failed | False | 1 | None | — | — | nan | nan | 1061.68 |
| run_014 | completed | failed | False | 1 | True | 1.00 | — | nan | nan | 1115.31 |
| run_015 | completed | strict | False | 1 | False | 0.97 | 2/21/0 | basal | Discuss tightening the maximum IOB ceiling as the single first change | 1181.05 |
| run_016 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | basal | Primary: discuss tightening the maximum insulin on board ceiling first, as a behaviourally neutral safety bound | 847.65 |
| run_017 | completed | strict | False | 1 | False | 0.97 | 1/22/0 | basal | Primary: discuss lowering the maximum IOB ceiling as a tail-risk guardrail | 1214.74 |
| run_018 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | basal | Reduce the UAM microbolus strength as the single first therapy-affecting step | 827.99 |
| run_019 | completed | strict | False | 1 | False | 0.97 | 2/21/0 | isf | Primary: discuss softening the dynamic ISF adjustment factor | 1010.18 |
| run_020 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | basal | Primary: reduce the maximum insulin-on-board guardrail toward the observed operating range | 998.96 |

### Schema violations remaining after correction

- run_002: meal_strategy_summary fields: ['confidence', 'confidence_note', 'exceptions', 'next_observation', 'rationale', 'suggestion']
- run_009: meal_strategy_summary fields: ['confidence', 'confidence_note', 'exceptions', 'next_observation', 'rationale', 'suggestion']
- run_015: meal_strategy_summary fields: ['confidence', 'confidence_note', 'exceptions', 'next_observation', 'rationale', 'suggestion']
- run_017: bad priority: ['Primary: discuss lowering the maximum IOB ceiling as a tail-risk guardrail', 'Begin logging one recurring eating occasion to unblock carb ratio and absorption assessment', 'Hold the UAM SMB cap reduction as a conditional third step only', 'Do not reduce the dynamic ISF adjustment factor at this stage', 'Discuss the safety multipliers with the care team as context, not as an immediate change']
- run_019: meal_strategy_summary fields: ['confidence', 'exceptions', 'exceptions_count', 'next_observation', 'rationale', 'suggestion']

## Experiment `real_sonnet5_20` — model `claude-sonnet-5`

- Runs: 20 (completed 20, failed 0)
- Final JSON extracted: 20/20 (methods: strict ×20)
- Fully schema-compliant: 18/20; mean schema score 0.994
- Mean wall time per run: 558s
- Estimated API cost: $20.44 total, $1.02 per run (list prices; output includes thinking)
- **App outcome (as the app behaves), over 20 completed runs:** accepted first time 18; accepted after the repair prompt 1; invalid JSON, no prompt offered 1; schema stop, no prompt offered 0; still rejected after repair 0
- **Accepted by the app but breaking Prompt 4's own rules:** 2/19 accepted runs; commonest: steps_enums_valid ×2, profile_rec_confidence_valid ×1, meal_confidence_valid ×1
- **App loop:** first pass parseable 19/20, first pass compliant 16/20; correction prompt sent in 4 run(s); compliant after correction 18/20
- Sections the app would flag: analysis_steps.meal_bolus_strategy.confidence ×2, analysis_steps.synthesis_plan.confidence ×2, analysis_steps.basal_targets.confidence ×1, parameter_decisions.aaps.core.sensitivity.current_value ×1, analysis_steps.profile_cr_isf_dia.confidence ×1, analysis_steps.automation_sensitivity_limits.confidence ×1, profile_recommendation.confidence ×1, meal_strategy_summary.confidence ×1; first pass not valid JSON at all ×1
- Corrections that changed a decision (not just format): 0/3 comparable; changed profile focus: 0/3 (1 unparseable first pass(es) not comparable)
- Decisions per run — change: 0.0 ×18, 1.0 ×1; keep: 23.0 ×18, 22.0 ×1; verify: 0.0 ×19
- profile_recommendation focus: basal ×13, target ×3, dia ×2, cr ×1
- profile_recommendation decision: keep ×18, change ×1; confidence: low ×13, medium ×5, low-medium ×1
- Primary recommendation area: meal ×6, safety ×3, basal ×2, dia ×2, target ×1, cr ×1, data ×1, data_quality ×1, safety_iob ×1, data_logging ×1; priority: high ×11, safety ×8
- Meal strategy confidence: low ×17, low-medium ×1, medium ×1; exceptions: 2.0 ×18, 1.0 ×1
- **Decision stability index** (mean per-parameter agreement): 0.998; parameters with unanimous decisions: 22/23
- Pairwise change-set Jaccard: mean 0.805; same primary area 11%; same profile focus 43%
- Pairwise text similarity — summary 0.058, profile recommendation 0.210, meal suggestion 0.054

### Parameter decision agreement

| parameter_key | current | modal | agreement | change | keep | verify | suggested values (when change) |
|---|---|---|---|---|---|---|---|
| profile.basal.16_00 | 0.5 U/h | keep | 0.95 | 1 | 18 | 0 | approximately 0.6 u/h (modest increase, verify stepwise) x1 |
| aaps.core.carb_absorption | min_5m_carbimpact=8 mg/dL/5 min; meal_max_absorption_hours=7 h | keep | 1.00 | 0 | 19 | 0 |  |
| aaps.core.safety_limits | max_basal_u_per_hour=12 U/h; max_iob_units=25 U | keep | 1.00 | 0 | 19 | 0 |  |
| aaps.core.sensitivity | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=70 % | keep | 1.00 | 0 | 19 | 0 |  |
| aaps.core.smb_activation | smb_always_enabled=true; smb_with_cob_enabled=false; smb_after_carbs_enabled=false; smb_with_temp_target_enabled=true; smb_with_high_temp_target_enabled=false | keep | 1.00 | 0 | 19 | 0 |  |
| aaps.core.smb_delivery | smb_interval_minutes=3 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=20 min | keep | 1.00 | 0 | 19 | 0 |  |
| aaps.core.smb_uam | smb_enabled=true; uam_enabled=true | keep | 1.00 | 0 | 19 | 0 |  |
| profile.basal.00_00 | 0.6 U/h | keep | 1.00 | 0 | 19 | 0 |  |
| profile.basal.05_00 | 0.7 U/h | keep | 1.00 | 0 | 19 | 0 |  |
| profile.basal.06_00 | 0.8 U/h | keep | 1.00 | 0 | 19 | 0 |  |
| profile.basal.10_00 | 0.7 U/h | keep | 1.00 | 0 | 19 | 0 |  |
| profile.basal.18_00 | 0.6 U/h | keep | 1.00 | 0 | 19 | 0 |  |
| profile.basal.19_00 | 0.7 U/h | keep | 1.00 | 0 | 19 | 0 |  |
| profile.cr.00_00 | 13 g/U | keep | 1.00 | 0 | 19 | 0 |  |
| profile.cr.04_00 | 11.1 g/U | keep | 1.00 | 0 | 19 | 0 |  |
| profile.cr.08_00 | 13.2 g/U | keep | 1.00 | 0 | 19 | 0 |  |
| profile.cr.16_00 | 10.5 g/U | keep | 1.00 | 0 | 19 | 0 |  |
| profile.cr.20_00 | 12.6 g/U | keep | 1.00 | 0 | 19 | 0 |  |
| profile.dia | 10 h | keep | 1.00 | 0 | 19 | 0 |  |
| profile.isf.00_00 | 56 mg/dL/U | keep | 1.00 | 0 | 19 | 0 |  |
| profile.target.00_00 | 90 mg/dL | keep | 1.00 | 0 | 19 | 0 |  |
| profile.target.08_00 | 100 mg/dL | keep | 1.00 | 0 | 19 | 0 |  |
| profile.target.23_00 | 90 mg/dL | keep | 1.00 | 0 | 19 | 0 |  |

### Analysis step status / confidence agreement

| step | modal status | agreement | modal confidence | agreement |
|---|---|---|---|---|
| data_quality | completed | 0.95 | medium | 0.53 |
| safety_overview | completed | 1.00 | medium | 0.68 |
| basal_targets | completed | 0.53 | medium | 0.84 |
| profile_cr_isf_dia | partial | 0.90 | low | 0.79 |
| automation_smb_uam | completed | 0.95 | medium | 1.00 |
| automation_sensitivity_limits | completed | 0.95 | medium | 0.84 |
| meal_bolus_strategy | partial | 0.95 | low | 0.84 |
| meal_ecarbs_absorption | blocked | 1.00 | low | 1.00 |
| synthesis_plan | completed | 1.00 | medium | 0.68 |

### Per-run overview

| run | status | 1st pass JSON | 1st pass OK | repairs | final OK | score | change/keep/verify | profile focus | primary rec | time (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| run_001 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Prioritize understanding recurrent overnight hypoglycemia before any other change | 568.06 |
| run_002 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | cr | Begin logging carbohydrate and e-carb entries | 544.16 |
| run_003 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Begin logging carbohydrate intake to resolve competing explanations | 481.71 |
| run_004 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Establish basic carbohydrate logging before further profile or automation changes | 509.89 |
| run_005 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Clarify the effective maximum basal ceiling before any basal change | 634.5 |
| run_006 | completed | failed | False | 1 | True | 1.00 | — | nan | nan | 503.59 |
| run_007 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Investigate the recurring correction-then-delayed-hypoglycemia pattern before any other change | 528.37 |
| run_008 | completed | strict | False | 1 | False | 0.97 | 0/23/0 | basal | Establish basic carbohydrate logging at recurring meal windows | 566.96 |
| run_009 | completed | strict | False | 1 | True | 1.00 | 0/23/0 | target | Review recurring hypoglycemia clusters and the correction-then-delayed-drop dosing pattern with a clinician before any other change | 696.64 |
| run_010 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | dia | Clinically verify DIA and correction-bolus tail behavior before any change | 534.31 |
| run_011 | completed | strict | False | 1 | False | 0.91 | 0/23/0 | dia | Review insulin action duration assumptions before any dosing parameter change | 682.36 |
| run_012 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Review recurring correction-driven rebound lows before any dosing-related change | 557.18 |
| run_013 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | basal | Review the 16:00 basal segment against the recurring afternoon peak | 550.07 |
| run_014 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Begin structured carbohydrate logging | 571.33 |
| run_015 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Begin logging carbohydrate entries for representative meals | 537.25 |
| run_016 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Review correction-dosing timing relative to insulin action time before any profile change | 489.19 |
| run_017 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Begin logging carbohydrate entries before changing any profile or automation setting | 616.56 |
| run_018 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Begin logging approximate meal timing and carbohydrate estimates in the two recurring rise windows | 539.59 |
| run_019 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Begin logging meal carbohydrate timing and amount | 547.33 |
| run_020 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Begin logging carbohydrate amounts and timestamps, focused on the recurring 10:00-17:00 local rise | 503.36 |

### Schema violations remaining after correction

- run_008: steps with invalid status [] / confidence ['basal_targets', 'meal_bolus_strategy', 'synthesis_plan']
- run_011: steps with invalid status [] / confidence ['profile_cr_isf_dia', 'automation_sensitivity_limits', 'meal_bolus_strategy', 'synthesis_plan'] | profile_recommendation.confidence=low-medium | meal_strategy_summary.confidence=low-medium
