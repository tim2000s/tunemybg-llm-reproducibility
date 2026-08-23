# Reasoning analysis — gemini-3.6-flash (50 runs, `real_gemini36flash_50`)

Each model rationale is split into sentences; sentences making the same point across runs are grouped. **Shared** = the point appears in at least 60% of the runs in that group; **varying** = it appears in some runs but not most. Counts are runs, not sentences. 'Evidence cited' lists the numbers and times the model quoted, with the number of runs quoting each.

## decision: Profile / basal 00:00

### keep — 39/50 runs

**Varying reasoning**

- (8/39) Overnight lows are primarily driven by the low target (90 mg/dL).
- (6/39) Target should be adjusted first before altering basal rates.
- (5/39) Maintain overnight basal rate at 0.6 U/h while evaluating the effect of raising overnight glucose target to 100 mg/dL.
- (4/39) Overnight glucose drops at 00:00-03:00 are confounded by late evening UAM SMB insulin stacking.
- (4/39) Keep basal unchanged while raising overnight target.
- (3/39) Baseline overnight basal is appropriate; nocturnal low risk should first be addressed by raising target from 90 to 100 mg/dL before altering basal rates.
- … 4 more varying points

Points made by a single run only: 31.

Evidence cited: 90mg/dl (14), 100mg/dl (13), 00:00 (8), 03:00 (5), 0.6u/h (5), 08:00 (4), 04:00 (4), 18.5% (3), 01:00 (3), 95% (2), 07:00 (2), 02:00 (1).

### change — 11/50 runs

**Varying reasoning**

- (5/11) Reducing basal from 0.6 U/h to 0.5 U/h prevents excessive nocturnal background insulin delivery.
- (4/11) High nocturnal hypoglycemia (18.5% TBR at 01:00 local) indicates background basal is too high during early sleep hours despite loop suspensions.
- (4/11) Overnight TBR reaches 18.5% around 01:00 local time.

Points made by a single run only: 4.

Phrases used by at least half the runs: “00 local” (7), “0.6 u/h” (7).

Evidence cited: 18.5% (11), 01:00 (9), 0.6u/h (7), 0.5u/h (5), 00:00 (4), 03:00 (4), 11.4% (3), 0u/h (2), 90mg/dl (1), 23:00 (1).

## decision: Profile / basal 05:00

### keep — 50/50 runs

**Shared reasoning**

- (31/50) Fasting glucose between 05:00 and 06:00 is stable (avg 99.5-104.2 mg/dL) with low hypoglycemia risk (TBR 2.5%-4.8%).

**Varying reasoning**

- (7/50) Basal rate is well calibrated.
- (4/50) Early morning fasting stability is good with TIR 95.2-97.5% between 04:00 and 07:00 local.
- (4/50) Keep current rate.
- (3/50) Glucose stability between 05:00 and 06:00 local time is adequate (mean BG 99.5 mg/dL, 95.2% TIR).
- (3/50) Fasting stability between 05:00 and 06:00 is excellent (95.2% TIR) with minimal hypo risk.
- (3/50) Current rate is appropriate.
- … 6 more varying points

Points made by a single run only: 15.

Evidence cited: 05:00 (35), 06:00 (21), 2.5% (20), 08:00 (15), 4.8% (10), 99.5mg/dl (9), 95% (9), 04:00 (8), 104.2mg/dl (6), 95.2% (6), 07:00 (6), 97.5% (5).

## decision: Profile / basal 06:00

### keep — 50/50 runs

**Varying reasoning**

- (14/50) Morning fasting window (06:00-08:00 local time) shows excellent stability with 97.5-98.7% TIR and minimal hypo risk (<2.5% TBR).
- (13/50) Morning glucose remains stable with average 99.5-110.5 mg/dL between 06:00 and 09:00 local time.
- (7/50) Keep current rate.
- (5/50) Morning baseline glucose remains well within target range.
- (4/50) Morning glucose (06:00-10:00) is stable (avg 99.5-132.9 mg/dL) with <1.3% TBR.
- (4/50) Current basal rate is effective.
- … 6 more varying points

Points made by a single run only: 18.

Evidence cited: 06:00 (24), 08:00 (13), 98.7% (12), 10:00 (11), 1.3% (8), 97.5% (6), 2.5% (5), 110.5mg/dl (5), 98% (4), 0% (4), 99.5mg/dl (3), 09:00 (3).

## decision: Profile / basal 10:00

### keep — 50/50 runs

**Varying reasoning**

- (9/50) Midday glucose rise is driven by unannounced meals rather than basal deficiency.
- (8/50) Midday rise (TAR 20.2% at 10:00 local) coincides with unannounced meal absorption.
- (5/50) Daytime glucose variations are heavily confounded by unannounced meals.
- (5/50) Maintain basal until meal bolusing is established.
- (4/50) Daytime glucose variations are dominated by unannounced meals and dynamic loop interventions.
- (4/50) Basal setting cannot be isolated until meal carb entries are logged.
- … 8 more varying points

Points made by a single run only: 25.

Evidence cited: 10:00 (7), 20.2% (3), 1.2% (1), 12:00 (1), 08:00 (1), 11:00 (1), 92% (1), 16:00 (1).

## decision: Profile / basal 16:00

### keep — 50/50 runs

**Varying reasoning**

- (7/50) Late afternoon lows at 18:00–19:00 are driven by accumulated UAM microboluses from afternoon spikes, not basal excess at 16:00.
- (7/50) Late afternoon rises are driven by unannounced meal absorption rather than basal deficiency.
- (5/50) Afternoon peak glucose (16:00 local avg 162.8 mg/dL) is driven by postprandial UAM absorption.
- (5/50) Late afternoon drops are caused by dynamic ISF SMB stacking.
- (3/50) Late afternoon hypoglycemic crashes (15.3% TBR at 19:00 local) stem from dynamic ISF and UAM SMB stacking (up to 5.9 U IOB) rather than excessive scheduled basal (0.5 U/h).
- (3/50) Basal rate of 0.5 U/h is appropriate.
- … 13 more varying points

Points made by a single run only: 20.

Phrases used by at least half the runs: “late afternoon” (28).

Evidence cited: 16:00 (14), 19:00 (12), 0.5u/h (9), 32.1% (6), 18:00 (6), 15.3% (3), 162.8mg/dl (3), 15:00 (3), 5.9u (1), 14:00 (1).

