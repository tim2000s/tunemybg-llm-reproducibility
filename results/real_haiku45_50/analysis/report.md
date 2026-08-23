# TuneMyBG reproducibility report

## Experiment `real_haiku45_50` — model `claude-haiku-4-5`

- Runs: 50 (completed 50, failed 0)
- Final JSON extracted: 49/50 (methods: fenced ×49, failed ×1)
- Fully schema-compliant: 3/49; mean schema score 0.930
- Mean wall time per run: 737s
- Estimated API cost: $24.67 total, $0.49 per run (list prices; output includes thinking)
- **App outcome (as the app behaves), over 50 completed runs:** accepted first time 17; accepted after the repair prompt 3; invalid JSON, no prompt offered 2; schema stop, no prompt offered 1; still rejected after repair 27
- **Accepted by the app but breaking Prompt 4's own rules:** 17/20 accepted runs; commonest: steps_enums_valid ×9, decisions_verify_rule ×5, meal_confidence_valid ×4, steps_fields_exact ×4, profile_rec_confidence_valid ×3
- **App loop:** first pass parseable 48/50, first pass compliant 2/50; correction prompt sent in 44 run(s); compliant after correction 3/50
- Sections the app would flag: profile_recommendation.focus ×29, analysis_steps.basal_targets.confidence ×18, analysis_steps.automation_smb_uam.confidence ×12, analysis_steps.meal_bolus_strategy.confidence ×9, analysis_steps.automation_sensitivity_limits ×7, analysis_steps.meal_bolus_strategy ×7, analysis_steps.meal_ecarbs_absorption ×7, analysis_steps.synthesis_plan.confidence ×7, analysis_steps.automation_smb_uam ×6, analysis_steps.synthesis_plan ×6, parameter_decisions.aaps.core.sensitivity.current_value ×6, analysis_steps.meal_ecarbs_absorption.confidence ×6; first pass not valid JSON at all ×2
- Corrections that changed a decision (not just format): 1/42 comparable; changed profile focus: 19/42 (2 unparseable first pass(es) not comparable)
- Decisions per run — change: 1.0 ×19, 2.0 ×13, 0.0 ×11, 3.0 ×3, 5.0 ×2, 4.0 ×1; keep: 22.0 ×17, 21.0 ×15, 23.0 ×7, 20.0 ×6, 19.0 ×2, 18.0 ×2; verify: 0.0 ×37, 1.0 ×9, 2.0 ×3
- profile_recommendation focus: basal ×18, meal_bolus_and_carb_logging ×2, isf ×2, meal_bolus_strategy ×2, ISF ×1, overall_profile_sequencing ×1, basal, carb ratio, ISF, and DIA collectively ×1, carb logging, then isf verification ×1, carbohydrate_ratio_and_meal_strategy ×1, DIA (insulin duration) ×1, DIA shortening (safety priority), basal timing adjustment (safety priority), basal increase at 10:00 segment (medium priority, conditional on ISF verification) ×1, basal_and_targets_and_cr_and_isf_and_dia ×1, carb_ratio ×1, basal_and_meal_strategy_interaction ×1, meal_bolus_timing ×1, Basal, ISF, CR, and target settings. ISF inadequacy drives Dynamic ISF compensation and overcorrection lows; overnight basal excess drives hour 1 lows; afternoon CR looseness combined with GLP-1 absorption delay drives sustained highs. Overnight target too tight buffers low risk when ISF and basal adjusted. ×1, insulin_sensitivity_and_action_duration ×1, basal_and_isf ×1, meal_bolus_strategy_and_afternoon_basal ×1, basal_carb_ratios_isf_dia ×1, DIA and meal_max_absorption_hours (carb and insulin absorption model parameters) ×1, basal and max_iob ×1, DIA (Duration of Insulin Action) ×1, basal_cr_isf_target ×1, meal_strategy_and_meal_absorption ×1, carb_ratio_daytime ×1, basal_target_cr_isf_dia ×1, basal and target at 00:00 ×1
- profile_recommendation decision: change ×30, keep ×18; confidence: high ×25, medium ×19, medium-high ×4
- Primary recommendation area: basal ×13, meal_bolus_strategy ×7, meal_strategy ×5, profile ×3, safety ×2, meal_logging ×2, carb_logging ×2, ISF ×1, Data and meal strategy ×1, meal strategy ×1, Carbohydrate logging (highest-leverage behavior change) ×1, dia ×1, behavioral_and_logging ×1, Data Integrity – ISF Verification ×1, isf ×1, meal_carbs ×1, profile_isf ×1, meal_detection_threshold ×1, profile_dia ×1, data_and_meal_documentation ×1, automation ×1, carbohydrate_logging_and_meal_strategy ×1; priority: high ×26, safety ×23
- Meal strategy confidence: medium ×29, low ×7, high ×6, low-medium ×2, medium-high ×2, medium_high ×1, medium (reactive strategy confirmed high confidence; carb-free approach valid). Low confidence in meal timing/size (inferred from glucose only; no logs). Medium confidence in GLP-1 effect quantification (absorption timing evident from telemetry, but effect magnitude not measured). ×1, low-to-medium ×1; exceptions: 2.0 ×45, 1.0 ×4
- **Decision stability index** (mean per-parameter agreement): 0.926; parameters with unanimous decisions: 6/23
- Pairwise change-set Jaccard: mean 0.113; same primary area 10%; same profile focus 13%
- Pairwise text similarity — summary 0.054, profile recommendation 0.043, meal suggestion 0.040

