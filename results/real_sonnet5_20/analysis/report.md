# TuneMyBG reproducibility report

## Experiment `real_sonnet5_20` — model `claude-sonnet-5`

- Runs: 20 (completed 20, failed 0)
- Final JSON extracted: 20/20 (methods: strict ×20)
- Fully schema-compliant: 18/20; mean schema score 0.994
- Mean wall time per run: 558s
- Estimated API cost: $20.44 total, $1.02 per run (list prices; output includes thinking)
- **App outcome (as the app behaves), over 20 completed runs:** accepted first time 18; accepted after the repair prompt 1; invalid JSON, no prompt offered 1; schema stop, no prompt offered 0; still rejected after repair 0
- **Accepted by the app but breaking Prompt 4's own rules:** 2/20 accepted runs; commonest: steps_enums_valid ×2, profile_rec_confidence_valid ×1, meal_confidence_valid ×1
- **App loop:** first pass parseable 19/20, first pass compliant 16/20; correction prompt sent in 4 run(s); compliant after correction 18/20
- Sections the app would flag: analysis_steps.meal_bolus_strategy.confidence ×2, analysis_steps.synthesis_plan.confidence ×2, analysis_steps.basal_targets.confidence ×1, parameter_decisions.aaps.core.sensitivity.current_value ×1, analysis_steps.profile_cr_isf_dia.confidence ×1, analysis_steps.automation_sensitivity_limits.confidence ×1, profile_recommendation.confidence ×1, meal_strategy_summary.confidence ×1; first pass not valid JSON at all ×1
- Corrections that changed a decision (not just format): 0/3 comparable; changed profile focus: 0/3 (1 unparseable first pass(es) not comparable)
- Decisions per run — change: 0 ×19, 1 ×1; keep: 23 ×19, 22 ×1; verify: 0 ×20
- profile_recommendation focus: basal ×14, target ×3, dia ×2, cr ×1
- profile_recommendation decision: keep ×19, change ×1; confidence: low ×14, medium ×5, low-medium ×1
- Primary recommendation area: meal ×6, safety ×3, data ×2, basal ×2, dia ×2, target ×1, cr ×1, data_quality ×1, safety_iob ×1, data_logging ×1; priority: high ×12, safety ×8
- Meal strategy confidence: low ×18, low-medium ×1, medium ×1; exceptions: 2 ×19, 1 ×1
- **Decision stability index** (mean per-parameter agreement): 0.998; parameters with unanimous decisions: 22/23
- Pairwise change-set Jaccard: mean 0.900; same primary area 11%; same profile focus 50%
- Pairwise text similarity — summary 0.067, profile recommendation 0.239, meal suggestion 0.059

### Parameter decision agreement

| parameter_key | current | modal | agreement | change | keep | verify | suggested values (when change) |
|---|---|---|---|---|---|---|---|
| profile.basal.16_00 | 0.5 U/h | keep | 0.95 | 1 | 19 | 0 | approximately 0.6 u/h (modest increase, verify stepwise) x1 |
| aaps.core.carb_absorption | min_5m_carbimpact=8 mg/dL/5 min; meal_max_absorption_hours=7 h | keep | 1.00 | 0 | 20 | 0 |  |
| aaps.core.safety_limits | max_basal_u_per_hour=12 U/h; max_iob_units=25 U | keep | 1.00 | 0 | 20 | 0 |  |
| aaps.core.sensitivity | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=70 % | keep | 1.00 | 0 | 20 | 0 |  |
| aaps.core.smb_activation | smb_always_enabled=true; smb_with_cob_enabled=false; smb_after_carbs_enabled=false; smb_with_temp_target_enabled=true; smb_with_high_temp_target_enabled=false | keep | 1.00 | 0 | 20 | 0 |  |
| aaps.core.smb_delivery | smb_interval_minutes=3 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=20 min | keep | 1.00 | 0 | 20 | 0 |  |
| aaps.core.smb_uam | smb_enabled=true; uam_enabled=true | keep | 1.00 | 0 | 20 | 0 |  |
| profile.basal.00_00 | 0.6 U/h | keep | 1.00 | 0 | 20 | 0 |  |
| profile.basal.05_00 | 0.7 U/h | keep | 1.00 | 0 | 20 | 0 |  |
| profile.basal.06_00 | 0.8 U/h | keep | 1.00 | 0 | 20 | 0 |  |
| profile.basal.10_00 | 0.7 U/h | keep | 1.00 | 0 | 20 | 0 |  |
| profile.basal.18_00 | 0.6 U/h | keep | 1.00 | 0 | 20 | 0 |  |
| profile.basal.19_00 | 0.7 U/h | keep | 1.00 | 0 | 20 | 0 |  |
| profile.cr.00_00 | 13 g/U | keep | 1.00 | 0 | 20 | 0 |  |
| profile.cr.04_00 | 11.1 g/U | keep | 1.00 | 0 | 20 | 0 |  |
| profile.cr.08_00 | 13.2 g/U | keep | 1.00 | 0 | 20 | 0 |  |
| profile.cr.16_00 | 10.5 g/U | keep | 1.00 | 0 | 20 | 0 |  |
| profile.cr.20_00 | 12.6 g/U | keep | 1.00 | 0 | 20 | 0 |  |
| profile.dia | 10 h | keep | 1.00 | 0 | 20 | 0 |  |
| profile.isf.00_00 | 56 mg/dL/U | keep | 1.00 | 0 | 20 | 0 |  |
| profile.target.00_00 | 90 mg/dL | keep | 1.00 | 0 | 20 | 0 |  |
| profile.target.08_00 | 100 mg/dL | keep | 1.00 | 0 | 20 | 0 |  |
| profile.target.23_00 | 90 mg/dL | keep | 1.00 | 0 | 20 | 0 |  |

