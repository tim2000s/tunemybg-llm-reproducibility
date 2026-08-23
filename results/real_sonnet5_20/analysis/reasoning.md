# Reasoning analysis — claude-sonnet-5 (20 runs, `real_sonnet5_20`)

Each model rationale is split into sentences; sentences making the same point across runs are grouped. **Shared** = the point appears in at least 60% of the runs in that group; **varying** = it appears in some runs but not most. Counts are runs, not sentences. 'Evidence cited' lists the numbers and times the model quoted, with the number of runs quoting each.

## decision: Profile / basal 00:00

### keep — 20/20 runs

**Varying reasoning**

- (4/20) The 00:00-02:00 hypoglycemia risk resolves within a few hours on the same or adjacent segment, more consistent with an IOB/correction tail than an excessive 00:00 rate; no isolated evidence of a rate defect.
- (3/20) Hour 0 local shows elevated time-below-range (18.5%), but this more plausibly reflects residual IOB from evening correction boluses within the 10-hour DIA window than excess basal at this rate.
- (2/20) Overnight time-below-range is elevated (10-18.5% across hours 0-3 local), but this is confounded by possible residual insulin-on-board from evening corrections under the 10-hour DIA and by unlogged carbohydrate intake; no isolated evidence implicates the basal rate itself.
- (2/20) Uncertainty: cannot separate basal-too-high from IOB carryover with current data.
- (2/20) Dependency: profile.dia and evening correction timing.

Points made by a single run only: 26.

Phrases used by at least half the runs: “time below range” (15).

Evidence cited: 18.5% (9), 11.4% (5), 00:00 (5), 02:00 (3), 03:00 (2), 10h (1), 23:00 (1), 21:00 (1), 90mg/dl (1), 57mg/dl (1), 04:00 (1), 07:00 (1).

## decision: Profile / basal 05:00

### keep — 20/20 runs

**Varying reasoning**

- (8/20) Hours 04:00-06:00 local show strong time in range (95.2%-97.5%) with low variability, providing no evidence of a defect in this segment.
- (5/20) This window (hour 4-5 local) shows strong performance (time-in-range 95.2-95.8%, low time-below-range); no evidence supports a change.
- (3/20) No evidence supports a change.
- (2/20) Evidence: hourly_glucose_local hours 4-5.

Points made by a single run only: 11.

Phrases used by at least half the runs: “time in range” (16).

Evidence cited: 97.5% (5), 95.2% (5), 06:00 (4), 04:00 (4), 05:00 (3), 0% (2), 99% (2), 98.7% (2), 07:00 (1), 08:00 (1), 95% (1), 98% (1).

## decision: Profile / basal 06:00

### keep — 20/20 runs

**Varying reasoning**

- (3/20) Hour 06:00-07:00 local shows the best time in range of the day (97.5%-98.7%), providing no evidence supporting a change to this segment.
- (3/20) Local hour 6 is the best-performing hour of the day (98.7% time-in-range, 99.5 mg/dL average), directly supporting this segment as currently effective.
- (2/20) Hours 6-7 local show the highest time-in-range in the dataset (97.5-98.7%), a positive pattern with no evidence of a defect at this rate.
- (2/20) Same dawn-window evidence as the 05:00 segment shows strong control with no indication of a defect.
- (2/20) Uncertainty: cannot separate basal adequacy from meal effect without carb data.
- (2/20) Dependency: profile.cr.08_00, meal logging.

Points made by a single run only: 16.

Phrases used by at least half the runs: “time in range” (12).

Evidence cited: 98.7% (11), 06:00 (5), 05:00 (3), 07:00 (2), 10:00 (2), 99.5mg/dl (2), 97.5% (1), 148.0mg/dl (1), 148mg/dl (1), 99% (1), 110.5mg/dl (1), 09:00 (1).

## decision: Profile / basal 10:00

### keep — 20/20 runs

**Varying reasoning**

- (2/20) Dependency: aaps.core.smb_activation and Temporary Target pattern.

Points made by a single run only: 29.

Evidence cited: 10:00 (4), 08:00 (3), 16:00 (3), 12:00 (2), 135mg/dl (2), 17:00 (2), 0.8u/h (2), 09:00 (1), 32.1% (1), 162.8mg/dl (1), 16.6% (1), 148.0mg/dl (1).

## decision: Profile / basal 16:00

### keep — 19/20 runs

**Varying reasoning**

- (2/19) Coincides with the single worst hyperglycemia hour in the dataset (32.1% time-above-range), but three competing explanations (basal shortfall, unlogged meals, temporary-target SMB suppression on 2026-08-18) remain unresolved; flagged as the top priority for reassessment once carbohydrate logging is available.
- (2/19) This segment coincides with the day's peak time-above-range hour (32.1%), but meal timing and temporary-target SMB suppression are equally plausible explanations that have not been separated; changing this without carb data risks masking a different root cause.
- (2/19) Evidence: hourly_glucose_local hour 15-16; representative_loop_statuses 2026-08-14T18:40; dependency: basal_targets, automation_sensitivity_limits.

Points made by a single run only: 22.

Phrases used by at least half the runs: “time above range” (15).

Evidence cited: 32.1% (14), 162.8mg/dl (4), 16:00 (4), 135mg/dl (2), 4u/h (1), 5.9u/h (1), 10.5g/u (1).

### change — 1/20 runs

Points made by a single run only: 2.

Phrases used by at least half the runs: “current_basal_safety_multiplier derived ceiling” (1), “fully excluded” (1), “time above range” (1), “dynamic isf variability” (1), “event uncertainty unlogged” (1), “avoid confounding results” (1), “tested in isolation” (1), “severe hyperglycemia event” (1), “cannot be fully” (1), “exceeded the current_basal_safety_multiplier” (1), “ceiling during severe” (1), “highest time above” (1).

Evidence cited: 32.1% (1), 162.8mg/dl (1).

## decision: Profile / basal 18:00

### keep — 20/20 runs

**Varying reasoning**

- (4/20) Covers hours 18:00-19:00 local showing declining glucose from the afternoon peak with reasonable time-in-range (80.4%), no clear defect signal.
- (3/20) Hour 18 local shows moderate time-in-range (80.4%) without a clearly isolated pattern; insufficient evidence for change.
- (2/20) This transitional evening segment shows moderate control with no strong signal of insufficiency or excess in the hourly data.
- (2/20) Evidence: hourly_glucose_local hour 17-19; dependency: basal_targets, profile_cr_isf_dia.

Points made by a single run only: 15.

