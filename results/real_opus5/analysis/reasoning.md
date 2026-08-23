# Reasoning analysis — claude-opus-5 (19 runs, `real_opus5`)

Each model rationale is split into sentences; sentences making the same point across runs are grouped. **Shared** = the point appears in at least 60% of the runs in that group; **varying** = it appears in some runs but not most. Counts are runs, not sentences. 'Evidence cited' lists the numbers and times the model quoted, with the number of runs quoting each.

## decision: Profile / basal 00:00

### keep — 19/19 runs

**Shared reasoning**

- (19/19) The 00:00-05:00 local block shows time below range of 11.4, 18.5, 10.1 and 10.2 percent at hours 23, 1, 2 and 3 local with means of 93.3, 90.6, 101.9 and 104.7 mg/dL and spontaneous recovery by 04:00, which is a real pattern.

**Varying reasoning**

- (2/19) Late-evening correction windows on 08-12 and 08-17 show falls of 56 to 68 mg/dL over four hours from doses of 0.05 to 0.15 units, confirming a carry-over tail under a 10-hour DIA.
- (2/19) Dependencies: coupled to the 10 hour duration of insulin action, to the dynamic sensitivity curve and to the pending insulin on board ceiling change, which must be observed first.

Points made by a single run only: 50.

Phrases used by at least half the runs: “below range” (19), “10 hour” (13), “insulin on board” (13), “local hours” (12), “time below range” (11), “hours 00” (11), “10 hour dia” (10), “basal excess” (10), “percent below range” (10).

Evidence cited: 00:00 (13), 03:00 (9), 04:00 (9), 18.5% (8), 10.2% (8), 01:00 (7), 05:00 (6), 104.7mg/dl (5), 02:00 (5), 23:00 (4), 10h (4), 3.0% (4).

## decision: Profile / basal 05:00

### keep — 19/19 runs

**Shared reasoning**

- (19/19) Evidence: the 05:00 local hour shows an average of 104.2 mg/dL, 95.2 percent in range, 4.8 percent below range and 0.0 percent above range, and 06:00 shows 99.5 mg/dL with 97.5 percent in range.

**Varying reasoning**

- (6/19) Dependencies: none that would justify a change; no adjustment is supported.
- (5/19) Uncertainty: minimal for this segment; the single 42 mg/dL reading at 07:19 local on 2026-08-21 occurred on the day of a sensor change and is excluded from attribution.
- (3/19) Dependencies: none that would justify change, and altering a well-performing segment would add noise to the planned sequential tests.
- (3/19) Uncertainty: none material; this is one of the best-controlled windows in the dataset.
- (3/19) Dependency: none that would justify altering it.
- (3/19) Uncertainty: none material for this segment.
- … 4 more varying points

Points made by a single run only: 17.

Phrases used by at least half the runs: “below range” (17), “percent below” (14), “4.8 percent” (14), “above range” (13), “dependencies none” (13), “percent below range” (13), “95.2 percent” (13), “4.8 percent below” (12), “99.5 mg/dl” (11), “104.2 mg/dl” (11), “percent time” (10), “local hour” (10).

Evidence cited: 4.8% (14), 05:00 (13), 95.2% (13), 99.5mg/dl (11), 104.2mg/dl (11), 06:00 (10), 97.5% (8), 0.0% (7), 07:19 (5), 42mg/dl (5), 2.5% (3), 08:00 (3).

## decision: Profile / basal 06:00

### keep — 19/19 runs

**Shared reasoning**

- (19/19) Evidence: the 06:00 to 09:00 local block covered by this segment shows means of 99.5, 99.5, 110.5 and 132.9 mg/dL with time in range of 97.5, 98.7, 98.2 and 91.1 percent and time below range of 2.5, 1.3, 0.0 and 0.0 percent.

**Varying reasoning**

- (7/19) Uncertainty: the single 42 mg/dL reading at 07:19 local on 08-21 preceded a sensor change by two hours, so an artifact cannot be excluded.
- (7/19) Dependencies: separating meal effect here requires the carbohydrate logging observation; until then no basal change is supportable.
- (3/19) Uncertainty: the rise beginning at 09:00 local may reflect either dawn physiology or unannounced breakfast, which cannot be separated without carbohydrate data.
- (3/19) The only uncertainty is that the 09:00-10:00 local rise begins here and may be meal-related, which cannot be resolved without carbohydrate entries.
- (2/19) Uncertainty: the rise toward 10:00 local reaching 148.0 mg/dL begins inside this segment, but with zero carb entries a morning meal is the more plausible driver than basal.
- (2/19) Dependencies: none that would justify change; this segment is explicitly protected in the implementation order.
- … 2 more varying points

Points made by a single run only: 20.

Phrases used by at least half the runs: “below range” (18), “time in range” (11), “percent below range” (10), “local hours” (10).

Evidence cited: 06:00 (12), 09:00 (11), 10:00 (9), 42mg/dl (9), 0.0% (9), 08:00 (8), 07:19 (7), 132.9mg/dl (7), 1.3% (6), 07:00 (6), 91.1% (6), 148.0mg/dl (5).

## decision: Profile / basal 10:00

### keep — 19/19 runs

**Shared reasoning**

- (12/19) Evidence: hours 10:00 to 15:00 local average 148.0, 132.3, 141.3, 135.0, 148.1, and 153.0 mg/dL with time above range of 7.5 to 26.3 percent.

**Varying reasoning**

- (4/19) Dependencies: raising basal here would add insulin ahead of the 18:00-19:00 low window where time below range reaches 15.3 percent, which the 5.1 percent overall time below range does not permit.
- (4/19) Uncertainty: high.
- (3/19) Evidence: the rise begins here, with 10:00 local at 148.0 mg/dL and 20.2 percent above range, and 08:00 immediately before shows 0 percent below range and only 1.8 percent above range.
- (3/19) Dependencies: any upward change here would add insulin that remains active into the 18:00 to 19:00 hypoglycemia cluster under a 10-hour DIA, so it must wait until that cluster is resolved.
- (2/19) Dependency: this must wait for the carbohydrate logging observation, since raising daytime basal without meal data risks adding insulin whose tail lands in the 18:00 to 20:00 local window that already carries 7.7 and 15.3 percent time below range.
- (2/19) Uncertainty: the afternoons of 08-17 and 08-18 inside this segment contained 180-minute SMB blackouts from 135 mg/dL temporary targets and are excluded from inference.
- … 2 more varying points

Points made by a single run only: 35.

Phrases used by at least half the runs: “above range” (17), “time above range” (12), “hours 10” (10).

Evidence cited: 10:00 (12), 18:00 (11), 19:00 (10), 153.0mg/dl (7), 26.3% (6), 20.2% (5), 16:00 (4), 15.3% (4), 23.6% (3), 162.8mg/dl (3), 148.0mg/dl (3), 15:00 (3).

## decision: Profile / basal 16:00

### keep — 19/19 runs

**Shared reasoning**

- (18/19) Evidence: local hour 16:00 is the highest of the day at 162.8 mg/dL with 32.1 percent above range and zero percent below range, and it coincides exactly with the lowest scheduled basal segment.

**Varying reasoning**

- (6/19) Nevertheless at least three competing explanations remain unresolved: unannounced carbohydrates, SMB suppression during the two 180-minute 135 mg/dL temporary targets on 08-17 and 08-18 that overlap this hour, and GLP-1 related delayed absorption after doses on 08-14, 08-17 and 08-20.
- (3/19) Uncertainty: high.
- (2/19) Dependencies: raising this segment would feed the 18:00 to 19:00 window where time below range is 7.7 and 15.3 percent with 41 and 42 mg/dL nadirs, so change is unsafe before the automation steps and carbohydrate logging are evaluated.
- (2/19) Dependencies: blocked by the safety constraint from the hypoglycaemia stage that no change may increase insulin between 16:00 and 19:00 local, and by the pending meal workflow evidence.

Points made by a single run only: 45.

Phrases used by at least half the runs: “above range” (19), “32.1 percent” (18), “162.8 mg/dl” (18), “below range” (17), “percent above range” (16), “32.1 percent above” (15), “15.3 percent” (13), “percent below range” (11), “lowest basal” (11), “00 local” (10).

Evidence cited: 32.1% (18), 162.8mg/dl (18), 18:00 (16), 16:00 (15), 19:00 (14), 15.3% (13), 0.0% (8), 17:00 (6), 135mg/dl (5), 148.9mg/dl (4), 20:00 (3), 0.5u/h (3).

## decision: Profile / basal 18:00

### keep — 19/19 runs

**Shared reasoning**

- (13/19) Evidence: the 18:00 local hour shows an average of 124.2 mg/dL with 80.4 percent in range but 7.7 percent below range and a minimum of 42 mg/dL.

**Varying reasoning**

- (3/19) Uncertainty: a small basal contribution cannot be excluded.
- (2/19) Evidence: 18:00 local shows 7.7 percent below range with a mean of 124.2 mg/dL, and the level-2 clusters of 2026-08-13 and 2026-08-14 fall in and just after this hour.
- (2/19) Dependencies: the automation change to the maximum insulin on board must be evaluated first.
- (2/19) Dependency: reassess only after the insulin-on-board ceiling change has been observed, since that change targets the same mechanism.
- (2/19) Uncertainty: high as to cause.

Points made by a single run only: 46.

Phrases used by at least half the runs: “below range” (19), “7.7 percent” (19), “42 mg/dl” (13), “local hour” (13), “7.7 percent below” (13), “percent below range” (13), “minimum of 42” (12), “124.2 mg/dl” (10).

Evidence cited: 7.7% (19), 18:00 (13), 42mg/dl (13), 124.2mg/dl (10), 0.2u (7), 120min (6), 56mg/dl (5), 178mg/dl (4), 0.6u/h (4), 17:20 (3), 11.9% (3), 0.1u/h (2).

## decision: Profile / basal 19:00

### keep — 19/19 runs

**Shared reasoning**

