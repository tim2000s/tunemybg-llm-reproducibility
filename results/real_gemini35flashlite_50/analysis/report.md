# TuneMyBG reproducibility report

## Experiment `real_gemini35flashlite_50` — model `gemini-3.5-flash-lite`

- Runs: 50 (completed 50, failed 0)
- Final JSON extracted: 49/50 (methods: strict ×48, brace_slice ×1, failed ×1)
- Fully schema-compliant: 41/49; mean schema score 0.994
- Mean wall time per run: 34s
- **App outcome (as the app behaves), over 50 completed runs:** accepted first time 38; accepted after the repair prompt 1; invalid JSON, no prompt offered 10; schema stop, no prompt offered 1; still rejected after repair 0
- **Accepted by the app but breaking Prompt 4's own rules:** 8/49 accepted runs; commonest: top_level_exact ×3, steps_enums_valid ×3, decisions_values_valid ×1, decisions_verify_rule ×1, meal_fields_exact ×1
- **App loop:** first pass parseable 40/50, first pass compliant 32/50; correction prompt sent in 18 run(s); compliant after correction 41/50
- Sections the app would flag: analysis_steps.basal_targets.confidence ×3, issues ×2, strengths ×2, analysis_steps.automation_sensitivity_limits.confidence ×2, analysis_steps.synthesis_plan.confidence ×2, parameter_decisions.aaps.core.carb_absorption ×1, analysis_steps.meal_ecarbs_absorption.confidence ×1, parameter_decisions ×1, profile_recommendation ×1; first pass not valid JSON at all ×10
- Corrections that changed a decision (not just format): 1/8 comparable; changed profile focus: 0/8 (10 unparseable first pass(es) not comparable)
- Decisions per run — change: 0.0 ×39, 1.0 ×6, 2.0 ×4; keep: 23.0 ×38, 22.0 ×7, 21.0 ×4; verify: 0.0 ×48, 1.0 ×1
- profile_recommendation focus: basal ×41, isf ×3, dia ×2, cr ×2, target ×1
- profile_recommendation decision: keep ×43, change ×6; confidence: medium ×46, high ×3
- Primary recommendation area: basal ×22, meal ×7, cr ×6, smb ×5, aaps ×5, meal_strategy ×1, profile ×1, target ×1, safety ×1; priority: high ×27, medium ×14, safety ×8
- Meal strategy confidence: medium ×47, low ×1, high ×1; exceptions: 2.0 ×21, 1.0 ×16, 0.0 ×12
- **Decision stability index** (mean per-parameter agreement): 0.987; parameters with unanimous decisions: 19/23
- Pairwise change-set Jaccard: mean 0.649; same primary area 24%; same profile focus 70%
- Pairwise text similarity — summary 0.138, profile recommendation 0.496, meal suggestion 0.142

### Parameter decision agreement

| parameter_key | current | modal | agreement | change | keep | verify | suggested values (when change) |
|---|---|---|---|---|---|---|---|
| aaps.core.safety_limits | max_basal_u_per_hour=12 U/h; max_iob_units=25 U | keep | 0.84 | 8 | 41 | 0 | max_basal_u_per_hour=12 u/h; max_iob_units=6 u x5 | max_basal_u_per_hour=12 u/h; max_iob_units=10 u x1 | max_basal_u_per_hour=12 u/h; max_iob_units=8 u x1 | max_basal_u_per_hour=12 u/h; max_iob_units=15 u x1 |
| profile.basal.00_00 | 0.6 U/h | keep | 0.90 | 5 | 44 | 0 | 0.5 u/h x5 |
| profile.isf.00_00 | 56 mg/dL/U | keep | 0.98 | 0 | 48 | 1 |  |
| profile.target.00_00 | 90 mg/dL | keep | 0.98 | 1 | 48 | 0 | 95 mg/dl x1 |
| aaps.core.carb_absorption | min_5m_carbimpact=8 mg/dL/5 min; meal_max_absorption_hours=7 h | keep | 1.00 | 0 | 49 | 0 |  |
| aaps.core.sensitivity | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=70 % | keep | 1.00 | 0 | 49 | 0 |  |
| aaps.core.smb_activation | smb_always_enabled=true; smb_with_cob_enabled=false; smb_after_carbs_enabled=false; smb_with_temp_target_enabled=true; smb_with_high_temp_target_enabled=false | keep | 1.00 | 0 | 49 | 0 |  |
| aaps.core.smb_delivery | smb_interval_minutes=3 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=20 min | keep | 1.00 | 0 | 49 | 0 |  |
| aaps.core.smb_uam | smb_enabled=true; uam_enabled=true | keep | 1.00 | 0 | 49 | 0 |  |
| profile.basal.05_00 | 0.7 U/h | keep | 1.00 | 0 | 49 | 0 |  |
| profile.basal.06_00 | 0.8 U/h | keep | 1.00 | 0 | 49 | 0 |  |
| profile.basal.10_00 | 0.7 U/h | keep | 1.00 | 0 | 49 | 0 |  |
| profile.basal.16_00 | 0.5 U/h | keep | 1.00 | 0 | 49 | 0 |  |
| profile.basal.18_00 | 0.6 U/h | keep | 1.00 | 0 | 49 | 0 |  |
| profile.basal.19_00 | 0.7 U/h | keep | 1.00 | 0 | 49 | 0 |  |
| profile.cr.00_00 | 13 g/U | keep | 1.00 | 0 | 49 | 0 |  |
| profile.cr.04_00 | 11.1 g/U | keep | 1.00 | 0 | 49 | 0 |  |
| profile.cr.08_00 | 13.2 g/U | keep | 1.00 | 0 | 49 | 0 |  |
| profile.cr.16_00 | 10.5 g/U | keep | 1.00 | 0 | 49 | 0 |  |
| profile.cr.20_00 | 12.6 g/U | keep | 1.00 | 0 | 49 | 0 |  |
| profile.dia | 10 h | keep | 1.00 | 0 | 49 | 0 |  |
| profile.target.08_00 | 100 mg/dL | keep | 1.00 | 0 | 49 | 0 |  |
| profile.target.23_00 | 90 mg/dL | keep | 1.00 | 0 | 49 | 0 |  |

