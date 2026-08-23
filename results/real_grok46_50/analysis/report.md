# TuneMyBG reproducibility report

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
- Decisions per run — change: 0 ×40, 2 ×6, 1 ×4; keep: 23 ×40, 21 ×6, 22 ×4; verify: 0 ×50
- profile_recommendation focus: target ×33, basal ×17
- profile_recommendation decision: keep ×40, change ×10; confidence: medium ×50
- Primary recommendation area: target ×33, basal ×16, profile ×1; priority: safety ×41, high ×9
- Meal strategy confidence: low ×44, medium ×6; exceptions: 2 ×38, 1 ×7, 0 ×5
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