### Analysis step status / confidence agreement

| step | modal status | agreement | modal confidence | agreement |
|---|---|---|---|---|
| data_quality | completed | 0.95 | medium | 0.50 |
| safety_overview | completed | 1.00 | medium | 0.65 |
| basal_targets | completed | 0.50 | medium | 0.85 |
| profile_cr_isf_dia | partial | 0.90 | low | 0.80 |
| automation_smb_uam | completed | 0.95 | medium | 1.00 |
| automation_sensitivity_limits | completed | 0.95 | medium | 0.85 |
| meal_bolus_strategy | partial | 0.90 | low | 0.85 |
| meal_ecarbs_absorption | blocked | 1.00 | low | 1.00 |
| synthesis_plan | completed | 1.00 | medium | 0.70 |

### Per-run overview

| run | status | 1st pass JSON | 1st pass OK | repairs | final OK | score | change/keep/verify | profile focus | primary rec | time (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| run_001 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Prioritize understanding recurrent overnight hypoglycemia before any other change | 568.06 |
| run_002 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | cr | Begin logging carbohydrate and e-carb entries | 544.16 |
| run_003 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Begin logging carbohydrate intake to resolve competing explanations | 481.71 |
| run_004 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Establish basic carbohydrate logging before further profile or automation changes | 509.89 |
| run_005 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Clarify the effective maximum basal ceiling before any basal change | 634.5 |
| run_006 | completed | failed | False | 1 | True | 1.00 | 0/23/0 | basal | Establish carbohydrate logging before further profile or automation changes | 503.59 |
| run_007 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Investigate the recurring correction-then-delayed-hypoglycemia pattern before any other change | 528.37 |
| run_008 | completed | strict | False | 1 | False | 0.97 | 0/23/0 | basal | Establish basic carbohydrate logging at recurring meal windows | 566.96 |
| run_009 | completed | strict | False | 1 | True | 1.00 | 0/23/0 | target | Review recurring hypoglycemia clusters and the correction-then-delayed-drop dosing pattern with a clinician before any other change | 696.64 |
| run_010 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | dia | Clinically verify DIA and correction-bolus tail behavior before any change | 534.31 |
| run_011 | completed | strict | False | 1 | False | 0.91 | 0/23/0 | dia | Review insulin action duration assumptions before any dosing parameter change | 682.36 |
| run_012 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Review recurring correction-driven rebound lows before any dosing-related change | 557.18 |
| run_013 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | basal | Review the 16:00 basal segment against the recurring afternoon peak | 550.07 |
| run_014 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Begin structured carbohydrate logging | 571.33 |
| run_015 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Begin logging carbohydrate entries for representative meals | 537.25 |
| run_016 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Review correction-dosing timing relative to insulin action time before any profile change | 489.19 |
| run_017 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Begin logging carbohydrate entries before changing any profile or automation setting | 616.56 |
| run_018 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Begin logging approximate meal timing and carbohydrate estimates in the two recurring rise windows | 539.59 |
| run_019 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Begin logging meal carbohydrate timing and amount | 547.33 |
| run_020 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Begin logging carbohydrate amounts and timestamps, focused on the recurring 10:00-17:00 local rise | 503.36 |

### Schema violations remaining after correction

- run_008: steps with invalid status [] / confidence ['basal_targets', 'meal_bolus_strategy', 'synthesis_plan']
- run_011: steps with invalid status [] / confidence ['profile_cr_isf_dia', 'automation_sensitivity_limits', 'meal_bolus_strategy', 'synthesis_plan'] | profile_recommendation.confidence=low-medium | meal_strategy_summary.confidence=low-medium