- (18/19) Evidence: the 19:00 local hour has the highest daytime time below range at 15.3 percent with a minimum of 41 mg/dL, and basal rises to 0.7 U/h precisely here.

**Varying reasoning**

- (3/19) Uncertainty is high.

Points made by a single run only: 51.

Phrases used by at least half the runs: “15.3 percent” (19), “below range” (19), “41 mg/dl” (15), “local hour” (14), “minimum of 41” (13), “time below range” (11).

Evidence cited: 15.3% (19), 41mg/dl (15), 19:00 (14), 105.4mg/dl (9), 18:00 (7), 0.2u (5), 234mg/dl (4), 0.7u/h (4), 17:20 (3), 120min (3), 178mg/dl (3), 56mg/dl (3).

## decision: Profile / CR 00:00

### keep — 19/19 runs

**Varying reasoning**

- (8/19) Evidence: carbohydrate entries are 0, total carbohydrates 0.0 g, the carbohydrate treatment list is empty and carbohydrate-on-board is 0 in every sampled loop status, so this ratio has never been exercised during the period.
- (7/19) Evidence: carb_entries is 0, total_carbs_g is 0.0, carb_treatment_entries is empty and COB is zero in all 24 sampled loop statuses, so this ratio was never applied to any dose during the period.
- (4/19) Uncertainty: complete, since no observation exists that could support or refute the value.
- (3/19) Dependency: blocked until carbohydrate logging exists.
- (3/19) Dependencies: becomes assessable only after carbohydrate announcement begins.
- (2/19) Evidence: this segment is confirmed active because CR 13.0 and neighbouring values appear in loop reasons at the correct local times, but it was never used for dosing, since carb_entries is 0, total_carbs_g is 0.0, carb_treatment_entries is empty and COB is 0 in every sampled cycle.
- … 5 more varying points

Points made by a single run only: 31.

Phrases used by at least half the runs: “carbohydrate logging” (12), “loop reason strings” (12).

Evidence cited: 2% (4), 13.3g/u (2), 00:00 (1), 04:00 (1), 13.0g/u (1), 178mg/dl (1), 0.2u (1).

## decision: Profile / CR 04:00

### keep — 19/19 runs

**Varying reasoning**

- (6/19) It is confirmed active, appearing as 11.1 in loop reason strings at 04:01, 04:55, 06:30 and 07:29 local.
- (6/19) Dependencies: requires carbohydrate logging plus a meal actually occurring in the 04:00-08:00 local window, which the glucose pattern does not suggest is common.
- (5/19) Dependencies: requires carbohydrate logging before any assessment is possible.
- (5/19) Uncertainty: complete.
- (3/19) Dependencies: carbohydrate logging is required before any carb ratio can be assessed.
- (3/19) No carbohydrate was entered at any time in the 14-day window, so this segment produced no dosing and cannot be validated or refuted.
- … 5 more varying points

Points made by a single run only: 23.

Evidence cited: 08:00 (8), 04:00 (8), 04:01 (6), 04:55 (2), 11.1g/u (2), 06:30 (1), 07:29 (1), 98.7% (1), 03:01 (1), 100% (1).

## decision: Profile / CR 08:00

### keep — 19/19 runs

**Shared reasoning**

- (13/19) The morning rise from 110.5 to 148.0 mg/dL between 08:00 and 10:00 local was handled entirely by UAM, so it carries no information about the carb ratio.

**Varying reasoning**

- (4/19) Dependencies: the morning window is the lowest-hypoglycemia-risk window in the day at 0.0 percent below range at 08:00 and 09:00 local, so it is the safest place to test this ratio once meals are logged.
- (4/19) Uncertainty: complete.
- (3/19) Evidence: confirmed active in loop reasons at 09:11 and 15:00 local, yet unused because no carbohydrate was logged.
- (3/19) The value appears in reason strings at 09:11 local, matching the profile segment and confirming profile activity only.
- (2/19) Dependencies: this is the first carb ratio that will become verifiable once the morning meal is logged.
- (2/19) Dependencies: carbohydrate logging for the morning meal would be needed before any judgement.
- … 2 more varying points

Points made by a single run only: 32.

Phrases used by at least half the runs: “00 local” (14), “148.0 mg/dl” (12), “10 00 local” (11), “carbohydrate logging” (11).

Evidence cited: 10:00 (16), 148.0mg/dl (12), 08:00 (10), 09:00 (5), 07:00 (5), 09:11 (4), 1.2% (2), 15:00 (2), 14:55 (2), 13.2g/u (2), 0.0% (2), 20.2% (2).

## decision: Profile / CR 16:00

### keep — 19/19 runs

**Varying reasoning**

- (11/19) This is the strongest carb ratio in the profile and covers the worst hyperglycemia block, but with zero carbohydrate entries it was never applied, so the 32.1 percent time above range at 16:00 local says nothing about its correctness.
- (5/19) Confirmed active in a loop reason at 16:54 local.
- (4/19) Uncertainty: complete.
- (2/19) Dependencies: this is the specific segment that the recommended carbohydrate logging for the 12:00-17:00 meal would first make assessable.
- (2/19) Dependencies: blocked pending carbohydrate logging; must not be adjusted preemptively.
- (2/19) Evidence: not exercised, with zero carbohydrate entries.
- … 2 more varying points

Points made by a single run only: 36.

Phrases used by at least half the runs: “above range” (12), “carb ratio” (10), “carbohydrate entries” (10).

Evidence cited: 16:00 (12), 32.1% (8), 19:00 (4), 16:54 (4), 18:00 (3), 20:00 (2), 17:00 (2), 22.6% (2), 162.8mg/dl (2), 19:40 (1), 18:46 (1), 17:06 (1).

## decision: Profile / CR 20:00

### keep — 19/19 runs

**Varying reasoning**

- (6/19) Uncertainty: complete.
- (5/19) Evidence: confirmed active in loop reasons at 22:16 local on 08-07 and 22:09 local on 08-21, and unused because no carbohydrate was logged.
- (4/19) Evidence: the evening rise between 20:00 and 22:00 local is modest, with means of 117.0, 120.0 and 127.6 mg/dL, and no carbohydrates were announced in this or any other window.
- (3/19) Dependencies: blocked until carbohydrate logging exists, and any evening change would additionally interact with the 22:00 to 03:00 low window.
- (3/19) Dependencies: blocked pending carbohydrate logging.
- (3/19) Uncertainty: total.
- … 6 more varying points

Points made by a single run only: 29.

Evidence cited: 03:00 (6), 22:00 (5), 23:00 (5), 20:00 (4), 22:09 (4), 127.6mg/dl (3), 22:16 (3), 18.5% (2), 0.05u (2), 240min (2), 21:00 (1), 24:00 (1).

## decision: Profile / ISF 00:00

### keep — 19/19 runs

**Varying reasoning**

- (8/19) Evidence: dynamic sensitivity is enabled with a 70 percent adjustment factor and autosens is disabled, and observed effective sensitivity ranges from 27.8 to 124.0 mg/dL per unit, so the flat 56 value is an anchor rather than the operative sensitivity.
- (5/19) The value is overwritten every cycle: observed effective sensitivity spans 124.0 mg/dL per unit at 69.8 mg/dL down to 27.8 at 245.7 mg/dL, crossing 56 near 150 to 170 mg/dL.
- (2/19) No clean ISF measurement exists because every recorded correction is contaminated by concurrent boosted SMB and temp basal, for example 0.2 units at 08-14 17:20 local followed by minus 178 mg/dL at 120 minutes where 56 mg/dL per unit predicts about minus 11.
- (2/19) Dependencies: the correct lever is the dynamic ISF adjustment factor, and changing both the anchor and the multiplier together would violate the rule against moving dependent parameters, so this stays fixed until the automation change has been evaluated.
- (2/19) Uncertainty: high, because this profile value acts as a scaling reference for the whole dynamic curve rather than as the direct correction factor, so a change would move both the weak normal-range response and the strong high-glucose response at once.
- (2/19) Changing the static value would shift the whole dynamic curve in both directions at once, weakening low-glucose safety at the same time as it moderates high-glucose aggressiveness.
- … 2 more varying points

Points made by a single run only: 53.

Phrases used by at least half the runs: “adjustment factor” (16), “dynamic sensitivity” (15), “70 percent” (14), “effective sensitivity” (11), “dynamic isf” (10).

Evidence cited: 70% (14), 124.0mg/dl (10), 124mg/dl (9), 56mg/dl (5), 27.8mg/dl (4), 178mg/dl (3), 120min (2), 245.7mg/dl (2), 5.1% (2), 246mg/dl (2), 0.2u (2), 262mg/dl (2).

## decision: Profile / target 00:00

### keep — 19/19 runs

**Varying reasoning**

- (8/19) However sampled loop target_bg values ranged from 80 to 116 mg/dL against profile targets of only 90 and 100, and both autosens target flags are false, so fork logic outside decision_inventory is modulating the effective target and a profile target edit has unproven leverage.
- (8/19) Evidence: local hours 00:00 to 03:00 carry 10.1 to 18.5 percent time below range, which would ordinarily argue for raising the overnight target.
- (4/19) Evidence: this target covers 00:00 to 08:00, a span containing both the worst overnight low hour (01:00 at 18.5 percent below range) and the best hours of the day (06:00 and 07:00 at 98.7 and 98.2 percent time in range), so a single change would affect both.
- (3/19) Uncertainty is high.
- (2/19) Dependencies: blocked until the source of loop targets below the profile value is identified.

Points made by a single run only: 45.

Phrases used by at least half the runs: “below range” (15), “18.5 percent” (12), “116 mg/dl” (11), “autosens target” (10).

Evidence cited: 18.5% (12), 116mg/dl (11), 00:00 (8), 01:00 (6), 03:00 (5), 90mg/dl (5), 08:00 (4), 10.2% (3), 106.0mg/dl (3), 04:00 (2), 07:00 (2), 10.1% (1).

## decision: Profile / target 08:00