Evidence cited: 19:00 (4), 18:00 (3), 80.4% (3), 7.7% (2), 11.9% (2), 124.2mg/dl (1), 15.3% (1), 6.6% (1), 16:00 (1).

## decision: Profile / basal 19:00

### keep — 20/20 runs

**Varying reasoning**

- (5/20) Hour 19 shows the highest evening time below range (15.3%), but this plausibly reflects overlap with afternoon correction-bolus IOB tails given the long DIA rather than this basal segment itself.
- (2/20) Same uncertainty as the 18:00 segment regarding insulin-on-board tail versus basal magnitude; no isolated evidence supports a change to this segment specifically.
- (2/20) Evidence: hourly_glucose_local hour 19-20.

Points made by a single run only: 17.

Evidence cited: 15.3% (6), 19:00 (4), 18:00 (2), 00:00 (2), 01:00 (2), 92% (2), 24:00 (1), 16:00 (1), 88.6% (1), 21:00 (1), 23:00 (1).

## decision: Profile / CR 00:00

### keep — 20/20 runs

**Shared reasoning**

- (16/20) Zero carbohydrate entries exist in the entire 14-day period, so no carb-ratio segment can be validated against actual meal response.

**Varying reasoning**

- (2/20) Evidence: treatment_summary carb_entries equals zero.
- (2/20) No change is supportable from this data.

Points made by a single run only: 8.

Phrases used by at least half the runs: “carbohydrate entries exist” (19), “zero carbohydrate entries” (14), “carb ratio” (13), “14 day” (12).

## decision: Profile / CR 04:00

### keep — 20/20 runs

**Varying reasoning**

- (3/20) Same carbohydrate-logging gap as all other carb-ratio segments; cannot support a change without meal-linked glucose response data.
- (3/20) No carbohydrate entries exist to test this ratio against observed glucose response.
- (3/20) Same carbohydrate-logging blocker as all CR segments; no meal-linked data exists to test this value.
- (2/20) No carbohydrate entries exist anywhere in the 14-day period, making it impossible to validate any carb ratio segment against actual meal response.
- (2/20) Zero carbohydrate entries exist in the entire dataset, so no meal-response evidence is available to validate or challenge this ratio.
- (2/20) Same as the 00:00 segment: zero carbohydrate entries block any validation of this ratio.
- … 2 more varying points

Points made by a single run only: 6.

Phrases used by at least half the runs: “carbohydrate entries” (12).

Evidence cited: 00:00 (1).

## decision: Profile / CR 08:00

### keep — 20/20 runs

**Varying reasoning**

- (3/20) Same carbohydrate-logging gap as all other carb-ratio segments; cannot support a change without meal-linked glucose response data.
- (2/20) This segment overlaps a recurring morning rise pattern, but with zero carb entries the rise cannot be attributed to this carb ratio versus an unlogged meal or automation suppression.
- (2/20) Zero carbohydrate entries exist in the entire dataset, so no meal-response evidence is available to validate or challenge this ratio, despite this segment overlapping the recurring morning rise pattern.

Points made by a single run only: 18.

Evidence cited: 06:00 (1), 10:00 (1), 20.2% (1), 07:00 (1), 13:00 (1).

## decision: Profile / CR 16:00

### keep — 20/20 runs

**Varying reasoning**

- (3/20) This segment covers the peak daytime hyperglycemia window, increasing the value of resolving the carbohydrate-logging gap here specifically, but no meal-linked evidence currently exists to support a change.

Points made by a single run only: 22.

Evidence cited: 135mg/dl (1), 08:00 (1), 16:00 (1).

## decision: Profile / CR 20:00

### keep — 20/20 runs

**Varying reasoning**

- (3/20) Same blocking data gap as all carb ratio segments: zero logged carbohydrate entries prevent any meal-response validation.
- (3/20) No carbohydrate entries exist to test this ratio against observed evening glucose response.
- (2/20) Zero carbohydrate entries exist in the entire dataset, so no meal-response evidence is available to validate or challenge this ratio.
- (2/20) Same blocking reason: no carbohydrate entries exist to validate this ratio.
- (2/20) Evidence: treatment_summary carb_entries equals zero.

Points made by a single run only: 13.

Phrases used by at least half the runs: “carbohydrate entries” (13), “carbohydrate entries exist” (10).

## decision: Profile / ISF 00:00

### keep — 20/20 runs

**Varying reasoning**

- (2/20) This flat value matches a declared FLAT ISF strategy noted in a mid-period profile switch event.
- (2/20) Evidence: representative_loop_statuses variable_sens values; smb_settings dynamic_isf_adjustment_factor_percent=70.
- (2/20) Dependency: aaps.core.sensitivity.
- (2/20) Dependency: automation_sensitivity_limits and DIA.

Points made by a single run only: 28.

Phrases used by at least half the runs: “dynamic isf” (19), “effective sensitivity” (13).

Evidence cited: 178.7mg/dl (8), 70% (7), 124mg/dl (3), 178.6mg/dl (1), 179mg/dl (1), 144.8mg/dl (1).

## decision: Profile / target 00:00

### keep — 20/20 runs

**Varying reasoning**

- (3/20) Overnight time-below-range is elevated at hours 0-1 local, but the evidence points to residual correction-bolus IOB rather than the target level itself, since hours 3-7 local (same target segment) show strong time-in-range (89-98.7%).
- (2/20) The overnight hypoglycemia pattern at hours 00:00-02:00 local resolves by hours 03:00-07:00 local under the same or a closely related target, suggesting residual insulin-on-board tail rather than the target value as the driver.
- (2/20) This tight overnight target plausibly interacts with the observed overnight time-below-range, but is confounded by correction-bolus timing and cannot be isolated as the cause.

Points made by a single run only: 18.

Evidence cited: 98.7% (1), 03:00 (1), 00:00 (1), 02:00 (1), 07:00 (1).

## decision: Profile / target 08:00

### keep — 20/20 runs

**Varying reasoning**

- (2/20) This daytime target window includes both well-controlled morning hours and the worst afternoon hyperglycemia, a range too broad to attribute to the target value itself without separating meal, temporary-target, and basal effects.
- (2/20) Daytime hyperglycemia overlaps with multiple Temporary Target overrides to ~135 mg/dL on several days, which confounds assessment of whether the baseline 100 mg/dL target itself needs adjustment.
- (2/20) Daytime hyperglycemia in this window is more plausibly linked to unlogged meals, basal step-down, or SMB-suppression during high temp targets than to the target value itself; no isolated evidence implicates this setting.
- (2/20) Daytime highs are better explained by unlogged meal effects and reactive UAM dosing than by this target value; no isolated evidence supports a change.
- (2/20) Evidence: hourly_glucose_local hours 8-17.