### Parameter decision agreement

| parameter_key | current | modal | agreement | change | keep | verify | suggested values (when change) |
|---|---|---|---|---|---|---|---|
| aaps.core.carb_absorption | min_5m_carbimpact=8 mg/dL/5 min; meal_max_absorption_hours=7 h | keep | 0.76 | 7 | 37 | 5 | min_5m_carbimpact=12–15 mg/dl/5 min; meal_max_absorption_hours=7 h x1 | min_5m_carbimpact=5 mg/dl/5 min; meal_max_absorption_hours=7 h x1 | min_5m_carbimpact=8 mg/dl/5 min; meal_max_absorption_hours=8–9 h x1 | min_5m_carbimpact=6 mg/dl/5 min; meal_max_absorption_hours=7 h x1 | min_5m_carbimpact=8 mg/dl/5min; meal_max_absorption_hours=3-4 h x1 | min_5m_carbimpact=8 mg/dl/5 min; meal_max_absorption_hours=10 h x1 | min_5m_carbimpact=12 mg/dl/5 min; meal_max_absorption_hours=7 h x1 |
| profile.basal.10_00 | 0.7 U/h | keep | 0.76 | 12 | 37 | 0 | 0.8 u/h x5 | 0.85 u/h x3 | 0.85–0.95 u/h x1 | 0.8–0.85 u/h x1 | 0.9 u/h x1 | 0.7 u/h x1 |
| profile.basal.16_00 | 0.5 U/h | keep | 0.78 | 11 | 38 | 0 | 0.6 u/h x5 | 0.7 u/h x3 | 0.7–0.75 u/h x1 | 0.65 x1 | 0.8 u/h x1 |
| profile.isf.00_00 | 56 mg/dL/U | keep | 0.82 | 7 | 40 | 2 | 90 mg/dl/u x1 | 110 mg/dl/u x1 | 40 mg/dl/u (00:00–08:00); 28 mg/dl/u (08:00–23:00) x1 | 50 mg/dl/u x1 | 40 mg/dl/u x1 | 100 mg/dl/u x1 | 80-100 mg/dl/u x1 |
| aaps.core.sensitivity | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=70 % | keep | 0.86 | 3 | 42 | 4 | autosens_enabled=false; dynamic_sensitivity_enabled=true; autosens_raises_target=false; autosens_lowers_target=false; dynamic_isf_adjustment_factor_percent=50 % x2 | dynamic_isf_adjustment_factor_percent=85 x1 |
| profile.basal.00_00 | 0.6 U/h | keep | 0.86 | 7 | 42 | 0 | 0.5 u/h x6 | 0.55 u/h x1 |
| profile.dia | 10 h | keep | 0.86 | 6 | 42 | 1 | 5.5 h x2 | 6.0–7.0 h x1 | 8 h x1 | 5-6 h x1 | 7.5 x1 |
| aaps.core.safety_limits | max_basal_u_per_hour=12 U/h; max_iob_units=25 U | keep | 0.92 | 3 | 45 | 1 | max_basal_u_per_hour=12 u/h; max_iob_units=8 u x1 | max_basal_u_per_hour=12 u/h; max_iob_units=20 u x1 | max_basal_u_per_hour=12 u/h; max_iob_units=18 u x1 |
| aaps.core.smb_activation | smb_always_enabled=true; smb_with_cob_enabled=false; smb_after_carbs_enabled=false; smb_with_temp_target_enabled=true; smb_with_high_temp_target_enabled=false | keep | 0.92 | 2 | 45 | 2 | smb_with_cob_enabled should be true (after meal-bolus validation); others unchanged x1 | smb_always_enabled=true; smb_with_cob_enabled=false; smb_after_carbs_enabled=true; smb_with_temp_target_enabled=true; smb_with_high_temp_target_enabled=false x1 |
| profile.cr.08_00 | 13.2 g/U | keep | 0.96 | 2 | 47 | 0 | 11.5 g/u x1 | 12.5 g/u x1 |
| profile.target.00_00 | 90 mg/dL | keep | 0.96 | 2 | 47 | 0 | 100 mg/dl x1 | 95 mg/dl x1 |
| aaps.core.smb_delivery | smb_interval_minutes=3 min; max_smb_basal_minutes=15 min; max_uam_smb_basal_minutes=20 min | keep | 0.98 | 1 | 48 | 0 | smb_interval_minutes=3 min; max_smb_basal_minutes=10 min; max_uam_smb_basal_minutes=15 min x1 |
| profile.basal.06_00 | 0.8 U/h | keep | 0.98 | 1 | 48 | 0 | 0.80 u/h (add new segment at 08:00) or increase 06:00 segment from 0.8 to 0.92 u/h x1 |
| profile.basal.18_00 | 0.6 U/h | keep | 0.98 | 1 | 48 | 0 | 0.5 u/h x1 |
| profile.basal.19_00 | 0.7 U/h | keep | 0.98 | 1 | 48 | 0 | 0.6 u/h x1 |
| profile.cr.16_00 | 10.5 g/U | keep | 0.98 | 1 | 48 | 0 | 9.5 g/u x1 |
| profile.target.23_00 | 90 mg/dL | keep | 0.98 | 1 | 48 | 0 | 100 mg/dl x1 |
| aaps.core.smb_uam | smb_enabled=true; uam_enabled=true | keep | 1.00 | 0 | 49 | 0 |  |
| profile.basal.05_00 | 0.7 U/h | keep | 1.00 | 0 | 49 | 0 |  |
| profile.cr.00_00 | 13 g/U | keep | 1.00 | 0 | 49 | 0 |  |
| profile.cr.04_00 | 11.1 g/U | keep | 1.00 | 0 | 49 | 0 |  |
| profile.cr.20_00 | 12.6 g/U | keep | 1.00 | 0 | 49 | 0 |  |
| profile.target.08_00 | 100 mg/dL | keep | 1.00 | 0 | 49 | 0 |  |

