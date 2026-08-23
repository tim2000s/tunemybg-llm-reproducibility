# Handling of a package with no carbohydrate entries

The real package has 0 carbohydrate entries in 14 days, 655 insulin entries and an empty declared meal strategy, so carb ratios were never exercised. Counts are over runs the app accepted.

| Model | Runs | Notices no carbs | Changes a CR | CR rationale cites missing carbs | CR called untestable | Infers meals from glucose | Advises carb logging | First recommendation is logging | meal_bolus_strategy status | meal confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| deepseek/deepseek-v4-pro | 48 | 48/48 (100%) | 0/48 (0%) | 32/48 (67%) | 27/48 (56%) | 48/48 (100%) | 45/48 (94%) | 6/48 (12%) | blocked ×29, partial ×14, completed ×5 | low ×43, medium ×5 |
| gemini-3.1-pro-preview | 50 | 50/50 (100%) | 0/50 (0%) | 44/50 (88%) | 32/50 (64%) | 50/50 (100%) | 47/50 (94%) | 14/50 (28%) | completed ×40, blocked ×7, partial ×3 | high ×24, medium ×21, low ×5 |
| gemini-3.5-flash-lite | 39 | 32/39 (82%) | 0/39 (0%) | 15/39 (38%) | 11/39 (28%) | 39/39 (100%) | 32/39 (82%) | 13/39 (33%) | completed ×39 | medium ×38, low ×1 |
| gemini-3.6-flash | 50 | 50/50 (100%) | 0/50 (0%) | 37/50 (74%) | 34/50 (68%) | 50/50 (100%) | 50/50 (100%) | 16/50 (32%) | completed ×41, partial ×9 | medium ×39, high ×5, low ×5, medium-high ×1 |
| gpt-5.4-mini | 48 | 48/48 (100%) | 0/48 (0%) | 42/48 (88%) | 35/48 (73%) | 48/48 (100%) | 25/48 (52%) | 2/48 (4%) | partial ×32, completed ×16 | low ×43, low-to-medium ×2, low-medium ×2, low_medium ×1 |
| gpt-5.6-sol | 50 | 50/50 (100%) | 0/50 (0%) | 42/50 (84%) | 35/50 (70%) | 50/50 (100%) | 15/50 (30%) | 0/50 (0%) | partial ×50 | low ×50 |
| x-ai/grok-4.6 | 50 | 50/50 (100%) | 0/50 (0%) | 50/50 (100%) | 44/50 (88%) | 50/50 (100%) | 38/50 (76%) | 2/50 (4%) | partial ×47, completed ×3 | low ×44, medium ×6 |
| claude-haiku-4-5 | 20 | 20/20 (100%) | 0/20 (0%) | 15/20 (75%) | 15/20 (75%) | 20/20 (100%) | 20/20 (100%) | 4/20 (20%) | completed ×20 | medium ×12, low ×3, low-medium ×2, medium-high ×2, high ×1 |
| meta-llama/llama-4-maverick | 44 | 31/44 (70%) | 2/44 (5%) | 0/44 (0%) | 0/44 (0%) | 44/44 (100%) | 37/44 (84%) | 6/44 (14%) | completed ×43, partial ×1 | low ×34, medium ×8, high ×1, low to medium ×1 |
| claude-opus-5 | 11 | 11/11 (100%) | 0/11 (0%) | 11/11 (100%) | 9/11 (82%) | 11/11 (100%) | 10/11 (91%) | 0/11 (0%) | partial ×11 | low ×11 |
| claude-sonnet-5 | 19 | 19/19 (100%) | 0/19 (0%) | 19/19 (100%) | 15/19 (79%) | 19/19 (100%) | 17/19 (89%) | 6/19 (32%) | partial ×18, completed ×1 | low ×17, low-medium ×1, medium ×1 |

## What the models said about the carb ratios

Sentences from the CR-row rationales, grouped across runs; the count is runs making the point.

### deepseek/deepseek-v4-pro

- (12/48) Cannot assess; keep until meal data present.
- (11/48) CR cannot be evaluated.
- (9/48) No carb entries;
- (8/48) No meal data to assess.
- (6/48) No carb data; keep.

### gemini-3.1-pro-preview

