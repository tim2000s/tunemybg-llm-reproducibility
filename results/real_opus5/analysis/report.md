# TuneMyBG reproducibility report

## Experiment `real_opus5` — model `claude-opus-5`

- Runs: 20 (completed 20, failed 0)
- Final JSON extracted: 19/20 (methods: strict ×19, failed ×1)
- Fully schema-compliant: 14/19; mean schema score 0.992
- Mean wall time per run: 1025s
- Estimated API cost: $56.64 total, $2.83 per run (list prices; output includes thinking)
- **App outcome (as the app behaves), over 20 completed runs:** accepted first time 10; accepted after the repair prompt 1; invalid JSON, no prompt offered 9; schema stop, no prompt offered 0; still rejected after repair 0
- **Accepted by the app but breaking Prompt 4's own rules:** 5/19 accepted runs; commonest: meal_fields_exact ×4, recommendations_priority_valid ×1
- **App loop:** first pass parseable 11/20, first pass compliant 5/20; correction prompt sent in 15 run(s); compliant after correction 14/20
- Sections the app would flag: meal_strategy_summary ×5, analysis_steps ×1, education ×1, implementation_steps ×1, issues ×1, parameter_decisions ×1, profile_recommendation ×1, recommendations ×1, safety_notes ×1, strengths ×1, profile_recommendation.focus ×1, profile_recommendation.decision ×1; first pass not valid JSON at all ×9
- Corrections that changed a decision (not just format): 1/7 comparable; changed profile focus: 1/7 (9 unparseable first pass(es) not comparable)
- Decisions per run — change: 1.0 ×11, 2.0 ×7, 3.0 ×1; keep: 22.0 ×11, 21.0 ×7, 20.0 ×1; verify: 0.0 ×19
- profile_recommendation focus: basal ×13, dia ×3, isf ×3
- profile_recommendation decision: keep ×19; confidence: medium ×15, low ×4
- Primary recommendation area: smb ×14, isf ×3, safety_limits ×1, meal ×1; priority: safety ×17, high ×1
- Meal strategy confidence: low ×19; exceptions: 2.0 ×19
- **Decision stability index** (mean per-parameter agreement): 0.970; parameters with unanimous decisions: 20/23
- Pairwise change-set Jaccard: mean 0.540; same primary area 55%; same profile focus 49%
- Pairwise text similarity — summary 0.182, profile recommendation 0.158, meal suggestion 0.029

### Parameter decision agreement