Points made by a single run only: 15.

Evidence cited: 135mg/dl (4), 100mg/dl (2), 10mg/dl (1), 290mg/dl (1).

## decision: Profile / target 23:00

### keep — 20/20 runs

**Varying reasoning**

- (3/20) Same rationale as the 00:00 target segment; this transition boundary is not implicated by the available evidence.
- (2/20) No evidence links this target segment to observed patterns; overnight time-below-range is better explained by the evening correction-stacking hypothesis than by this target value.
- (2/20) No specific evidence isolates this late-night target segment as a driver of the observed overnight hypoglycemia pattern, which is more plausibly linked to IOB carryover.
- (2/20) Evidence: hourly_glucose_local hour 23 (88.6% time-in-range, some lows).

Points made by a single run only: 14.

Evidence cited: 00:00 (7), 88.6% (1), 23:00 (1).

## decision: Profile / DIA

### keep — 20/20 runs

**Varying reasoning**

- (2/20) This value is plausible for the declared insulin type; observed insulin-on-board stacking is a candidate contributor to the hypo/hyper oscillation, but unlogged meals remain an equally plausible explanation, so no isolated evidence supports a specific DIA change.

Points made by a single run only: 31.

Evidence cited: 360min (6), 25u (2), 6h (2), 240min (1), 10h (1), 120min (1), 5.94u (1), 19.7u (1).

## decision: AAPS / SMB and UAM

### keep — 20/20 runs

**Varying reasoning**

- (3/20) With zero carbohydrate logging throughout the period, UAM is the only available mechanism for detecting and responding to glucose rises; both settings are functioning as the sole meal-adjacent dosing pathway and no evidence supports disabling either.
- (2/20) Both are enabled and behaving as expected, with carbohydrates-on-board consistently at zero and no evidence of duplicate carbohydrate counting; unannounced-meal supplementation appears to be functioning as the sole meal-coverage mechanism given the absence of carbohydrate logging.
- (2/20) SMB and UAM are functioning as the intended fallback dosing mechanism given zero carbohydrate logging; loop reasons consistently show COB: 0 with active UAM behavior, and no internal defect was found.

Points made by a single run only: 20.

## decision: AAPS / SMB activation conditions

### keep — 20/20 runs

**Varying reasoning**

- (3/20) Evidence: representative_events Temporary Target entries on 2026-08-17 and 2026-08-18; hourly_glucose_local hours 13-16.
- (2/20) smb_with_cob_enabled and smb_after_carbs_enabled are inert given zero COB throughout the period, not a defect. smb_with_high_temp_target_enabled=false correlates with SMB suppression during some but not all high-glucose afternoon days with an active 135 mg/dL Temporary Target; this correlation does not isolate cause from the basal step-down or possible unlogged meals occurring on non-Temporary-Target high-glucose days, so a change is not yet supported.
- (2/20) Dependency: meal_bolus_strategy and basal.16_00.
- (2/20) These settings are consistent with a no-carb-logging workflow.

Points made by a single run only: 27.

Phrases used by at least half the runs: “smb_with_high_temp_target_enabled false” (13), “135 mg/dl” (12), “temporary targets” (12), “135 mg/dl temporary” (11).

Evidence cited: 135mg/dl (12), 16:00 (1).

## decision: AAPS / SMB strength and frequency

### keep — 20/20 runs

**Varying reasoning**

- (2/20) Observed SMB dose sizes and frequency in representative_treatments and therapy_response_windows show no evidence of runaway or insufficient delivery relative to these limits; no change is supported.

Points made by a single run only: 24.

Evidence cited: 0.35u (2), 2.4u (1), 0.5u (1), 5min (1).

## decision: AAPS / max basal and max IOB limits

### keep — 20/20 runs

**Varying reasoning**

- (2/20) Neither limit is approached at any point in the 14-day period (peak enacted rate approximately 4 U/h, peak IOB 5.935 U), so these are not a binding constraint on any observed episode.
- (2/20) Observed maximum enacted rate (4 U/h) and peak IOB (5.935 U) remain far below these ceilings, indicating the limits are not constraining current dosing and are not implicated in the observed excursions.
- (2/20) Evidence: representative_loop_statuses 2026-08-14T18:40 maxSafeBasal field; dependency: basal_targets, automation_sensitivity_limits.

Points made by a single run only: 27.

Evidence cited: 5.935u (11), 4u/h (10), 25u (3), 5.94u (3), 5.9u (2), 16:00 (2), 4.8u/h (1), 16u (1), 12u/h (1), 4.0u/h (1), 19:00 (1), 19.7u (1).

## decision: AAPS / Autosens and Dynamic ISF

### keep — 20/20 runs

**Varying reasoning**

- (3/20) Autosens disabled alongside Dynamic ISF enabled is an internally consistent, non-conflicting configuration; observed sensitivity_ratio values near 1.0 reflect a neutral adjustment layer distinct from the wider variable_sens swings produced by Dynamic ISF, and no evidence indicates a conflict or malfunction.
- (3/20) Autosens disabled alongside Dynamic ISF enabled is a coherent intentional pairing, not a conflict.

Points made by a single run only: 35.

Phrases used by at least half the runs: “dynamic isf” (15).

Evidence cited: 70% (5), 100% (1), 56mg/dl (1), 178.7mg/dl (1).

## decision: AAPS / carbohydrate absorption model

### keep — 20/20 runs

**Varying reasoning**

- (3/20) Carbohydrates-on-board is zero in every sampled loop status because no carbohydrate entries exist in the period, so this model is functionally untested and no evidence-based change can be supported.
- (2/20) This model cannot be validated because zero carbohydrate entries exist in the period;
- (2/20) Evidence: treatment_summary carb_entries=0; therapy_response_windows all is_extended_carbs=false.

Points made by a single run only: 20.

Phrases used by at least half the runs: “carbohydrate entries” (12).

## profile recommendation

### basal — 14/20 runs

**Varying reasoning**