### keep — 19/19 runs

**Varying reasoning**

- (4/19) Uncertainty: the same override problem applies, with effective targets of 80 mg/dL observed on 08-10, 08-18, 08-19 and 08-21 within this segment.
- (4/19) Evidence: this daytime target covers the safest window in the dataset, with 0.0 percent time below range at 08:00 and 09:00 local, so there is no hypoglycemia argument for raising it, and the afternoon time above range is better explained by the sensitivity curve and unannounced meals than by the target.
- (4/19) Uncertainty: high.
- (3/19) Evidence: the window covered by this target contains both the best block of the day, 04:00 to 09:00 local flat and in range, and the worst above-range block, 10:00 to 17:00, so no single target change would serve both.
- (2/19) Evidence: the daytime block covered by this target contains both the highest elevation at 16:00 local and the highest single-hour time below range at 19:00 local, a bidirectional pattern that a single target change cannot address in one direction.
- (2/19) Loop statuses in these hours report effective targets of 80, 82, 87, 90, 99, 104, 108 and 116 mg/dL, so the declared 100 mg/dL is frequently not the value in use.
- … 2 more varying points

Points made by a single run only: 41.

Phrases used by at least half the runs: “below range” (11).

Evidence cited: 08:00 (9), 80mg/dl (8), 116mg/dl (7), 100mg/dl (5), 09:00 (4), 135mg/dl (4), 0.0% (3), 32.1% (3), 19:00 (3), 16:00 (3), 108mg/dl (3), 17:00 (3).

## decision: Profile / target 23:00

### keep — 19/19 runs

**Shared reasoning**

- (13/19) Hour 23 local averages 105.7 mg/dL with 88.7 percent in range, 1.2 percent above range and 10.1 percent below range.

**Varying reasoning**

- (3/19) Uncertainty: high.
- (2/19) Uncertainty: the declared target is not the operative one, and this hour also sits downstream of the afternoon and evening insulin tail, so the target is not established as the driver.
- (2/19) Dependency: evaluate together with the 00:00 target only after the insulin tail question is resolved, and not simultaneously with any basal or DIA change.
- (2/19) No change is supported.

Points made by a single run only: 44.

Phrases used by at least half the runs: “below range” (19), “10.1 percent” (15), “105.7 mg/dl” (14), “percent below range” (13), “00 local” (11), “10.1 percent below” (11), “local hour” (10).

Evidence cited: 10.1% (15), 23:00 (15), 105.7mg/dl (14), 00:00 (11), 88.7% (6), 1.2% (5), 03:00 (4), 116mg/dl (3), 90mg/dl (2), 22:00 (2), 18.5% (2), 01:00 (1).

## decision: Profile / DIA

### keep — 19/19 runs

**Varying reasoning**

- (6/19) Evidence: DIA 10 hours is long, but shortening it is unsupported and would likely be harmful, because therapy response windows repeatedly show real glucose change still occurring at 240 and 360 minutes, for example 08-19 with minus 161 mg/dL at 240 minutes and minus 176 at 360, and 08-17 with minus 68 and minus 50.
- (5/19) Evidence: 10 hours with free_peak_oref keeps afternoon insulin counted as active into the 18:00 to 19:00 and 23:00 to 03:00 local hypoglycemia clusters and inflates the insulin-on-board readings of 4.73 and 5.935 units used to judge stacking.
- (3/19) Dependencies: shortening DIA would change insulin-on-board accounting across every other lever simultaneously and must not be combined with the planned sensitivity test.
- (3/19) Evidence: DIA is 10 hours with insulin_type free_peak_oref, but the insulin peak time is not supplied anywhere in the package, so only the tail length and not the activity curve can be assessed.
- (3/19) Dependency: this is the designated next profile candidate after the quiet-evening verification described in the profile recommendation.
- (2/19) Evidence: a 10 hour duration with a free peak insulin model is consistent with the observed long tails, where 0.05 U at 125 mg/dL preceded 68 mg/dL at 180 minutes and 57 at 240 minutes on 08-17, 0.15 U at 138 preceded 82 to 87 mg/dL on 08-12, and 0.05 U at 93 preceded 69 mg/dL on 08-10, since such small boluses cannot themselves cause those falls.
- … 4 more varying points

Points made by a single run only: 49.

Phrases used by at least half the runs: “insulin on board” (16), “10 hours” (11), “peak time” (11).

Evidence cited: 10h (13), 360min (7), 240min (6), 18:00 (4), 03:00 (3), 19:00 (3), 5.1% (3), 66mg/dl (3), 6h (3), 5.935u (3), 23:00 (2), 68mg/dl (2).

## decision: AAPS / SMB and UAM

### keep — 19/19 runs

**Shared reasoning**

- (13/19) Evidence: both components have non-null values, so verify is not applicable.

**Varying reasoning**

- (11/19) Disabling either would remove all coverage of the local 13:00 to 17:00 block that reaches 32.1 percent time above range at 16:00.
- (6/19) Evidence: with zero carbohydrate entries and COB reported as 0 in all 24 sampled loop statuses, UAM is the only mechanism providing meal coverage, and aggregate outcomes remain good at 86.0 percent time in range and 32.6 percent coefficient of variation.
- (5/19) Uncertainty: low for this decision.
- (4/19) With carb entries at 0 and carbs on board at 0 in every sampled status, UAM is the sole meal detection mechanism and SMB is the sole meal coverage mechanism, so disabling either would remove all meal coverage from a system that currently achieves 86.0 percent time in range.
- (4/19) UAM is treated strictly as unannounced-rise detection; because COB is always 0, no duplicate carbohydrate counting can occur and none is assumed.
- (3/19) With zero carbohydrate entries across 14 days, the unannounced-meal path is the only mechanism that responds to eating, and achieving 86.0 percent time in range with a mean of 121.6 mg/dL under those conditions is only possible because both are enabled.
- … 8 more varying points

Points made by a single run only: 26.

Phrases used by at least half the runs: “disabling either” (17), “non null” (12), “carbohydrate entries” (12), “above range” (11), “meal coverage” (11), “percent time” (11), “86.0 percent” (11), “zero carbohydrate entries” (11), “time in range” (11), “disabling either switch” (11).

Evidence cited: 86.0% (11), 17:00 (9), 32.1% (8), 13:00 (4), 10:00 (3), 32.6% (3), 16:00 (3), 14:00 (2), 98.7% (2), 09:00 (2), 32% (1), 121.6mg/dl (1).

## decision: AAPS / SMB activation conditions

### keep — 19/19 runs

**Shared reasoning**

- (14/19) Evidence: all five components have non-null values, so verify is not applicable.

**Varying reasoning**

- (11/19) The group is internally coherent: smb_always_enabled true makes the two carbohydrate-conditional flags inert in the current data, and smb_with_temp_target_enabled true with smb_with_high_temp_target_enabled false means microboluses are suppressed while a high temporary target runs, which occurred during the 180-minute 135 mg/dL targets on 2026-08-17 and 2026-08-18.
- (5/19) The high-temporary-target suppression setting is operative and is currently the user's only working manual brake, applied through 135 mg/dL temporary targets on 08-09, 08-17, 08-18, 08-19 and 08-20.
- (4/19) The live interaction is smb_with_high_temp_target_enabled false combined with repeated 135 mg/dL temporary targets, twice for 180 minutes on 08-17 and 08-18, which suppresses SMB during the highest above-range hours.
- (3/19) Dependencies: the two carbohydrate-conditioned flags become observable only after carbohydrate logging begins, so they must be re-examined after that step rather than changed now.
- (2/19) Dependencies: enabling microbolusing during high temporary targets would push against the dominant safety constraint of 5.1 percent time below range with two level 2 evening events, so no change is supportable; verify is not available because all five components are non-null.
- (2/19) Dependencies: enabling SMB with high temporary targets would add insulin into the constrained 17:00 to 02:00 local window and would contradict the dominant safety finding, so keep is the correct outcome despite the identified interaction.
- … 3 more varying points

Points made by a single run only: 43.

Phrases used by at least half the runs: “135 mg/dl” (18), “temporary targets” (18), “five components” (15), “smb_always_enabled true” (14), “smb_with_high_temp_target_enabled false” (12), “non null” (12), “high temporary” (10), “180 minute” (10), “mg/dl temporary targets” (10), “135 mg/dl temporary” (10).

Evidence cited: 135mg/dl (18), 180min (5), 12.8% (5), 290mg/dl (3), 15.3% (3), 5.1% (3), 100mg/dl (2), 190mg/dl (2), 108mg/dl (2), 15:24 (2), 13:30 (1), 02:00 (1).

## decision: AAPS / SMB strength and frequency

### keep — 14/19 runs

**Varying reasoning**

- (8/14) Evidence: all three components are non-null, so verify is not permissible.
- (3/14) However the configured cap does not bound delivered SMB in this build: at 08-19 16:54 local with a 0.5 U/h basal segment the 20-minute allowance implies roughly 0.17 units, yet the text records UAM High Boost enacted with SMB equals 1.6 units, and at 08-07 22:16 local standardMaxBolus 0.2 accompanies 0.4 units microbolused.
- (3/14) Crucially they are not the binding constraint: build-specific boost logic delivered 0.4 U against a 0.2 U standard cap on 2026-08-07 and an SMB of 1.6 U on 2026-08-19, and those multipliers are not exposed as configurable items in this package.
- (3/14) These values are already more conservative than AAPS defaults of 30 and 30 minutes, with a standard 3 minute interval, and no SMB interval was inferred from any remaining-time text in the loop reasons.
- (3/14) The 3-minute interval is read directly from raw_settings and not inferred from any waiting message.
- (2/14) Evidence: with basal of 0.5 to 0.8 U/h the 20-minute UAM allowance implies a base cap near 0.17 to 0.27 U, consistent with the logged standardMaxBolus of 0.2, yet delivered SMB reached 0.4 U under a boost of 1.57 and 1.6 U under UAM High Boost, so boost multipliers that are absent from the settings inventory dominate the delivered size.
- … 5 more varying points

