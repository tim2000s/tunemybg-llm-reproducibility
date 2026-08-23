# TuneMyBG reproducibility report

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
- Decisions per run — change: 3 ×36, 1 ×5, 4 ×5, 2 ×4; keep: 20 ×36, 22 ×5, 19 ×5, 21 ×4; verify: 0 ×50
- profile_recommendation focus: target ×46, basal ×4
- profile_recommendation decision: change ×45, keep ×5; confidence: high ×50
- Primary recommendation area: target ×17, automation ×9, safety_limits ×8, aaps.core.safety_limits ×6, aaps ×4, safety ×3, automation_safety ×1, automation_sensitivity_limits ×1, limits ×1; priority: safety ×45, high ×5
- Meal strategy confidence: high ×24, medium ×21, low ×5; exceptions: 0 ×50
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
