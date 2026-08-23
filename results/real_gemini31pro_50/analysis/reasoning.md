# Reasoning analysis — gemini-3.1-pro-preview (50 runs, `real_gemini31pro_50`)

Each model rationale is split into sentences; sentences making the same point across runs are grouped. **Shared** = the point appears in at least 60% of the runs in that group; **varying** = it appears in some runs but not most. Counts are runs, not sentences. 'Evidence cited' lists the numbers and times the model quoted, with the number of runs quoting each.

## decision: Profile / basal 00:00

### keep — 49/50 runs

**Varying reasoning**

- (7/49) Fix safety limits first.
- (7/49) Keep basal stable while addressing targets and safety limits first.
- (5/49) Overnight hypoglycemia is driven by UAM stacking, not the underlying basal rate.
- (4/49) Overnight lows are likely driven by the tight 90 mg/dL target rather than excess basal.
- (3/49) Keep current basal while testing the safer Max IOB limits and higher targets, as automation stacking is the primary driver of the lows.
- (2/49) Overnight hypoglycemia is likely driven by extreme UAM automation stacking rather than the scheduled basal rate.
- … 5 more varying points

Points made by a single run only: 39.

Evidence cited: 90mg/dl (4), 04:00 (1).

### change — 1/50 runs

Points made by a single run only: 1.

Phrases used by at least half the runs: “reduction in basal” (1), “00 supports slight” (1), “basal delivery” (1), “overnight lows” (1), “slight reduction” (1), “lows between 00” (1), “delivery at midnight” (1), “incidence of overnight” (1), “00 and 03” (1), “high incidence” (1).

Evidence cited: 00:00 (1), 03:00 (1).

## decision: Profile / basal 05:00

### keep — 50/50 runs

**Varying reasoning**

- (5/50) Keep until AAPS safety limits are fixed to prevent confounding variables.
- (4/50) Morning fasting glucose is stable; no change supported at this time.
- (3/50) Fasting control from 04:00 to 08:00 is stable.
- (3/50) Morning basal is performing adequately; primary issues are evening/nocturnal.
- (2/50) True fasting needs are obscured by frequent suspension of basal to prevent UAM-induced hypoglycemia.
- (2/50) Morning glucose is relatively stable; keep basal unchanged while addressing limits.
- … 5 more varying points

Points made by a single run only: 32.

Evidence cited: 07:00 (2), 08:00 (2), 04:00 (2), 05:00 (1), 3:00 (1), 1:00 (1), 97.5% (1), 98% (1), 0% (1), 95% (1).

## decision: Profile / basal 06:00

### keep — 50/50 runs

**Varying reasoning**

- (5/50) Keep until AAPS safety limits are fixed.
- (3/50) Morning fasting numbers are highly stable; no change needed.
- (3/50) Morning glucose is stable; keep for now.
- (3/50) Morning basal is performing adequately.
- (2/50) True fasting needs are obscured by frequent suspension of basal to prevent UAM-induced hypoglycemia.
- (2/50) Morning basal appears adequate; no changes recommended until safety limits are fixed.
- … 3 more varying points

Points made by a single run only: 34.

Evidence cited: 98.7% (1), 04:00 (1).

## decision: Profile / basal 10:00

### keep — 50/50 runs

**Varying reasoning**

- (4/50) Keep until AAPS safety limits are fixed.
- (2/50) Daytime basal rates appear functional and should be kept stable while overnight safety is addressed.
- (2/50) Daytime basal appears supportive of the 86% overall time in range.
- (2/50) Midday stability is acceptable; primary issues are localized to the evening.
- (2/50) Daytime stability is acceptable when disconnected from meal events.
- (2/50) Daytime basals show strong performance; no evidence supports changing.
- … 1 more varying points

Points made by a single run only: 42.

Evidence cited: 86% (1), 92% (1), 86.0% (1).

## decision: Profile / basal 16:00

### keep — 50/50 runs

**Varying reasoning**

- (4/50) Keep until AAPS safety limits are fixed.
- (4/50) Afternoon hyperglycemia is driven by unannounced meals, not a basal deficit.
- (3/50) Late afternoon basal is stable.
- (2/50) Late afternoon and evening lows are driven by UAM overcorrections from unannounced meals, not necessarily an excessive profile basal.
- (2/50) Afternoon variability is dominated by unannounced meals and massive UAM stacking, obscuring basal performance.
- (2/50) Cannot isolate pure basal needs due to massive UAM insulin interference.
- … 4 more varying points

Points made by a single run only: 34.

Evidence cited: 18:00 (1), 16:00 (1).

## decision: Profile / basal 18:00

### keep — 50/50 runs

**Varying reasoning**

- (4/50) Evening lows are caused by UAM insulin stacking from afternoon meals, not this basal segment.
- (4/50) Keep until AAPS safety limits are fixed.
- (2/50) Keep basal steady until safety limits are reduced.
- (2/50) Evening basal must be kept stable while UAM stacking is addressed.
- (2/50) Retain to avoid changing multiple dependent variables simultaneously.