- (4/14) Keep all current basal segments unchanged for now, including the 10:00-16:00 and 16:00 segments that coincide with the largest recurring afternoon hyperglycemia, because a plausible unlogged meal effect has not been ruled out.
- (3/14) Overnight (00:00-02:00) and evening (18:00-19:00) hours show elevated time below range, but therapy_response_windows and representative_loop_statuses show correction-bolus IOB tails coinciding with these same windows, making basal excess and IOB carryover indistinguishable with current data.
- (2/14) Keep all current basal segments unchanged, including the 16:00 segment implicated in the afternoon hyperglycemia pattern and the automation safety-ceiling interaction, until carbohydrate context is available to separate meal effects from basal effects.

Points made by a single run only: 30.

Phrases used by at least half the runs: “basal segments unchanged” (12), “unchanged for now” (9), “unlogged meals” (8).

Evidence cited: 16:00 (12), 10:00 (6), 00:00 (6), 19:00 (4), 0.5u/h (4), 02:00 (3), 18:00 (2), 17:00 (2), 32.1% (2), 162.8mg/dl (2), 12u/h (1), 0.8u/h (1).

### target — 3/20 runs

**Shared reasoning**

- (2/3) Keep the current target segments (90 mg/dL overnight and 23:00, 100 mg/dL daytime) unchanged for now, since the overnight hypoglycemia pattern appears more consistent with a delayed tail effect from evening correction dosing and the long duration of insulin action than with the target itself, and the basal rate is already at its daily minimum during the affected hours.

Points made by a single run only: 6.

Phrases used by at least half the runs: “time below range” (3), “unchanged for now” (3), “target segments” (3), “90 mg/dl” (3), “target segments unchanged” (2), “local time below” (2), “overnight hypoglycemia” (2), “long duration” (2), “changing the target” (2), “correction dosing” (2), “insulin action” (2), “duration of insulin” (2).

Evidence cited: 90mg/dl (3), 23:00 (2), 08:00 (1), 100mg/dl (1), 03:00 (1), 00:00 (1), 0.6u/h (1), 18.5% (1).

### dia — 2/20 runs

Points made by a single run only: 4.

Phrases used by at least half the runs: “10 hour dia” (2), “correction boluses” (2), “hypoglycemia cluster” (1), “hours after correction” (1), “decline continuing hours” (1), “uam boost event” (1), “post correction glucose” (1), “isolated extreme uam” (1), “correction glucose decline” (1), “one competing explanation” (1), “dia alone” (1), “therapy response windows” (1).

Evidence cited: 6h (1), 360min (1).

### cr — 1/20 runs

Points made by a single run only: 3.

Phrases used by at least half the runs: “carb context making” (1), “carb ratio segments” (1), “10.5 and 12.6” (1), “entries for representative” (1), “unchanged this cycle” (1), “begin logging carbohydrate” (1), “handled by smb/uam” (1), “smb/uam without carb” (1), “making carb ratio” (1), “14 day period” (1), “655 insulin entries” (1), “cycle and begin” (1).

Evidence cited: 12.6g/u (1).

## primary recommendation

### meal — 6/20 runs

**Shared reasoning**

- (4/6) Begin logging carbohydrate amounts and timestamps, focused on the recurring 10:00-17:00 local rise.

**Varying reasoning**

- (3/6) No carbohydrate entries exist anywhere in the 14-day package and no meal-strategy values are declared, so carb ratios, meal-bolus timing, and e-carb suitability cannot currently be evaluated with confidence.

Points made by a single run only: 11.

Phrases used by at least half the runs: “carbohydrate entries exist” (5), “begin logging” (5), “14 day” (4), “logging carbohydrate” (4), “00 local” (4), “entries exist anywhere” (3), “begin logging carbohydrate” (3), “carb ratios” (3), “16 00 local” (3).

Evidence cited: 16:00 (4), 10:00 (4), 07:00 (2), 17:00 (2), 11:00 (1), 12:00 (1).

### safety — 3/20 runs

**Shared reasoning**

- (3/3) Three separate episodes (2026-08-13, 2026-08-14, 2026-08-19) show a large correction bolus followed 2-4 hours later by a substantial glucose drop, some reaching level-2 hypoglycemia.
- (2/3) Review recurring hypoglycemia clusters and the correction-then-delayed-drop dosing pattern with a clinician before any other change.

Points made by a single run only: 3.

Phrases used by at least half the runs: “correction then delayed” (2), “correction bolus” (2), “recurring correction” (2), “review recurring” (2).

Evidence cited: 4h (1), 6h (1), 2h (1).

### data — 2/20 runs

**Shared reasoning**

- (2/2) Zero carbohydrate entries exist across the full 14-day period, which blocks separation of meal effects from basal, CR, ISF, and DIA effects in both the overnight low pattern and the daytime 16:00 high pattern.
- (2/2) Establish basic carbohydrate logging before further profile or automation changes.

Points made by a single run only: 1.

Phrases used by at least half the runs: “carbohydrate logging” (2), “profile or automation” (2), “meal effects” (2), “14 day period” (2), “automation changes zero” (2), “effects from basal” (2), “carbohydrate entries exist” (2), “period which blocks” (2), “changes zero carbohydrate” (2), “zero carbohydrate entries” (2), “separating meal effects” (1), “entries exist anywhere” (1).

Evidence cited: 16:00 (1).

### basal — 2/20 runs

Points made by a single run only: 7.

Phrases used by at least half the runs: “severe hyperglycemia event” (2), “basal segment” (2), “effective maximum basal” (1), “segments this mechanism” (1), “max_basal_u_per_hour of 12” (1), “capped near u/h” (1), “0.8 u/h basal” (1), “u/h well below” (1), “maximum basal ceiling” (1), “basal change” (1), “low 0.5 0.8” (1), “14 severe hyperglycemia” (1).

Evidence cited: 5.9u/h (1), 12u/h (1), 0.8u/h (1), 4u/h (1), 16:00 (1), 162.8mg/dl (1), 32.1% (1), 0.5u/h (1).

### dia — 2/20 runs

Points made by a single run only: 5.

Phrases used by at least half the runs: “glucose still” (2), “10 hour dia” (2), “change multiple” (2), “correction bolus tail” (1), “falling substantially hours” (1), “clusters this pattern” (1), “hours after correction” (1), “coinciding at least” (1), “still falling substantially” (1), “pattern could reflect” (1), “multiple therapy response” (1), “therapy response windows” (1).

Evidence cited: 6h (1), 360min (1).

### target — 1/20 runs

Points made by a single run only: 2.

Phrases used by at least half the runs: “understanding recurrent overnight” (1), “recurrent overnight hypoglycemia” (1), “highest local time” (1), “time below range” (1), “lowest rate” (1), “unresolved alternative explanations” (1), “prioritize understanding recurrent” (1), “18.5 occur overnight” (1), “basal is already” (1), “rate but evening” (1), “declared target” (1), “tightest 90 mg/dl” (1).

