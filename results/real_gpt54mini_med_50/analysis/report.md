# TuneMyBG reproducibility report

## Experiment `real_gpt54mini_med_50` — model `gpt-5.4-mini`

- Runs: 50 (completed 50, failed 0)
- Final JSON extracted: 50/50 (methods: strict ×50)
- Fully schema-compliant: 23/50; mean schema score 0.979
- Mean wall time per run: 123s
- **App outcome (as the app behaves), over 50 completed runs:** accepted first time 48; accepted after the repair prompt 0; invalid JSON, no prompt offered 1; schema stop, no prompt offered 0; still rejected after repair 1
- **Accepted by the app but breaking Prompt 4's own rules:** 25/48 accepted runs; commonest: steps_enums_valid ×22, meal_confidence_valid ×5, profile_rec_confidence_valid ×3, meal_fields_exact ×2, profile_rec_fields_exact ×1
- **App loop:** first pass parseable 49/50, first pass compliant 23/50; correction prompt sent in 27 run(s); compliant after correction 23/50
- Sections the app would flag: analysis_steps.automation_smb_uam.confidence ×15, analysis_steps.profile_cr_isf_dia.confidence ×12, meal_strategy_summary.confidence ×5, analysis_steps.automation_sensitivity_limits.confidence ×5, analysis_steps.meal_bolus_strategy.confidence ×4, profile_recommendation.confidence ×3, analysis_steps.synthesis_plan.confidence ×2, meal_strategy_summary ×2, parameter_decisions.aaps.core.carb_absorption.current_value ×1, analysis_steps.safety_overview.confidence ×1, analysis_steps.basal_targets.confidence ×1, profile_recommendation ×1; first pass not valid JSON at all ×1
- Corrections that changed a decision (not just format): 0/26 comparable; changed profile focus: 0/26 (1 unparseable first pass(es) not comparable)
- Decisions per run — change: 0 ×48, 1 ×2; keep: 23 ×48, 22 ×2; verify: 0 ×50
- profile_recommendation focus: basal ×49, cr ×1
- profile_recommendation decision: keep ×48, change ×2; confidence: medium ×46, medium-low ×3, low ×1
- Primary recommendation area: basal ×34, profile ×13, basal_and_targets ×1, meal ×1, profile_and_data ×1; priority: high ×46, medium ×3, safety ×1
- Meal strategy confidence: low ×45, low-to-medium ×2, low-medium ×2, low_medium ×1; exceptions: 2 ×42, 0 ×5, 1 ×3
- **Decision stability index** (mean per-parameter agreement): 0.998; parameters with unanimous decisions: 22/23
- Pairwise change-set Jaccard: mean 0.922; same primary area 52%; same profile focus 96%
- Pairwise text similarity — summary 0.050, profile recommendation 0.582, meal suggestion 0.113

### Parameter decision agreement

| parameter_key | current | modal | agreement | change | keep | verify | suggested values (when change) |
|---|---|---|---|---|---|---|---|
| profile.basal.00_00 | 0.6 U/h | keep | 0.96 | 2 | 48 | 0 | 0.55 u/h x2 |
| aaps.core.carb_absorption | min_5m_carbimpact=8 mg/dL/5 min; meal_max_absorption_hours=7 h | keep | 1.00 | 0 | 50 | 0 |  |
| aaps.core.safety_limits | max_basal_u_per_hour=12 U/h; max_iob_units=25 U | keep | 1.00 | 0 | 50 | 0 |  |
| aaps.core.sensitivity | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=70 % | keep | 1.00 | 0 | 50 | 0 |  |
| aaps.core.smb_activation | smb_always_enabled=true; smb_with_cob_enabled=false; smb_after_carbs_enabled=false; smb_with_temp_target_enabled=true; smb_with_high_temp_target_enabled=false | keep | 1.00 | 0 | 50 | 0 |  |
| aaps.core.smb_delivery | smb_interval_minutes=3 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=20 min | keep | 1.00 | 0 | 50 | 0 |  |
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
| profile.target.00_00 | 90 mg/dL | keep | 1.00 | 0 | 50 | 0 |  |
| profile.target.08_00 | 100 mg/dL | keep | 1.00 | 0 | 50 | 0 |  |
| profile.target.23_00 | 90 mg/dL | keep | 1.00 | 0 | 50 | 0 |  |

### Analysis step status / confidence agreement

| step | modal status | agreement | modal confidence | agreement |
|---|---|---|---|---|
| data_quality | completed | 1.00 | high | 1.00 |
| safety_overview | completed | 1.00 | high | 0.94 |
| basal_targets | partial | 0.84 | medium | 0.98 |
| profile_cr_isf_dia | partial | 0.86 | low | 0.42 |
| automation_smb_uam | completed | 1.00 | medium | 0.44 |
| automation_sensitivity_limits | completed | 0.96 | medium | 0.86 |
| meal_bolus_strategy | partial | 0.68 | low | 0.92 |
| meal_ecarbs_absorption | partial | 0.34 | low | 1.00 |
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
| run_009 | completed | failed | False | 1 | False | 0.94 | 0/23/0 | basal | Hold profile steady and verify overnight basal first | 141.51 |
| run_010 | completed | strict | False | 1 | False | 0.94 | 0/23/0 | basal | Keep the current profile and verify fasting overnight behavior before any dependent edit | 133.16 |
| run_011 | completed | strict | False | 1 | False | 0.94 | 0/23/0 | basal | Keep the profile unchanged and separate the problem windows before considering any dependent edit | 155.06 |
| run_012 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the basal profile unchanged and verify the daytime rise with meal-logged observation | 118.95 |
| run_013 | completed | strict | False | 1 | False | 0.97 | 0/23/0 | basal | Keep the profile unchanged for now | 139.96 |
| run_014 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the profile unchanged and verify one quiet overnight block | 107.94 |
| run_015 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the basal profile unchanged and verify with one fasting-like window | 121.95 |
| run_016 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Log representative meals before changing bolus settings | 118.94 |
| run_017 | completed | strict | False | 1 | False | 0.97 | 0/23/0 | basal | Keep the current profile and verify one fasting-like window before any profile change | 130.35 |
| run_018 | completed | strict | False | 1 | False | 0.97 | 0/23/0 | basal | Keep the current profile unchanged and verify with one documented meal day first | 132.0 |
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