Points made by a single run only: 47.

Phrases used by at least half the runs: “three components” (10), “high boost” (10), “non null” (8), “uam high boost” (8), “minute interval” (8), “20 minute” (7), “0.8 u/h” (7).

Evidence cited: 0.4u (11), 1.6u (10), 0.2u (8), 0.8u/h (7), 0.27u (5), 20min (3), 3min (3), 15min (2), 0.5u/h (2), 30min (2), 16:00 (2), 0.3u (2).

### change — 5/19 runs

**Varying reasoning**

- (2/5) Evidence: reason strings confirm the basal-minutes setting sets the microbolus sizing base, with 0.7 U/h basal producing standardMaxBolus 0.2 and 0.8 U/h producing standardMaxBolus 0.3 at 20 minutes; boost logic then delivered 0.4 U against a 0.2 U base and, in a UAM High Boost case on 08-19, 1.6 U with 4.73 U already on board.
- (2/5) Downstream consequences are falls of 178, 168 and 125 mg/dL after user doses of 0.65 U or less, guard predictions of -4 and -59 mg/dL with 120-minute zero temporary basals, IOB peaks of 4.73 and 5.935 U with COB 0, and evening time below range of 7.7 and 15.3 percent with minima of 41 and 42 mg/dL.
- (2/5) Only max_uam_smb_basal_minutes is proposed for change, from 20 to 15 minutes.

Points made by a single run only: 25.

Phrases used by at least half the runs: “15 minutes” (3), “cgm cadence” (3), “u/h basal” (3), “proposed for change” (3), “high boost” (3), “reason strings” (3).

Evidence cited: 1.6u (4), 15min (4), 4.73u (3), 0.2u (3), 0.4u (3), 20min (3), 59mg/dl (2), 178mg/dl (2), 0.65u (2), 0.5u/h (2), 0.7u/h (2), 5.935u (2).

## decision: AAPS / max basal and max IOB limits

### change — 17/19 runs

**Varying reasoning**

- (7/17) The maximum basal component is kept because it is inert: the effective ceiling is 4 U/h produced by the maximum daily safety multiplier of 5 applied to the highest profile basal of 0.8 U/h, shown directly by a reason string adjusting a required rate of 5.9 down to a maximum safe basal of 4, so 12 U/h is a cosmetic inconsistency rather than an active risk.
- (6/17) Uncertainty: only 24 of 6214 statuses were sampled so 5.935 U is a floor rather than a true peak, and it is unresolved whether total_insulin_u includes basal delivery, which changes estimated total daily dose between roughly 20 and 36 U per day and therefore the appropriate ceiling; the exact value must be set by the care team against the actual total daily dose.
- (5/17) Both components are non-null so verify is not permitted.
- (4/17) Both components are non-null, so verify is not applicable.
- (3/17) The 25 U insulin on board limit exceeds a full day of insulin, given 275.95 U over fourteen days and a 16.2 U per day scheduled basal, while the highest observed insulin on board was 5.935 U at 245 mg/dL and 4.73 U at 262 mg/dL, both with zero carbohydrates on board; a limit of 8 U would therefore not have blocked any dosing observed in this period while bounding the accumulation that preceded 234 to 56 mg/dL within 120 minutes on 08-14, 264 to 96 within 120 minutes on 08-19 and 206 to 53 within 180 minutes on 08-16.
- (2/17) Evidence: both components are non-null, so verify is not permissible and change is supported with explicit old and new values. max_basal_u_per_hour of 12 is retained unchanged because it is demonstrably inert: the binding ceiling observed at 08-14 19:40 local is an adjusted required rate of 5.9 reduced to maxSafeBasal 4, consistent with the 0.8 U/h peak profile basal and the daily safety multiplier of 5.0, and the highest temp basal seen anywhere is 3.6 to 4.0 U/h, so 12 U/h is never reached. max_iob_units changes from 25 U to 10 U because 25 units is roughly one full day of insulin or more against 16.2 units of scheduled basal per day and 275.95 units recorded over 14 days, and therefore never engages.
- … 7 more varying points

Points made by a single run only: 55.

Phrases used by at least half the runs: “total daily dose” (14), “insulin on board” (14), “12 u/h” (11), “non null” (10), “observed insulin” (9).

Evidence cited: 25u (13), 12u/h (11), 5.935u (11), 4u/h (10), 4.73u (10), 16.2u (8), 0.8u/h (7), 2.12u (6), 8u (6), 36u (6), 120min (5), 27.8mg/dl (5).

### keep — 2/19 runs

Points made by a single run only: 10.

Phrases used by at least half the runs: “peak observed” (2), “12 u/h” (2), “bound against peak” (1), “u/day profile basal” (1), “offers no practical” (1), “daily safety multiplier” (1), “practical protection” (1), “failure mode” (1), “iob of 25” (1), “5.9 reduced” (1), “multiplier of 5.0” (1), “never bound” (1).

Evidence cited: 12u/h (2), 25u (2), 5.935u (2), 0.8u/h (1), 16.2u (1), 275.95u (1), 4u/h (1).

## decision: AAPS / Autosens and Dynamic ISF

### keep — 13/19 runs

**Shared reasoning**

- (11/13) All five components are non-null, so verify is not applicable.

**Varying reasoning**

- (4/13) A sensitivity ratio of 1 in most statuses is a neutral current adjustment and not evidence of anything disabled; the values 0.79, 0.88, 0.91, 0.92, 0.94 and 0.98 occur on hypo-guard cycles and are consistent with the dynamic path working.
- (4/13) The configuration is internally correct: Autosens disabled with dynamic sensitivity enabled is the coherent pairing, and both Autosens target flags being false is consistent with that.
- (3/13) Sensitivity_ratio values of 0.79 to 1.0 are read as neutral or mildly reduced current adjustments computed by the fork, not as evidence that Autosens is running.
- (2/13) Uncertainty: the 70 percent factor is mathematically anchored to the profile ISF of 56 and to total daily dose, and the internal daily dose value used by the algorithm is not exposed, so the factor and the anchor cannot be evaluated separately within this package.
- (2/13) Sampled sensitivity ratios of 1, 0.98, 0.94, 0.92, 0.91, 0.88 and 0.79 are treated as neutral or dynamically derived current adjustments and are explicitly not used as evidence about whether Autosens is enabled.

Points made by a single run only: 51.

Phrases used by at least half the runs: “five components” (9), “dynamic sensitivity” (8), “non null” (8), “70 percent” (8), “effective sensitivity” (7).

Evidence cited: 70% (8), 124.0mg/dl (4), 56mg/dl (4), 124mg/dl (4), 32.1% (4), 17:00 (3), 16:00 (3), 170mg/dl (2), 262mg/dl (2), 18.5% (2), 19:00 (2), 42.5mg/dl (1).

### change — 6/19 runs

**Shared reasoning**

- (4/6) Evidence: all five components have non-null values, so verify is not permitted.

**Varying reasoning**

- (2/6) Evidence: the four switches are internally consistent, since dynamic sensitivity supersedes autosens and both autosens target switches correctly follow autosens being disabled, so none of them is proposed for change.
- (2/6) Uncertainty: medium.
- (2/6) Dependencies: this must not be changed together with profile ISF or the microbolus caps, which act on the same effective dose, and it should follow the completed max IOB observation period.

Points made by a single run only: 30.

Phrases used by at least half the runs: “adjustment factor” (5), “60 percent” (4), “five components” (4), “around the flat” (3), “reducing the factor” (3), “components have non” (3), “0.79 to 1.0” (3), “70 to 60” (3), “120 minutes” (3), “non null” (3), “27.8 mg/dl/u” (3), “low glucose” (3).

Evidence cited: 60% (4), 27.8mg/dl (4), 56mg/dl (4), 120min (3), 124.0mg/dl (3), 5.1% (3), 70mg/dl (2), 96mg/dl (2), 6h (2), 200mg/dl (2), 37.9mg/dl (2), 116mg/dl (2).

## decision: AAPS / carbohydrate absorption model

### keep — 19/19 runs

**Shared reasoning**

- (15/19) Evidence: both components have non-null values, so verify is not applicable.

**Varying reasoning**

- (7/19) Uncertainty: no observational basis exists to tune either value, and no duration is inferred from any aggregate, since the average extended carbohydrate duration field is null.
- (6/19) Both settings act only on carbohydrates-on-board decay and absorption modelling, and carbohydrates on board are zero in all 24 sampled loop statuses with zero carb entries and zero extended carb entries across 14 days, so both are entirely inert and no observation in the package can support or refute either.
- (5/19) Both settings act only when carbohydrate on board exceeds zero, and carbohydrate on board was zero in every sampled loop status across the entire 14-day period with zero carbohydrate entries recorded, so neither setting was ever exercised and neither can have contributed to any observed pattern.
- (5/19) Evidence: these two parameters govern COB decay and meal absorption modelling, and neither has been exercised once during the period. carb_entries is 0, total_carbs_g is 0.0, carb_treatment_entries is empty, extended_carb_entries is 0, average_extended_carb_duration_min is a genuine null, and cob is 0 in every sampled loop status.
- (4/19) Dependencies: these settings only become reviewable once carbohydrate logging produces real carb-on-board data, so they are held unchanged.
- (3/19) One forward-looking caution rather than a change: both become active the moment carbohydrate entry begins, and meal_max_absorption_hours of 7 combined with DIA 10 hours could sustain dosing into the 18:00 to 19:00 and 22:00 to 01:00 windows that already carry 7.7 to 18.5 percent below range.
- … 4 more varying points

Points made by a single run only: 32.

Phrases used by at least half the runs: “carbohydrate logging” (12), “non null” (12), “every sampled” (12), “duration is inferred” (11), “sampled loop” (10).

Evidence cited: 8mg/dl (4), 5min (4), 18:00 (3), 7h (3), 18.5% (2), 10h (2), 6h (2), 03:00 (1), 22:00 (1), 01:00 (1), 19:00 (1), 11:00 (1).