Evidence cited: 18.5% (1), 90mg/dl (1).

### cr — 1/20 runs

Points made by a single run only: 2.

Phrases used by at least half the runs: “zero carb entries” (1), “entries zero carb” (1), “bolus and carb” (1), “begin logging carbohydrate” (1), “carbohydrate and carb” (1), “14 day period” (1), “655 insulin entries” (1), “meal bolus” (1), “carb entries exist” (1), “period despite 655” (1), “every carb ratio” (1), “carb ratio segment” (1).

### data_quality — 1/20 runs

Points made by a single run only: 2.

Phrases used by at least half the runs: “recur around two” (1), “windows correction bolus” (1), “entries exist anywhere” (1), “meal windows correction” (1), “assessment of carb” (1), “ratio meal bolus” (1), “lunch but zero” (1), “strategy and carb” (1), “patterns recur around” (1), “clock windows plausible” (1), “carbohydrate entries exist” (1), “recurring meal windows” (1).

### safety_iob — 1/20 runs

Points made by a single run only: 3.

Phrases used by at least half the runs: “action this pattern” (1), “followed hours later” (1), “clinician before adjusting” (1), “isf or basal” (1), “fast rises 2026” (1), “rises 2026 08” (1), “adjusting dia isf” (1), “review correction dosing” (1), “stacking under 10” (1), “board stacking” (1), “basal since” (1), “change several large” (1).

Evidence cited: 6h (1).

### data_logging — 1/20 runs

Points made by a single run only: 2.

Phrases used by at least half the runs: “carbohydrate absorption model” (1), “separating meal effects” (1), “baseline during meals” (1), “entries exist anywhere” (1), “ratios the flat” (1), “begin logging carbohydrate” (1), “14 day record” (1), “logging carbohydrate entries” (1), “profile or automation” (1), “afternoon hyperglycemia pattern” (1), “prevents separating meal” (1), “model and prevents” (1).

## summary

### 20 runs

**Varying reasoning**

- (9/20) Fourteen days of closed-loop data show good CGM coverage (98.7%) with overall time-in-range of 86%, but with recurring nocturnal hypoglycemia clusters (00:00-03:00 local), recurring daytime hyperglycemia clustering 10:00-17:00 local (worst at hour 16, TAR 32.1%), and several severe glucose extremes on 2026-08-13, 08-14, 08-15, 08-18, 08-19, and 08-21.
- (9/20) No carbohydrate entries exist anywhere in the period, which blocks direct validation of carb ratios and meal-bolus behavior.
- (8/20) The active aaps_profile is treated as authoritative and applicable across the full period per profile_context, despite a mid-period profile switch on 2026-08-13.
- (6/20) Fourteen days of good-quality CGM data (98.7% coverage) show overall time-in-range of 86.0% with elevated variability (CV 32.6%), time-below-range of 5.1% (above common targets), and time-above-range of 8.9%.
- (5/20) Fourteen days of high-quality closed-loop AAPS/Nightscout data (98.7% CGM coverage) show overall time-in-range of 86.0% with average glucose 121.6 mg/dL, alongside recurring level-2 hypoglycemia clusters, two unexplained severe hyperglycemia clusters, and a repeating late-morning-to-afternoon rise followed by an evening-to-overnight low.
- (4/20) No carbohydrate entries or e-carbs exist anywhere in the period, and no prebolus or immediate-bolus-percentage strategy is declared or observed, so all visible meal-related glucose action comes from reactive SMB/UAM correction dosing rather than carb-ratio-based bolusing.
- … 8 more varying points

Points made by a single run only: 32.

Phrases used by at least half the runs: “time in range” (17), “carbohydrate entries” (15), “overall time” (15), “exist anywhere” (14), “entries exist” (13), “entries exist anywhere” (12), “hypoglycemia clusters” (12), “98.7 coverage” (11), “hyperglycemia clusters” (11), “carbohydrate entries exist” (10), “severe hyperglycemia” (10), “00 local” (10).

Evidence cited: 98.7% (15), 86.0% (13), 5.1% (9), 16:00 (7), 17:00 (7), 32.6% (7), 121.6mg/dl (6), 135mg/dl (6), 10:00 (5), 32.1% (4), 86% (4), 42mg/dl (3).

## issues

### 20 runs

**Varying reasoning**

- (10/20) Severe hypoglycemia clusters occurred on 2026-08-13, 2026-08-14, and 2026-08-21; severe hyperglycemia clusters occurred on 2026-08-15 and 2026-08-18, with several of these days showing elevated time above and below range simultaneously.
- (6/20) Zero carbohydrate entries exist anywhere in the 14-day dataset, which blocks direct evaluation of carb ratios, meal bolus timing, and e-carb strategy.
- (5/20) Recurring hyperglycemia in the 10:00-17:00 local window, peaking at hour 16 local (32.1% time-above-range), with at least three unresolved competing explanations.
- (3/20) A recurring daytime glucose rise in local hours 10:00-16:00 (peaking at 32.1% time-above-range at 16:00) is visible, with no carbohydrate entries anywhere in the dataset to explain it through carb-ratio dosing.
- (3/20) Zero carbohydrate entries were logged across the entire 14-day period, blocking direct separation of meal effects from basal, CR, and automation effects in multiple recurring patterns.
- (3/20) Elevated glucose variability (coefficient of variation 32.6 percent) alongside a below-range time percentage (5.1 percent) above typical targets.
- … 4 more varying points

Points made by a single run only: 34.

Phrases used by at least half the runs: “carbohydrate entries” (16), “below range” (16), “time above range” (15), “time below range” (15), “14 day” (15), “carb ratio” (13), “hypoglycemia clusters” (13), “zero carbohydrate” (12), “14 day period” (12), “hyperglycemia clusters” (12), “carbohydrate entries exist” (12), “zero carbohydrate entries” (11).

Evidence cited: 32.1% (12), 5.1% (11), 32.6% (8), 293mg/dl (7), 42mg/dl (7), 135mg/dl (7), 17:00 (7), 10:00 (6), 16:00 (5), 4% (3), 360min (3), 00:00 (3).

## step findings: data_quality

### 20 runs

**Shared reasoning**

- (17/20) CGM coverage is good (98.7%, ~5-minute cadence, 10 gaps, largest 65 minutes, no duplicates or invalid entries).

**Varying reasoning**