Points made by a single run only: 48.

Evidence cited: 19:00 (3), 18:00 (3), 15.3% (1), 0.6u/h (1), 20:00 (1).

## decision: Profile / basal 19:00

### keep — 50/50 runs

**Varying reasoning**

- (5/50) Keep until safety limits are fixed.
- (2/50) Keep evening basal steady while assessing the impact of new target and AAPS safety limits.
- (2/50) Evening basal appears stable when not overwhelmed by meal-related UAM insulin.
- (2/50) Evening basal must be kept stable while UAM stacking is addressed.
- (2/50) Retain to avoid changing multiple dependent variables simultaneously.
- (2/50) Keep current value.

Points made by a single run only: 47.

Evidence cited: 19:00 (3), 20:00 (2), 0.7u/h (1), 18:00 (1).

## decision: Profile / CR 00:00

### keep — 50/50 runs

**Varying reasoning**

- (8/50) CR cannot be evaluated because the user logs zero carbs.
- (5/50) Cannot be evaluated due to 0 logged carbohydrates.
- (4/50) Cannot evaluate CR because no carbs are logged.
- (4/50) Cannot evaluate carbohydrate ratios without logged meal data.
- (3/50) Zero logged carbs in the dataset means Carb Ratios cannot be evaluated or safely changed.
- (3/50) No logged carbs available to validate or adjust Carb Ratios.
- … 6 more varying points

Points made by a single run only: 23.

## decision: Profile / CR 04:00

### keep — 50/50 runs

**Varying reasoning**

- (8/50) CR cannot be evaluated because the user logs zero carbs.
- (6/50) Cannot be evaluated due to 0 logged carbohydrates.
- (5/50) Cannot evaluate without logged carbs.
- (3/50) Zero logged carbs in the dataset means Carb Ratios cannot be evaluated or safely changed.
- (3/50) Carbohydrates are not being logged, making CR adjustments untestable.
- (3/50) Cannot evaluate CR because no carbs are logged.
- … 6 more varying points

Points made by a single run only: 15.

## decision: Profile / CR 08:00

### keep — 50/50 runs

**Varying reasoning**

- (8/50) CR cannot be evaluated because the user logs zero carbs.
- (6/50) Cannot be evaluated due to 0 logged carbohydrates.
- (5/50) Cannot evaluate without logged carbs.
- (3/50) Zero logged carbs in the dataset means Carb Ratios cannot be evaluated or safely changed.
- (3/50) Carbohydrates are not being logged, making CR adjustments untestable.
- (3/50) Cannot evaluate CR because no carbs are logged.
- … 6 more varying points

Points made by a single run only: 15.

## decision: Profile / CR 16:00

### keep — 50/50 runs

**Varying reasoning**

- (8/50) CR cannot be evaluated because the user logs zero carbs.
- (6/50) Cannot be evaluated due to 0 logged carbohydrates.
- (5/50) Cannot evaluate without logged carbs.
- (3/50) Zero logged carbs in the dataset means Carb Ratios cannot be evaluated or safely changed.
- (3/50) Carbohydrates are not being logged, making CR adjustments untestable.
- (3/50) Cannot evaluate CR because no carbs are logged.
- … 6 more varying points

Points made by a single run only: 15.

## decision: Profile / CR 20:00

### keep — 50/50 runs

**Varying reasoning**

- (8/50) CR cannot be evaluated because the user logs zero carbs.
- (6/50) Cannot be evaluated due to 0 logged carbohydrates.
- (5/50) Cannot evaluate without logged carbs.
- (3/50) Zero logged carbs in the dataset means Carb Ratios cannot be evaluated or safely changed.
- (3/50) Carbohydrates are not being logged, making CR adjustments untestable.
- (3/50) Cannot evaluate CR because no carbs are logged.
- … 6 more varying points

Points made by a single run only: 15.

## decision: Profile / ISF 00:00

### keep — 50/50 runs

**Varying reasoning**

- (8/50) ISF is heavily modulated by Dynamic ISF.
- (3/50) ISF serves as the baseline for Dynamic ISF and UAM.
- (2/50) The flat ISF of 56 is an appropriate baseline, and Dynamic ISF (70%) is already heavily modifying it.
- (2/50) A flat 56 mg/dL/U may be too aggressive for overnights, but this cannot be cleanly separated from UAM insulin stacking.
- (2/50) ISF evaluation is heavily obscured by Dynamic ISF overrides and 100% UAM dosing.
- (2/50) Do not change the baseline ISF while targets and safety limits are the primary culprits for hypoglycemia.
- … 9 more varying points

Points made by a single run only: 49.

Phrases used by at least half the runs: “dynamic isf” (35).

Evidence cited: 70% (3), 56mg/dl (2), 100% (1), 25u (1).

## decision: Profile / target 00:00

### change — 45/50 runs

**Varying reasoning**