## profile recommendation

### basal — 13/19 runs

**Varying reasoning**

- (7/13) Keep all 17 profile rows unchanged, including all seven basal segments, the flat ISF of 56 mg/dL per unit, the five carb ratios, the three targets and the 10-hour DIA.
- (7/13) The dawn segments are validated by 95.2 to 98.7 percent time in range between 03:00 and 08:00 local with at most 1.2 percent above range.
- (4/13) Targets cannot be assessed because the effective target ranged from 80 to 116 mg/dL rather than the declared 90, 100 and 90.
- (3/13) Keep all 17 profile values unchanged for now, including the 0.5 U/h segment from 16:00, and address the low exposure through the single automation change to the UAM microbolus basal-minutes cap instead.
- (2/13) The early-night trough at 01:00 local shows 18.5 percent below range, but glucose recovers to a stable level near 105 mg/dL by 03:00 and 04:00 within the same 00:00 to 05:00 basal segment, which contradicts a sustained basal excess and points instead to carried-over insulin activity from evening dosing.
- (2/13) The 04:00 to 09:00 local window shows 95 to 99 percent time in range on the existing 0.6 to 0.8 U/h segments, which corroborates the basal level.
- … 5 more varying points

Points made by a single run only: 61.

Phrases used by at least half the runs: “below range” (11), “isf of 56” (10), “time below range” (9), “00 local” (9), “17 profile” (9), “keep all 17” (9), “0.5 u/h” (9), “carb ratios” (9), “56 mg/dl/u” (8), “10 hour” (8), “profile row” (8), “time in range” (8).

Evidence cited: 16:00 (10), 56mg/dl (10), 0.5u/h (9), 04:00 (9), 08:00 (8), 19:00 (7), 98.7% (7), 03:00 (7), 10h (7), 0.7u/h (6), 18:00 (6), 162.8mg/dl (5).

### dia — 3/19 runs

**Shared reasoning**

- (2/3) Keep all 17 profile rows unchanged for now, including the duration of insulin action of 10 hours, and verify the insulin-on-board tail hypothesis by checking whether early-evening lows persist after the maximum insulin-on-board ceiling is reduced and site reliability is confirmed.

Points made by a single run only: 19.

Phrases used by at least half the runs: “00 local” (3), “dynamic sensitivity” (3), “10 hours” (3), “17 profile” (3), “insulin on board” (3), “keep all 17” (3), “insulin action” (2), “low pattern” (2), “116 mg/dl” (2), “dia at 10” (2), “verify dia” (2), “00 to 03” (2).

Evidence cited: 10h (3), 03:00 (2), 18:00 (2), 19:00 (2), 20:00 (2), 23:00 (2), 116mg/dl (2), 04:00 (2), 56mg/dl (2), 120min (1), 178mg/dl (1), 4u/h (1).

### isf — 3/19 runs

**Shared reasoning**

- (3/3) Keep all 17 profile parameters unchanged for now, including the flat ISF of 56 mg/dL per unit, and address the sensitivity problem at the automation layer instead by discussing a reduction of dynamic_isf_adjustment_factor_percent from 70 to 60.

Points made by a single run only: 20.

Phrases used by at least half the runs: “00 local” (3), “116 mg/dl” (3), “70 percent” (3), “00 to 08” (2), “dynamic sensitivity” (2), “automation layer” (2), “profile rows unchanged” (2), “27.8 to 124.0” (2), “below range” (2), “insulin peak time” (2), “0.5 u/h” (2), “unchanged for now” (2).

Evidence cited: 116mg/dl (3), 70% (3), 56mg/dl (3), 04:00 (2), 08:00 (2), 10h (2), 0.5u/h (2), 124.0mg/dl (2), 16:00 (2), 03:00 (1), 23:00 (1), 99% (1).

## primary recommendation

### smb — 14/19 runs

**Varying reasoning**

- (5/14) Discuss tightening the maximum insulin on board ceiling as the single primary change.
- (4/14) Primary: review the max IOB ceiling as the first and only change this cycle. max_iob_units is currently 25 units while scheduled basal is roughly 16.2 units per day and the highest observed insulin on board across the sampled statuses is 5.935 units at 08-21 22:10 local, with a second peak of 4.73 units at 08-19 16:55 local.
- (3/14) Max IOB is 25 U while total insulin is approximately 19.7 U per day, so the configured ceiling exceeds a full day of insulin and cannot act as a backstop.
- (3/14) Discuss lowering the maximum insulin-on-board limit toward observed usage.
- (2/14) Observed insulin on board reached 4.73 U on 08-19 at 16:54 local and 5.935 U on 08-21 at 22:09 local, both with carbohydrates on board 0, and at the 27.8 mg/dL per unit effective sensitivity recorded in the second case that quantity represents a very large pending fall with a 10-hour DIA to unwind it.
- (2/14) It therefore provides no practical ceiling in a system that reached 41 to 56 mg/dL nadirs after documented stacking episodes on 2026-08-13, 2026-08-14, and 2026-08-19.
- … 4 more varying points

Points made by a single run only: 61.

Phrases used by at least half the runs: “insulin on board” (10), “routine dosing” (7), “maximum insulin” (7).

Evidence cited: 4.73u (10), 25u (7), 5.935u (7), 1.6u (4), 245mg/dl (4), 16.2u (4), 19:00 (3), 0.4u (3), 2.12u (3), 8u (3), 36u (3), 16:55 (2).

### isf — 3/19 runs

**Shared reasoning**

- (3/3) Primary: discuss softening the dynamic ISF adjustment factor.
- (2/3) Observed variable sensitivity is 27.8 and 37.9 mg/dL per unit at 245-262 mg/dL versus 108.4 to 124.0 at 70-95 mg/dL, so the loop is at its most aggressive exactly when glucose is highest, and that insulin then acts across a 10-hour DIA into the hours that already carry the most hypoglycemia, namely 18:00-19:00 local at 7.7 and 15.3 percent below range and 23:00-03:00 local at 10.1 to 18.5 percent.
- (2/3) The known trade-off is that it also moves the protective high value of 124 mg/dL per unit at low glucose toward the anchor, and afternoon time above range may increase in the short term; the expected net direction is still a reduction in lows, because the observed lows follow high-glucose overcorrection rather than baseline over-basal.

Points made by a single run only: 14.

Phrases used by at least half the runs: “dynamic isf adjustment” (3), “percent below range” (3), “isf adjustment factor” (3), “time above range” (3), “high glucose” (3), “applies undocumented boost” (2), “5.1 percent” (2), “one lever” (2), “37.9 and 27.8” (2), “low glucose” (2), “roughly twice” (2), “effective sensitivity” (2).

Evidence cited: 5.1% (2), 27.8mg/dl (2), 124mg/dl (2), 47mg/dl (2), 120min (2), 240min (2), 18:00 (2), 19:00 (2), 03:00 (2), 15.3% (2), 18.5% (2), 56mg/dl (2).

### safety_limits — 1/19 runs

Points made by a single run only: 5.

Phrases used by at least half the runs: “reduce the maximum” (1), “actually act” (1), “duration questions” (1), “legitimate value observed” (1), “insulin need recorded” (1), “never limited delivery” (1), “accumulation seen” (1), “sensitivity and duration” (1), “08 21 ceiling” (1), “genuine insulin need” (1), “19 and 5.935” (1), “dosing parameter” (1).

Evidence cited: 25u (1), 7u (1), 4.73u (1), 5.935u (1).

### meal — 1/19 runs

Points made by a single run only: 4.

Phrases used by at least half the runs: “carb ratio assessment” (1), “exposure which makes” (1), “absorption model prevents” (1), “glucose was already” (1), “action while carrying” (1), “00 and 22” (1), “changes no insulin” (1), “lowest risk first” (1), “ratios were never” (1), “separating an afternoon” (1), “ratio assessment blocks” (1), “days so carb” (1).

Evidence cited: 22:00 (1), 17:00 (1), 18:00 (1), 19:00 (1), 03:00 (1), 10:00 (1).

## summary

### 19 runs

**Shared reasoning**

- (19/19) Two distinct patterns dominate: elevated glucose from 09:00 to 17:00 local (peak hour 16:00, mean 162.8 mg/dL, 32.1 percent above range) and clustered hypoglycemia in two windows, 23:00 to 03:00 local (up to 18.5 percent below range at 01:00) and 18:00 to 19:00 local (7.7 and 15.3 percent below range).
- (19/19) Overall glucose average 121.6 mg/dL, time in range 86.0 percent, time above range 8.9 percent, time below range 5.1 percent, coefficient of variation 32.6 percent.
- (16/19) Fourteen days of Nightscout data with 98.7 percent CGM coverage at 5-minute cadence, 3995 valid entries, no invalid or duplicate readings, and a largest gap of 65 minutes.

**Varying reasoning**

- (10/19) Across the whole period there are zero carb entries, zero e-carb entries and carbohydrates on board reported as zero in every sampled loop status, so the system operates fully in unannounced-meal mode with UAM and SMB providing all meal coverage.
- (8/19) Dynamic ISF is active with a 70 percent adjustment factor and produces effective sensitivity between 27.8 and 124 mg/dL per unit against a flat profile ISF anchor of 56, roughly twice as strong as the profile value at high glucose.
- (7/19) Confounders present in the same days include three GLP-1 notes (08-14, 08-17, 08-20), an occlusion and pump error on 08-19, three site changes and two sensor changes.
- (5/19) No carbohydrates were logged during the entire period (0 carb entries, 0 grams, no extended carb entries), and the user-declared analysis_context contains an empty meal_strategies list, so declaration and telemetry agree that meal insulin was delivered entirely reactively by the loop.
- (4/19) The overnight and early morning window (04:00 to 08:00 local) is the most stable part of the day with 95 to 98 percent time in range.
- (3/19) Loop statuses show insulin on board reaching 4.73 U and 5.935 U against a profile basal total of 16.2 U/day, with single microboluses up to 1.6 U and temporary basal rates up to 4.0 U/h, followed by reactive 120-minute zero-basal periods with minimum guard predictions of -4 and -59 mg/dL.
- … 9 more varying points