- (10/20) Zero carbohydrate entries exist anywhere in the 14-day period.
- (10/20) A Profile Switch to the currently authoritative flat-ISF, u200 dilute-basal profile occurred mid-period (2026-08-13T21:23Z), so applicability of the current profile to 2026-08-07 through 2026-08-13 relies on the user's declared historical_applicability rather than direct telemetry linkage.
- (7/20) Zero carbohydrate entries exist across 2,315 treatments and 655 insulin entries; all sampled boluses are typed Correction Bolus.
- (3/20) Loop status telemetry is only a 24-item representative sample out of 6214 total device statuses.
- (2/20) Zero carbohydrate entries exist across the whole period despite meal-shaped excursions. profile_context explicitly declares historical_applicability=yes for the current authoritative aaps_profile across the full period, which corrects an earlier working assumption (from checkpoint review) that the Profile Switch events clustered on 2026-08-13T21:23-21:24 necessarily indicate an unknown, different prior configuration for days before that date; per package guidance, historical applicability is a separate user declaration and must not be inferred from telemetry linkage, so that earlier speculation is downgraded to a low-confidence residual observation rather than a firm data gap.
- (2/20) Representative treatment and device-status samples are limited relative to totals (40 of 2315 treatments, 24 of 6214 device statuses). profile_context explicitly declares historical_applicability as yes for the current aaps_profile, so the mid-period Profile Switch events around 2026-08-13 are treated as reconfirmation within the same declared configuration; an earlier working hypothesis of profile discontinuity across the period is retracted based on this explicit declaration.
- … 4 more varying points

Points made by a single run only: 14.

Phrases used by at least half the runs: “carbohydrate entries” (18), “cgm coverage” (17), “profile switch” (17), “zero carbohydrate entries” (16), “10 gaps” (16), “minute cadence” (14), “10 gaps largest” (14), “carbohydrate entries exist” (13), “cadence 10 gaps” (13), “gaps largest 65” (13), “65 minutes” (12), “invalid entries” (11).

Evidence cited: 98.7% (20), 65min (20), 21:23 (3), 5min (3), 21:24 (1), 10h (1), 12% (1), 50% (1), 16.2u (1).

## step findings: safety_overview

### 20 runs

**Shared reasoning**

- (19/20) Severe hypoglycemia clusters occurred on 2026-08-13 (down to 42 mg/dL), 2026-08-14 (down to 41 mg/dL), and 2026-08-21 (42 mg/dL); severe hyperglycemia clusters occurred on 2026-08-15 and 2026-08-18 (up to 293 and 290 mg/dL).

**Varying reasoning**

- (9/20) Aggregate time-below-range 5.1% and time-above-range 8.9% with CV 32.6%.
- (8/20) Overall TIR 86.0%, TAR 8.9%, TBR 5.1%, CV 32.6%.
- (3/20) Local-hour pattern shows overnight (00:00-03:00) TBR elevated (10-18%) despite the day's lowest basal segment, and afternoon (13:00-17:00) shows the worst TAR, peaking 32.1% at hour 16, followed by a rebound TBR spike at hour 19.
- (2/20) Confounders present: GLP-1 doses on 08-14/08-17/08-20, an Occlusion and Pump Error announcement on 08-19, five Temporary Target activations (targets ~108-135 mg/dL) on multiple days, site changes on 08-10/08-13/08-17, sensor changes on 08-11/08-21, and declining uploader/pump battery near period end.
- (2/20) Severe high clusters occurred Aug 15 (~16:30 UTC, 286-293 mg/dL) and Aug 18 (~12:00 UTC, 285-290 mg/dL).
- (2/20) The 2026-08-19 hyperglycemia coincides with a logged pump Occlusion and Pump Error announcement, a plausible device-related confound.
- … 1 more varying points

Points made by a single run only: 29.

Phrases used by at least half the runs: “hyperglycemia clusters” (13), “hypoglycemia clusters” (13), “42 mg/dl” (12), “293 mg/dl” (11), “severe hyperglycemia clusters” (11), “below range” (10), “15 and 2026” (10).

Evidence cited: 5.1% (20), 32.6% (16), 8.9% (13), 42mg/dl (12), 293mg/dl (11), 86.0% (10), 290mg/dl (7), 4% (6), 51mg/dl (6), 41mg/dl (5), 48mg/dl (5), 32.1% (4).

## step findings: basal_targets

### 20 runs

**Varying reasoning**

- (9/20) The 00:00-01:00 local window shows elevated time-below-range (11.4% and 18.5%) with at least two competing explanations (the 00:00 basal segment of 0.6 U/h, the 90 mg/dL overnight target combined with aggressive UAM, or a residual effect of an unlogged evening correction) that current data cannot separate.
- (4/20) The 10:00-16:00 basal segment (0.7 U/h, dropping to 0.5 U/h at 16:00) spans the period of heaviest recurring hyperglycemia (time-above-range 14.0-32.1%, peak average 162.8 mg/dL at hour 16 local), but this cannot be separated from a possible unlogged meal effect.
- (4/20) Overnight 03:00-07:00 local shows strong control (TIR 95.2-98.7%).
- (3/20) The 04:00-08:00 window shows excellent control (TIR 95-98.7%), supporting current basal/target there.
- (2/20) Daytime hours (approximately 09:00-17:00 local) show sustained hyperglycemia (average 132-163 mg/dL, time-above-range up to 32.1%) spanning the 06:00, 10:00, and 16:00 basal segment boundaries and overlapping carb-ratio segment boundaries; this is consistent with basal or CR insufficiency but equally consistent with unlogged meals and Dynamic ISF behavior, and cannot be resolved without carbohydrate data.
- (2/20) Overnight (00:00-03:00 local) hypoglycemia elevation occurs during the day's lowest basal rate (0.6 U/h), arguing against overnight basal excess as primary driver; more likely a delayed tail effect from evening correction dosing combined with a tight 90 mg/dL overnight target.
- … 2 more varying points

Points made by a single run only: 50.

Phrases used by at least half the runs: “0.5 u/h” (16), “135 mg/dl” (13), “00 local” (13), “temporary targets” (12), “hour 16” (12), “time below range” (12), “90 mg/dl” (10), “time above range” (10).

Evidence cited: 32.1% (16), 0.5u/h (16), 18.5% (16), 00:00 (15), 16:00 (15), 135mg/dl (13), 90mg/dl (10), 10:00 (10), 17:00 (9), 98.7% (8), 162.8mg/dl (7), 0.7u/h (6).

## step findings: profile_cr_isf_dia