- (8/45) A target of 90 mg/dL provides zero safety buffer for lingering UAM IOB, contributing to severe 18.5% TBR at 01:00.
- (5/45) A 90 mg/dL target provides insufficient safety buffer for the algorithm, contributing to severe nocturnal hypoglycemia (10-18% TBR).
- (5/45) A 90 mg/dL target leaves insufficient buffer against UAM insulin momentum, driving severe overnight lows.
- (3/45) A target of 90 mg/dL provides zero safety buffer.
- (3/45) A 90 mg/dL overnight target provides zero safety buffer and is directly contributing to severe early-morning hypoglycemia.
- (3/45) Raising it creates a necessary safety buffer.
- … 5 more varying points

Points made by a single run only: 18.

Phrases used by at least half the runs: “90 mg/dl” (30).

Evidence cited: 90mg/dl (30), 18.5% (16), 01:00 (10), 18% (7), 100mg/dl (5), 11.4% (2), 110mg/dl (2), 10% (2), 03:00 (1), 02:00 (1), 00:00 (1), 23:00 (1).

### keep — 5/50 runs

Points made by a single run only: 5.

Evidence cited: 90mg/dl (1).

## decision: Profile / target 08:00

### keep — 49/50 runs

**Varying reasoning**

- (4/49) Daytime target of 100 mg/dL is reasonable and provides a minimal safety buffer during waking hours.
- (4/49) Daytime target of 100 mg/dL is performing adequately given the high overall Time in Range.
- (4/49) Daytime target is appropriate and daytime stability is mostly functional.
- (2/49) 100 mg/dL is standard.
- (2/49) Daytime target of 100 mg/dL is appropriate and avoids contributing to excessive daytime lows.
- (2/49) Current target is reasonable for daytime.
- … 1 more varying points

Points made by a single run only: 31.

Phrases used by at least half the runs: “daytime target” (29), “100 mg/dl” (25).

Evidence cited: 100mg/dl (25), 86% (3).

### change — 1/50 runs

Points made by a single run only: 1.

Phrases used by at least half the runs: “provides safer buffer” (1), “uam insulin absorption” (1), “buffer against unpredictable” (1), “raising the daytime” (1), “unpredictable uam insulin” (1), “target provides safer” (1), “daytime target provides” (1), “insulin absorption dynamics” (1).

## decision: Profile / target 23:00

### change — 45/50 runs

**Varying reasoning**

- (5/45) A 90 mg/dL target leaves no safety buffer against late-acting UAM insulin in the late evening, driving a high rate of severe lows.
- (4/45) Raising to 100 mg/dL adds a buffer.
- (3/45) A 90 mg/dL target provides insufficient safety buffer for the algorithm, contributing to severe nocturnal hypoglycemia.
- (2/45) Matches the 00:00 target change to provide consistent protection against hypoglycemia as UAM corrections from the evening carry over into the night.
- (2/45) A target of 90 mg/dL provides insufficient buffer against residual IOB from UAM corrections, causing severe hypoglycemia.
- (2/45) The 23:00 drop to 90 mg/dL traps evening UAM insulin, leading directly into nocturnal hypoglycemia.
- … 4 more varying points

Points made by a single run only: 29.

Evidence cited: 90mg/dl (21), 23:00 (6), 00:00 (5), 100mg/dl (4), 110mg/dl (3), 18% (2), 03:00 (2), 08:00 (1), 10.1% (1).

### keep — 5/50 runs

Points made by a single run only: 5.

Evidence cited: 90mg/dl (1).

## decision: Profile / DIA

### keep — 50/50 runs

**Varying reasoning**

- (10/50) 10 hours is standard and appropriate for the Oref1 algorithm.
- (6/50) DIA of 10 hours is standard for modern AAPS configurations.
- (5/50) 10 hours is standard for Oref1.
- (5/50) 10 hours is standard and safe for AAPS oref1.
- (3/50) A 10-hour DIA is conservative and appropriate for AAPS automation.
- (3/50) Standard default DIA value for ultra-rapid/rapid insulin in Oref1; no evidence supports changing it.
- … 2 more varying points

Points made by a single run only: 18.

Phrases used by at least half the runs: “10 hours” (32), “hours is standard” (27).

Evidence cited: 10h (37).

## decision: AAPS / SMB and UAM

### keep — 50/50 runs

**Varying reasoning**

- (10/50) Keep enabled, but constrain safety limits.
- (7/50) UAM is essential since the user logs zero carbs.
- (4/50) UAM is required since no carbs are logged.
- (4/50) Appropriate for the user's unannounced meal strategy.
- (4/50) UAM is currently the only mechanism handling meals.
- (3/50) UAM is required for the user's zero-announcement strategy.
- … 7 more varying points

Points made by a single run only: 25.

## decision: AAPS / SMB activation conditions

### keep — 50/50 runs

**Varying reasoning**

