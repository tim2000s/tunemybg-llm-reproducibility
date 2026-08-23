# TuneMyBG reproducibility report

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
- Decisions per run — change: 3 ×19, 4 ×13, 2 ×7, 1 ×5, 5 ×4, 6 ×2; keep: 20 ×19, 19 ×13, 21 ×7, 22 ×5, 18 ×4, 17 ×2; verify: 0 ×50
- profile_recommendation focus: target ×39, basal ×11
- profile_recommendation decision: change ×44, keep ×6; confidence: high ×49, medium ×1
- Primary recommendation area: smb ×22, target ×16, safety_limits ×5, basal ×3, aaps ×3, safety ×1; priority: safety ×49, high ×1
- Meal strategy confidence: medium ×39, high ×5, low ×5, medium-high ×1; exceptions: 1 ×27, 2 ×23
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