## decision: Profile / basal 18:00

### keep — 49/50 runs

**Varying reasoning**

- (8/49) Hypoglycemia at 18:00–19:00 is caused by earlier UAM SMB stacking rather than excessive basal insulin.
- (6/49) Hypoglycemia at 19:00 (15.3% TBR) is driven by afternoon UAM SMB stacking rather than basal excess.
- (5/49) Maintain current basal rate pending meal bolus timing adjustments.
- (4/49) Evening lows at 19:00 (15.3% TBR) are driven by stacked afternoon UAM SMBs.
- (3/49) Withhold basal change until safety limits are tightened.
- (3/49) Keep rate unchanged until automation dynamic ISF over-dosing is resolved.
- … 4 more varying points

Points made by a single run only: 41.

Evidence cited: 19:00 (24), 15.3% (15), 18:00 (10), 14:00 (2), 16:00 (2), 11.9% (1), 20:00 (1), 0.6u/h (1).

### change — 1/50 runs

Points made by a single run only: 1.

Phrases used by at least half the runs: “evening hypoglycemia 11.9” (1), “peak evening hypoglycemia” (1), “0.6 u/h” (1), “hypoglycemia 11.9 15.3” (1), “coincides with peak” (1), “stepping up basal” (1), “18 00 coincides” (1), “basal to 0.6” (1), “u/h at 18” (1), “11.9 15.3 tbr” (1), “tbr at 18” (1).

Evidence cited: 11.9% (1), 19:00 (1), 18:00 (1), 15.3% (1), 0.6u/h (1).

## decision: Profile / basal 19:00

### keep — 47/50 runs

**Varying reasoning**

- (8/47) Evening glucose stabilizes after 20:00 (TIR 92.3%).
- (4/47) TBR peaks at 15.3% at 19:00 local.
- (2/47) Evening glucose stabilizes after 20:00 (avg 117-120 mg/dL, TIR >88%), supporting the 0.7 U/h setting.
- (2/47) However, this is driven by stacked afternoon UAM SMBs rather than basal excess alone.
- (2/47) Nighttime transition basal is stable; maintain current rate and evaluate after addressing overnight target and safety limits.
- (2/47) Maintain scheduled rate until meal SMB over-delivery is resolved through upfront carb logging.
- … 6 more varying points

Points made by a single run only: 37.

Evidence cited: 20:00 (9), 19:00 (7), 15.3% (5), 92.3% (5), 0.7u/h (2), 21:00 (2), 13:00 (1), 17:00 (1), 22:00 (1), 88% (1), 120mg/dl (1), 90% (1).

### change — 3/50 runs

Points made by a single run only: 5.

Phrases used by at least half the runs: “15.3 tbr” (2), “0.7 u/h” (2).

Evidence cited: 19:00 (3), 15.3% (2), 0.7u/h (2), 105.4mg/dl (1), 18:00 (1), 0.6u/h (1), 0.5u/h (1).

## decision: Profile / CR 00:00

### keep — 50/50 runs

**Varying reasoning**

- (15/50) Zero carb entries logged in telemetry.
- (7/50) CR cannot be evaluated directly; maintain current setting until meal logging is established.
- (6/50) CR cannot be evaluated without meal data.
- (5/50) Absence of logged carbohydrate entries prevents direct evaluation of CR accuracy.
- (5/50) Evidence: Zero meal carb entries logged.
- (4/50) Zero carb entries logged in Nightscout; insufficient data to evaluate CR accuracy.
- … 11 more varying points

Points made by a single run only: 15.

## decision: Profile / CR 04:00

### keep — 50/50 runs

**Varying reasoning**

- (12/50) Evidence: Zero carb entries logged.
- (6/50) No early morning meal entries logged.
- (5/50) CR cannot be evaluated without logged meals.
- (4/50) Zero carb entries logged in Nightscout; insufficient data to evaluate CR accuracy.
- (4/50) No early morning meal carb entries were recorded.
- (4/50) Keep current value.
- … 10 more varying points

Points made by a single run only: 18.

## decision: Profile / CR 08:00

### keep — 50/50 runs

**Varying reasoning**

- (14/50) Zero carb entries logged in telemetry.
- (5/50) Morning meals are unannounced.
- (4/50) CR cannot be evaluated without logged meals.
- (4/50) Maintain current setting.
- (4/50) Carbohydrate logging is absent in telemetry.
- (2/50) User should test pre-bolusing before modifying CR.
- … 6 more varying points

Points made by a single run only: 32.

Evidence cited: 290mg/dl (1), 20.2% (1), 10:00 (1).

## decision: Profile / CR 16:00

### keep — 50/50 runs

**Varying reasoning**

- (10/50) Zero carb entries logged in telemetry.
- (6/50) Afternoon meals are currently unannounced.
- (5/50) Cannot evaluate CR accuracy without logged meal carbs.
- (3/50) Keep profile CR until explicit meal logging occurs.
- (3/50) Maintain current CR.
- (3/50) CR cannot be evaluated without meal entries.
- … 9 more varying points

Points made by a single run only: 30.

Evidence cited: 10.5g/u (3), 32.1% (2), 16:00 (1), 15.3% (1).

## decision: Profile / CR 20:00

### keep — 50/50 runs

**Varying reasoning**

- (12/50) Evidence: Zero carb entries logged.
- (6/50) Maintain current setting.
- (3/50) Evening CR performance cannot be isolated without carb entry telemetry; keep current parameter.
- (3/50) Zero carb entries logged in Nightscout; insufficient data to evaluate CR accuracy.
- (3/50) CR cannot be evaluated without logged meals.
- (3/50) No late evening meal entries logged; retain setting.
- … 9 more varying points

Points made by a single run only: 21.

Evidence cited: 86.2% (1), 92.3% (1).

## decision: Profile / ISF 00:00

### keep — 50/50 runs

**Varying reasoning**

- (13/50) Baseline ISF is 56 mg/dL/U.
- (10/50) Baseline ISF is modified dynamically by Dynamic ISF (70% factor).
- (8/50) Dynamic ISF is active at 70%.
- (4/50) Keep baseline ISF at 56 mg/dL/U while adjusting Dynamic ISF factor.
- (4/50) Keep profile baseline while adjusting safety limits.
- (4/50) Keep base ISF stable while tuning automation settings.
- … 13 more varying points

