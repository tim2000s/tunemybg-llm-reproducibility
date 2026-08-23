# TuneMyBG reproducibility report

## Experiment `smoke_repair` — model `mock`

- Runs: 8 (completed 8, failed 0)
- Final JSON extracted: 8/8 (methods: strict ×8)
- Fully schema-compliant: 8/8; mean schema score 1.000
- Mean wall time per run: 0s
- **App loop:** first pass parseable 8/8, first pass compliant 0/8; correction prompt sent in 8 run(s); compliant after correction 8/8
- Sections the app would flag: profile_recommendation.decision ×8
- Corrections that changed a decision (not just format): 0/8; changed profile focus: 0/8
- Decisions per run — change: 6 ×2, 5 ×2, 8 ×1, 3 ×1, 4 ×1, 9 ×1; keep: 16 ×2, 17 ×2, 14 ×1, 15 ×1, 19 ×1, 12 ×1; verify: 0 ×4, 1 ×4
- profile_recommendation focus: isf ×5, basal ×2, cr ×1
- profile_recommendation decision: change ×8; confidence: medium ×8
- Primary recommendation area: smb ×3, isf ×3, basal ×1, cr ×1; priority: medium ×8
- Meal strategy confidence: medium ×8; exceptions: 0 ×8
- **Decision stability index** (mean per-parameter agreement): 0.727; parameters with unanimous decisions: 2/22
- Pairwise change-set Jaccard: mean 0.180; same primary area 21%; same profile focus 39%
- Pairwise text similarity — summary 0.730, profile recommendation 1.000, meal suggestion 1.000

### Parameter decision agreement

| parameter_key | current | modal | agreement | change | keep | verify | suggested values (when change) |
|---|---|---|---|---|---|---|---|
| aaps.core.smb_uam | smb_enabled=true; uam_enabled=true | keep | 0.50 | 4 | 4 | 0 | smb_enabled=true; uam_enabled=true +10% x4 |
| profile.isf.12_00 | nan | change | 0.50 | 4 | 4 | 0 | 45 mg/dl/u +10% x4 |
| profile.target.00_00 | 90 mg/dL | change | 0.50 | 4 | 4 | 0 | 95-110 mg/dl +10% x4 |
| profile.target.06_00 | nan | change | 0.50 | 4 | 4 | 0 | 90-105 mg/dl +10% x4 |
| aaps.core.safety_limits | max_basal_u_per_hour=12 U/h; max_iob_units=25 U | keep | 0.62 | 3 | 5 | 0 | max_basal_u_per_hour=2.4 u/h; max_iob_units=8 u +10% x3 |
| aaps.core.sensitivity | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=70 % | keep | 0.62 | 1 | 5 | 2 | autosens_enabled=null; dynamic_sensitivity_enabled=null; autosens_raises_target=null; autosens_lowers_target=null; dynamic_isf_adjustment_factor_percent=100 % +10% x1 |
| profile.basal.18_00 | 0.6 U/h | keep | 0.62 | 3 | 5 | 0 | 1.05 u/h +10% x3 |
| profile.cr.12_00 | nan | keep | 0.62 | 3 | 5 | 0 | 11 g/u +10% x3 |
| profile.isf.18_00 | nan | change | 0.62 | 5 | 3 | 0 | 40 mg/dl/u +10% x5 |
| aaps.core.carb_absorption | min_5m_carbimpact=8 mg/dL/5 min; meal_max_absorption_hours=7 h | keep | 0.75 | 2 | 6 | 0 | min_5m_carbimpact=3 mg/dl/5 min; meal_max_absorption_hours=6 h +10% x2 |
| aaps.core.smb_activation | smb_always_enabled=true; smb_with_cob_enabled=false; smb_after_carbs_enabled=false; smb_with_temp_target_enabled=true; smb_with_high_temp_target_enabled=false | keep | 0.75 | 0 | 6 | 2 |  |
| profile.basal.12_00 | nan | keep | 0.75 | 2 | 6 | 0 | 0.9 u/h +10% x2 |
| profile.cr.00_00 | 13 g/U | keep | 0.75 | 2 | 6 | 0 | 12 g/u +10% x2 |
| profile.dia | 10 h | keep | 0.75 | 2 | 6 | 0 | 5.5 h +10% x2 |
| profile.isf.06_00 | nan | keep | 0.75 | 2 | 6 | 0 | 42 mg/dl/u +10% x2 |
| aaps.core.smb_delivery | smb_interval_minutes=3 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=20 min | keep | 0.88 | 1 | 7 | 0 | smb_interval_minutes=3 min; max_smb_basal_minutes=45 min; max_uam_smb_basal_minutes=30 min +10% x1 |
| profile.basal.06_00 | 0.8 U/h | keep | 0.88 | 1 | 7 | 0 | 0.95 u/h +10% x1 |
| profile.cr.06_00 | nan | keep | 0.88 | 1 | 7 | 0 | 10 g/u +10% x1 |
| profile.cr.18_00 | nan | keep | 0.88 | 1 | 7 | 0 | 9 g/u +10% x1 |
| profile.target.22_00 | nan | keep | 0.88 | 1 | 7 | 0 | 100-115 mg/dl +10% x1 |
| profile.basal.00_00 | 0.6 U/h | keep | 1.00 | 0 | 8 | 0 |  |
| profile.isf.00_00 | 56 mg/dL/U | keep | 1.00 | 0 | 8 | 0 |  |

### Analysis step status / confidence agreement

| step | modal status | agreement | modal confidence | agreement |
|---|---|---|---|---|
| data_quality | completed | 0.75 | medium | 0.50 |
| safety_overview | completed | 0.50 | high | 0.62 |
| basal_targets | completed | 0.62 | medium | 0.38 |
| profile_cr_isf_dia | partial | 0.62 | low | 0.50 |
| automation_smb_uam | partial | 0.50 | high | 0.75 |
| automation_sensitivity_limits | completed | 0.50 | low | 0.50 |
| meal_bolus_strategy | completed | 0.75 | low | 0.38 |
| meal_ecarbs_absorption | completed | 0.50 | medium | 0.38 |
| synthesis_plan | partial | 0.62 | low | 0.38 |

### Per-run overview

| run | status | 1st pass JSON | 1st pass OK | repairs | final OK | score | change/keep/verify | profile focus | primary rec | time (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| run_001 | completed | strict | False | 1 | True | 1.00 | 8/14/0 | isf | mock primary | 0.0 |
| run_002 | completed | strict | False | 1 | True | 1.00 | 6/16/0 | basal | mock primary | 0.0 |
| run_003 | completed | strict | False | 1 | True | 1.00 | 6/15/1 | isf | mock primary | 0.0 |
| run_004 | completed | strict | False | 1 | True | 1.00 | 3/19/0 | isf | mock primary | 0.0 |
| run_005 | completed | fenced | False | 1 | True | 1.00 | 5/17/0 | cr | mock primary | 0.0 |
| run_006 | completed | strict | False | 1 | True | 1.00 | 5/16/1 | basal | mock primary | 0.0 |
| run_007 | completed | fenced | False | 1 | True | 1.00 | 4/17/1 | isf | mock primary | 0.0 |
| run_008 | completed | fenced | False | 1 | True | 1.00 | 9/12/1 | isf | mock primary | 0.0 |
