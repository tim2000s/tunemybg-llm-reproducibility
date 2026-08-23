# TuneMyBG reproducibility report

## Experiment `real_llama4maverick_50` — model `meta-llama/llama-4-maverick`

- Runs: 50 (completed 50, failed 0)
- Final JSON extracted: 49/50 (methods: fenced ×44, brace_slice ×5, failed ×1)
- Fully schema-compliant: 41/49; mean schema score 0.990
- Mean wall time per run: 85s
- **App outcome (as the app behaves), over 50 completed runs:** accepted first time 19; accepted after the repair prompt 25; invalid JSON, no prompt offered 2; schema stop, no prompt offered 0; still rejected after repair 4
- **Accepted by the app but breaking Prompt 4's own rules:** 5/46 accepted runs; commonest: decisions_fields_exact ×4, steps_enums_valid ×1, meal_confidence_valid ×1
- **App loop:** first pass parseable 48/50, first pass compliant 19/50; correction prompt sent in 31 run(s); compliant after correction 41/50
- Sections the app would flag: parameter_decisions ×28, parameter_decisions.profile.basal.00_00.current_value ×4, parameter_decisions.profile.basal.05_00.current_value ×4, parameter_decisions.aaps.core.safety_limits.current_value ×2, profile_recommendation.focus ×2, profile_recommendation.decision ×2, parameter_decisions.profile.basal.06_00.current_value ×1, parameter_decisions.profile.basal.10_00.current_value ×1, parameter_decisions.profile.basal.16_00.current_value ×1, parameter_decisions.profile.basal.18_00.current_value ×1, parameter_decisions.profile.basal.19_00.current_value ×1, parameter_decisions.profile.cr.00_00.current_value ×1; first pass not valid JSON at all ×2
- Corrections that changed a decision (not just format): 27/28 comparable; changed profile focus: 2/28 (2 unparseable first pass(es) not comparable)
- Decisions per run — change: 1.0 ×35, 2.0 ×11, 4.0 ×1, 0.0 ×1, 3.0 ×1; keep: 22.0 ×35, 21.0 ×11, 19.0 ×1, 23.0 ×1, 20.0 ×1; verify: 0.0 ×49
- profile_recommendation focus: basal ×43, isf ×4, cr ×1, max_iob_units ×1
- profile_recommendation decision: change ×32, keep ×17; confidence: medium ×47, high ×1, low ×1
- Primary recommendation area: basal ×26, AAPS safety limits ×6, AAPS ×5, profile ×5, meal strategy ×3, Meal Logging ×1, meal logging ×1, Meal Strategy ×1; priority: medium ×25, high ×23
- Meal strategy confidence: low ×38, medium ×8, high ×1, low to medium ×1; exceptions: 1.0 ×34, 2.0 ×8, 0.0 ×6
- **Decision stability index** (mean per-parameter agreement): 0.952; parameters with unanimous decisions: 16/23
- Pairwise change-set Jaccard: mean 0.397; same primary area 31%; same profile focus 77%
- Pairwise text similarity — summary 0.338, profile recommendation 0.555, meal suggestion 0.464

### Parameter decision agreement