Points made by a single run only: 20.

Phrases used by at least half the runs: “dynamic isf” (49), “56 mg/dl/u” (32), “baseline isf” (25).

Evidence cited: 56mg/dl (32), 70% (26), 37mg/dl (2), 28mg/dl (2), 50% (1), 19.7u (1), 37.9mg/dl (1), 27.8mg/dl (1).

## decision: Profile / target 00:00

### change — 39/50 runs

**Shared reasoning**

- (24/39) Raising target to 100 mg/dL provides necessary safety buffer.

**Varying reasoning**

- (16/39) Overnight TBR reaches 18.5% at 01:00 local time.
- (9/39) Overnight TBR is 10.1%-18.5% between 23:00 and 03:00 local time.
- (8/39) 90 mg/dL overnight target offers insufficient buffer against nocturnal hypoglycemia (TBR 18.5% at 01:00 local).
- (5/39) Raising target from 90 to 100 mg/dL increases safety buffer during sleep.
- (2/39) A 90 mg/dL nocturnal target provides insufficient safety margin given 11.4%-18.5% TBR in early sleep hours.
- (2/39) Raising target to 100 mg/dL reduces nocturnal hypo risk.

Points made by a single run only: 9.

Phrases used by at least half the runs: “100 mg/dl” (35), “target to 100” (21), “90 mg/dl” (20).

Evidence cited: 18.5% (38), 100mg/dl (35), 01:00 (20), 90mg/dl (20), 10.1% (11), 00:00 (9), 03:00 (7), 23:00 (5), 11.4% (3), 04:00 (3), 08:00 (2), 18% (1).

### keep — 11/50 runs

**Varying reasoning**

- (2/11) Address the 00:00 basal segment first before considering target changes.
- (2/11) Overnight target of 90 mg/dL is appropriate for closed-loop operation when fasting.

Points made by a single run only: 11.

Phrases used by at least half the runs: “target of 90” (8), “90 mg/dl” (8).

Evidence cited: 90mg/dl (8), 00:00 (3), 100mg/dl (1).

## decision: Profile / target 08:00

### keep — 50/50 runs

**Varying reasoning**

- (19/50) Daytime target of 100 mg/dL is appropriate and safe.
- (10/50) Daytime target of 100 mg/dL provides an appropriate balance between glycemic control and safety.
- (5/50) Daytime target of 100 mg/dL is appropriate and provides reasonable safety margin.
- (3/50) Daytime target of 100 mg/dL provides a stable target baseline.
- (3/50) Daytime target of 100 mg/dL is appropriate and well tolerated.
- (3/50) Keep current target.
- … 2 more varying points

Points made by a single run only: 10.

Phrases used by at least half the runs: “100 mg/dl” (50), “daytime target” (48), “target of 100” (43).

Evidence cited: 100mg/dl (50), 98.2% (1), 91.1% (1), 07:00 (1), 09:00 (1), 86% (1), 98% (1).

## decision: Profile / target 23:00

### change — 39/50 runs

**Varying reasoning**

- (22/39) Align late-night target starting at 23:00 with the 100 mg/dL overnight safety target to prevent late evening drops.
- (5/39) TBR reaches 10.1% at 23:00 local time.
- (4/39) Aligns late evening target with overnight 100 mg/dL safety buffer to prevent early nocturnal drops.
- (4/39) Raising target to 100 mg/dL aligns night target safety.
- (3/39) Aligns late-night target with 100 mg/dL to reduce early nocturnal hypoglycemia.
- (2/39) Target at 23:00 drops to 90 mg/dL right as hour 23 TBR hits 10.1%.

Points made by a single run only: 12.

Phrases used by at least half the runs: “100 mg/dl” (32).

Evidence cited: 100mg/dl (32), 23:00 (19), 00:00 (12), 10.1% (6), 90mg/dl (5), 11.4% (3), 08:00 (3), 22:00 (1).

### keep — 11/50 runs

**Varying reasoning**

- (4/11) Late night target of 90 mg/dL is consistent with overnight profile strategy.

Points made by a single run only: 9.

Evidence cited: 90mg/dl (3), 00:00 (1).

## decision: Profile / DIA

### keep — 50/50 runs

**Varying reasoning**

- (14/50) A 10-hour DIA accurately reflects modern rapid-acting insulin decay tails and prevents premature basal restoration.
- (7/50) DIA of 10.0 hours accurately models modern exponential insulin decay curves in oref1 loops.
- (5/50) 10-hour DIA is appropriate for oref1 dynamic sensitivity exponential models.
- (5/50) Keep current setting.
- (4/50) 10-hour DIA is standard and necessary for oref1 dynamic algorithms to prevent insulin stacking calculations.
- (4/50) 10.0 hours is optimal for oref1 with Dynamic ISF to model long tail insulin activity.
- … 5 more varying points

Points made by a single run only: 13.

Phrases used by at least half the runs: “hour dia” (32), “10 hour” (30), “10 hour dia” (28).

Evidence cited: 10.0h (13), 10h (4).

## decision: AAPS / SMB and UAM

### keep — 50/50 runs

**Varying reasoning**

- (8/50) SMB and UAM functionality are required for closed-loop operation.
- (4/50) Maintain both enabled.
- (3/50) SMB and UAM functionality should remain active, but guarded by reduced Max IOB and Max Basal safety ceilings.
- (3/50) SMB and UAM are necessary for closed-loop operation; unannounced meal management requires these enabled.
- (3/50) Both SMB and UAM are required to manage unannounced meals in user's current workflow.
- (3/50) SMB and UAM are required for the user's unannounced meal workflow.
- … 11 more varying points

Points made by a single run only: 21.

Phrases used by at least half the runs: “smb and uam” (45).

Evidence cited: 86.0% (1).

## decision: AAPS / SMB activation conditions

### keep — 50/50 runs

**Varying reasoning**

- (9/50) Activation conditions are appropriately configured for closed-loop operation.
- (8/50) Activation conditions are appropriate for current unannounced meal usage.
- (6/50) Keep current settings.
- (2/50) Activation conditions are functional; safety improvements should be achieved via Max IOB/Max Basal bounds rather than disabling SMBs.
- (2/50) Activation conditions support unannounced meals; safety is addressed via max IOB and target adjustments.
- (2/50) SMB activation parameters are consistent with user's unannounced meal strategy.
- … 8 more varying points