### Analysis step status / confidence agreement

| step | modal status | agreement | modal confidence | agreement |
|---|---|---|---|---|
| data_quality | completed | 1.00 | high | 1.00 |
| safety_overview | completed | 1.00 | high | 1.00 |
| basal_targets | completed | 1.00 | medium | 0.94 |
| profile_cr_isf_dia | completed | 1.00 | medium | 1.00 |
| automation_smb_uam | completed | 1.00 | high | 0.96 |
| automation_sensitivity_limits | completed | 1.00 | high | 0.71 |
| meal_bolus_strategy | completed | 1.00 | medium | 0.98 |
| meal_ecarbs_absorption | completed | 1.00 | medium | 0.78 |
| synthesis_plan | completed | 1.00 | medium | 0.57 |

### Per-run overview

| run | status | 1st pass JSON | 1st pass OK | repairs | final OK | score | change/keep/verify | profile focus | primary rec | time (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| run_001 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Monitor Early Nocturnal Basal Delivery | 31.33 |
| run_002 | completed | failed | False | 1 | True | 1.00 | 2/21/0 | basal | Reduce Overnight Basal Rates | 44.25 |
| run_003 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | isf | Introduce Carbohydrate Logging | 28.78 |
| run_004 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Establish Consistent Meal Logging | 30.62 |
| run_005 | completed | failed | False | 1 | True | 1.00 | 0/23/0 | basal | Log Carbohydrate Intake for Closed-Loop Optimization | 41.41 |
| run_006 | completed | failed | False | 1 | False | 0.91 | 0/22/1 | basal | Verify Overnight Basal and ISF Settings | 37.09 |
| run_007 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Verify Overnight Basal Rates | 28.21 |
| run_008 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Review Max IOB Safety Limit | 28.94 |
| run_009 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Verify Overnight Basal Rates for Nocturnal Dips | 28.45 |
| run_010 | completed | strict | False | 1 | False | 0.97 | 0/23/0 | dia | Initiate Carbohydrate Logging | 44.23 |
| run_011 | completed | failed | False | 1 | True | 1.00 | 0/23/0 | dia | Introduce Manual Carbohydrate Logging | 41.58 |
| run_012 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Pilot Manual Carb Logging | 29.32 |
| run_013 | completed | strict | False | 1 | False | 0.97 | 0/23/0 | isf | Maintain Profile Baselines and Verify Meal Logging | 42.67 |
| run_014 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Begin Consistent Carbohydrate Logging | 29.75 |
| run_015 | completed | strict | False | 1 | False | 0.97 | 1/22/0 | target | Adjust Overnight Target | 45.07 |
| run_016 | completed | failed | False | 1 | True | 1.00 | 0/23/0 | basal | Review Overnight Basal and Target Segments | 36.89 |
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
| run_028 | completed | failed | False | 1 | True | 1.00 | 1/22/0 | basal | Reduce Maximum IOB Safety Limit | 43.79 |
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
| run_039 | completed | failed | False | 1 | True | 1.00 | 0/23/0 | basal | Verify Overnight Basal Stability | 39.71 |
| run_040 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | basal | Reduce Max IOB Limit for Safety | 29.83 |
| run_041 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | cr | Initiate Manual Carb Logging for Verification | 29.39 |
| run_042 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | cr | Begin Recording Manual Carbohydrate Entries | 26.15 |
| run_043 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Begin Recording Carbohydrate Entries | 28.29 |
| run_044 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Evaluate Carbohydrate Logging for Complex Meals | 32.23 |
| run_045 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Review Max IOB Safety Limit | 33.47 |
| run_046 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Verify Overnight Basal and Fasting Stability | 30.41 |
| run_047 | completed | failed | False | 1 | False | 0.97 | 0/23/0 | basal | Monitor Early Overnight Basal and Target | 42.84 |
| run_048 | completed | failed | False | 1 | True | 1.00 | 1/22/0 | basal | Reduce Max IOB Safety Limit | 38.76 |
| run_049 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | basal | Reduce Early-Night Basal Rate | 30.69 |
| run_050 | completed | strict | False | 1 | True | 1.00 | 0/23/0 | basal | Review Max IOB Safety Limit | 37.78 |

### Schema violations remaining after correction

- run_006: invalid decision value: ['profile.isf.00_00'] | verify without null component: ['profile.isf.00_00'] | meal_strategy_summary fields: ['confidence', 'exceptions', 'next_observation', 'rationale']
- run_010: top-level keys differ: missing=['issues', 'strengths'] extra=[]
- run_013: steps with invalid status [] / confidence ['basal_targets', 'automation_sensitivity_limits', 'synthesis_plan']
- run_015: decisions with wrong field set: ['aaps.core.carb_absorption']
- run_018: steps with invalid status [] / confidence ['basal_targets', 'automation_sensitivity_limits']
- run_023: top-level keys differ: missing=['issues', 'strengths'] extra=[]
- run_026: steps with invalid status [] / confidence ['meal_ecarbs_absorption']
- run_047: top-level keys differ: missing=['issues', 'strengths'] extra=[]