- (9/50) These conditions are appropriate for a fully unannounced meal strategy.
- (9/50) Current activation conditions are standard for a UAM-heavy setup.
- (4/50) Settings align with the active pure-UAM strategy.
- (2/50) These activation conditions appropriately support a pure UAM setup where COB is permanently zero.
- (2/50) Activation settings correctly reflect a UAM-dependent approach.
- (2/50) smb_always_enabled is required for the zero-announcement strategy to function.
- … 4 more varying points

Points made by a single run only: 22.

Evidence cited: 100% (1).

## decision: AAPS / SMB strength and frequency

### keep — 47/50 runs

**Varying reasoning**

- (3/47) Delivery frequency is standard and does not need adjustment, provided the maximum safety limits are fixed.
- (3/47) Intervals are aggressive but standard for highly responsive UAM setups.
- (3/47) Standard UAM delivery parameters.
- (2/47) Aggressive delivery is a side effect of relying solely on UAM; fixing the safety limits ceiling is a safer first step.
- (2/47) Rapid delivery interval is acceptable only if the total ceiling (Max IOB) is safely restricted.
- (2/47) The danger lies in the Max IOB and Max Basal limits overriding these, not the intervals themselves.
- … 4 more varying points

Points made by a single run only: 42.

Evidence cited: 3min (1), 20min (1).

### change — 3/50 runs

Points made by a single run only: 4.

Phrases used by at least half the runs: “minute interval” (3).

Evidence cited: 5min (1).

## decision: AAPS / max basal and max IOB limits

### change — 46/50 runs

**Varying reasoning**

- (9/46) A Max IOB of 25 U and Max Basal of 12 U/h are dangerously high given the ~20 U Total Daily Dose.
- (4/46) Current limits are dangerously wide for a profile with a 0.8 U/h max basal.
- (3/46) Current limits are dangerously high and enable the system to stack massive amounts of insulin for unannounced evening meals, causing the 41 mg/dL overnight lows.
- (3/46) Current limits are exceptionally dangerous for a user with ~0.6 U/h basal.
- (2/46) Limits are exceptionally high compared to the scheduled basal (0.8 max), allowing massive over-correction overnight and following meals.
- (2/46) 25 U IOB is dangerously high for a ~20 U/day profile.
- … 8 more varying points

Points made by a single run only: 41.

Evidence cited: 25u (20), 20u (15), 12u/h (9), 0.8u/h (5), 7u (5), 0.6u/h (4), 19.7u (4), 16u (3), 3u/h (1), 41mg/dl (1), 25% (1), 0.7u/h (1).

### keep — 4/50 runs

Points made by a single run only: 8.

Phrases used by at least half the runs: “max iob” (2), “dangerously high” (2).

Evidence cited: 25u (1).

## decision: AAPS / Autosens and Dynamic ISF

### keep — 50/50 runs

**Varying reasoning**

- (8/50) Dynamic ISF is functioning as intended.
- (6/50) Dynamic ISF is functioning as designed.
- (4/50) Dynamic ISF is currently compensating for unannounced meals.
- (2/50) Dynamic ISF is functioning as configured.
- (2/50) Dynamic ISF is currently the primary engine managing unannounced meals.
- (2/50) Dynamic ISF is acceptable as long as max basal and max IOB limits are safely constrained.
- … 6 more varying points

Points made by a single run only: 39.

Phrases used by at least half the runs: “dynamic isf” (49).

Evidence cited: 25u (1).

## decision: AAPS / carbohydrate absorption model

### keep — 50/50 runs

**Varying reasoning**

- (6/50) Settings are inactive due to zero logged carbs.
- (4/50) Standard absorption limits are acceptable, though currently unused since zero carbs are logged.
- (4/50) Keep default values.
- (4/50) Not actively impacting loop mechanics since zero carbs are entered.
- (4/50) Currently inactive due to lack of logged carbohydrates.
- (3/50) Irrelevant until the user begins logging carbohydrates.
- … 7 more varying points

Points made by a single run only: 18.

Evidence cited: 7h (1).

## profile recommendation

### target — 46/50 runs

**Shared reasoning**

- (43/46) Raise the 23:00 and 00:00 targets from 90 mg/dL to 100 mg/dL.

**Varying reasoning**

- (5/46) The 90 mg/dL target at 23:00 and 00:00 directly correlates with severe overnight hypoglycemia (up to 18.5% TBR at 1 AM).
- (4/46) An overnight target of 90 mg/dL combined with residual UAM insulin from unannounced dinners and GLP-1 therapy is causing severe nocturnal hypoglycemia (18.5% TBR at 01:00).
- (3/46) The overnight target of 90 mg/dL leaves zero safety buffer for leftover active insulin generated by UAM corrections for late evening meals, contributing heavily to the severe 11-18% TBR seen between midnight and 02:00.
- (3/46) The 90 mg/dL target overnight leaves no safety buffer and is directly associated with extreme Time Below Range (18.5% at 01:00).
- (3/46) Raising the target creates a necessary safety buffer.
- (2/46) The 90 mg/dL nighttime targets at 23:00 and 00:00 offer insufficient safety margins against UAM-induced insulin stacking, contributing to the severe 11-18% Time Below Range observed in the early morning hours.
- … 7 more varying points