### Analysis step status / confidence agreement

| step | modal status | agreement | modal confidence | agreement |
|---|---|---|---|---|
| data_quality | completed | 1.00 | high | 1.00 |
| safety_overview | completed | 1.00 | high | 0.98 |
| basal_targets | completed | 1.00 | medium | 0.35 |
| profile_cr_isf_dia | completed | 0.98 | medium | 0.84 |
| automation_smb_uam | completed | 1.00 | high | 0.67 |
| automation_sensitivity_limits | completed | 1.00 | high | 0.47 |
| meal_bolus_strategy | completed | 0.98 | medium | 0.54 |
| meal_ecarbs_absorption | completed | 0.98 | low | 0.33 |
| synthesis_plan | completed | 1.00 | medium | 0.49 |

### Per-run overview

| run | status | 1st pass JSON | 1st pass OK | repairs | final OK | score | change/keep/verify | profile focus | primary rec | time (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| run_001 | completed | failed | False | 1 | None | — | — | nan | nan | 929.57 |
| run_002 | completed | fenced | False | 1 | False | 0.91 | 2/21/0 | ISF | Correct ISF underestimation from 56 to 90 mg/dL/U | 632.36 |
| run_003 | completed | fenced | False | 1 | False | 0.82 | 1/20/2 | overall_profile_sequencing | Restart carb logging immediately for 3 complete days | 793.77 |
| run_004 | completed | fenced | False | 1 | False | 0.97 | 1/22/0 | basal, carb ratio, ISF, and DIA collectively | Reduce max_iob from 25 U to 6-8 U immediately | 909.28 |
| run_005 | completed | failed | False | 1 | False | 0.85 | 0/21/2 | carb logging, then isf verification | Enable carb logging (Nightscout treatment entries) immediately for all meals and snacks; log carb amount (grams) and meal time. Continue for minimum 7 days to establish baseline. | 905.72 |
| run_006 | completed | fenced | False | 1 | False | 0.97 | 1/22/0 | basal | Reduce basal 00:00 from 0.6 U/h to 0.55 U/h or 0.5 U/h to address hour 1 lows (18.5% TBR, nadir 42–55 mg/dL). | 703.18 |
| run_007 | completed | fenced | False | 1 | False | 0.91 | 2/21/0 | basal | Raise basal in 10:00–16:00 afternoon window to address persistent hyperglycemia. | 767.54 |
| run_008 | completed | fenced | False | 1 | False | 0.97 | 3/20/0 | basal | Implement meal carbohydrate logging | 838.02 |
| run_009 | completed | fenced | False | 1 | False | 0.97 | 2/20/1 | basal | Reduce overnight and evening basal segments to address recurrent hypoglycemia | 708.92 |
| run_010 | completed | fenced | False | 1 | False | 0.85 | 1/21/1 | carbohydrate_ratio_and_meal_strategy | PRIMARY: Implement carbohydrate entry logging | 825.12 |
| run_011 | completed | fenced | False | 1 | False | 0.91 | 1/22/0 | DIA (insulin duration) | Reduce DIA from 10 to 5-6 hours (PRIMARY RECOMMENDATION) | 900.18 |
| run_012 | completed | fenced | False | 1 | False | 0.97 | 1/22/0 | basal | Increase afternoon basal conservatively (16:00 segment 0.5→0.65 U/h; 10:00–13:00 segment 0.7→0.80 U/h) and monitor for 2–3 days. | 640.85 |
| run_013 | completed | fenced | False | 1 | False | 0.97 | 2/21/0 | basal | Increase basal rate 10:00–16:00 window to address midday elevation | 872.31 |
| run_014 | completed | fenced | False | 1 | False | 0.94 | 0/23/0 | meal_bolus_and_carb_logging | Initiate carbohydrate logging for all meals and snacks | 788.18 |
| run_015 | completed | fenced | False | 1 | False | 0.91 | 3/19/1 | DIA shortening (safety priority), basal timing adjustment (safety priority), basal increase at 10:00 segment (medium priority, conditional on ISF verification) | Verify pump-resident ISF setting and confirm insulin type | 776.69 |
| run_016 | completed | fenced | False | 1 | False | 0.97 | 1/22/0 | basal | Verify and increase basal in afternoon peak window (08:00–17:00 local) | 836.38 |
| run_017 | completed | fenced | False | 1 | False | 0.88 | 0/23/0 | basal_and_targets_and_cr_and_isf_and_dia | Begin logging meal carbohydrate amounts and timing (CRITICAL PRIMARY ACTION) | 786.27 |
| run_018 | completed | fenced | False | 1 | False | 0.97 | 2/21/0 | basal | Strengthen afternoon basal (10:00–15:59) and eliminate evening basal valley (16:00–17:59) to address concurrent hyperglycemia and hypoglycemia clustering. | 704.72 |
| run_019 | completed | fenced | False | 1 | False | 0.91 | 1/22/0 | basal | Increase basal rate 10:00–16:00 window from 0.7 to 0.8 U/h to address primary afternoon hyperglycemia driver | 606.77 |
| run_020 | completed | fenced | False | 1 | False | 0.94 | 0/23/0 | carb_ratio | Implement carb entry logging for 1–2 weeks | 694.21 |
| run_021 | completed | fenced | True | 0 | True | 1.00 | 2/21/0 | isf | Raise ISF from 56 to 110 mg/dL/U | 436.96 |
| run_022 | completed | fenced | False | 1 | False | 0.97 | 1/22/0 | basal_and_meal_strategy_interaction | Implement carb logging for 3–5 days to validate profile and meal patterns | 717.72 |
| run_023 | completed | fenced | False | 1 | False | 0.97 | 1/22/0 | basal | Establish consistent meal bolus strategy: prebolus 0–15 min, immediate bolus 20–30% of total. | 801.35 |
| run_024 | completed | fenced | False | 1 | False | 0.88 | 0/22/1 | meal_bolus_timing | Add modest prebolus to reduce UAM detection lag and afternoon highs | 739.63 |
| run_025 | completed | fenced | False | 1 | False | 0.94 | 1/22/0 | basal | Restore meal carbohydrate logging | 667.65 |
| run_026 | completed | fenced | False | 1 | False | 0.94 | 1/21/1 | basal | Implement carb logging immediately (prerequisite for all downstream optimizations) | 745.78 |
| run_027 | completed | fenced | False | 1 | False | 0.97 | 2/20/1 | basal | Increase midday basal 10:00–17:00 from 0.7 to 0.85 U/h; eliminate 16:00 step-down to 0.5 U/h | 944.08 |
| run_028 | completed | fenced | False | 1 | False | 0.97 | 5/18/0 | Basal, ISF, CR, and target settings. ISF inadequacy drives Dynamic ISF compensation and overcorrection lows; overnight basal excess drives hour 1 lows; afternoon CR looseness combined with GLP-1 absorption delay drives sustained highs. Overnight target too tight buffers low risk when ISF and basal adjusted. | Lower and segment profile ISF to match true insulin sensitivity | 710.84 |
| run_029 | completed | fenced | False | 1 | True | 1.00 | 1/22/0 | isf | Add explicit prebolus and at-meal bolus to replace SMB-only meal coverage | 792.93 |
| run_030 | completed | fenced | False | 1 | False | 0.97 | 4/19/0 | insulin_sensitivity_and_action_duration | Lower ISF baseline from 56 to 40 mg/dL/U | 686.03 |
| run_031 | completed | fenced | False | 0 | False | 0.97 | 1/22/0 | basal | Reduce early-morning basal 00:00 UTC from 0.6 U/h to 0.5 U/h | 426.54 |
| run_032 | completed | fenced | False | 1 | False | 0.91 | 5/18/0 | basal_and_isf | Verify and adjust overnight basal rate (00:00) down from 0.6 to 0.5 U/h or increase overnight target from 90 to 95–100 mg/dL | 764.49 |
| run_033 | completed | fenced | False | 0 | False | 0.68 | 2/21/0 | nan | Raise insulin sensitivity factor (ISF) from 56 to 80-100 mg/dL/U | 577.34 |
| run_034 | completed | fenced | True | 0 | True | 1.00 | 1/22/0 | basal | Increase basal from 0.5 U/h to 0.8 U/h at 16:00 local segment. | 461.91 |
| run_035 | completed | fenced | False | 1 | False | 0.91 | 2/21/0 | meal_bolus_strategy_and_afternoon_basal | Lower min_5m_carbimpact to accelerate early meal detection | 724.7 |
| run_036 | completed | fenced | False | 0 | False | 0.97 | 0/21/2 | basal | Adopt prebolus and meal logging to separate meal bolus from basal and SMB | 582.68 |
| run_037 | completed | fenced | False | 1 | False | 0.97 | 0/23/0 | basal_carb_ratios_isf_dia | Enable carbohydrate logging for 5-7 days to validate CR and unlock pre-bolus capability | 887.81 |
| run_038 | completed | fenced | False | 1 | False | 0.94 | 2/21/0 | DIA and meal_max_absorption_hours (carb and insulin absorption model parameters) | Reduce DIA from 10h to 5-6h | 800.37 |
| run_039 | completed | fenced | False | 1 | False | 0.91 | 2/21/0 | basal and max_iob | Reduce max IOB to limit afternoon IOB accumulation and evening overcorrection lows | 717.54 |
| run_040 | completed | fenced | False | 1 | False | 0.88 | 1/21/1 | DIA (Duration of Insulin Action) | Reduce DIA from 10h to 7.5h to eliminate nocturnal IOB carryover | 788.99 |
| run_041 | completed | fenced | False | 1 | False | 0.85 | 1/22/0 | meal_bolus_strategy | Enable post-meal SMB brake to reduce early-morning hypoglycemia | 725.07 |
| run_042 | completed | fenced | False | 1 | False | 0.94 | 1/22/0 | basal_cr_isf_target | Add one day of carbohydrate entries to resolve meal size and CR validation | 702.18 |
| run_043 | completed | fenced | False | 1 | False | 0.97 | 0/23/0 | meal_bolus_and_carb_logging | Implement carbohydrate logging for all meals; required to validate CR and meal-bolus strategy | 730.26 |
| run_044 | completed | fenced | False | 1 | False | 0.94 | 1/22/0 | meal_strategy_and_meal_absorption | Enable carb logging to unblock COB-gated automation and enable CR/ISF validation. | 744.07 |
| run_045 | completed | fenced | False | 1 | False | 0.94 | 0/23/0 | basal | Obtain 3–5 day meal diary with carbohydrate amounts, timing, and macronutrient composition. | 907.66 |
| run_046 | completed | fenced | False | 1 | False | 0.88 | 0/22/1 | meal_bolus_strategy | Add prebolus delivery to reduce meal-insulin delay and postprandial hyperglycemia | 681.6 |
| run_047 | completed | fenced | False | 1 | False | 0.94 | 3/20/0 | carb_ratio_daytime | Reduce UAM sensitivity threshold to prevent false meal detection and excessive SMB | 747.28 |
| run_048 | completed | fenced | False | 0 | False | 0.91 | 2/20/1 | basal | Log all meals with estimated carbs; this is the primary change enabling all downstream improvements | 462.67 |
| run_049 | completed | fenced | False | 1 | False | 0.91 | 0/23/0 | basal_target_cr_isf_dia | Implement carbohydrate entry for every meal (primary, highest-priority action) | 787.1 |
| run_050 | completed | fenced | False | 1 | False | 0.91 | 2/21/0 | basal and target at 00:00 | Lower basal at 00:00 or raise target at 00:00 to address early-morning hypoglycemia (primary safety issue) | 742.92 |

### Schema violations remaining after correction

- run_002: steps with wrong field set: ['data_quality', 'safety_overview', 'basal_targets', 'profile_cr_isf_dia', 'automation_smb_uam', 'automation_sensitivity_limits', 'meal_bolus_strategy', 'meal_ecarbs_absorption', 'synthesis_plan'] | steps with invalid status [] / confidence ['basal_targets', 'synthesis_plan'] | profile_recommendation.focus=ISF
- run_003: steps with invalid status [] / confidence ['basal_targets', 'automation_smb_uam', 'synthesis_plan'] | current_value not copied exactly: ['aaps.core.sensitivity'] | invalid decision value: ['profile.isf.00_00', 'profile.dia'] | verify without null component: ['profile.isf.00_00', 'profile.dia'] | profile_recommendation.focus=overall_profile_sequencing | profile_recommendation.decision=keep but profile rows imply change
- run_004: profile_recommendation.focus=basal, carb ratio, ISF, and DIA collectively
- run_005: steps with wrong field set: ['basal_targets', 'profile_cr_isf_dia', 'automation_smb_uam', 'automation_sensitivity_limits', 'meal_bolus_strategy', 'meal_ecarbs_absorption', 'synthesis_plan'] | steps with invalid status [] / confidence ['basal_targets', 'synthesis_plan'] | current_value not copied exactly: ['aaps.core.smb_activation'] | verify without null component: ['aaps.core.smb_activation', 'aaps.core.carb_absorption'] | profile_recommendation.focus=carb logging, then isf verification
- run_006: steps with invalid status [] / confidence ['basal_targets', 'profile_cr_isf_dia', 'meal_ecarbs_absorption']
- run_007: steps with invalid status [] / confidence ['profile_cr_isf_dia', 'automation_smb_uam', 'meal_bolus_strategy', 'synthesis_plan'] | profile_recommendation.confidence=medium-high | meal_strategy_summary.confidence=low-medium
- run_008: steps with invalid status [] / confidence ['basal_targets', 'automation_sensitivity_limits']
- run_009: verify without null component: ['aaps.core.sensitivity']
- run_010: steps with wrong field set: ['basal_targets', 'profile_cr_isf_dia', 'automation_smb_uam', 'automation_sensitivity_limits', 'meal_bolus_strategy', 'meal_ecarbs_absorption', 'synthesis_plan'] | steps with invalid status [] / confidence ['basal_targets', 'automation_smb_uam', 'meal_bolus_strategy'] | verify without null component: ['aaps.core.carb_absorption'] | profile_recommendation.focus=carbohydrate_ratio_and_meal_strategy | meal_strategy_summary.confidence=medium_high
- run_011: steps with wrong field set: ['automation_sensitivity_limits'] | steps with invalid status [] / confidence ['meal_ecarbs_absorption'] | profile_recommendation.focus=DIA (insulin duration)
- run_012: steps with wrong field set: ['meal_bolus_strategy']
- run_013: steps with wrong field set: ['automation_smb_uam', 'automation_sensitivity_limits', 'meal_bolus_strategy', 'meal_ecarbs_absorption']
- run_014: steps with invalid status [] / confidence ['basal_targets', 'automation_sensitivity_limits', 'meal_ecarbs_absorption'] | profile_recommendation.focus=meal_bolus_and_carb_logging
- run_015: invalid decision value: ['profile.isf.00_00'] | verify without null component: ['profile.isf.00_00'] | profile_recommendation.focus=DIA shortening (safety priority), basal timing adjustment (safety priority), basal increase at 10:00 segment (medium priority, conditional on ISF verification)
- run_016: meal_strategy_summary.confidence=medium-high
- run_017: analysis_steps keys ['data_quality', 'safety_overview', 'basal_targets', 'profile_cr_isf_dia', 'automation_smb_uam', 'automation_sensitivity_limits', 'synthesis_plan'] != workflow ['data_quality', 'safety_overview', 'basal_targets', 'profile_cr_isf_dia', 'automation_smb_uam', 'automation_sensitivity_limits', 'meal_bolus_strategy', 'meal_ecarbs_absorption', 'synthesis_plan'] | steps with invalid status [] / confidence ['profile_cr_isf_dia'] | current_value not copied exactly: ['aaps.core.sensitivity'] | profile_recommendation.focus=basal_and_targets_and_cr_and_isf_and_dia
- run_018: steps with wrong field set: ['basal_targets', 'profile_cr_isf_dia', 'automation_smb_uam', 'automation_sensitivity_limits', 'meal_bolus_strategy', 'meal_ecarbs_absorption', 'synthesis_plan']
- run_019: steps with invalid status [] / confidence ['basal_targets', 'automation_smb_uam', 'automation_sensitivity_limits', 'meal_bolus_strategy'] | profile_recommendation.confidence=medium-high | meal_strategy_summary.confidence=low-medium
- run_020: steps with invalid status [] / confidence ['automation_smb_uam'] | profile_recommendation.focus=carb_ratio
- run_022: profile_recommendation.focus=basal_and_meal_strategy_interaction
- run_023: steps with invalid status [] / confidence ['basal_targets', 'automation_smb_uam', 'automation_sensitivity_limits']
- run_024: steps with invalid status [] / confidence ['basal_targets'] | current_value not copied exactly: ['aaps.core.sensitivity'] | verify without null component: ['aaps.core.sensitivity'] | profile_recommendation.focus=meal_bolus_timing
- run_025: steps with invalid status [] / confidence ['basal_targets', 'meal_bolus_strategy', 'synthesis_plan'] | profile_recommendation.confidence=medium-high
- run_026: steps with invalid status [] / confidence ['safety_overview', 'profile_cr_isf_dia'] | verify without null component: ['aaps.core.smb_activation']
- run_027: verify without null component: ['aaps.core.carb_absorption']
- run_028: profile_recommendation.focus=Basal, ISF, CR, and target settings. ISF inadequacy drives Dynamic ISF compensation and overcorrection lows; overnight basal excess drives hour 1 lows; afternoon CR looseness combined with GLP-1 absorption delay drives sustained highs. Overnight target too tight buffers low risk when ISF and basal adjusted.
- run_030: profile_recommendation.focus=insulin_sensitivity_and_action_duration
- run_031: steps with invalid status [] / confidence ['profile_cr_isf_dia', 'meal_ecarbs_absorption', 'synthesis_plan']
- run_032: steps with invalid status [] / confidence ['basal_targets', 'automation_sensitivity_limits', 'meal_ecarbs_absorption', 'synthesis_plan'] | profile_recommendation.focus=basal_and_isf | profile_recommendation.confidence=medium-high
- run_033: top-level keys differ: missing=['profile_recommendation'] extra=[] | required sections absent or wrong type: ['profile_recommendation'] | profile_recommendation is not an object | steps with invalid status [] / confidence ['profile_cr_isf_dia', 'meal_bolus_strategy', 'meal_ecarbs_absorption', 'synthesis_plan'] | profile_recommendation missing required field(s): ['focus', 'decision', 'recommendation', 'rationale'] | profile_recommendation fields: [] | profile_recommendation.focus=None | profile_recommendation.decision=None | profile_recommendation.confidence=None | profile_recommendation.decision=None but profile rows imply change | meal_strategy_summary.confidence=medium (reactive strategy confirmed high confidence; carb-free approach valid). Low confidence in meal timing/size (inferred from glucose only; no logs). Medium confidence in GLP-1 effect quantification (absorption timing evident from telemetry, but effect magnitude not measured).
- run_035: steps with invalid status [] / confidence ['basal_targets'] | profile_recommendation.focus=meal_bolus_strategy_and_afternoon_basal | bad priority: ['No profile parameter changes indicated (CR, ISF, DIA, targets, non-afternoon basal remain stable)', 'Autosens remains disabled (intentional active tuning phase)', 'Dynamic ISF remains enabled at 70% (will operate at more moderate levels once meal bolusing is improved)']
- run_036: verify without null component: ['aaps.core.sensitivity', 'aaps.core.carb_absorption']
- run_037: profile_recommendation.focus=basal_carb_ratios_isf_dia
- run_038: current_value not copied exactly: ['aaps.core.carb_absorption'] | profile_recommendation.focus=DIA and meal_max_absorption_hours (carb and insulin absorption model parameters)
- run_039: steps with invalid status [] / confidence ['automation_smb_uam', 'automation_sensitivity_limits', 'meal_bolus_strategy', 'meal_ecarbs_absorption'] | profile_recommendation.focus=basal and max_iob | meal_strategy_summary.confidence=low-to-medium
- run_040: steps with invalid status [] / confidence ['meal_ecarbs_absorption'] | current_value not copied exactly: ['profile.dia', 'aaps.core.sensitivity', 'aaps.core.carb_absorption'] | verify without null component: ['aaps.core.carb_absorption'] | profile_recommendation.focus=DIA (Duration of Insulin Action)
- run_041: steps with wrong field set: ['profile_cr_isf_dia', 'automation_smb_uam', 'automation_sensitivity_limits', 'meal_bolus_strategy', 'meal_ecarbs_absorption', 'synthesis_plan'] | steps with invalid status [] / confidence ['profile_cr_isf_dia', 'meal_bolus_strategy'] | current_value not copied exactly: ['aaps.core.sensitivity'] | profile_recommendation.focus=meal_bolus_strategy | bad priority: ['Trial e-carbs for lunch meal if identified as slow-absorbing (high-fat, >40g carbs) during carb logging']
- run_042: steps with invalid status [] / confidence ['basal_targets', 'automation_smb_uam', 'meal_bolus_strategy'] | profile_recommendation.focus=basal_cr_isf_target
- run_043: profile_recommendation.focus=meal_bolus_and_carb_logging
- run_044: steps with wrong field set: ['meal_ecarbs_absorption', 'synthesis_plan'] | profile_recommendation.focus=meal_strategy_and_meal_absorption
- run_045: steps with invalid status [] / confidence ['basal_targets', 'automation_smb_uam', 'meal_bolus_strategy', 'synthesis_plan'] | meal_strategy_summary.confidence=medium-high
- run_046: steps with invalid status [] / confidence ['basal_targets', 'automation_smb_uam', 'synthesis_plan'] | verify without null component: ['aaps.core.sensitivity'] | profile_recommendation.focus=meal_bolus_strategy | profile_recommendation.decision=change but profile rows imply keep
- run_047: steps with invalid status [] / confidence ['basal_targets', 'automation_smb_uam', 'meal_bolus_strategy'] | profile_recommendation.focus=carb_ratio_daytime
- run_048: steps with wrong field set: ['safety_overview', 'basal_targets', 'profile_cr_isf_dia', 'automation_smb_uam', 'automation_sensitivity_limits', 'meal_bolus_strategy', 'meal_ecarbs_absorption', 'synthesis_plan'] | verify without null component: ['aaps.core.safety_limits'] | change without a distinct suggested_value: ['profile.basal.10_00']
- run_049: steps with invalid status [] / confidence ['basal_targets'] | decisions with wrong field set: ['profile.basal.00_00', 'profile.basal.05_00', 'profile.basal.06_00', 'profile.basal.10_00', 'profile.basal.16_00', 'profile.basal.18_00', 'profile.basal.19_00', 'profile.cr.00_00', 'profile.cr.04_00', 'profile.cr.08_00', 'profile.cr.16_00', 'profile.cr.20_00', 'profile.isf.00_00', 'profile.target.00_00', 'profile.target.08_00', 'profile.target.23_00', 'profile.dia', 'aaps.core.smb_uam', 'aaps.core.smb_activation', 'aaps.core.smb_delivery', 'aaps.core.safety_limits', 'aaps.core.sensitivity', 'aaps.core.carb_absorption'] | profile_recommendation.focus=basal_target_cr_isf_dia
- run_050: steps with invalid status [] / confidence ['basal_targets', 'automation_smb_uam'] | current_value not copied exactly: ['aaps.core.sensitivity'] | profile_recommendation.focus=basal and target at 00:00