Points made by a single run only: 22.

Phrases used by at least half the runs: “activation conditions” (34).

## decision: AAPS / SMB strength and frequency

### keep — 46/50 runs

**Varying reasoning**

- (14/46) Delivery timing is standard for oref1.
- (4/46) Delivery parameters are standard for oref1; control over-dosing via Max IOB safety ceiling instead.
- (3/46) SMB delivery settings (3-min interval, 15/20 min max basal) are standard oref1 parameters.
- (3/46) Delivery interval and SMB basal minute caps are appropriate when constrained by lower max IOB limits.
- (3/46) Safety capping will be handled via Max IOB and Max Basal limits.
- (3/46) SMB delivery frequency is appropriate.
- … 4 more varying points

Points made by a single run only: 30.

Phrases used by at least half the runs: “max iob” (26).

Evidence cited: 20min (3), 3min (1), 10u (1).

### change — 4/50 runs

Points made by a single run only: 4.

Phrases used by at least half the runs: “max_uam_smb_basal_minutes from 20” (4), “15 min” (3), “20 to 15” (3), “unannounced meals” (2), “lowering max_uam_smb_basal_minutes” (2).

Evidence cited: 15min (4), 20min (1).

## decision: AAPS / max basal and max IOB limits

### change — 49/50 runs

**Varying reasoning**

- (24/49) Current Max IOB (25 U) exceeds total daily dose (~19.7 U), and Max Basal (12 U/h) is 15x max scheduled basal (0.8 U/h).
- (16/49) Reducing Max IOB to 7.0 U (~35% of TDD) and Max Basal to 3.0 U/h establishes a vital safety ceiling.
- (6/49) Reducing Max IOB to 5.0 U (~25% TDD) and Max Basal to 3.5 U/h prevents runaway insulin delivery.
- (6/49) Current limits (25 U Max IOB, 12 U/h Max Basal) are unsafe relative to 19.7 U/day total daily dose.
- (4/49) Lowering to 7.0 U Max IOB and 3.0 U/h Max Basal prevents dangerous runaway delivery.
- (3/49) Max IOB of 25 U is dangerously high for a total daily dose of ~19.7 U/day, enabling extreme IOB accumulation during delayed meal absorption.
- … 7 more varying points

Points made by a single run only: 25.

Phrases used by at least half the runs: “max iob” (45), “max basal” (43), “12 u/h” (33), “19.7 u/day” (32).

Evidence cited: 25u (46), 19.7u (45), 12u/h (33), 7.0u (20), 3.5u/h (15), 3.0u/h (13), 35% (11), 125% (10), 100% (5), 30% (5), 0.8u/h (5), 6.0u (4).

### keep — 1/50 runs

Points made by a single run only: 2.

Phrases used by at least half the runs: “retain as baseline” (1), “oref caps prevent” (1), “internal oref caps” (1), “19.7 internal oref” (1), “safety limits” (1), “limits are broad” (1), “relative to tdd” (1), “caps prevent dangerous” (1), “dangerous basal enactments” (1), “prevent dangerous basal” (1), “basal enactments retain” (1), “tdd 19.7 internal” (1).

Evidence cited: 19.7u (1).

## decision: AAPS / Autosens and Dynamic ISF

### keep — 37/50 runs

**Varying reasoning**

- (11/37) Dynamic ISF at 70% adjustment factor provides effective responsive sensitivity scaling.
- (8/37) Dynamic ISF at 70% effectively manages high glucose spikes; capping Max IOB prevents Dynamic ISF from over-dosing during unannounced meal peaks.
- (3/37) Maintain setting.
- (3/37) Dynamic ISF configuration is functioning as designed.
- (2/37) Restricting Max IOB addresses over-dosing risk without altering dynamic sensitivity tuning.

Points made by a single run only: 25.

Phrases used by at least half the runs: “dynamic isf” (37), “isf at 70” (20).

Evidence cited: 70% (27).

### change — 13/50 runs

**Varying reasoning**

- (7/13) The 70% Dynamic ISF factor scales effective ISF down to ~28 mg/dL/U during postprandial spikes, driving SMB over-delivery and late hypoglycemia (15.3% TBR at 19:00).
- (4/13) Moderating to 50% reduces extreme SMB aggressiveness.
- (2/13) Dynamic ISF at 70% factor drops ISF down to ~28 mg/dL/U during postprandial rises, causing stacked SMBs and subsequent late afternoon hypos.
- (2/13) Reducing factor to 50% tempers aggressive auto-dosing.
- (2/13) Lowering factor to 50% moderates peak SMB aggressiveness.

Points made by a single run only: 10.

Phrases used by at least half the runs: “dynamic isf” (13), “effective isf” (7), “28 mg/dl/u” (7).

Evidence cited: 50% (13), 70% (13), 28mg/dl (7), 19:00 (5), 15.3% (4), 38mg/dl (2), 27.8mg/dl (2), 27mg/dl (1).

## decision: AAPS / carbohydrate absorption model

### keep — 49/50 runs

**Varying reasoning**

- (19/49) Absorption model parameters are standard for oref1 dynamic carb decay.
- (6/49) 7-hour max absorption accommodates GLP-1 delayed gastric emptying.
- (5/49) Carb absorption parameters are appropriate.
- (5/49) Keep current settings.
- (4/49) Min 5m carb impact (8 mg/dL/5min) and 7-hour max absorption are appropriate for oref1 dynamic carb decay.
- (4/49) Maintain current configuration.
- … 3 more varying points

Points made by a single run only: 16.

Evidence cited: 5min (4), 8mg/dl (4), 7h (3), 7.0h (1).

### change — 1/50 runs

Points made by a single run only: 4.

Phrases used by at least half the runs: “carb absorption truncating” (1), “stacking late uam” (1), “meal carbohydrate logging” (1), “medium until meal” (1), “forces unrealistically rapid” (1), “8.0 to 4.0” (1), “absorption truncating cob” (1), “truncating cob prematurely” (1), “min forces unrealistically” (1), “reduce min_ m_carbimpact” (1), “unrealistically rapid modeled” (1), “prematurely and stacking” (1).

Evidence cited: 5min (1), 4.0mg/dl (1), 8.0mg/dl (1).

## profile recommendation

### target — 39/50 runs

**Shared reasoning**