Points made by a single run only: 28.

Phrases used by at least half the runs: “minute cadence” (19), “time below range” (19), “32.6 percent” (19), “121.6 mg/dl” (19), “fourteen days” (19), “above range” (19), “5.1 percent” (19), “86.0 percent” (19), “time in range” (19), “32.1 percent” (19), “98.7 percent” (19), “coefficient of variation” (19).

Evidence cited: 32.1% (19), 32.6% (19), 5.1% (19), 162.8mg/dl (19), 86.0% (19), 98.7% (19), 121.6mg/dl (19), 18:00 (17), 16:00 (17), 18.5% (17), 19:00 (16), 15.3% (16).

## issues

### 19 runs

**Shared reasoning**

- (16/19) Time below range of 5.1 percent exceeds the 4 percent goal and is concentrated in two clock windows: 18.5 percent at 01:00 local and 15.3 percent at 19:00 local, with 00:00, 02:00, 03:00 and 23:00 all near 10 percent.

**Varying reasoning**

- (10/19) Level-2 clusters occurred on 08-13 around 18:00 local (51, 47, 42, 45 mg/dL) and on 08-14 around 19:04-19:14 local (48, 41, 41 mg/dL).
- (9/19) The period is non-stationary, containing three GLP-1 1.25 mg doses on 08-14, 08-17 and 08-20, an occlusion with pump error on 08-19, three site changes, two sensor changes and one profile switch.
- (8/19) Profile target segments therefore cannot be evaluated as the operative control, and no target change can be justified from these data.'} {'area': 'cr', 'title': 'Carb ratios cannot be verified because no carbohydrate data exists', 'description': 'Across fourteen days there are zero carb entries, zero grams of carbohydrate, zero extended carb entries and COB reported as 0 in every sampled loop status.
- (6/19) The configured limits therefore describe the base rather than the operative ceiling, which reduces the predictability of any change to those caps.'} {'area': 'isf', 'title': 'Effective sensitivity is set by dynamic ISF, not by the profile ISF value', 'description': 'With dynamic sensitivity enabled and Autosens disabled, observed variable sensitivity spans 27.8 to 124.0 mg/dL per unit against a flat profile ISF of 56.
- (6/19) The boost multiplier is not exposed as an adjustable parameter, so reducing the UAM cap of 20 minutes may have less effect than expected.'} {'title': 'Loop targets depart from the profile target segments without a declared mechanism', 'detail': 'Profile targets are 90, 100 and 90 mg/dL, yet sampled loop targets fall to 80 mg/dL during rises on 08-10, 08-15, 08-18, 08-19 and 08-21 and rise to 116 mg/dL when a low is predicted on 08-16, although both autosens target flags are false and logged temporary targets are only 135 and 108 mg/dL.
- (5/19) Target conflict (low severity): the authoritative profile declares targets of 90, 100 and 90 mg/dL, but loop statuses report target_bg values including 80, 86, 87, 99, 104, 105, 108 and 116 mg/dL.
- … 18 more varying points

Points made by a single run only: 114.

Phrases used by at least half the runs: “time below range” (18), “insulin on board” (18), “5.1 percent” (17), “above range” (17), “15.3 percent” (17), “32.1 percent” (16), “percent above” (15), “carb ratio” (15), “temporary targets” (14), “percent above range” (14), “41 mg/dl” (14), “32.1 percent above” (13).

Evidence cited: 19:00 (17), 15.3% (17), 5.1% (17), 32.1% (16), 16:00 (16), 4% (16), 18:00 (15), 41mg/dl (14), 25u (14), 03:00 (13), 23:00 (12), 42mg/dl (12).

## step findings: data_quality

### 19 runs

**Shared reasoning**

- (18/19) CGM data are sufficient for hourly and daily pattern analysis: 3995 valid entries, 0 invalid, 0 duplicate, 0 out of period, estimated cadence 5.0 minutes, coverage 98.7 percent of 4046 expected readings, 10 gaps with a largest gap of 65 minutes.
- (17/19) Local timezone is BST at UTC plus 60 minutes, and hourly_glucose_local is a verified plus one hour shift of hourly_glucose.
- (15/19) The profile is structurally complete: 7 basal segments, 5 carb-ratio segments, 1 flat ISF segment, 3 target segments and DIA.
- (12/19) The first day (2026-08-07, 33 readings) and last day (2026-08-21, 269 readings) are partial and are excluded from daily comparisons.
- (12/19) Only a sample of telemetry is included (24 of 6214 device statuses, 40 of 2315 treatments, 24 therapy response windows).

**Varying reasoning**

- (10/19) The build is customized: reason strings contain Enhanced oref1, UAM Boost 1 and 2, UAM High Boost, prTrial, twin, antBackout and a G3 pre-UAM uncertainty hold, and effective targets appear that are not derivable from the three profile target segments.
- (9/19) Carbohydrate telemetry is entirely absent: carb_entries 0, total_carbs_g 0.0, carb_treatment_entries empty, extended_carb_entries 0.
- (5/19) Confounders inside the window: profile switch on 08-13, site changes 08-10, 08-13 and 08-17, sensor changes 08-11 and 08-21, occlusion and pump error on 08-19, and GLP-1 1.25 mg notes on 08-14, 08-17 and 08-20.
- (5/19) Scheduled basal totals 16.2 U per day, matching the profile-switch label of 16 to 2 U per day.
- (4/19) Two cross-checks against loop output: carb ratios quoted by the algorithm match the profile at the 04:00, 08:00, 16:00 and 20:00 segments, while the 00:00 to 04:00 window repeatedly reports 13.3 g per unit against the profile value of 13.0.
- (3/19) The profile is complete: all 17 profile inventory items carry concrete values, and profile_context states historical applicability is yes with the aaps_profile as authoritative source, so the profile is treated as valid for the entire period.
- … 6 more varying points

Points made by a single run only: 16.

Phrases used by at least half the runs: “10 gaps” (19), “65 minutes” (19), “98.7 percent” (19), “largest gap” (15), “3995 valid entries” (15), “profile switch” (15), “carb ratio” (13), “60 minutes” (13), “local time” (12), “one hour” (12), “33 readings” (12), “6214 device statuses” (12).

Evidence cited: 98.7% (19), 65min (19), 60min (14), 16.2u (10), 5.0min (9), 275.95u (4), 56mg/dl (3), 00:00 (3), 04:00 (3), 116mg/dl (3), 1h (2), 2% (2).

## step findings: safety_overview

### 19 runs

**Shared reasoning**

- (18/19) Time below range is 5.1 percent overall, above the usual 4 percent ceiling, while time in range is 86.0 percent and coefficient of variation 32.6 percent.
- (17/19) Hypoglycemia is clustered, not diffuse: local hour 01:00 at 18.5 percent, 19:00 at 15.3 percent, 00:00 at 11.4 percent, 03:00 at 10.2 percent, 02:00 and 23:00 at 10.1 percent, 18:00 at 7.7 percent and 22:00 at 6.6 percent.
- (17/19) Two level-2 hypoglycaemia clusters occurred: 08-13 between 17:59 and 18:14 local with 51, 47, 42 and 45 mg/dL, and 08-14 between 19:04 and 19:14 local with 48, 41 and 41 mg/dL, plus an isolated 42 mg/dL on 08-21 at 07:19 local.
- (13/19) Severe highs cluster on 2026-08-15 around 17:29-17:39 local at 286-293 mg/dL and on 2026-08-18 around 12:54-13:14 local at 285-290 mg/dL.

**Varying reasoning**

- (11/19) Confounders: GLP-1 1.25 mg on 08-14, 08-17 and 08-20; occlusion and pump error announcements on 08-19; site changes on 08-10, 08-13 and 08-17; sensor changes on 08-11 and 08-21.
- (10/19) Worst days were 08-14 (time in range 70.8 percent) and 08-18 (time in range 71.9 percent, time below range 12.8 percent).
- (7/19) Large fall amplitudes follow highs: 234 to 56 mg/dL in 120 minutes, 264 to 96 mg/dL in 120 minutes, 206 to 53 mg/dL in 180 minutes, 172 to 47 mg/dL in 240 minutes.
- (7/19) Hyperglycemia is clustered from 10:00 to 17:00 local, peaking at 16:00 with 32.1 percent above range and a mean of 162.8 mg/dL.
- (5/19) A single 42 mg/dL on 08-21 at 07:19 local occurred about two hours before a sensor change and may be an artifact.
- (5/19) Hypoglycemia is the leading safety signal.
- … 7 more varying points

Points made by a single run only: 38.

Phrases used by at least half the runs: “below range” (19), “time below range” (18), “5.1 percent” (18), “pump error” (17), “15.3 percent” (16), “occlusion and pump” (16), “insulin on board” (15), “42 mg/dl” (15), “07 19 local” (14), “percent below range” (14), “41 mg/dl” (14), “32.6 percent” (14).

Evidence cited: 5.1% (18), 4% (17), 15.3% (16), 18:00 (16), 03:00 (15), 42mg/dl (15), 07:19 (14), 19:00 (14), 41mg/dl (14), 32.6% (14), 23:00 (13), 10.2% (13).

## step findings: basal_targets

### 19 runs

**Shared reasoning**

- (15/19) The most fasting-like window, 04:00-08:00 local, is the best-controlled part of the day: averages 106.0, 104.2, 99.5, 99.5 and 110.5 mg/dL, time in range 95.8 to 98.7 percent, time below range 0.0 to 4.8 percent, and no time above range.
- (14/19) The overnight window from 23:00 to 07:00 local is flat in mean terms (105.7, 93.3, 90.6, 101.9, 104.7, 106.0, 104.2, 99.5, 99.5 mg/dL) with no sustained rise or fall, but the hypoglycemia burden is concentrated in its first hours and then disappears: 10.1, 11.4, 18.5, 10.1 and 10.2 percent below range from 23:00 to 03:00, against 3.0, 4.8, 2.5 and 1.3 percent from 04:00 to 07:00, with 95 to 99 percent in range from 04:00 to 08:00.

