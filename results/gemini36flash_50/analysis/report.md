# TuneMyBG reproducibility report

## Experiment `gemini36flash_50` — model `gemini-3.6-flash`

- Runs: 50 (completed 50, failed 0)
- Final JSON extracted: 50/50 (methods: strict ×50)
- Fully schema-compliant: 49/50; mean schema score 0.999
- Mean wall time per run: 81s
- **App outcome (as the app behaves), over 50 completed runs:** accepted first time 50; accepted after the repair prompt 0; invalid JSON, no prompt offered 0; schema stop, no prompt offered 0; still rejected after repair 0
- **Accepted by the app but breaking Prompt 4's own rules:** 1/50 accepted runs; commonest: steps_enums_valid ×1
- **App loop:** first pass parseable 50/50, first pass compliant 49/50; correction prompt sent in 1 run(s); compliant after correction 49/50
- Sections the app would flag: analysis_steps.meal_ecarbs_absorption.confidence ×1
- Corrections that changed a decision (not just format): 0/1 comparable; changed profile focus: 0/1
- Decisions per run — change: 0 ×50; keep: 20 ×50; verify: 2 ×50
- profile_recommendation focus: basal ×40, cr ×10
- profile_recommendation decision: keep ×50; confidence: high ×50
- Primary recommendation area: meal_strategy ×21, meal_bolus ×7, smb ×5, profile ×4, basal ×4, meal_timing ×3, aaps ×3, cr ×2, meal ×1; priority: low ×41, medium ×9
- Meal strategy confidence: high ×50; exceptions: 1 ×29, 2 ×21
- **Decision stability index** (mean per-parameter agreement): 1.000; parameters with unanimous decisions: 22/22
- Pairwise change-set Jaccard: mean 1.000; same primary area 21%; same profile focus 67%
- Pairwise text similarity — summary 0.252, profile recommendation 0.574, meal suggestion 0.323

### Parameter decision agreement

| parameter_key | current | modal | agreement | change | keep | verify | suggested values (when change) |
|---|---|---|---|---|---|---|---|
| aaps.core.carb_absorption | min_5m_carbimpact=3 mg/dL/5 min; meal_max_absorption_hours=6 h | keep | 1.00 | 0 | 50 | 0 |  |
| aaps.core.safety_limits | max_basal_u_per_hour=2.4 U/h; max_iob_units=8 U | keep | 1.00 | 0 | 50 | 0 |  |
| aaps.core.sensitivity | autosens_enabled=null; dynamic_sensitivity_enabled=null; autosens_raises_target=null; autosens_lowers_target=null; dynamic_isf_adjustment_factor_percent=100 % | verify | 1.00 | 0 | 0 | 50 |  |
| aaps.core.smb_activation | smb_always_enabled=null; smb_with_cob_enabled=null; smb_after_carbs_enabled=null; smb_with_temp_target_enabled=null; smb_with_high_temp_target_enabled=null | verify | 1.00 | 0 | 0 | 50 |  |
| aaps.core.smb_delivery | smb_interval_minutes=3 min; max_smb_basal_minutes=45 min; max_uam_smb_basal_minutes=30 min | keep | 1.00 | 0 | 50 | 0 |  |
| aaps.core.smb_uam | smb_enabled=true; uam_enabled=true | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.00_00 | 0.85 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.06_00 | 0.95 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.12_00 | 0.9 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.basal.18_00 | 1.05 U/h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.00_00 | 12 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.06_00 | 10 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.12_00 | 11 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.cr.18_00 | 9 g/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.dia | 5.5 h | keep | 1.00 | 0 | 50 | 0 |  |
| profile.isf.00_00 | 48 mg/dL/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.isf.06_00 | 42 mg/dL/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.isf.12_00 | 45 mg/dL/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.isf.18_00 | 40 mg/dL/U | keep | 1.00 | 0 | 50 | 0 |  |
| profile.target.00_00 | 95-110 mg/dL | keep | 1.00 | 0 | 50 | 0 |  |
| profile.target.06_00 | 90-105 mg/dL | keep | 1.00 | 0 | 50 | 0 |  |
| profile.target.22_00 | 100-115 mg/dL | keep | 1.00 | 0 | 50 | 0 |  |

### Analysis step status / confidence agreement

| step | modal status | agreement | modal confidence | agreement |
|---|---|---|---|---|
| data_quality | completed | 1.00 | high | 1.00 |
| safety_overview | completed | 1.00 | high | 1.00 |
| basal_targets | completed | 1.00 | high | 0.96 |
| profile_cr_isf_dia | completed | 1.00 | high | 0.98 |
| automation_smb_uam | completed | 0.96 | high | 0.92 |
| automation_sensitivity_limits | completed | 0.94 | high | 0.86 |
| meal_bolus_strategy | completed | 1.00 | high | 1.00 |
| meal_ecarbs_absorption | completed | 1.00 | high | 0.98 |
| synthesis_plan | completed | 1.00 | high | 1.00 |