| parameter_key | current | modal | agreement | change | keep | verify | suggested values (when change) |
|---|---|---|---|---|---|---|---|
| aaps.core.sensitivity | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=70 % | keep | 0.68 | 6 | 13 | 0 | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=60 % x5 | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=55 to 60 % x1 |
| aaps.core.smb_delivery | smb_interval_minutes=3 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=20 min | keep | 0.74 | 5 | 14 | 0 | smb_interval_minutes=3 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=15 min x4 | smb_interval_minutes=5 to 8 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=20 min x1 |
| aaps.core.safety_limits | max_basal_u_per_hour=12 U/h; max_iob_units=25 U | change | 0.90 | 17 | 2 | 0 | max_basal_u_per_hour=12 u/h; max_iob_units=8 u x6 | max_basal_u_per_hour=12 u/h; max_iob_units=10 u x3 | max_basal_u_per_hour=12 u/h; max_iob_units=7 u x1 | max_basal_u_per_hour=12 u/h; max_iob_units=a reachable backstop with clear headroom above the observed peak of 5.94 u, for example 8-10 u, to be confirmed with the care team x1 | max_basal_u_per_hour=12 u/h; max_iob_units=8 to 10 u x1 | max_basal_u_per_hour=12 u/h; max_iob_units=6 to 8 u for review with the care team x1 | max_basal_u_per_hour=4 u/h; max_iob_units=8 u x1 | max_basal_u_per_hour=12 u/h unchanged; max_iob_units reduced from 25 u to a care-team-agreed ceiling clearly above routine operating iob and far below 25 u, for example in the region of 8 to 10 u if total daily dose is confirmed near 20 u per day x1 | max_basal_u_per_hour=5 u/h; max_iob_units=10 u x1 | max_basal_u_per_hour=12 u/h; max_iob_units in the region of 8 to 10 u, to be agreed with the care team x1 |
| aaps.core.carb_absorption | min_5m_carbimpact=8 mg/dL/5 min; meal_max_absorption_hours=7 h | keep | 1.00 | 0 | 19 | 0 |  |
| aaps.core.smb_activation | smb_always_enabled=true; smb_with_cob_enabled=false; smb_after_carbs_enabled=false; smb_with_temp_target_enabled=true; smb_with_high_temp_target_enabled=false | keep | 1.00 | 0 | 19 | 0 |  |
| aaps.core.smb_uam | smb_enabled=true; uam_enabled=true | keep | 1.00 | 0 | 19 | 0 |  |
| profile.basal.00_00 | 0.6 U/h | keep | 1.00 | 0 | 19 | 0 |  |
| profile.basal.05_00 | 0.7 U/h | keep | 1.00 | 0 | 19 | 0 |  |
| profile.basal.06_00 | 0.8 U/h | keep | 1.00 | 0 | 19 | 0 |  |
| profile.basal.10_00 | 0.7 U/h | keep | 1.00 | 0 | 19 | 0 |  |
| profile.basal.16_00 | 0.5 U/h | keep | 1.00 | 0 | 19 | 0 |  |
| profile.basal.18_00 | 0.6 U/h | keep | 1.00 | 0 | 19 | 0 |  |
| profile.basal.19_00 | 0.7 U/h | keep | 1.00 | 0 | 19 | 0 |  |
| profile.cr.00_00 | 13 g/U | keep | 1.00 | 0 | 19 | 0 |  |
| profile.cr.04_00 | 11.1 g/U | keep | 1.00 | 0 | 19 | 0 |  |
| profile.cr.08_00 | 13.2 g/U | keep | 1.00 | 0 | 19 | 0 |  |
| profile.cr.16_00 | 10.5 g/U | keep | 1.00 | 0 | 19 | 0 |  |
| profile.cr.20_00 | 12.6 g/U | keep | 1.00 | 0 | 19 | 0 |  |
| profile.dia | 10 h | keep | 1.00 | 0 | 19 | 0 |  |
| profile.isf.00_00 | 56 mg/dL/U | keep | 1.00 | 0 | 19 | 0 |  |
| profile.target.00_00 | 90 mg/dL | keep | 1.00 | 0 | 19 | 0 |  |
| profile.target.08_00 | 100 mg/dL | keep | 1.00 | 0 | 19 | 0 |  |
| profile.target.23_00 | 90 mg/dL | keep | 1.00 | 0 | 19 | 0 |  |

### Analysis step status / confidence agreement

| step | modal status | agreement | modal confidence | agreement |
|---|---|---|---|---|
| data_quality | completed | 1.00 | high | 1.00 |
| safety_overview | completed | 1.00 | high | 0.63 |
| basal_targets | partial | 1.00 | medium | 0.63 |
| profile_cr_isf_dia | partial | 1.00 | low | 0.90 |
| automation_smb_uam | completed | 0.95 | medium | 1.00 |
| automation_sensitivity_limits | completed | 0.79 | medium | 0.95 |
| meal_bolus_strategy | partial | 1.00 | low | 1.00 |
| meal_ecarbs_absorption | blocked | 0.95 | low | 1.00 |
| synthesis_plan | completed | 1.00 | medium | 1.00 |

### Per-run overview