### 20 runs

**Shared reasoning**

- (13/20) The profile declares a single flat ISF of 56 mg/dL/U for the whole day, but Dynamic ISF (enabled, 70% adjustment factor) produces effective sensitivity values ranging roughly from 27.8 to 178.7 mg/dL/U across sampled loop statuses, meaning the static profile value is only a loose anchor and outcome variability cannot be attributed to it in isolation.

**Varying reasoning**

- (10/20) Carb ratio segments cannot be evaluated at all because zero carbohydrate entries exist.
- (3/20) The single flat ISF segment (56 mg/dL/U) corresponds to a profile-switch note referencing a flat-ISF configuration.
- (3/20) Carb ratio segments (13, 11.1, 13.2, 10.5, 12.6 g/U) cannot be validated against any actual meal data because carb_entries is 0 for the entire period.
- (2/20) Carb ratio is lowest (10.5 g/U) at 16:00, coinciding with the worst afternoon hyperglycemia, but this cannot be confirmed as CR insufficiency without carb data.
- (2/20) A 10-hour duration of insulin action is long relative to typical rapid-acting insulin, which could plausibly extend the insulin tail behind large corrections, but the declared diluted U200 insulin strategy may independently justify slower modeled kinetics; this remains an unresolved two-sided hypothesis.
- (2/20) DIA of 10 hours is long relative to typical rapid-acting durations and is a plausible contributor to insulin-on-board stacking seen in some correction-response windows, but this cannot yet be separated from automation safety-limit behavior.

Points made by a single run only: 31.

Phrases used by at least half the runs: “56 mg/dl/u” (19), “dynamic isf” (18), “carb ratio” (16), “10 hours” (15), “single flat” (15), “cannot be validated” (14), “flat isf” (13), “carb ratio segments” (12), “adjustment factor” (10), “entries exist” (10).

Evidence cited: 56mg/dl (20), 10h (18), 70% (14), 178.7mg/dl (9), 360min (5), 16:00 (4), 10.5g/u (4), 12.6g/u (3), 124mg/dl (3), 25u (2), 6h (2), 13.2g/u (2).

## step findings: automation_smb_uam

### 20 runs

**Varying reasoning**

- (3/20) SMB and UAM are both enabled and UAM activity appears in nearly every non-zero-dose loop reason sampled, functioning as the practical meal-detection mechanism given zero carbohydrate logging, without duplicating carbohydrate-on-board (always 0 in samples). smb_with_cob_enabled and smb_after_carbs_enabled are both false and untested since no carbohydrates were ever logged. smb_with_high_temp_target_enabled is false, and elevated 135 mg/dL, 180-minute temporary targets on 2026-08-17 and 2026-08-18 raise a plausible but inconsistent link to SMB suppression, since 2026-08-17 was a comparatively good day (time-above-range 4.2 percent) despite the same pattern, while 2026-08-18 was one of the worst days (time-above-range 15.3 percent); no loop sample falls inside the 2026-08-18 window to confirm suppression occurred.
- (3/20) SMB delivery limits (3-minute interval, 15 and 20 minute basal-minute caps) do not appear to be constraining delivery based on observed dose sizes.
- (3/20) SMB interval and basal-minute limits (3/15/20 minutes) show no internal inconsistency.
- (2/20) SMB and UAM are both enabled and are functioning as the sole real-time meal-response mechanism given zero logged carbohydrates; loop reasons consistently show UAM engaging with COB: 0.

Points made by a single run only: 47.

Phrases used by at least half the runs: “135 mg/dl” (17), “smb and uam” (16), “temporary targets” (15), “135 mg/dl temporary” (12), “smb_with_high_temp_target_enabled false” (11), “mg/dl temporary targets” (10).

Evidence cited: 135mg/dl (17), 20min (3), 4.2% (2), 15.3% (2), 25u (1), 4h (1), 100% (1), 25min (1), 48mg/dl (1), 13:55 (1), 18h (1), 0.35u (1).

## step findings: automation_sensitivity_limits

### 20 runs

**Varying reasoning**

- (8/20) Max basal (12 U/h) and max IOB (25 U) limits are never approached (peak observed enacted rate ~4 U/h, peak IOB 5.935 U), so they are not a binding constraint on any observed episode.
- (7/20) The carbohydrate absorption model (min_5m_carbimpact=8, meal_max_absorption_hours=7) is functionally untested since COB is always 0.
- (7/20) Autosens is disabled while Dynamic ISF is enabled, a standard non-conflicting combination; observed sensitivity_ratio values (0.79-1.0) are neutral dynamic adjustments, not evidence of a disabled Autosens problem.
- (3/20) Autosens is disabled while Dynamic ISF is enabled, avoiding a double-adjustment risk; this is internally coherent. sensitivity_ratio near 1 during quiet periods is a neutral computed adjustment, not evidence of a disabled mechanism.
- (2/20) One sampled event on 2026-08-16 shows the system correctly withholding dosing when a projected low was detected, indicating the safety brake is functioning as intended.
- (2/20) max_iob_units of 25 U was never approached (sampled peak 5.935 U), exonerating it as a driver of observed insulin-on-board stacking;

Points made by a single run only: 39.

Phrases used by at least half the runs: “12 u/h” (18), “dynamic isf” (13), “max_basal_u_per_hour 12 u/h” (12), “max_iob_units 25” (12), “never approached” (10).

Evidence cited: 25u (19), 12u/h (18), 4u/h (17), 5.935u (12), 70% (4), 5.9u/h (3), 56mg/dl (2), 256mg/dl (1), 135mg/dl (1), 4.8u/h (1), 179mg/dl (1), 16:00 (1).

## step findings: meal_bolus_strategy

### 20 runs

**Shared reasoning**

- (17/20) aaps_profile.analysis_context.meal_strategies is an empty array and strategy_stable_for_period is null, meaning no prebolus, immediate-bolus-percentage, or e-carb values are declared for this period; this is a genuine absence, not an omission.

**Varying reasoning**

- (10/20) All 24 sampled therapy_response_windows are Correction Boluses; no Meal Bolus event appears anywhere in representative_treatments or therapy_response_windows.
- (8/20) Several correction boluses are followed by glucose rises rather than falls over 120 minutes (for example 2026-08-09 09:01, 2026-08-12 11:40, 2026-08-14 10:25, 2026-08-16 07:50, 2026-08-17 12:30, 2026-08-20 06:54, 2026-08-21 12:50), recurring around two clock windows plausible for breakfast and lunch, consistent with unlogged carbohydrate intake outrunning small correction doses.
- (4/20) Morning (07:00-10:00 local) and midday/afternoon (11:00-17:00 local) windows show recurring rises with correction responses that do not fully arrest the rise within 6 hours, while the evening window (18:00-21:00 local) shows smaller, more effective corrections.
- (2/20) Declared and observed data agree there is no prebolus timing, immediate bolus percentage, or meal-tagged bolus anywhere in the package, so none of these can be evaluated against CR, ISF, or DIA.