### Per-run overview

| run | status | 1st pass JSON | 1st pass OK | repairs | final OK | score | change/keep/verify | profile focus | primary rec | time (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| run_001 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Extend Prebolus Time for Weekday Breakfast | 71.68 |
| run_002 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | cr | Maintain Current Profile Parameters | 86.35 |
| run_003 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | cr | Optimize Prebolus Timing for Weekend Brunch | 91.75 |
| run_004 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Optimize prebolus timing for weekend brunch | 80.2 |
| run_005 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Optimize Weekday Breakfast Prebolus Timing | 81.53 |
| run_006 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Maintain Current Profile and Automation Settings | 79.54 |
| run_007 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Verify Unpopulated AAPS Settings Toggles | 87.04 |
| run_008 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | cr | Test Slightly Extended Prebolus for Weekend Brunch | 88.35 |
| run_009 | completed | strict | False | 1 | False | 0.97 | 0/20/2 | basal | Evaluate Weekend Brunch Prebolus and Bolus Split | 112.88 |
| run_010 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Maintain Current Profile & Settings | 76.24 |
| run_011 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Optimize Weekend Brunch Prebolus Timing | 90.28 |
| run_012 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Optimize Weekend Brunch Bolus Timing | 93.76 |
| run_013 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Verify Unpopulated AAPS Settings in Application UI | 87.01 |
| run_014 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | cr | Optimize Weekend Brunch Prebolus Timing | 87.41 |
| run_015 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Verify AAPS Activation Switches in UI | 76.53 |
| run_016 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Extend prebolus interval for weekend brunches | 79.67 |
| run_017 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Adjust Weekend Brunch Immediate Bolus Split and Pre-bolus Timing | 79.17 |
| run_018 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Refine Morning Prebolus Timing | 88.5 |
| run_019 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Optimize Prebolus Lead Time for Weekday Breakfast | 83.23 |
| run_020 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Verify AAPS Activation Toggles in User Interface | 83.41 |
| run_021 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | cr | Extend Prebolus Timing for Weekend Brunch | 87.07 |
| run_022 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | cr | Evaluate Prebolus Timing for Weekend Brunch | 82.29 |
| run_023 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | cr | Optimize Prebolus Timing for Weekend Brunch | 80.71 |
| run_024 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Optimize Prebolus Timing for Weekend Brunch | 89.37 |
| run_025 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Extend Prebolus Window for Weekend Brunch | 76.1 |
| run_026 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Optimize Weekend Brunch Prebolus Timing | 80.77 |
| run_027 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Optimize Prebolus Timing for Weekend Brunch | 79.63 |
| run_028 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Maintain Current Profile Parameters | 76.56 |
| run_029 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Maintain Current Basal, CR, ISF, Target, and DIA Parameters | 79.46 |
| run_030 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Maintain Current Profile and Automation Settings | 77.6 |
| run_031 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Maintain Current Profile Basal and Parameters | 66.96 |
| run_032 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | cr | Extend Prebolus Timing for Weekend Brunch | 82.71 |
| run_033 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Maintain Active Insulin Profile and Settings | 74.76 |
| run_034 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Extend Weekend Brunch Prebolus Lead Time | 81.58 |
| run_035 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Optimize Weekend Brunch Prebolus Timing | 84.51 |
| run_036 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Refine Weekend Brunch Prebolus and Meal Strategy | 70.47 |
| run_037 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Verify AAPS UI Toggle States | 79.48 |
| run_038 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Verify Unpopulated AAPS Settings in User Interface | 70.75 |
| run_039 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Extend Prebolus Timing for Weekend Brunch | 76.66 |
| run_040 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Optimize Weekend Brunch Prebolus Timing | 88.07 |
| run_041 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Verify Handset UI Feature Flags | 87.31 |
| run_042 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Extend prebolus duration for high-fat weekend brunches | 76.45 |
| run_043 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | cr | Extend Prebolus Timing for Weekend Brunch | 79.86 |
| run_044 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Test Slightly Extended Prebolus for Weekend Brunch | 72.64 |
| run_045 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Verify Unpopulated AAPS Settings in Application Preferences | 75.8 |
| run_046 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | cr | Maintain Current Profile Settings | 77.15 |
| run_047 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Verify UI Toggles in AAPS Preference Settings | 80.86 |
| run_048 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Extend Prebolus Timing for Weekend Brunch | 82.0 |
| run_049 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Maintain Current Profile Basal and Therapy Settings | 70.15 |
| run_050 | completed | strict | True | 0 | True | 1.00 | 0/20/2 | basal | Optimize Prebolus Timing for Weekend Brunch | 76.07 |

### Schema violations remaining after correction

- run_009: steps with invalid status [] / confidence ['meal_ecarbs_absorption']