**Varying reasoning**

- (11/19) On targets, the profile defines 90, 100 and 90 mg/dL, but sampled effective targets span 80, 84, 86, 87, 90, 96.4, 99, 101, 104, 105, 106, 108 and 116 mg/dL.
- (9/19) The lowest segment of 0.5 U per hour from 16:00 sits under the highest glucose hours, 162.8 mg/dL at 16:00 with 32.1 percent above range and 148.9 mg/dL at 17:00 with 22.6 percent above range, while the highest evening segment of 0.7 U per hour from 19:00 sits over the worst evening hypoglycemia hour at 15.3 percent below range.
- (4/19) Some derive from user temporary targets of 135 mg/dL on 08-09, 08-17, 08-18, 08-19 and 08-20 and 108 mg/dL on 08-15, yet 80 mg/dL appears specifically on the most aggressive high glucose loops on 08-10, 08-18, 08-19 and 08-21, below the profile floor, and Autosens target adjustment is disabled in both directions.
- (3/19) Profile targets cannot be validated because effective target_bg in the sampled statuses ranges from 80 to 116 mg/dL, systematically lower at high glucose and higher at low-glucose risk, which is not explained by the three profile target segments or by the six temporary targets and not by autosens, since both autosens target flags are false.
- (3/19) The morning rise from 99.5 mg/dL at 07:00 to 148.0 mg/dL at 10:00 sits inside the highest basal segment (0.8 U/h) with zero percent below range; dawn effect and unlogged breakfast cannot be separated.
- (3/19) The dawn and early morning window is the best-controlled part of the day and gives no reason to alter the 05:00 and 06:00 basal segments.
- … 6 more varying points

Points made by a single run only: 72.

Phrases used by at least half the runs: “below range” (18), “116 mg/dl” (17), “00 local” (16), “0.5 u/h” (16), “temporary targets” (16), “above range” (15), “percent below range” (12), “90 mg/dl” (11), “fasting like” (11), “basal defect” (10), “fasting like window” (10).

Evidence cited: 16:00 (19), 116mg/dl (17), 18:00 (17), 19:00 (16), 0.5u/h (16), 08:00 (16), 04:00 (16), 03:00 (15), 23:00 (14), 06:00 (12), 05:00 (11), 90mg/dl (11).

## step findings: profile_cr_isf_dia

### 19 runs

**Shared reasoning**

- (12/19) Carb ratios of 13, 11.1, 13.2, 10.5, and 12.6 g/U cannot be evaluated because there were zero carbohydrate entries in 14 days, so no meal bolus was ever driven by a carb ratio.

**Varying reasoning**

- (9/19) ISF is a single flat 56 mg/dL per unit segment, but effective sensitivity is dynamic because dynamic_sensitivity_enabled is true with an adjustment factor of 70 percent and autosens_enabled is false.
- (7/19) Because dynamic sensitivity is enabled and autosens is disabled, the loop never used 56 for its own dosing; observed effective sensitivity ranged from 124 mg/dL/U at low glucose with low insulin on board down to 27.8 mg/dL/U at high glucose with high insulin on board, roughly twice as aggressive as the profile value in exactly the state that precedes the documented hypoglycemia clusters.
- (5/19) Carb ratio assessment is blocked.
- (5/19) DIA is 10 hours with insulin_type free_peak_oref and no peak time supplied.
- (4/19) The five carb ratio segments are confirmed active in the loop, but with zero carb entries and cob equal to 0 in every sampled status, no carb-to-insulin ratio has been exercised during the period, so the values can be neither validated nor falsified.
- (4/19) Carb ratios cannot be validated or refuted.
- … 13 more varying points

Points made by a single run only: 76.

Phrases used by at least half the runs: “carb ratio” (17), “10 hours” (16), “70 percent” (14), “dynamic sensitivity” (14), “insulin on board” (13), “10.5 and 12.6” (13), “12.6 g/u” (12), “adjustment factor” (12), “single flat” (11), “56 mg/dl/u” (11), “profile isf” (10), “carb ratios” (10).

Evidence cited: 56mg/dl (19), 10h (19), 70% (14), 12.6g/u (12), 124.0mg/dl (10), 360min (8), 124mg/dl (8), 120min (6), 245.7mg/dl (6), 27.8mg/dl (6), 240min (6), 178mg/dl (5).

## step findings: automation_smb_uam

### 19 runs

**Shared reasoning**

- (13/19) Activation conditions are internally coherent: smb_always_enabled true functionally supersedes smb_with_cob_enabled false and smb_after_carbs_enabled false, both of which are inert without carbohydrate entries.

**Varying reasoning**

- (11/19) Temporary targets of 135 mg/dL were set for 180 minutes on 2026-08-17 at 13:30 to 16:30 local and for 180 minutes on 2026-08-18 at 15:24 to 18:24 local, both inside the afternoon plateau, and on 08-17 a 0.15 unit correction at 126 mg/dL was followed by 190 mg/dL at 180 minutes.
- (9/19) These caps are nevertheless not the binding constraint, because build-specific boost logic multiplies past them: standardMaxBolus 0.2 followed by microbolusing 0.4 U on 2026-08-07, an increased SMB percentage message on 2026-08-18 with insulinReq 1.45, and a UAM high boost with SMB equal to 1.6 U on 2026-08-19 while IOB was already 4.73 U.
- (6/19) SMB and UAM are the only meal coverage present, since COB is 0 in every sampled status and no carb entries exist; no duplicate COB counting is present because UAM predictions never overlap with a non-zero COB.
- (6/19) The configured minute caps reconcile exactly with reported standardMaxBolus values: 15 minutes against 0.7 to 0.8 U/h basal gives 0.175 to 0.20 U matching a reported 0.2, and 20 minutes against 0.8 U/h gives 0.267 U matching a reported 0.3.
- (4/19) SMB and UAM are both enabled and are load-bearing: with zero carb entries they are the only mechanism providing meal coverage, so disabling either would remove all meal coverage.
- (4/19) All six AAPS groups were reproduced and every component carries a non-null value, so verify is not available for any group in this analysis.
- … 12 more varying points

Points made by a single run only: 81.

Phrases used by at least half the runs: “temporary targets” (18), “high boost” (18), “135 mg/dl” (17), “smb and uam” (14), “smb_always_enabled true” (13), “uam high boost” (13), “activation conditions” (13), “20 minutes” (11), “135 mg/dl temporary” (11), “false and smb_after_carbs_enabled” (11), “smb_with_cob_enabled false” (11), “smb_after_carbs_enabled false” (11).

Evidence cited: 135mg/dl (17), 0.4u (14), 1.6u (12), 20min (11), 0.8u/h (9), 15min (8), 180min (8), 4.73u (8), 0.2u (7), 0.27u (5), 3min (5), 13:30 (4).

## step findings: automation_sensitivity_limits

### 19 runs

**Shared reasoning**

- (14/19) The carbohydrate absorption group is entirely inert because carbohydrates on board are zero throughout; min_5m_carbimpact 8 and meal_max_absorption_hours 7 cannot be supported or refuted by any observation in this package.
- (13/19) The configured maximum basal of 12 U/h is not the binding constraint and changing it alone would have no effect: the observed clamp is 4.0 U/h, shown explicitly in a reason string as adjusted required rate 5.9 reduced to maximum safe basal 4, which equals the maximum daily safety multiplier of 5.0 times the peak profile basal of 0.8 U/h.

**Varying reasoning**

- (11/19) Autosens is disabled while dynamic sensitivity is enabled with the oref1 sensitivity algorithm, which is a coherent pairing; the non-unity sensitivity ratios of 0.79, 0.88, 0.91, 0.92, 0.94 and 0.98 therefore arise from the dynamic path, and ratio 1 elsewhere is a neutral current adjustment rather than a disabled feature.
- (11/19) Autosens is disabled while dynamic sensitivity is enabled at a 70 percent adjustment factor, with both autosens target flags false.
- (3/19) Effective sensitivity spans 27.8 to 124.0 mg/dL/U around a flat profile ISF of 56 mg/dL/U, so the running sensitivity is roughly twice as strong as the profile above 200 mg/dL and roughly half as strong below 100 mg/dL.
- (3/19) Observed sensitivity_ratio values of 1.0, 0.98, 0.94, 0.92, 0.91, 0.88, and 0.79 are treated as neutral or restraining current adjustments, not as evidence about the autosens switch; the 0.79 value on 2026-08-16 accompanied a 120-minute zero temporary basal, showing the sensitivity layer does restrain dosing at times.
- (2/19) On limits, max_basal_u_per_hour of 12 U/h never binds because the effective ceiling is set by max_daily_safety_multiplier of 5 applied to the largest basal of 0.8 U/h, which produced the observed maxSafeBasal of 4 U/h reached on 08-14. max_iob_units of 25 U is approximately 1.27 times the observed 14-day mean daily bolus insulin and was never approached, since peak observed insulin on board was 5.94 U, so it has never engaged and could not have limited any observed event.
- (2/19) Importantly, max_basal of 12 U/h is not the binding constraint: the logs show adj. req. rate 5.9 to maxSafeBasal 4 on 2026-08-14 and enacted rates of 3.2, 3.6 and 4.0 U/h, so the real ceiling comes from max_daily_safety_multiplier of 5 times the maximum profile basal of 0.8 U/h, equal to 4.0 U/h, with current_basal_safety_multiplier of 6 times 0.7 U/h giving 4.2 U/h.
- … 3 more varying points

Points made by a single run only: 102.