| parameter_key | current | modal | agreement | change | keep | verify | suggested values (when change) |
|---|---|---|---|---|---|---|---|
| aaps.core.safety_limits | max_basal_u_per_hour=12 U/h; max_iob_units=25 U | change | 0.55 | 27 | 22 | 0 | max_basal_u_per_hour=12 u/h; max_iob_units=15 u x11 | max_basal_u_per_hour=12 u/h; max_iob_units=20 u x5 | {"max_iob_units": 15} x3 | {"max_basal_u_per_hour": 12, "max_iob_units": 15} x1 | max_iob_units=20 x1 | {"max_basal_u_per_hour": 6, "max_iob_units": 10} x1 | max_iob_units=20 u x1 | {"max_iob_units": 20} x1 | {"max_iob_units": 15, "max_basal_u_per_hour": 6} x1 | max_basal_u_per_hour=10 u/h; max_iob_units=25 u x1 | max_iob_units=15 u x1 |
| profile.basal.00_00 | 0.6 U/h | change | 0.55 | 27 | 22 | 0 | 0.65 u/h x19 | 0.55 u/h x5 | 0.55 x3 |
| profile.isf.00_00 | 56 mg/dL/U | keep | 0.92 | 4 | 45 | 0 | 50 mg/dl/u x3 | 55 mg/dl/u x1 |
| profile.basal.16_00 | 0.5 U/h | keep | 0.96 | 2 | 47 | 0 | 0.55 u/h x1 | 0.6 u/h x1 |
| profile.cr.00_00 | 13 g/U | keep | 0.96 | 2 | 47 | 0 | 12.5 g/u x2 |
| profile.basal.05_00 | 0.7 U/h | keep | 0.98 | 1 | 48 | 0 | 0.65 u/h x1 |
| profile.basal.06_00 | 0.8 U/h | keep | 0.98 | 1 | 48 | 0 | 0.75 u/h x1 |
| aaps.core.carb_absorption | min_5m_carbimpact=8 mg/dL/5 min; meal_max_absorption_hours=7 h | keep | 1.00 | 0 | 49 | 0 |  |
| aaps.core.sensitivity | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=70 % | keep | 1.00 | 0 | 49 | 0 |  |
| aaps.core.smb_activation | smb_always_enabled=true; smb_with_cob_enabled=false; smb_after_carbs_enabled=false; smb_with_temp_target_enabled=true; smb_with_high_temp_target_enabled=false | keep | 1.00 | 0 | 49 | 0 |  |
| aaps.core.smb_delivery | smb_interval_minutes=3 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=20 min | keep | 1.00 | 0 | 49 | 0 |  |
| aaps.core.smb_uam | smb_enabled=true; uam_enabled=true | keep | 1.00 | 0 | 49 | 0 |  |
| profile.basal.10_00 | 0.7 U/h | keep | 1.00 | 0 | 49 | 0 |  |
| profile.basal.18_00 | 0.6 U/h | keep | 1.00 | 0 | 49 | 0 |  |
| profile.basal.19_00 | 0.7 U/h | keep | 1.00 | 0 | 49 | 0 |  |
| profile.cr.04_00 | 11.1 g/U | keep | 1.00 | 0 | 49 | 0 |  |
| profile.cr.08_00 | 13.2 g/U | keep | 1.00 | 0 | 49 | 0 |  |
| profile.cr.16_00 | 10.5 g/U | keep | 1.00 | 0 | 49 | 0 |  |
| profile.cr.20_00 | 12.6 g/U | keep | 1.00 | 0 | 49 | 0 |  |
| profile.dia | 10 h | keep | 1.00 | 0 | 49 | 0 |  |
| profile.target.00_00 | 90 mg/dL | keep | 1.00 | 0 | 49 | 0 |  |
| profile.target.08_00 | 100 mg/dL | keep | 1.00 | 0 | 49 | 0 |  |
| profile.target.23_00 | 90 mg/dL | keep | 1.00 | 0 | 49 | 0 |  |

### Analysis step status / confidence agreement

| step | modal status | agreement | modal confidence | agreement |
|---|---|---|---|---|
| data_quality | completed | 1.00 | high | 1.00 |
| safety_overview | completed | 1.00 | medium | 0.88 |
| basal_targets | completed | 0.98 | medium | 0.98 |
| profile_cr_isf_dia | completed | 0.96 | medium | 1.00 |
| automation_smb_uam | completed | 1.00 | medium | 0.49 |
| automation_sensitivity_limits | completed | 1.00 | medium | 0.92 |
| meal_bolus_strategy | completed | 0.98 | low | 0.84 |
| meal_ecarbs_absorption | completed | 0.98 | low | 0.86 |
| synthesis_plan | completed | 1.00 | medium | 0.96 |

### Per-run overview

| run | status | 1st pass JSON | 1st pass OK | repairs | final OK | score | change/keep/verify | profile focus | primary rec | time (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| run_001 | completed | fenced | False | 1 | True | 1.00 | 2/21/0 | basal | Verify basal rates | 141.12 |
| run_002 | completed | fenced | False | 1 | True | 1.00 | 2/21/0 | basal | Review basal profile | 135.81 |
| run_003 | completed | fenced | False | 1 | None | — | — | nan | nan | 165.23 |
| run_004 | completed | fenced | True | 0 | True | 1.00 | 1/22/0 | basal | Adjust basal profile | 66.09 |
| run_005 | completed | fenced | True | 0 | True | 1.00 | 1/22/0 | basal | Adjust max IOB | 72.49 |
| run_006 | completed | fenced | False | 1 | False | 0.76 | 1/22/0 | basal | Adjust basal rate profile for better overnight control | 88.94 |
| run_007 | completed | fenced | False | 1 | True | 1.00 | 2/21/0 | basal | Review basal rates and targets. | 95.75 |
| run_008 | completed | fenced | True | 0 | True | 1.00 | 1/22/0 | basal | Verify and adjust basal rates | 66.05 |
| run_009 | completed | fenced | False | 1 | True | 1.00 | 1/22/0 | basal | Review basal rates for potential adjustments | 90.61 |
| run_010 | completed | fenced | False | 1 | False | 0.97 | 1/22/0 | basal | Review and adjust basal rates based on fasting glucose patterns. | 90.36 |
| run_011 | completed | fenced | True | 0 | True | 1.00 | 2/21/0 | basal | Adjust basal rates | 63.89 |
| run_012 | completed | failed | False | 1 | True | 1.00 | 1/22/0 | basal | Adjust basal rates | 100.01 |
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
| run_025 | completed | fenced | False | 1 | False | 0.94 | 1/22/0 | max_iob_units | Adjust max IOB | 78.69 |
| run_026 | completed | fenced | False | 1 | True | 1.00 | 1/22/0 | basal | Adjust max IOB to a safer limit | 87.87 |
| run_027 | completed | failed | False | 1 | True | 1.00 | 4/19/0 | basal | nan | 99.79 |
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