- (34/39) Raise overnight target segments (00:00 and 23:00) from 90 mg/dL to 100 mg/dL.

**Varying reasoning**

- (12/39) Overnight Time Below Range reaches 18.5% at 01:00 local time.
- (9/39) Overnight Time Below Range reaches 10.1%-18.5% between 00:00 and 04:00 local time.
- (5/39) Raising the target from 90 mg/dL to 100 mg/dL between 23:00 and 08:00 provides an immediate safety buffer against nocturnal hypoglycemia while keeping basal delivery stable.
- (5/39) A target of 90 mg/dL leaves no safety margin for minor IOB variations or sensor noise during sleep.
- (4/39) Telemetry demonstrates recurring nocturnal hypoglycemia (TBR 10.1% to 18.5% between 23:00 and 03:00 local time).
- (4/39) Keep all profile basal, CR, ISF, DIA, and target settings unchanged.
- … 6 more varying points

Points made by a single run only: 26.

Phrases used by at least half the runs: “90 mg/dl” (35), “100 mg/dl” (35), “mg/dl to 100” (35), “overnight target” (26), “00 local” (25), “00 from 90” (24), “time below range” (21), “00 local time” (21).

Evidence cited: 18.5% (35), 100mg/dl (35), 90mg/dl (35), 08:00 (29), 23:00 (29), 01:00 (20), 00:00 (19), 10.1% (13), 03:00 (11), 04:00 (6), 05:00 (2), 0.5u/h (2).

### basal — 11/50 runs

**Shared reasoning**

- (7/11) Time Below Range between 00:00 and 03:00 local time reaches 18.5% at 01:00 despite mean nocturnal glucose being near target (90.6 mg/dL).
- (7/11) Reduce 00:00–05:00 profile basal from 0.60 U/h to 0.50 U/h.

Points made by a single run only: 15.

Phrases used by at least half the runs: “00 local” (9), “01 00 local” (6), “00 local time” (6), “basal segment” (6), “0.6 u/h” (6).

Evidence cited: 18.5% (10), 01:00 (9), 00:00 (9), 0.6u/h (6), 0.5u/h (5), 03:00 (5), 0.60u/h (4), 0.50u/h (4), 05:00 (4), 90.6mg/dl (2), 90mg/dl (2), 23:00 (2).

## primary recommendation

### smb — 22/50 runs

**Shared reasoning**

- (21/22) Reduce AAPS Max IOB and Max Basal Safety Limits.
- (17/22) Current Max IOB (25 U) exceeds 125% of Total Daily Insulin (~19.7 U/day), and Max Basal (12 U/h) is 15–24× scheduled basal.

**Varying reasoning**

- (5/22) Lowering Max IOB to ~7.0 U (~35% TDI) and Max Basal to ~3.5 U/h creates a critical software guardrail against dangerous UAM insulin stacking.
- (4/22) This allows the algorithm to stack dangerous amounts of insulin during unannounced meal spikes or CGM noise.
- (3/22) Lower max_iob_units from 25.0 U to 5.0 U (~25% of TDD) and max_basal_u_per_hour from 12.0 U/h to 3.5 U/h.
- (2/22) Reducing Max IOB to ~6.0-7.0 U (~30-35% TDD) and Max Basal to 2.5-3.0 U/h restores necessary safety boundaries.
- (2/22) Reducing Max IOB to 7.0 U (~35% TDD) and Max Basal to 3.0 U/h (~4x max basal rate) restores critical safety guardrails.

Points made by a single run only: 15.

Phrases used by at least half the runs: “max iob” (22), “max basal” (20), “iob and max” (18), “total daily” (18), “safety limits” (17), “basal safety” (17), “max basal safety” (16), “basal safety limits” (16), “aaps max” (14), “19.7 u/day” (14), “aaps max iob” (13), “reduce aaps” (12).

Evidence cited: 19.7u (18), 25u (14), 12u/h (9), 7.0u (9), 25.0u (8), 3.5u/h (8), 12.0u/h (7), 35% (7), 125% (6), 3.0u/h (6), 0.8u/h (3), 30% (3).

### target — 16/50 runs

**Shared reasoning**

- (16/16) Increase the target glucose from 90 mg/dL to 100 mg/dL between 23:00 and 08:00 to reduce nocturnal time below range (currently up to 18.5%).
- (11/16) Raise Overnight Target to 100 mg/dL.

**Varying reasoning**

- (5/16) Raise Overnight Target to Reduce Nocturnal Hypoglycemia.
- (2/16) Raising the target to 100 mg/dL provides a safer buffer against nocturnal lows without compromising overall control.

Points made by a single run only: 4.

Phrases used by at least half the runs: “90 mg/dl” (16), “100 mg/dl” (16), “raise overnight” (16), “raise overnight target” (14), “00 and 08” (12), “mg/dl to 100” (11), “target to 100” (9), “mg/dl between 23” (8).

Evidence cited: 100mg/dl (16), 90mg/dl (16), 08:00 (14), 18.5% (13), 23:00 (13), 00:00 (7), 04:00 (5), 10.1% (5), 01:00 (3), 70mg/dl (1).

### safety_limits — 5/50 runs

**Shared reasoning**

- (4/5) Reduce AAPS Max IOB and Max Basal Safety Limits.
- (3/5) Lowering Max IOB to ~7.0 U (~35% TDD) and Max Basal to 3.5 U/h (~4x max basal) provides essential software protection against runaway insulin stacking.

Points made by a single run only: 9.

Phrases used by at least half the runs: “iob to 7.0” (4), “max basal” (4), “max iob 25” (4), “iob and max” (4), “19.7 u/day” (4), “max basal safety” (3), “basal 12 u/h” (3), “total daily” (3), “basal safety limits” (3), “max basal 12” (3), “unannounced meal” (3), “sensor errors” (3).

Evidence cited: 7.0u (4), 25u (4), 19.7u (4), 12u/h (3), 35% (3), 3.5u/h (3), 3.0u/h (1), 5.9u (1), 8.0u (1), 100% (1), 25.0u (1), 127% (1).

### basal — 3/50 runs

**Shared reasoning**

- (3/3) Lower the 00:00–05:00 basal segment from 0.60 U/h to 0.50 U/h to reduce overnight insulin pressure and eliminate recurring 00:00–03:00 hypoglycemia.
- (2/3) Reduce Overnight Basal Rate.