Points made by a single run only: 35.

Phrases used by at least half the runs: “90 mg/dl” (45), “00 and 00” (39), “mg/dl target” (28), “safety buffer” (26), “targets from 90” (25), “00 targets” (24), “100 mg/dl” (24), “90 mg/dl target” (24).

Evidence cited: 90mg/dl (45), 23:00 (44), 00:00 (44), 100mg/dl (24), 110mg/dl (21), 18.5% (19), 01:00 (11), 18% (10), 03:00 (8), 02:00 (4), 10% (2), 1am (2).

### basal — 4/50 runs

**Varying reasoning**

- (2/4) Keep all profile basals, CRs, and ISFs constant while fixing AAPS safety limits.

Points made by a single run only: 9.

Phrases used by at least half the runs: “insulin stacking” (3), “aaps safety limits” (3), “max iob” (3), “limits are corrected” (2), “basal cr isf” (2), “profile settings basal” (2), “kept stable” (2), “extreme insulin stacking” (2).

## primary recommendation

### target — 17/50 runs

**Shared reasoning**

- (13/17) Raise Overnight Target for Safety.

**Varying reasoning**

- (3/17) Raising the target to at least 110 mg/dL gives the loop time to react.
- (2/17) The target of 90 mg/dL overnight provides no room for the algorithm to suspend insulin effectively before a crash, especially given the heavy UAM insulin stacking from unannounced evening meals.
- (2/17) The 90 mg/dL overnight target provides insufficient buffer against UAM-driven insulin stacking, directly contributing to the 23:00-03:00 lows.
- (2/17) Raising this target will help prevent the severe crashes observed between 22:00 and 03:00.
- (2/17) Raising this target to 100 mg/dL provides a necessary safety margin.
- (2/17) A target of 90 mg/dL provides almost zero room for loop overshoots.
- … 2 more varying points

Points made by a single run only: 18.

Phrases used by at least half the runs: “90 mg/dl” (17), “raise overnight” (14), “safety buffer” (11), “target of 90” (10), “overnight target” (10).

Evidence cited: 90mg/dl (17), 23:00 (6), 100mg/dl (6), 110mg/dl (5), 03:00 (5), 01:00 (3), 18.5% (3), 22:00 (1), 08:00 (1), 41mg/dl (1), 18% (1), 00:00 (1).

### automation — 9/50 runs

**Shared reasoning**

- (8/9) Reduce Max IOB and Max Basal Limits.
- (6/9) Current limits (Max IOB 25 U, Max Basal 12 U/h) are extremely dangerous and allow the system to stack massive amounts of insulin for unannounced meals, causing severe crashes.

**Varying reasoning**

- (5/9) Reduce Dangerous Safety Limits.
- (2/9) The current Max IOB of 25 U is higher than your entire daily insulin requirement.

Points made by a single run only: 5.

Phrases used by at least half the runs: “max iob” (9), “max basal” (9), “12 u/h” (7), “amounts of insulin” (6), “massive amounts” (5), “25 and max” (5), “safety limits” (5).

Evidence cited: 25u (9), 12u/h (7), 19.7u (1), 0.7u/h (1), 8u (1), 0.6u/h (1), 20u (1).

### safety_limits — 8/50 runs

**Shared reasoning**

- (6/8) Reduce Max IOB and Max Basal limits.

**Varying reasoning**

- (4/8) Reduce AAPS Safety Limits.
- (2/8) A Max IOB of 25 U is extremely unsafe for a user who requires only ~20 U total per day.

Points made by a single run only: 12.

Phrases used by at least half the runs: “max iob” (6), “max basal” (5), “safety limits” (5).

Evidence cited: 25u (5), 12u/h (3), 0.6u/h (2), 20u (2), 50% (1), 5u (1).

### aaps.core.safety_limits — 6/50 runs

**Shared reasoning**

- (5/6) Reduce Max IOB and Max Basal Limits.

**Varying reasoning**

- (3/6) This allows the system to stack massive amounts of insulin for unannounced meals, leading directly to severe evening crashes.
- (2/6) The current Max IOB (25 U) and Max Basal (12 U/h) are extremely high for a user with a ~20 U Total Daily Dose.

Points made by a single run only: 8.

Phrases used by at least half the runs: “max iob” (6), “iob and max” (5), “max basal” (5), “total daily dose” (4), “amounts of insulin” (4), “12 u/h” (4), “unannounced meals” (3).

Evidence cited: 25u (5), 12u/h (4), 20u (3), 5u (1), 2.5u/h (1).

### aaps — 4/50 runs

**Shared reasoning**

- (4/4) This allows the UAM algorithm to stack dangerous amounts of insulin to fight delayed meals, directly causing the severe nighttime crashes.
- (3/4) Restrict Max IOB and Max Basal Limits.

