# TuneMyBG reproducibility report

## Experiment `real_deepseek_v4pro_50` — model `deepseek/deepseek-v4-pro`

- Runs: 50 (completed 50, failed 0)
- Final JSON extracted: 50/50 (methods: strict ×50)
- Fully schema-compliant: 36/50; mean schema score 0.991
- Mean wall time per run: 360s
- **App outcome (as the app behaves), over 50 completed runs:** accepted first time 45; accepted after the repair prompt 3; invalid JSON, no prompt offered 0; schema stop, no prompt offered 2; still rejected after repair 0
- **Accepted by the app but breaking Prompt 4's own rules:** 14/50 accepted runs; commonest: steps_enums_valid ×11, top_level_exact ×1, profile_rec_confidence_valid ×1, decisions_fields_exact ×1, decisions_verify_rule ×1
- **App loop:** first pass parseable 50/50, first pass compliant 33/50; correction prompt sent in 17 run(s); compliant after correction 36/50
- Sections the app would flag: analysis_steps.profile_cr_isf_dia.confidence ×7, analysis_steps.automation_sensitivity_limits.confidence ×4, parameter_decisions.profile.cr.00_00 ×2, profile_recommendation.focus ×2, parameter_decisions.profile.basal.10_00 ×1, parameter_decisions.profile.basal.16_00 ×1, education ×1, eduction ×1, profile_recommendation.confidence ×1, analysis_steps.automation_smb_uam.confidence ×1, parameter_decisions.profile.basal.00_00.current_value ×1, parameter_decisions.profile.basal.05_00.current_value ×1
- Corrections that changed a decision (not just format): 0/17 comparable; changed profile focus: 2/17
- Decisions per run — change: 2 ×21, 1 ×17, 3 ×6, 0 ×2, 5 ×2, 4 ×1, 6 ×1; keep: 21 ×21, 22 ×17, 20 ×5, 23 ×2, 19 ×2, 18 ×2, 17 ×1; verify: 0 ×49, 1 ×1
- profile_recommendation focus: basal ×28, isf ×17, dia ×4, target ×1
- profile_recommendation decision: change ×39, keep ×11; confidence: medium ×39, high ×8, low ×2, medium-high ×1
- Primary recommendation area: basal ×18, isf ×16, aaps_safety_limits ×2, dia ×2, meal_strategy ×1, data_foundation ×1, aaps_safety ×1, aaps ×1, automation_sensitivity_limits ×1, uam_aggressiveness ×1, UAM SMB delivery ×1, automation_sensitivity ×1, meal ×1, target ×1, aaps_uam ×1; priority: high ×32, safety ×16, medium ×1
- Meal strategy confidence: low ×45, medium ×5; exceptions: 0 ×46, 2 ×4
- **Decision stability index** (mean per-parameter agreement): 0.915; parameters with unanimous decisions: 10/23
- Pairwise change-set Jaccard: mean 0.213; same primary area 22%; same profile focus 42%
- Pairwise text similarity — summary 0.066, profile recommendation 0.311, meal suggestion 0.083

### Parameter decision agreement