Points made by a single run only: 1.

Phrases used by at least half the runs: “0.60 u/h” (3), “basal rate” (3), “u/h to 0.50” (3), “reduce overnight” (3), “0.50 u/h” (3), “reduce overnight basal” (2), “overnight basal rate” (2), “00 basal segment” (2), “segment from 0.60” (2), “05 00 basal” (2).

Evidence cited: 00:00 (3), 0.60u/h (3), 05:00 (3), 0.50u/h (3), 18.5% (2), 03:00 (2), 01:00 (1), 23:00 (1).

### aaps — 3/50 runs

**Shared reasoning**

- (3/3) Current safety limits (Max Basal 12 U/h, Max IOB 25 U) are dangerously disproportionate to the total daily dose (~19.7 U/day) and scheduled basal rates (max 0.8 U/h).
- (2/3) 35% of TDD or 3.5x max daily basal) and Max Basal to 3.0 U/h creates an essential safety ceiling against severe automated over-dosing.

Points made by a single run only: 2.

Phrases used by at least half the runs: “max basal” (3), “safety limits” (3), “total daily” (3), “max iob” (3), “essential safety ceiling” (2), “creates an essential” (2), “scheduled basal” (2), “12 u/h” (2), “u/h max” (2), “safety limits max” (2), “insulin stacking” (2), “sensor errors” (2).

Evidence cited: 25u (3), 35% (3), 12u/h (2), 7.0u (2), 3.0u/h (2), 19.7u (2), 7u (1), 4u/h (1), 0.8u/h (1).

### safety — 1/50 runs

Points made by a single run only: 3.

Phrases used by at least half the runs: “25 exceeds 125” (1), “insulin 19.7 u/day” (1), “automated over dosing” (1), “24 scheduled basal” (1), “u/h is 15” (1), “125 of total” (1), “iob to 8.0” (1), “tighten aaps max” (1), “u/h and max” (1), “daily insulin 19.7” (1), “basal to 4.0” (1), “u/day lower max” (1).

Evidence cited: 12u/h (1), 25u (1), 8.0u (1), 4.0u/h (1), 125% (1), 19.7u (1).

## summary

### 50 runs

**Shared reasoning**

- (50/50) Hypoglycemia is concentrated overnight (10.1%-18.5% TBR from 23:00 to 03:00 local time) and in the late afternoon/early evening (15.3% TBR at 19:00 local time).
- (36/50) Analysis of 14 days of Nightscout telemetry shows a overall Time in Range (70-180 mg/dL) of 86.0% with a mean glucose of 121.6 mg/dL.
- (34/50) Safety limits for Max IOB (25 U) and Max Basal (12 U/h) are also excessively loose relative to the total daily dose (~19.7 U/day).

**Varying reasoning**

- (22/50) Zero carbohydrates were logged during the period, forcing AAPS to rely entirely on Unannounced Meal (UAM) detection and Super Micro Boluses (SMB).
- (6/50) Because zero meal carbohydrates are logged, the loop relies entirely on Unannounced Meal (UAM) detection, SMBs, and Dynamic ISF (70%).
- (4/50) Addressing safety limits, raising overnight targets, and incorporating pre-bolusing for meals will reduce severe hypoglycemia risk while preserving overall control.
- (3/50) However, significant safety concerns exist due to an elevated Time Below Range of 5.1% (exceeding the 4.0% clinical safety threshold), with severe hypoglycemic excursions reaching 41–42 mg/dL.
- (3/50) Dynamic ISF scaling (70% adjustment factor) combined with delayed gastric absorption under GLP-1 therapy triggers aggressive postprandial microboluses that result in late insulin stacking and crashes.
- (3/50) Delayed UAM insulin delivery combined with Dynamic ISF creates postprandial spikes followed by late insulin stacking.
- … 8 more varying points

Points made by a single run only: 37.

Phrases used by at least half the runs: “time in range” (48), “time below range” (39), “max iob” (39), “dynamic isf” (39), “unannounced meal” (37), “00 local” (37), “121.6 mg/dl” (36), “12 u/h” (33), “max basal” (33), “15.3 tbr” (32), “safety limits” (32), “unannounced meal uam” (32).

Evidence cited: 86.0% (50), 18.5% (47), 15.3% (46), 19:00 (45), 25u (39), 121.6mg/dl (36), 5.1% (36), 12u/h (33), 19.7u (30), 01:00 (28), 03:00 (21), 180mg/dl (21).

## issues

### 50 runs

**Shared reasoning**

- (45/50) Extreme AAPS safety limits (Max IOB 25 U, Max Basal 12 U/h) relative to Total Daily Dose (~19.7 U/day).
- (37/50) Significant nocturnal hypoglycemia risk between 00:00 and 03:00 local time, peaking at 18.5% TBR at 01:00 local.

**Varying reasoning**

- (22/50) Overall Time Below Range (<70 mg/dL) is 5.1%, exceeding the recommended clinical safety threshold of <4.0%.
- (10/50) Recurrent late afternoon/evening hypoglycemia peak (18:00-19:00 local time) reaching 15.3% TBR at 19:00.
- (10/50) Complete absence of logged meal carbohydrates, forcing total reliance on reactive UAM SMB delivery that stacks behind GLP-1 delayed absorption.
- (9/50) Recurrent late-afternoon postprandial hypoglycemia between 18:00 and 19:00 local time (15.3% TBR at 19:00).
- (8/50) Complete absence of meal carbohydrate logging forces total reliance on reactive UAM microboluses.
- (6/50) Pronounced afternoon postprandial spikes (32.1% TAR at 16:00 local) followed by sharp evening drops into hypoglycemia (15.3% TBR at 19:00 local) due to unannounced meal UAM delays.
- … 18 more varying points

Points made by a single run only: 25.

Phrases used by at least half the runs: “max iob” (43), “00 local” (42), “total daily” (37), “time below range” (36), “max basal” (33), “19.7 u/day” (33), “15.3 tbr” (31), “00 local time” (31), “19 00 local” (30), “total daily dose” (29), “18.5 tbr” (27).

Evidence cited: 18.5% (48), 19:00 (45), 15.3% (44), 19.7u (41), 01:00 (38), 5.1% (33), 4.0% (30), 25u (30), 12u/h (24), 03:00 (22), 25.0u (18), 00:00 (18).

## step findings: data_quality

