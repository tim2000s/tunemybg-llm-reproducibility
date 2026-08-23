# TuneMyBG reproducibility report

## Experiment `real_gpt56sol_med_50` — model `gpt-5.6-sol`

- Runs: 50 (completed 50, failed 0)
- Final JSON extracted: 50/50 (methods: strict ×50)
- Fully schema-compliant: 50/50; mean schema score 1.000
- Mean wall time per run: 306s
- **App outcome (as the app behaves), over 50 completed runs:** accepted first time 50; accepted after the repair prompt 0; invalid JSON, no prompt offered 0; schema stop, no prompt offered 0; still rejected after repair 0
- **Accepted by the app but breaking Prompt 4's own rules:** 0/50 accepted runs; commonest: —
- **App loop:** first pass parseable 50/50, first pass compliant 50/50; correction prompt sent in 0 run(s); compliant after correction 50/50
- Decisions per run — change: 0 ×32, 1 ×16, 2 ×2; keep: 23 ×32, 22 ×16, 21 ×2; verify: 0 ×50
- profile_recommendation focus: target ×39, basal ×11
- profile_recommendation decision: keep ×32, change ×18; confidence: medium ×50
- Primary recommendation area: target ×28, basal ×9, profile ×8, safety_and_data ×2, data_and_profile ×2, safety ×1; priority: safety ×50
- Meal strategy confidence: low ×50; exceptions: 2 ×25, 0 ×13, 1 ×12
- **Decision stability index** (mean per-parameter agreement): 0.983; parameters with unanimous decisions: 21/23
- Pairwise change-set Jaccard: mean 0.517; same primary area 36%; same profile focus 65%
- Pairwise text similarity — summary 0.144, profile recommendation 0.341, meal suggestion 0.080

### Parameter decision agreement

| parameter_key | current | modal | agreement | change | keep | verify | suggested values (when change) |
|---|---|---|---|---|---|---|---|
| profile.target.00_00 | 90 mg/dL | keep | 0.64 | 18 | 32 | 0 | 100 mg/dl x18 |
| profile.target.23_00 | 90 mg/dL | keep | 0.96 | 2 | 48 | 0 | 100 mg/dl x2 |
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
| safety_overview | completed | 1.00 | high | 1.00 |
| basal_targets | partial | 0.96 | medium | 1.00 |
| profile_cr_isf_dia | partial | 1.00 | low | 0.86 |
| automation_smb_uam | completed | 0.86 | medium | 1.00 |
| automation_sensitivity_limits | completed | 0.86 | medium | 1.00 |
| meal_bolus_strategy | partial | 1.00 | low | 1.00 |
| meal_ecarbs_absorption | partial | 0.64 | low | 0.96 |
| synthesis_plan | completed | 1.00 | medium | 1.00 |

### Per-run overview

| run | status | 1st pass JSON | 1st pass OK | repairs | final OK | score | change/keep/verify | profile focus | primary rec | time (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| run_001 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Primary: keep the profile stable and verify the low pattern first | 306.33 |
| run_002 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Review the 00:00 glucose target first | 295.55 |
| run_003 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the profile while verifying the overnight low pattern | 283.02 |
| run_004 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Primary: verify the context of recurrent lows before changing the profile | 321.76 |
| run_005 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Primary: review the midnight target | 305.87 |
| run_006 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the profile and verify the overnight pattern first | 302.41 |
| run_007 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the profile unchanged while verifying recurrent lows | 336.12 |
| run_008 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the profile unchanged while verifying the recurrent low pattern | 334.16 |
| run_009 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Prioritize overnight low attribution before changing the profile | 291.91 |
| run_010 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the profile and verify the overnight low pattern first | 324.26 |
| run_011 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | target | Increase the contiguous overnight target safety margin | 321.26 |
| run_012 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the profile unchanged while verifying the low patterns | 288.45 |
| run_013 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Reconstruct recurrent low-glucose sequences before changing settings | 320.74 |
| run_014 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Primary: test a less aggressive midnight target | 321.32 |
| run_015 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Characterize recurrent lows before changing settings | 314.54 |
| run_016 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Primary: reconstruct severe-low insulin sequences before changing settings | 293.48 |
| run_017 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Primary review: raise the midnight target | 290.85 |
| run_018 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Primary: review a higher 00:00 target | 319.99 |
| run_019 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Primary: keep the profile stable while isolating overnight lows | 324.49 |
| run_020 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Validate the overnight pattern before changing the profile | 280.94 |
| run_021 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Primary: review a higher 00:00 target | 309.68 |
| run_022 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Verify overnight profile behavior first | 292.43 |
| run_023 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Primary review: reduce overnight low pressure | 301.36 |
| run_024 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the selected profile while verifying the overnight low pattern | 325.18 |
| run_025 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the profile provisionally and verify the low pattern first | 303.87 |
| run_026 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Verify the overnight low pattern before changing the profile | 287.43 |
| run_027 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the profile unchanged while verifying overnight insulin exposure | 318.29 |
| run_028 | completed | strict | True | 0 | True | 1.00 | 2/21/0 | target | Review one continuous overnight target change first | 313.38 |
| run_029 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the current profile while validating the recurrent low pattern | 304.17 |
| run_030 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Primary: review a higher 00:00 overnight target | 318.9 |
| run_031 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Verify the recurrent low pattern before changing the profile | 308.23 |
| run_032 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Primary: preserve the profile while verifying the recurrent overnight low pattern | 286.82 |
| run_033 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Primary review: raise the 00:00 target candidate | 324.32 |
| run_034 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Verify the overnight low pattern before changing the profile | 307.37 |
| run_035 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the profile unchanged while verifying low-IOB overnight behaviour | 284.71 |
| run_036 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the profile unchanged while verifying the overnight low pattern | 315.93 |
| run_037 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Review one conservative overnight target change first | 303.84 |
| run_038 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Validate the overnight low mechanism before changing the profile | 354.35 |
| run_039 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the profile stable while verifying the high-IOB-to-late-low pattern | 300.03 |
| run_040 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the profile while verifying the overnight low mechanism | 296.4 |
| run_041 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Keep the profile while verifying the overnight low pattern | 292.08 |
| run_042 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Primary: review a higher 00:00 target | 308.57 |
| run_043 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | basal | Verify the recurrent overnight low pattern before changing the profile | 306.89 |
| run_044 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Primary: review a higher overnight target | 311.07 |
| run_045 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Review a higher midnight target first | 301.12 |
| run_046 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the profile unchanged while verifying overnight low exposure | 273.97 |
| run_047 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Primary review: increase the 00:00 target segment | 297.51 |
| run_048 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Primary review: raise the 00:00 target | 287.64 |
| run_049 | completed | strict | True | 0 | True | 1.00 | 0/23/0 | target | Keep the profile stable while isolating overnight lows | 290.42 |
| run_050 | completed | strict | True | 0 | True | 1.00 | 1/22/0 | target | Primary: review a higher target after midnight | 320.62 |