**Varying reasoning**

- (2/4) The max_iob_units limit of 25 U and max_basal_u_per_hour of 12 U/h are excessively high for a profile with basal rates under 1.0 U/h.

Points made by a single run only: 5.

Phrases used by at least half the runs: “amounts of insulin” (4), “directly causing” (2), “iob and max” (2), “max iob” (2), “severe nighttime” (2), “massive amounts” (2), “causing severe” (2), “max basal” (2), “safety limits” (2), “max_basal_u_per_hour of 12” (2), “u/h are excessively” (2), “12 u/h” (2).

Evidence cited: 25u (3), 12u/h (2), 0.8u/h (1), 1.0u/h (1), 20u (1).

### safety — 3/50 runs

**Shared reasoning**

- (2/3) Current limits (25 U Max IOB and 12 U/h Max Basal) are disproportionately high compared to the ~19.7 U total daily insulin and 0.8 U/h max profile basal.

Points made by a single run only: 6.

Phrases used by at least half the runs: “12 u/h” (3), “basal limits” (2), “max iob” (2), “max basal” (2), “0.8 u/h” (2).

Evidence cited: 12u/h (3), 25u (3), 0.8u/h (2), 20u (1), 19.7u (1).

### automation_safety — 1/50 runs

Points made by a single run only: 4.

Phrases used by at least half the runs: “times your highest” (1), “correcting unannounced evening” (1), “15 times” (1), “scheduled basal lowering” (1), “prevent the algorithm” (1), “basal is 12” (1), “estimated total daily” (1), “low overnight” (1), “safety limits max” (1), “meals and driving” (1), “12 u/h” (1), “reduce aaps safety” (1).

Evidence cited: 12u/h (1), 25u (1).

### automation_sensitivity_limits — 1/50 runs

Points made by a single run only: 2.

Phrases used by at least half the runs: “day causing severe” (1), “iob and max” (1), “limits current limits” (1), “max basal limits” (1), “uam over corrections” (1), “causing severe uam” (1), “limits allow aaps” (1), “aaps to deliver” (1), “deliver more insulin” (1), “tighten max iob” (1), “full day causing” (1), “required for full” (1).

### limits — 1/50 runs

Points made by a single run only: 3.

Phrases used by at least half the runs: “iob of 25” (1), “reduce max iob” (1), “total of 16” (1), “25 is excessively” (1), “meals driving severe” (1), “amounts of insulin” (1), “driving severe nighttime” (1), “allows uam” (1), “safety max iob” (1), “daily basal total” (1), “unannounced meals driving” (1), “excessively high” (1).

Evidence cited: 16u (1), 25u (1).

## summary

### 50 runs

**Varying reasoning**

- (13/50) The system is operating without logged carbohydrates, relying entirely on Unannounced Meals (UAM) and Dynamic ISF to manage glucose rises.
- (13/50) The data shows a 100% unannounced meal (UAM) strategy with zero logged carbohydrates.
- (10/50) Dangerously high safety limits (Max IOB of 25 U and Max Basal of 12 U/h) are allowing the system to over-correct prolonged post-meal spikes, directly resulting in severe evening and overnight hypoglycemia.
- (7/50) The data shows a 14-day period with 98.7% CGM coverage and strong overall Time in Range (86.0%).
- (5/50) Time In Range is very strong at 86%, but Time Below Range is elevated at 5.1% and highly concentrated during the night (23:00 to 03:00 local time).
- (4/50) The profile demonstrates excellent overall Time in Range (86%) achieved through a completely unannounced meal (UAM) strategy combined with Dynamic ISF.
- … 15 more varying points

Points made by a single run only: 51.

Phrases used by at least half the runs: “safety limits” (32), “unannounced meals” (26), “time in range” (25).

Evidence cited: 90mg/dl (22), 86.0% (17), 25u (15), 5.1% (8), 12u/h (7), 18.5% (6), 03:00 (6), 86% (6), 01:00 (5), 23:00 (4), 100% (3), 98.7% (2).

## issues

### 50 runs

**Shared reasoning**

- (40/50) Severe and recurring nocturnal hypoglycemia between 23:00 and 03:00, reaching up to 18.5% Time Below Range at 01:00.

**Varying reasoning**

- (29/50) Dangerously high safety limits in AAPS (max IOB of 25 U and max basal of 12 U/h) relative to a 0.6 U/h basal profile.
- (13/50) Overnight glucose targets are set to 90 mg/dL, providing zero safety buffer for late-acting insulin.
- (10/50) Significant afternoon hyperglycemia, with Time Above Range (TAR) exceeding 20% between 14:00 and 17:00.
- (4/50) Zero carbohydrate entries logged over 14 days, forcing the system to rely entirely on reactive UAM SMBs.
- (4/50) Max IOB (25 U) exceeds the user's Total Daily Dose (~20 U), completely neutralizing its function as a safety ceiling.
- (4/50) The 90 mg/dL target from 23:00 to 08:00 provides almost no safety buffer against UAM-driven insulin stacking.
- … 16 more varying points