| run | status | 1st pass JSON | 1st pass OK | repairs | final OK | score | change/keep/verify | profile focus | primary rec | time (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| run_001 | completed | failed | False | 1 | True | 1.00 | 1/22/0 | dia | Primary: review the max IOB ceiling as the first and only change this cycle | 1052.83 |
| run_002 | completed | strict | False | 1 | False | 0.97 | 1/22/0 | dia | Reduce the maximum insulin-on-board ceiling as the single first change | 1136.97 |
| run_003 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | basal | Primary: discuss reducing the unannounced-meal microbolus ceiling as the single first change | 831.17 |
| run_004 | completed | failed | False | 1 | True | 1.00 | 2/21/0 | isf | Discuss reducing max IOB as the first, independent step | 1036.08 |
| run_005 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | dia | Reduce the maximum insulin-on-board ceiling to a value that can actually act | 795.29 |
| run_006 | completed | failed | False | 1 | True | 1.00 | 1/22/0 | basal | Discuss tightening the maximum insulin on board ceiling as the single primary change | 1003.84 |
| run_007 | completed | failed | False | 1 | True | 1.00 | 2/21/0 | basal | Primary: reduce the dynamic ISF adjustment factor as the single first change | 1048.0 |
| run_008 | completed | failed | False | 1 | True | 1.00 | 2/21/0 | basal | Primary: discuss aligning the UAM microbolus basal-minutes cap with the non-UAM cap | 1009.03 |
| run_009 | completed | strict | False | 1 | False | 0.97 | 3/20/0 | basal | Discuss lowering the maximum insulin-on-board limit toward observed usage | 1066.07 |
| run_010 | completed | failed | False | 1 | True | 1.00 | 2/21/0 | basal | Primary: reduce max IOB from 25 U to a level proportionate to daily insulin | 1101.54 |
| run_011 | completed | raw_decode_prefix | False | 1 | True | 1.00 | 1/22/0 | basal | Reduce the maximum insulin on board ceiling as a single independent safety guardrail | 1196.14 |
| run_012 | completed | strict | False | 1 | True | 1.00 | 1/22/0 | basal | Begin logging one recurring daytime eating occasion before changing any insulin setting | 958.94 |
| run_013 | completed | failed | False | 1 | None | — | — | nan | nan | 1061.68 |
| run_014 | completed | failed | False | 1 | True | 1.00 | 1/22/0 | isf | Primary: discuss a conservative reduction of the dynamic ISF adjustment factor | 1115.31 |
| run_015 | completed | strict | False | 1 | False | 0.97 | 2/21/0 | basal | Discuss tightening the maximum IOB ceiling as the single first change | 1181.05 |
| run_016 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | basal | Primary: discuss tightening the maximum insulin on board ceiling first, as a behaviourally neutral safety bound | 847.65 |
| run_017 | completed | strict | False | 1 | False | 0.97 | 1/22/0 | basal | Primary: discuss lowering the maximum IOB ceiling as a tail-risk guardrail | 1214.74 |
| run_018 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | basal | Reduce the UAM microbolus strength as the single first therapy-affecting step | 827.99 |
| run_019 | completed | strict | False | 1 | False | 0.97 | 2/21/0 | isf | Primary: discuss softening the dynamic ISF adjustment factor | 1010.18 |
| run_020 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | basal | Primary: reduce the maximum insulin-on-board guardrail toward the observed operating range | 998.96 |

### Schema violations remaining after correction

- run_002: meal_strategy_summary fields: ['confidence', 'confidence_note', 'exceptions', 'next_observation', 'rationale', 'suggestion']
- run_009: meal_strategy_summary fields: ['confidence', 'confidence_note', 'exceptions', 'next_observation', 'rationale', 'suggestion']
- run_015: meal_strategy_summary fields: ['confidence', 'confidence_note', 'exceptions', 'next_observation', 'rationale', 'suggestion']
- run_017: bad priority: ['Primary: discuss lowering the maximum IOB ceiling as a tail-risk guardrail', 'Begin logging one recurring eating occasion to unblock carb ratio and absorption assessment', 'Hold the UAM SMB cap reduction as a conditional third step only', 'Do not reduce the dynamic ISF adjustment factor at this stage', 'Discuss the safety multipliers with the care team as context, not as an immediate change']
- run_019: meal_strategy_summary fields: ['confidence', 'exceptions', 'exceptions_count', 'next_observation', 'rationale', 'suggestion']