- (8/50) CR cannot be evaluated because the user logs zero carbs.
- (5/50) Cannot be evaluated due to 0 logged carbohydrates.
- (5/50) Cannot evaluate without logged carbs.
- (4/50) Cannot evaluate CR because no carbs are logged.
- (3/50) Zero logged carbs in the dataset means Carb Ratios cannot be evaluated or safely changed.

### gemini-3.5-flash-lite

- (9/39) No meal carb data available to evaluate morning CR performance.
- (5/39) No declared carbohydrate entries exist to evaluate CR performance.
- (5/39) Cannot be evaluated without recorded carbohydrate entries.
- (4/39) Evidence: zero carb entries.
- (4/39) Dependencies: carb logging.

### gemini-3.6-flash

- (17/50) Evidence: Zero carb entries logged.
- (13/50) No early morning meal carb entries were recorded.
- (11/50) Withhold CR adjustments until explicit meal logging is established.
- (8/50) CR cannot be evaluated without logged meals.
- (7/50) Maintain current setting.

### gpt-5.4-mini

- (12/48) There are no carb entries or meal-linked windows to test this ratio.
- (9/48) Changing CR now would be speculative.
- (9/48) No carb entries exist, so this CR cannot be validated.
- (7/48) No carb logs exist, so no meal-based evidence can validate a CR change.
- (7/48) The late-morning rise could reflect meal timing, but there are no carb entries.

### gpt-5.6-sol

- (15/50) There are no meal-linked carbohydrate or bolus records for this segment.
- (14/50) No meal carbohydrate amount, bolus timing, or immediate bolus percentage is available for this interval.
- (14/50) No carbohydrate entries or meal-linked responses exist for this segment.
- (13/50) Morning and afternoon rises may reflect unannounced meals, timing, or absorption.
- (13/50) Basal, target, Dynamic ISF, SMB/UAM, and residual IOB remain unresolved dependencies.

### x-ai/grok-4.6

- (31/50) Evidence: zero carb entries and COB 0.
- (25/50) Dependencies: meal logging.
- (19/50) Evidence: no carb treatments in this or any segment.
- (16/50) Uncertainty: unused.
- (14/50) Dependencies: empty declared meal strategy.

### claude-haiku-4-5

- (15/20) CR 11.1 g/U for 04:00–08:00 (early morning, tightest CR value).
- (12/20) CR 13.2 g/U (08:00–16:00 local, 07:00–15:00 UTC) covers breakfast and lunch windows.
- (11/20) CR 12.6 g/U for 20:00–00:00 (evening).
- (8/20) Keep pending meal logging.
- (7/20) Cannot validate without meal logs.

### meta-llama/llama-4-maverick

- (20/44) No strong evidence to change.
- (8/44) Current CR is generally appropriate.
- (6/44) Dependencies: profile_cr_isf_dia.
- (4/44) Uncertainty due to lack of meal data.
- (3/44) CR seems reasonable.
- CR changes made despite no carb data: [('run_039', ['profile.cr.00_00']), ('run_048', ['profile.cr.00_00'])]

### claude-opus-5

- (7/11) Evidence: a consistent morning rise from 110.5 to 148.0 mg/dL exists between 08:00 and 10:00 local, but with zero carbohydrate entries no bolus was ever calculated from this ratio.
- (7/11) This is the strongest carb ratio in the profile and covers the worst hyperglycemia block, but with zero carbohydrate entries it was never applied, so the 32.1 percent time above range at 16:00 local says nothing about its correctness.
- (7/11) Evidence: carb_entries is 0, total_carbs_g is 0.0, carb_treatment_entries is empty and COB is zero in all 24 sampled loop statuses, so this ratio was never applied to any dose during the period.
- (4/11) Uncertainty: complete.
- (4/11) Evidence: no carbohydrate entries exist in the period, and the 04:00 to 08:00 local window shows 95.2 to 98.7 percent time in range with no meal signature.

### claude-sonnet-5

- (12/19) No carbohydrate entries exist anywhere in the 14-day period, making it impossible to validate any carb ratio segment against actual meal response.
- (3/19) Same carbohydrate-logging gap applies; no evidence exists to support a change.
- (3/19) Zero carbohydrate entries exist in the entire dataset, so no meal-response evidence is available to validate or challenge this ratio, despite this segment overlapping the recurring morning rise pattern.
- (3/19) No carbohydrate entries exist to test this ratio against; validation is fully blocked by the data gap.
- (3/19) Same carbohydrate-logging blocker as all CR segments; no meal-linked data exists to test this value.