Points made by a single run only: 42.

Phrases used by at least half the runs: “max iob” (33), “90 mg/dl” (32), “12 u/h” (29), “max basal” (26), “time below range” (25).

Evidence cited: 25u (43), 90mg/dl (32), 12u/h (29), 18.5% (27), 01:00 (21), 03:00 (18), 00:00 (15), 19:00 (15), 15.3% (14), 23:00 (13), 18:00 (13), 17:00 (8).

## step findings: data_quality

### 50 runs

**Varying reasoning**

- (18/50) CGM coverage is excellent at 98.7% over 14 days.
- (14/50) However, there are exactly zero carbohydrate entries logged over 14 days, indicating a fully unannounced meal strategy or absent logging.
- (8/50) The user relies entirely on Unannounced Meals (UAM).
- (8/50) However, the complete absence of logged carbohydrates means the system is operating in a 100% unannounced meal environment.
- (5/50) The system operates entirely in an unannounced meal (UAM) mode.
- (4/50) CGM coverage is excellent at 98.7%, but there are exactly 0 logged carbohydrate entries over 14 days.
- … 8 more varying points

Points made by a single run only: 28.

Evidence cited: 98.7% (26), 100% (6), 65min (1), 5.0min (1).

## step findings: safety_overview

### 50 runs

**Varying reasoning**

- (21/50) Time Below Range is 11.4% at 00:00, 18.5% at 01:00, and >10% through 03:00.
- (9/50) There is a significant safety risk from evening and overnight hypoglycemia.
- (4/50) Extreme lows down to 41 mg/dL were recorded.
- (3/50) There is a severe and systemic risk of evening and nocturnal hypoglycemia driven by aggressive evening insulin stacking and tight overnight targets.
- (3/50) There is a severe and persistent pattern of late-evening and early-overnight hypoglycemia.
- (3/50) Significant nocturnal hypoglycemia is present.
- … 10 more varying points

Points made by a single run only: 36.

Evidence cited: 18.5% (18), 03:00 (14), 19:00 (13), 5.1% (12), 00:00 (11), 18:00 (11), 01:00 (10), 15.3% (10), 32.1% (7), 41mg/dl (7), 23:00 (5), 11.4% (5).

## step findings: basal_targets

### 50 runs

**Varying reasoning**

- (9/50) The profile target drops aggressively to 90 mg/dL at 23:00 and 00:00.
- (5/50) The overnight target of 90 mg/dL provides insufficient safety buffer for a dynamic automated system.
- (4/50) It leaves no safety buffer against UAM or Dynamic ISF overshoot.
- (4/50) The overnight target of 90 mg/dL is too tight, directly contributing to the heavy TBR between 00:00 and 03:00.
- (4/50) The 90 mg/dL overnight target is too aggressive, especially given the pattern of severe nighttime hypoglycemia.
- (4/50) The 90 mg/dL target leaves very little margin for error.
- … 5 more varying points

Points made by a single run only: 52.

Phrases used by at least half the runs: “90 mg/dl” (50).

Evidence cited: 90mg/dl (50), 23:00 (16), 00:00 (8), 03:00 (4), 0.7u/h (3), 18.5% (2), 0.8u/h (2), 08:00 (2), 70mg/dl (1), 22:00 (1), 01:00 (1), 0.6u/h (1).

## step findings: profile_cr_isf_dia

### 50 runs

**Varying reasoning**

- (14/50) ISF is flat at 56 mg/dL/U.
- (10/50) ISF is flat at 56 mg/dL/U, and DIA is 10 hours.
- (5/50) The profile relies on a flat ISF of 56 mg/dL/U and a 10-hour DIA.
- (5/50) CR cannot be evaluated due to missing carb data.
- (5/50) Carb Ratios cannot be evaluated because no carbs are logged.
- (4/50) Carb ratios (10.5-13.2 g/U) are dormant because no carbs are logged.
- … 8 more varying points

Points made by a single run only: 52.

Phrases used by at least half the runs: “56 mg/dl/u” (34).

Evidence cited: 56mg/dl (34), 10h (11), 13.2g/u (6), 100% (2), 90mg/dl (2), 70% (1), 6h (1), 18:00 (1), 19:00 (1).

## step findings: automation_smb_uam

### 50 runs

**Varying reasoning**

- (6/50) The user relies entirely on UAM.
- (4/50) A rapid 3-minute SMB interval causes aggressive insulin stacking early in the glucose rise.
- (4/50) The system is functioning as a fully closed-loop, reactive system without manual meal announcements.
- (3/50) The system aggressively treats all glucose rises as unannounced meals (UAM), deploying SMBs every 3 minutes.
- (3/50) The user relies 100% on UAM for meal management.
- (3/50) The system is relying 100% on UAM to manage food.
- … 8 more varying points

Points made by a single run only: 57.