| parameter_key | current | modal | agreement | change | keep | verify | suggested values (when change) |
|---|---|---|---|---|---|---|---|
| aaps.core.safety_limits | max_basal_u_per_hour=12 U/h; max_iob_units=25 U | keep | 0.56 | 22 | 28 | 0 | max_basal_u_per_hour=12 u/h; max_iob_units=8 u x3 | max_basal_u_per_hour=12 u/h; max_iob_units=10 u x3 | max_basal_u_per_hour=12 u/h; max_iob_units=5 u x3 | max_basal_u_per_hour=3 u/h; max_iob_units=8 u x2 | max_basal_u_per_hour=4 u/h; max_iob_units=5 u x2 | max_basal_u_per_hour=4 u/h; max_iob_units=8 u x1 | max_basal_u_per_hour=2 u/h; max_iob_units=5 u x1 | max_basal_u_per_hour=12 u/h; max_iob_units=6 u x1 | max_basal_u_per_hour=12 u/h; max_iob_units=7 u x1 | max_basal_u_per_hour=3 u/h; max_iob_units=5 u x1 | max_basal_u_per_hour=2 u/h; max_iob_units=10 u x1 | max_basal_u_per_hour=12 u/h; max_iob_units=2.0 u x1 | max_basal_u_per_hour=12 u/h; max_iob_units=12 u x1 | max_basal_u_per_hour=4 u/h; max_iob_units=7 u x1 |
| profile.basal.00_00 | 0.6 U/h | keep | 0.56 | 22 | 28 | 0 | 0.5 u/h x20 | 0.55 u/h x2 |
| profile.isf.00_00 | 56 mg/dL/U | keep | 0.60 | 20 | 30 | 0 | 70 mg/dl/u x5 | 80 mg/dl/u x2 | 40 mg/dl/u x2 | 30 mg/dl/u x1 | 150 mg/dl/u x1 | 36 mg/dl/u x1 | 110 mg/dl/u x1 | 100 mg/dl/u x1 | 38 mg/dl/u x1 | 90 mg/dl/u x1 | 75 mg/dl/u x1 | 50 mg/dl/u x1 | 35 mg/dl/u x1 | 180 mg/dl/u x1 |
| aaps.core.sensitivity | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=70 % | keep | 0.82 | 9 | 41 | 0 | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=100 % x4 | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=50 % x2 | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=60 % x1 | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=85 % x1 | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=0 % x1 |
| profile.dia | 10 h | keep | 0.84 | 8 | 42 | 0 | 6 h x4 | 5 h x2 | 8 h x1 | 7 h x1 |
| aaps.core.smb_delivery | smb_interval_minutes=3 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=20 min | keep | 0.90 | 5 | 45 | 0 | smb_interval_minutes=3 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=10 min x2 | smb_interval_minutes=3 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=15 min x2 | smb_interval_minutes=10 min; max_smb_basal_minutes=10 min; max_uam_smb_basal_minutes=15 min x1 |
| aaps.core.carb_absorption | min_5m_carbimpact=8 mg/dL/5 min; meal_max_absorption_hours=7 h | keep | 0.92 | 3 | 46 | 1 | min_5m_carbimpact=5 mg/dl/5 min; meal_max_absorption_hours=7 h x2 | min_5m_carbimpact=3 mg/dl/5 min; meal_max_absorption_hours=5 h x1 |
| aaps.core.smb_activation | smb_always_enabled=true; smb_with_cob_enabled=false; smb_after_carbs_enabled=false; smb_with_temp_target_enabled=true; smb_with_high_temp_target_enabled=false | keep | 0.96 | 2 | 48 | 0 | smb_always_enabled=true; smb_with_cob_enabled=false; smb_after_carbs_enabled=false; smb_with_temp_target_enabled=false; smb_with_high_temp_target_enabled=false x1 | smb_always_enabled=false; smb_with_cob_enabled=false; smb_after_carbs_enabled=false; smb_with_temp_target_enabled=true; smb_with_high_temp_target_enabled=false x1 |
| profile.basal.19_00 | 0.7 U/h | keep | 0.96 | 2 | 48 | 0 | 0.6 u/h x2 |
| aaps.core.smb_uam | smb_enabled=true; uam_enabled=true | keep | 0.98 | 1 | 49 | 0 | smb_enabled=true; uam_enabled=false x1 |
| profile.basal.05_00 | 0.7 U/h | keep | 0.98 | 1 | 49 | 0 | 0.6 u/h x1 |
| profile.target.00_00 | 90 mg/dL | keep | 0.98 | 1 | 49 | 0 | 100 mg/dl x1 |
| profile.target.23_00 | 90 mg/dL | keep | 0.98 | 1 | 49 | 0 | 100 mg/dl x1 |
| profile.basal.06_00 | 0.8 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.10_00 | 0.7 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.16_00 | 0.5 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.18_00 | 0.6 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.00_00 | 13 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.04_00 | 11.1 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.08_00 | 13.2 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.16_00 | 10.5 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.20_00 | 12.6 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.target.08_00 | 100 mg/dL | keep | 1.00 | 0 | 50 | 0 |  |

### Analysis step status / confidence agreement

| step | modal status | agreement | modal confidence | agreement |
|---|---|---|---|---|
| data_quality | completed | 1.00 | high | 0.98 |
| safety_overview | completed | 0.98 | high | 0.88 |
| basal_targets | completed | 0.58 | medium | 0.96 |
| profile_cr_isf_dia | partial | 0.72 | low | 0.48 |
| automation_smb_uam | completed | 0.90 | medium | 0.56 |
| automation_sensitivity_limits | completed | 0.92 | medium | 0.46 |
| meal_bolus_strategy | blocked | 0.62 | low | 0.98 |
| meal_ecarbs_absorption | blocked | 0.68 | low | 0.94 |
| synthesis_plan | completed | 1.00 | medium | 0.54 |

### Per-run overview

| run | status | 1st pass JSON | 1st pass OK | repairs | final OK | score | change/keep/verify | profile focus | primary rec | time (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| run_001 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | isf | Begin carbohydrate entries for all meals | 339.41 |
| run_002 | completed | strict | False | 1 | True | 1.00 | 2/21/0 | basal | Reduce overnight basal rate | 459.95 |
| run_003 | completed | strict | False | 1 | False | 0.97 | 2/21/0 | basal | Reduce overnight basal (00:00–05:00) | 489.89 |
| run_004 | completed | strict | False | 1 | False | 0.97 | 3/20/0 | basal | Record all carbohydrate intake consistently | 401.71 |
| run_005 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | isf | Correct Insulin Sensitivity Factor (ISF) | 388.77 |
| run_006 | completed | strict | False | 1 | False | 0.97 | 1/22/0 | isf | Increase Insulin Sensitivity Factor (ISF) | 395.24 |
| run_007 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | basal | Reduce overnight basal rate (00:00–05:00) | 412.65 |
| run_008 | completed | strict | False | 1 | False | 0.94 | 1/22/0 | isf | Lower ISF to reduce hypoglycaemia risk | 433.42 |
| run_009 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Overnight basal verification | 287.55 |
| run_010 | completed | strict | False | 1 | True | 1.00 | 2/21/0 | basal | Reduce overnight basal rate 00:00–05:00 | 434.94 |
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