Phrases used by at least half the runs: “dynamic sensitivity” (17), “12 u/h” (16), “carbohydrate absorption” (16), “profile basal” (14), “autosens target” (14), “70 percent” (14), “insulin on board” (13), “carbohydrate absorption group” (11), “0.8 u/h” (11), “min_ m_carbimpact” (10), “basal of 0.8” (10).

Evidence cited: 12u/h (16), 70% (14), 25u (14), 4u/h (13), 5.935u (12), 0.8u/h (11), 27.8mg/dl (8), 4.0u/h (6), 16.2u (6), 8mg/dl (5), 2.12u (5), 5min (5).

## step findings: meal_bolus_strategy

### 19 runs

**Shared reasoning**

- (19/19) The user declaration in aaps_profile.analysis_context is present and timestamped 2026-08-21T21:08:10Z, with meal_strategies as an empty list, period_exceptions null and strategy_stable_for_period null.

**Varying reasoning**

- (11/19) Third, hypoglycaemia followed by a large unlogged rebound: 141 to 71 at 60 minutes to 225 at 120 minutes on 08-12, and 47 at 240 minutes to 204 at 360 minutes on 08-13.
- (10/19) There is therefore no declared prebolus value, no declared immediate-bolus percentage and no declared e-carb amount, offset or duration to reproduce, and because strategy_stable_for_period is not true, nothing here may be treated as a representative declaration for the period.
- (9/19) There is a late-morning rise from 110.5 mg/dL at 08:00 local to 148.0 at 10:00 with 20.2 percent above range, and a dominant afternoon rise from 135.0 at 13:00 to 162.8 at 16:00 with 32.1 percent above range, followed by the recurring trough at 19:00 local.
- (9/19) All 24 therapy response windows are correction boluses with extended carbohydrates false;
- (5/19) Declared strategy and observed execution are consistent with each other: the declaration is empty and execution is fully unannounced.
- (3/19) Individual windows show the same unannounced shape, for example 100 to 188 mg/dL within 60 minutes after 0.2 U on 08-14 and 189 to 206 mg/dL within 120 minutes after 0.35 U on 08-21.
- … 17 more varying points

Points made by a single run only: 76.

Phrases used by at least half the runs: “null and strategy_stable_for_period” (19), “response windows” (17), “immediate bolus” (17), “immediate bolus percentage” (15), “strategy_stable_for_period is null” (14), “therapy response” (14), “240 minutes” (13), “120 minutes” (13), “24 therapy response” (13), “therapy response windows” (13), “aaps_profile analysis_context” (13), “observed execution” (11).

Evidence cited: 0.2u (14), 120min (13), 240min (13), 60min (10), 10:00 (7), 180min (7), 16:00 (7), 360min (7), 2.4u (7), 19:00 (6), 17:20 (6), 17:00 (6).

## step findings: meal_ecarbs_absorption

### 19 runs

**Shared reasoning**

- (13/19) No extended carbohydrate evidence exists in the package. extended_carb_entries is 0, average_extended_carb_duration_min is null, carb_treatment_entries is an empty array and is_extended_carbs is false in all 24 therapy response windows.
- (12/19) E-carbs are not treated as equivalent to a pump extended bolus: e-carbs declare carbohydrate arriving over time to the absorption model, whereas an extended bolus delivers insulin over time, and neither is evidenced here.

**Varying reasoning**

- (9/19) No e-carb amount, start offset, duration, or observed action time exists to assess, and no duration is inferred from any aggregate.
- (7/19) There are zero extended carb entries, the average extended carb duration is null, every therapy response window is flagged as not extended carbs, and the carb treatment entries list is empty.
- (6/19) No e-carb amount, start offset or duration can therefore be assessed and none is proposed, and no duration is inferred from any aggregate average.
- (5/19) Indirect evidence of prolonged rises exists, for example the 2026-08-14 window rising 135 mg/dL at 240 minutes and remaining 131 mg/dL above start at 360 minutes, and the afternoon plateau failing to return to baseline, but slow absorption is only one candidate explanation alongside sequential unannounced eating, GLP-1 dosing on 08-14, 08-17, and 08-20 altering gastric emptying, SMB suppression under the 180-minute high temporary targets on 08-17 and 08-18, and the 08-19 occlusion.
- (3/19) The absorption parameters min_5m_carbimpact of 8 mg/dL per 5 minutes and meal_max_absorption_hours of 7 governed nothing during the period because COB was zero in all sampled statuses.
- (3/19) No extended carbohydrate assessment is possible.
- … 2 more varying points

Points made by a single run only: 50.

Phrases used by at least half the runs: “pump extended” (19), “start offset” (19), “amount start offset” (18), “extended carbohydrate” (16), “carbohydrate entries” (13), “action time” (13), “extended bolus” (13), “average_extended_carb_duration_min is null” (12), “therapy response” (12), “extended carbohydrates” (12), “carb amount start” (12), “pump extended bolus” (12).

Evidence cited: 8mg/dl (8), 5min (8), 7h (6), 17:00 (5), 360min (4), 16:00 (3), 12:00 (3), 10h (3), 08:00 (2), 18:00 (2), 18.5% (2), 19:00 (2).

## step findings: synthesis_plan

### 19 runs

**Varying reasoning**

- (10/19) A contradiction audit against aaps_profile, profile_context and decision_inventory produced three corrections to earlier reasoning.
- (6/19) All six AAPS groups have non-null components, so verify is unavailable and every AAPS decision is change or keep.
- (5/19) First, the early-night trough was initially attributable to the 00:00 basal segment, but the recovery to a stable level by 03:00 and 04:00 within the same 00:00 to 05:00 segment contradicts a sustained basal excess, so that hypothesis is downgraded.
- (5/19) Competing explanations were compared.
- (4/19) The daytime highs from 09:00 to 17:00 local are best explained by fully reactive UAM coverage of unannounced meals, not by the 0.5 U/h basal at 16:00; raising that basal is rejected because the same insulin would land in the 18:00 and 19:00 window that already carries 7.7 and 15.3 percent time below range.
- (4/19) Day-level confounders are datable and must not be averaged in: Occlusion and Pump Error on 08-19, temporary targets of 135 mg/dL on 08-17 and 08-18 that suppress SMB, a site change on 08-10, 08-13 and 08-17, a sensor change on 08-11 and 08-21, a profile switch on 08-13, and GLP-1 1.25 mg notes on 08-14, 08-17 and 08-20 with a roughly three-day cadence.
- … 10 more varying points

Points made by a single run only: 140.

Phrases used by at least half the runs: “competing explanations” (14), “dynamic sensitivity” (14), “contradiction audit” (12), “basal segment” (11), “aaps_profile profile_context” (11), “profile_context and decision_inventory” (11), “10 hour” (11), “audit against aaps_profile” (10), “insulin on board” (10), “0.5 u/h” (10), “00 basal” (10), “high glucose” (10).

Evidence cited: 16:00 (15), 19:00 (14), 03:00 (12), 18:00 (12), 0.5u/h (10), 25u (9), 04:00 (8), 00:00 (7), 5.935u (7), 23:00 (6), 4u/h (6), 09:00 (6).

## meal strategy

### 19 runs

**Shared reasoning**

- (14/19) The user declaration in aaps_profile.analysis_context is present and user-sourced, declared at 2026-08-21T21:08:10Z, but contains an empty meal_strategies list with period_exceptions null and strategy_stable_for_period null, so no declared prebolus minutes, immediate bolus percentage or extended-carb values exist and the declaration cannot be treated as representative for the period.

**Varying reasoning**

- (10/19) The declaration and the telemetry agree: all 24 therapy response windows are correction boluses with is_extended_carbs false, representative treatments contain only temp basals and correction boluses, 22 of 24 user doses are between 0.05 and 0.65 U, and carb_entries is 0 with COB 0 in every sampled status, so meals are handled entirely by UAM.
- (8/19) Observed execution is therefore fully reactive, with the daytime plateau from 10:00 to 17:00 local reaching 162.8 mg/dL at 16:00 with 32.1 percent above range, covered by boosted UAM SMB and temporary basal into a dynamic sensitivity of 27.8 to 42.5 mg/dL/U, producing insulin-on-board up to 5.94 U and low glucose concentrated at 18:00 to 19:00 and 22:00 to 03:00 local.
- (7/19) Keep SMB and UAM enabled throughout, since they are the only meal mechanism in use.
- (6/19) The excursion shape is well supported by 98.7 percent CGM coverage over 14 days: the midday to afternoon pattern rises from 12:00 local, peaks at 16:00 local at 162.8 mg/dL with 32.1 percent above range, and resolves over roughly six to seven hours into the 18:00 to 19:00 local hypoglycemia cluster at 7.7 and 15.3 percent below range.
- (5/19) Defer extended carbohydrate entries entirely until ordinary carbohydrate entries with six-hour follow-through exist, since absorption cannot be judged without them and extended carbohydrate entries are a carbohydrate-model construct rather than a pump extended bolus.
- (3/19) The consequence is visible in three recurring shapes across the 24 therapy response windows: under-dosed unannounced intake, such as 0.2 units at 100 mg/dL on 08-14 followed by 235 mg/dL at four hours; late high-glucose corrections that crash, such as 0.2 units at 234 mg/dL on 08-14 falling to 56 mg/dL within two hours and preceding the 41 to 48 mg/dL cluster; and unlogged rescue rebounds, such as 141 to 71 to 225 mg/dL within two hours on 08-12.
- … 6 more varying points

Points made by a single run only: 106.

Phrases used by at least half the runs: “immediate bolus percentage” (19), “smb and uam” (16), “response windows” (16), “therapy response” (14), “below range” (13), “therapy response windows” (13), “24 therapy response” (12), “00 local” (11), “carb ratio” (11), “uam enabled” (11), “prebolus timing” (11), “null and strategy_stable_for_period” (11).

Evidence cited: 18:00 (13), 16:00 (10), 19:00 (10), 0.2u (10), 32.1% (8), 162.8mg/dl (8), 15.3% (6), 17:00 (6), 10:00 (6), 240min (6), 120min (6), 03:00 (5).