Evidence cited: 100% (9), 3min (8), 12u/h (2), 25u (2), 0.8u/h (1), 13:00 (1), 17:00 (1), 20min (1), 32.1% (1), 16:00 (1).

## step findings: automation_sensitivity_limits

### 50 runs

**Varying reasoning**

- (16/50) Safety limits are dangerously high.
- (10/50) Max IOB is 25 U, and Max Basal is 12 U/h.
- (9/50) A max_iob_units of 25 U is higher than the user's Total Daily Dose.
- (4/50) This allows the UAM algorithm to stack massive amounts of insulin against delayed GLP-1 meal spikes, causing the severe nighttime crashes.
- (3/50) A 25 U max IOB on a ~19.7 U TDD allows the system to dump massive amounts of insulin during UAM spikes, directly causing the severe evening hypoglycemia.
- (3/50) Safety limits are exceptionally open. max_iob_units is 25 U and max_basal_u_per_hour is 12 U/h.
- … 12 more varying points

Points made by a single run only: 46.

Phrases used by at least half the runs: “max iob” (31), “safety limits” (31), “12 u/h” (25).

Evidence cited: 25u (41), 12u/h (25), 20u (5), 90mg/dl (4), 70% (4), 19.7u (3), 0.8u/h (3), 0.7u/h (2), 36mg/dl (2), 16u (2), 0.6u/h (2), 18:00 (2).

## step findings: meal_bolus_strategy

### 50 runs

**Varying reasoning**

- (12/50) The user employs a 100% reactive unannounced meal strategy.
- (7/50) The user relies entirely on reactive UAM.
- (4/50) There are no preboluses, no immediate meal boluses, and no announced carbs.
- (4/50) There is no prebolusing or immediate bolusing.
- (3/50) This fails mechanically against GLP-1 delayed gastric emptying.
- (3/50) There is no active meal bolus strategy to review.
- … 6 more varying points

Points made by a single run only: 57.

Evidence cited: 100% (17), 17:00 (3), 0% (3), 13:00 (1), 18:00 (1), 15.3% (1), 12:00 (1), 14:00 (1).

## step findings: meal_ecarbs_absorption

### 50 runs

**Shared reasoning**

- (32/50) E-carbs are not utilized.

**Varying reasoning**

- (3/50) AAPS lacks any forward-looking absorption model to pace insulin delivery and relies entirely on instantaneous CGM trends.
- (3/50) Despite the likely delayed gastric emptying from the GLP-1, no e-carbs are used.
- (3/50) Extended carbohydrates are not used.
- (2/50) The 7-hour meal max absorption limit is largely bypassed because UAM determines the dosing trajectory, stripping the system of the ability to pace insulin against delayed GLP-1 food absorption.
- (2/50) Extended absorption from GLP-1 is managed reactively, putting extreme stress on loop safety limits.
- (2/50) The user relies strictly on UAM to handle the delayed digestion characteristic of their GLP-1 medication.
- … 1 more varying points

Points made by a single run only: 36.

Evidence cited: 8mg/dl (1), 7h (1).

## step findings: synthesis_plan

### 50 runs

**Varying reasoning**

- (6/50) Immediate safety interventions require lowering the Max IOB limit and raising the overnight target.
- (6/50) The immediate priority is safety.
- (3/50) The mechanical root cause of the severe hypoglycemia is the combination of a 100% reactive UAM meal strategy and dangerously permissive AAPS max basal/IOB limits.
- (3/50) This must be addressed by raising the tight 90 mg/dL overnight target to 100 mg/dL and tightening the dangerously permissive max IOB and max basal limits.
- (3/50) The primary fixes are to raise the overnight target to provide a safety buffer and strictly rein in the max IOB limit.
- (3/50) Lowering the safety limits and raising the overnight target are the required first steps.
- … 10 more varying points

Points made by a single run only: 67.

Phrases used by at least half the runs: “max iob” (26), “overnight target” (25), “safety limits” (25).

Evidence cited: 90mg/dl (19), 25u (15), 100% (4), 100mg/dl (3), 3u/h (1), 23:00 (1), 00:00 (1), 10h (1).

## meal strategy

### 50 runs

**Varying reasoning**

- (12/50) The user relies on a 100% Unannounced Meals (UAM) 'zero-announce' strategy with zero logged carbs.
- (5/50) The user employs a 100% unannounced meal strategy.
- (4/50) Begin logging estimated carbohydrates at the time of eating.
- (4/50) The user relies entirely on Unannounced Meals (UAM) without logging carbs.
- (3/50) GLP-1 slows digestion, causing UAM to aggressively overdose early on, leading to later crashes.
- (3/50) The user currently logs zero carbohydrates and relies 100% on the Unannounced Meal (UAM) feature.
- … 13 more varying points

Points made by a single run only: 108.

Evidence cited: 100% (23), 4h (4), 18:00 (2), 0% (2), 90mg/dl (1), 60min (1), 15.3% (1), 15min (1), 50% (1), 6h (1), 18% (1), 25u (1).