Points made by a single run only: 25.

Phrases used by at least half the runs: “analysis_context meal_strategies” (19), “aaps_profile analysis_context” (18), “aaps_profile analysis_context meal_strategies” (17), “correction bolus” (17), “bolus percentage” (13), “immediate bolus percentage” (12), “genuine absence” (10).

Evidence cited: 07:00 (4), 10:00 (4), 360min (3), 264mg/dl (2), 13:00 (2), 17:00 (2), 240min (2), 10:25 (2), 11:40 (2), 4h (2), 11:00 (2), 6h (2).

## step findings: meal_ecarbs_absorption

### 20 runs

**Varying reasoning**

- (10/20) extended_carb_entries=0 and average_extended_carb_duration_min is null; no e-carb amount, start offset, or duration exists anywhere in the package.
- (6/20) extended_carb_entries is 0, average_extended_carb_duration_min is null, and carb_treatment_entries is empty; no e-carb entries exist and none are declared in analysis_context.
- (4/20) The carbohydrate absorption model settings (min_5m_carbimpact, meal_max_absorption_hours) remain entirely untested since COB is always 0.
- (3/20) extended_carb_entries is 0 and average_extended_carb_duration_min is null; no e-carb fields are declared in analysis_context.meal_strategies.
- (2/20) carb_treatment_entries is empty and extended_carb_entries is 0 with average_extended_carb_duration_min null; no e-carb usage occurred in the period, so no e-carb amount, offset, or duration can be assessed against a 6-hour glucose response.
- (2/20) COB remains 0 in every sampled loop status, so min_5m_carbimpact and meal_max_absorption_hours are entirely unexercised and cannot be evaluated against observed glucose action.

Points made by a single run only: 14.

Phrases used by at least half the runs: “start offset” (16), “amount start offset” (15), “carb amount” (14), “carb amount start” (13), “offset or duration” (11), “average_extended_carb_duration_min is null” (11).

Evidence cited: 240min (1), 360min (1).

## step findings: synthesis_plan

### 20 runs

**Varying reasoning**

- (3/20) A second unresolved tension is between DIA/IOB stacking and dynamic ISF aggressiveness as contributors to the hypo/hyper oscillation seen on 2026-08-13, 2026-08-14, and 2026-08-19.
- (3/20) Three competing, currently inseparable explanations exist for the 10:00-17:00 local hyperglycemia pattern: carb-ratio sizing, Temporary Target-driven SMB suppression (smb_with_high_temp_target_enabled=false overlapping 135 mg/dL targets), and unannounced meals.
- (3/20) The dominant unresolved issue across every stage is the complete absence of carbohydrate logging, which prevents separating meal effects from basal, CR, ISF, and DIA effects in both the overnight low pattern and the daytime 16:00 high pattern.
- (3/20) No profile or AAPS parameter change is supported by the current evidence; all recommended actions are observational or sequenced verification steps.
- (2/20) No profile or AAPS parameter has sufficient, unambiguous, single-cause evidence to support a numeric change today; the safest path is sequential verification starting with data collection (carb logging) and clinical review of DIA, before any basal, CR, or multiplier change is considered, and never changing basal and the safety multiplier together.
- (2/20) Across all stages, the dominant limiting factor is the complete absence of carbohydrate data, which blocks carb ratio verification and meal-timing analysis and confounds interpretation of basal, ISF, and automation behavior.
- … 2 more varying points

Points made by a single run only: 65.

Phrases used by at least half the runs: “carbohydrate logging” (15), “dynamic isf” (13).

Evidence cited: 16:00 (7), 135mg/dl (4), 17:00 (4), 10:00 (3), 90mg/dl (2), 00:00 (2), 12:00 (1), 5.1% (1), 4u/h (1), 12u/h (1), 0.8u/h (1), 10h (1).

## meal strategy

### 20 runs

**Varying reasoning**

- (2/20) Continue the current correction-only, UAM-driven approach for now, since no prebolus timing or immediate-bolus percentage is declared or observed in this period, and e-carbs are neither used nor declared; before making any change to prebolus, immediate-bolus percentage, SMB/UAM behavior, or e-carbs, begin logging actual carbohydrate entries so that recurring daytime glucose rises can be attributed to meals, Temporary Target SMB suppression, or automation timing rather than assumed.
- (2/20) No prebolus timing, immediate-bolus percentage, or e-carb strategy is declared or logged for this period, so none of these can currently be assessed or adjusted; continue relying on SMB and UAM as the sole reactive mechanism for now, and begin logging carbohydrate amount and timing before defining any prebolus, immediate-bolus percentage, or e-carb approach. aaps_profile.analysis_context.meal_strategies is empty and 655 of 655 insulin entries are correction boluses with zero carbohydrate entries logged, while hourly glucose data show two consistently recurring daily rise windows at 07:00-10:00 and 12:00-16:00 local.
- (2/20) Continue the current no-carb-counting, SMB/UAM-driven correction-only approach as the baseline, since this matches both the user's empty declared meal strategy and the fully observed execution with zero meal boluses; no prebolus timing or immediate bolus percentage change can be proposed because none exists in the data, and no e-carb use is declared or logged to adjust. aaps_profile.analysis_context.meal_strategies is empty, meaning no prebolus, immediate bolus percentage, or e-carb strategy has been declared, and every treatment and therapy_response_window entry is a Correction Bolus with COB always 0, confirming that declared and observed strategy agree on a correction-only workflow.

Points made by a single run only: 37.

Phrases used by at least half the runs: “immediate bolus percentage” (20), “prebolus timing” (19), “analysis_context meal_strategies” (16), “percentage or carb” (15), “aaps_profile analysis_context” (15), “aaps_profile analysis_context meal_strategies” (14), “timing immediate bolus” (11), “prebolus timing immediate” (11), “correction bolus” (11).

Evidence cited: 10:00 (5), 07:00 (2), 16:00 (2), 17:00 (2), 180min (1), 13:00 (1), 11:00 (1), 360min (1), 6h (1), 12:00 (1).