### 50 runs

**Varying reasoning**

- (22/50) CGM data coverage is excellent at 98.7% across 14 days (3,995 entries, largest gap 65 min).
- (16/50) Active AAPS profile and configuration settings are fully available.
- (14/50) CGM data coverage is excellent at 98.7% across 14 days with only minor gaps.
- (13/50) However, zero carbohydrate entries are logged in Nightscout.
- (7/50) Active AAPS profile and loop status telemetry are complete.
- (6/50) A critical telemetry gap exists: zero carb entries were recorded (0.0g carbs total), forcing all meal management onto UAM automation.
- … 13 more varying points

Points made by a single run only: 26.

Phrases used by at least half the runs: “14 days” (44), “coverage is excellent” (27), “excellent at 98.7” (25).

Evidence cited: 98.7% (50), 65min (18), 275.95u (9), 5.0min (3), 56mg/dl (3), 100% (2), 65.0min (2), 19.7u (2), 10h (2), 5min (2), 60min (1).

## step findings: safety_overview

### 50 runs

**Shared reasoning**

- (47/50) Hypoglycemia clusters in two clear windows: overnight (00:00–03:00 local, peaking at 18.5% TBR at 01:00 local) and late afternoon (18:00–20:00 local, peaking at 15.3% TBR at 19:00 local).

**Varying reasoning**

- (25/50) Total Time Below Range (<70 mg/dL) is 5.1%, exceeding the clinical target of <4.0%.
- (25/50) Extreme lows down to 41-42 mg/dL were recorded.
- (6/50) Mean glucose is 121.6 mg/dL with CV of 32.6%.
- (5/50) Overall glycemic control is high (86.0% TIR), but hypoglycemia risk is elevated at 5.1% TBR with recurrent severe dips (<50 mg/dL).
- (4/50) Overall glycaemic control shows good average glucose (121.6 mg/dL) and TIR (86.0%).
- (4/50) TAR (>180 mg/dL) is 8.9%, peaking during afternoon hours (12:00-17:00 local time, TAR 32.1% at 16:00).
- … 5 more varying points

Points made by a single run only: 9.

Phrases used by at least half the runs: “00 local” (34), “19 00 local” (26).

Evidence cited: 5.1% (46), 19:00 (40), 18.5% (37), 15.3% (35), 86.0% (31), 4.0% (30), 03:00 (29), 18:00 (28), 00:00 (26), 42mg/dl (24), 01:00 (19), 70mg/dl (17).

## step findings: basal_targets

### 50 runs

**Varying reasoning**

- (27/50) However, the overnight target of 90 mg/dL between 23:00 and 08:00 provides insufficient safety margin during 00:00-04:00, forcing frequent low-temp basal suspensions.
- (7/50) Morning fasting (04:00–08:00) is highly stable (TIR 95.2%–98.7%), confirming 0.7–0.8 U/h morning basal is accurate.
- (7/50) Morning fasting (05:00-08:00) is stable.
- (5/50) Evening basal step-up to 0.7 U/h at 19:00 coincides with 15.3% TBR.
- (5/50) Fasting morning basal (05:00-08:00) is stable.
- (4/50) Fasting glucose from 04:00 to 07:00 local is highly stable (mean 99.5-106.0 mg/dL, TIR >95%).
- … 12 more varying points

Points made by a single run only: 34.

Phrases used by at least half the runs: “90 mg/dl” (47), “target of 90” (28), “overnight target” (28).

Evidence cited: 90mg/dl (47), 08:00 (27), 00:00 (22), 0.7u/h (21), 0.6u/h (21), 0.8u/h (17), 05:00 (16), 19:00 (15), 23:00 (13), 18.5% (13), 03:00 (12), 04:00 (11).

## step findings: profile_cr_isf_dia

### 50 runs

**Varying reasoning**

- (24/50) Profile ISF is flat at 56 mg/dL/U with dynamic ISF active (70% adjustment factor).
- (21/50) Profile ISF is flat at 56 mg/dL/U with DIA at 10.0h.
- (9/50) DIA is set to 10.0 hours.
- (8/50) CR values cannot be directly validated due to zero logged carb entries.
- (8/50) DIA is set to 10.0 hours (appropriate for oref1 exponential model).
- (6/50) During high glucose spikes (>180 mg/dL), dynamic ISF aggressively strengthens effective ISF down to 27.8–37.9 mg/dL/U.
- … 10 more varying points

Points made by a single run only: 34.

Phrases used by at least half the runs: “56 mg/dl/u” (47), “dynamic isf” (45), “10.0 hours” (31).

Evidence cited: 56mg/dl (47), 10.0h (37), 70% (30), 38mg/dl (11), 10h (9), 37.9mg/dl (9), 13.2g/u (8), 4h (7), 200mg/dl (6), 16:00 (5), 14:00 (4), 27.8mg/dl (4).

## step findings: automation_smb_uam

### 50 runs

**Varying reasoning**

- (19/50) SMB and UAM are both enabled with smb_always_enabled=true.
- (8/50) AAPS relies entirely on UAM and SMB microboluses to cover unannounced meals.
- (6/50) This causes delayed insulin delivery relative to meal spikes, leading to high glucose at 13:00–16:00 followed by late insulin stacking crashes at 18:00–19:00.
- (5/50) SMB and UAM are continuously active.
- (4/50) SMB and UAM are both enabled (max UAM SMB basal minutes = 20 min, interval = 3 min).
- (3/50) The system relies entirely on UAM logic and 3-minute SMB microboluses for prandial coverage.
- … 7 more varying points

Points made by a single run only: 49.

Phrases used by at least half the runs: “smb and uam” (27).

Evidence cited: 20min (11), 3min (8), 19:00 (6), 16:00 (6), 18:00 (5), 100% (4), 4h (3), 13:00 (3), 5.9u (3), 1.6u (2), 2h (2), 32.1% (2).

## step findings: automation_sensitivity_limits

### 50 runs

**Shared reasoning**

- (39/50) Max IOB of 25.0 U exceeds 125% of TDD (~19.7 U/day), and Max Basal of 12.0 U/h is 15x–24x scheduled basal rates.

**Varying reasoning**

