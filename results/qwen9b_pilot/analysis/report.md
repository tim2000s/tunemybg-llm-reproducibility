# TuneMyBG reproducibility report

## Experiment `qwen9b_pilot` — model `qwen/qwen3.5-9b`

- Runs: 1 (completed 1, failed 0)
- Final JSON extracted: 1/1 (methods: strict ×1)
- Fully schema-compliant: 0/1; mean schema score 0.966
- Mean wall time per run: 4281s
- **App loop:** first pass parseable 1/1, first pass compliant 0/1; correction prompt sent in 0 run(s); compliant after correction 0/1
- Decisions per run — change: 2 ×1; keep: 19 ×1; verify: 1 ×1
- profile_recommendation focus: basal ×1
- profile_recommendation decision: change ×1; confidence: medium ×1
- Primary recommendation area: profile ×1; priority: high ×1
- Meal strategy confidence: medium ×1; exceptions: 2 ×1
- **Decision stability index** (mean per-parameter agreement): 1.000; parameters with unanimous decisions: 22/22

### Parameter decision agreement

| parameter_key | current | modal | agreement | change | keep | verify | suggested values (when change) |
|---|---|---|---|---|---|---|---|
| aaps.core.carb_absorption | min_5m_carbimpact=3 mg/dL/5 min; meal_max_absorption_hours=6 h | keep | 1.00 | 0 | 1 | 0 |  |
| aaps.core.safety_limits | max_basal_u_per_hour=2.4 U/h; max_iob_units=8 U | keep | 1.00 | 0 | 1 | 0 |  |
| aaps.core.sensitivity | autosens_enabled=null; dynamic_sensitivity_enabled=null; autosens_raises_target=null; autosens_lowers_target=null; dynamic_isf_adjustment_factor_percent=100 % | keep | 1.00 | 0 | 1 | 0 |  |
| aaps.core.smb_activation | smb_always_enabled=null; smb_with_cob_enabled=null; smb_after_carbs_enabled=null; smb_with_temp_target_enabled=null; smb_with_high_temp_target_enabled=null | verify | 1.00 | 0 | 0 | 1 |  |
| aaps.core.smb_delivery | smb_interval_minutes=3 min; max_smb_basal_minutes=45 min; max_uam_smb_basal_minutes=30 min | keep | 1.00 | 0 | 1 | 0 |  |
| aaps.core.smb_uam | smb_enabled=true; uam_enabled=true | keep | 1.00 | 0 | 1 | 0 |  |
| profile.basal.00_00 | 0.85 U/h | change | 1.00 | 1 | 0 | 0 | 0.78 u/h x1 |
| profile.basal.06_00 | 0.95 U/h | keep | 1.00 | 0 | 1 | 0 |  |
| profile.basal.12_00 | 0.9 U/h | keep | 1.00 | 0 | 1 | 0 |  |
| profile.basal.18_00 | 1.05 U/h | keep | 1.00 | 0 | 1 | 0 |  |
| profile.cr.00_00 | 12 g/U | keep | 1.00 | 0 | 1 | 0 |  |
| profile.cr.06_00 | 10 g/U | keep | 1.00 | 0 | 1 | 0 |  |
| profile.cr.12_00 | 11 g/U | keep | 1.00 | 0 | 1 | 0 |  |
| profile.cr.18_00 | 9 g/U | keep | 1.00 | 0 | 1 | 0 |  |
| profile.dia | 5.5 h | keep | 1.00 | 0 | 1 | 0 |  |
| profile.isf.00_00 | 48 mg/dL/U | change | 1.00 | 1 | 0 | 0 | 52 mg/dl/u x1 |
| profile.isf.06_00 | 42 mg/dL/U | keep | 1.00 | 0 | 1 | 0 |  |
| profile.isf.12_00 | 45 mg/dL/U | keep | 1.00 | 0 | 1 | 0 |  |
| profile.isf.18_00 | 40 mg/dL/U | keep | 1.00 | 0 | 1 | 0 |  |
| profile.target.00_00 | 95-110 mg/dL | keep | 1.00 | 0 | 1 | 0 |  |
| profile.target.06_00 | 90-105 mg/dL | keep | 1.00 | 0 | 1 | 0 |  |
| profile.target.22_00 | 100-115 mg/dL | keep | 1.00 | 0 | 1 | 0 |  |

### Analysis step status / confidence agreement

| step | modal status | agreement | modal confidence | agreement |
|---|---|---|---|---|
| data_quality | completed | 1.00 | high | 1.00 |
| safety_overview | completed | 1.00 | medium | 1.00 |
| basal_targets | completed | 1.00 | medium | 1.00 |
| profile_cr_isf_dia | completed | 1.00 | medium | 1.00 |
| automation_smb_uam | completed | 1.00 | high | 1.00 |
| automation_sensitivity_limits | completed | 1.00 | high | 1.00 |
| meal_bolus_strategy | completed | 1.00 | medium | 1.00 |
| meal_ecarbs_absorption | completed | 1.00 | medium | 1.00 |
| synthesis_plan | completed | 1.00 | high | 1.00 |

### Per-run overview

| run | status | 1st pass JSON | 1st pass OK | repairs | final OK | score | change/keep/verify | profile focus | primary rec | time (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| run_001 | completed | strict | False | 0 | False | 0.97 | 2/19/1 | basal | Review Basal Rate | 4281.2 |

### Schema violations remaining after correction

- run_001: decisions with wrong field set: ['profile.basal.00_00', 'profile.basal.06_00', 'profile.basal.12_00', 'profile.basal.18_00', 'profile.cr.00_00', 'profile.cr.06_00', 'profile.cr.12_00', 'profile.cr.18_00', 'profile.isf.00_00', 'profile.isf.06_00', 'profile.isf.12_00', 'profile.isf.18_00', 'profile.target.00_00', 'profile.target.06_00', 'profile.target.22_00', 'profile.dia', 'aaps.core.smb_uam', 'aaps.core.smb_activation', 'aaps.core.smb_delivery', 'aaps.core.safety_limits', 'aaps.core.sensitivity', 'aaps.core.carb_absorption']