- (13/50) AAPS safety limits are dangerously high relative to patient insulin requirements.
- (11/50) Dynamic ISF is active (70% adjustment factor) while Autosens is disabled.
- (3/50) AAPS safety limits are set excessively high (`max_iob_units: 25 U`, `max_basal_u_per_hour: 12 U/h`) relative to total daily insulin (~19.7 U/day).
- (3/50) Dynamic ISF (70%) aggressively shrinks effective ISF to 27-38 mg/dL/U during postprandial spikes >200 mg/dL.
- (3/50) These limits provide minimal protection against over-dosing during sensor noise or unannounced meal spikes.
- (2/50) Critical safety hazard identified in system limits: Max IOB is set to 25.0 U (127% of average TDD ~19.7 U), eliminating software safeguards against loop over-dosing.
- … 3 more varying points

Points made by a single run only: 31.

Phrases used by at least half the runs: “max iob” (40), “19.7 u/day” (39), “max basal” (35), “total daily” (32), “safety limits” (30), “total daily dose” (25).

Evidence cited: 19.7u (47), 25u (26), 25.0u (24), 12u/h (23), 12.0u/h (22), 70% (18), 0.8u/h (14), 125% (14), 127% (6), 28mg/dl (2), 27.8mg/dl (2), 37.9mg/dl (2).

## step findings: meal_bolus_strategy

### 50 runs

**Varying reasoning**

- (21/50) Post-prandial glucose peaks at 14:00–16:00 local (averaging 162.8 mg/dL with 32.1% TAR at 16:00 local) trigger heavy late-stage insulin delivery, causing predictable hypoglycemia at 18:00–20:00 local.
- (4/50) GLP-1 co-therapy delays gastric emptying, stretching meal absorption over 4-6 hours.
- (4/50) Observed execution shows 100% unannounced meals with 0 logged carbs.
- (3/50) Complete reliance on UAM for meal coverage causes delayed insulin delivery.
- (3/50) The complete absence of pre-meal boluses forces reactive UAM SMB stacking during postprandial glucose surges.
- (3/50) User executes 100% unannounced meal dosing via loop automation.
- … 11 more varying points

Points made by a single run only: 52.

Evidence cited: 16:00 (29), 19:00 (25), 32.1% (20), 15.3% (20), 100% (16), 18:00 (14), 14:00 (13), 162.8mg/dl (11), 20:00 (6), 17:00 (6), 293mg/dl (4), 2h (3).

## step findings: meal_ecarbs_absorption

### 50 runs

**Varying reasoning**

- (10/50) Notes indicate GLP-1 receptor agonist therapy (1.25mg doses on Aug 14, 17, 20), which delays gastric emptying.
- (9/50) Absorption model uses min_5m_carbimpact=8 mg/dL/5 min and 7h max absorption.
- (6/50) GLP-1 therapy (1.25mg) delays gastric emptying, extending carbohydrate absorption across 4-6 hours.
- (5/50) No extended carb or e-carb entries are present in telemetry.
- (4/50) No extended carbs (e-carbs) are logged.
- (2/50) Without carb entries or eCarb logs, slow-absorbing meals trigger prolonged UAM delivery and dynamic ISF strengthening, causing delayed insulin accumulation and late postprandial lows.
- … 4 more varying points

Points made by a single run only: 58.

Evidence cited: 5min (15), 8mg/dl (15), 7h (9), 6h (9), 5h (6), 7.0h (4), 8.0mg/dl (2), 17:00 (2), 4h (2), 10:00 (1), 16:00 (1), 13:00 (1).

## step findings: synthesis_plan

### 50 runs

**Varying reasoning**

- (14/50) Prioritized action plan: First, correct dangerous AAPS safety limits (Max IOB and Max Basal).
- (12/50) The primary clinical driver of hypoglycemia is an aggressive overnight target (90 mg/dL) combined with unannounced meal insulin stacking under GLP-1 therapy, exacerbated by excessively wide safety limits (Max IOB 25 U, Max Basal 12 U/h).
- (12/50) 2) Raise overnight target to 100 mg/dL;
- (7/50) 3) Dampen Dynamic ISF adjustment factor from 70% to 50% to prevent late postprandial SMB stacking.
- (6/50) 3) Initiate explicit meal carb logging with prebolusing.
- (5/50) 2) Raise overnight glucose target from 90 mg/dL to 100 mg/dL (23:00-08:00) to eliminate nocturnal hypos.
- … 14 more varying points

Points made by a single run only: 64.

Phrases used by at least half the runs: “max iob” (39), “max basal” (32), “safety limits” (30), “overnight target” (27), “90 mg/dl” (25).

Evidence cited: 90mg/dl (25), 25u (20), 100mg/dl (19), 12u/h (13), 70% (8), 00:00 (8), 0.6u/h (7), 50% (6), 18.5% (6), 15min (4), 5.1% (4), 3.5u/h (3).

## meal strategy

### 50 runs

**Varying reasoning**

- (17/50) Complete reliance on UAM delays insulin delivery, causing postprandial spikes (TAR 32.1% at 16:00 local) followed by late insulin stacking and hypoglycemia (15.3% TBR at 19:00 local, 18.5% TBR at 01:00 local).
- (14/50) Transition from 100% unannounced meals (UAM) to logging meal carbohydrates with a 10-15 minute prebolus delivering 60%-70% upfront bolus.
- (9/50) Announce main meals with a 10-15 minute pre-bolus delivering 100% upfront bolus for standard meals, and use e-carbs over 2-3 hours for high-fat or slow-absorbing meals.
- (5/50) Pre-bolusing aligns peak insulin action with carb absorption, preventing afternoon spikes (14:00–16:00 TAR up to 32.1%) that currently force Dynamic ISF to over-dose insulin and cause late evening hypoglycemia (18:00–19:00 TBR 15.3%).
- (5/50) GLP-1 therapy slows gastric emptying.
- (4/50) If logging carbohydrates, prebolus 10-15 minutes before eating with a 50-70% upfront bolus, and enter complex or slow-digesting meals under GLP-1 therapy as extended carbs (e-carbs) spread over 3-5 hours to prevent late SMB over-dosing.
- … 14 more varying points

Points made by a single run only: 83.

Phrases used by at least half the runs: “15.3 tbr” (28), “15 minute” (26).

Evidence cited: 15min (45), 100% (37), 19:00 (35), 15.3% (33), 16:00 (21), 32.1% (18), 4h (15), 14:00 (9), 50% (9), 18:00 (9), 3h (8), 70% (7).
