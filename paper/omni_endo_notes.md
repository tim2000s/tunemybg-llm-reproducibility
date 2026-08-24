# Omni-Endo AI review notes (24 August 2026)

Code review of github.com/rilhia/omni-endo-ai (public/index.html, server.js, README; MIT,
free, self-hosted; Glooko + Omnipod 5; copy-paste prompt into a user-chosen chat model).
Decision: left out of the JDST pieces; Tim has raised the findings with the developer and we
wait on their response. The drafted issue text is at omni_endo_issue.md (not posted by us).

## Key issues found

1. No model pinned, no sampling control: the study's variability findings apply unchanged.
2. Mandatory web-research phase adds a second stochastic input.
3. Multi-phase workflow compounds variance: the model picks the 48 to 72 hour deep-dive
   window, so early draws redirect what data is examined.
4. No validation of any kind (also no pretence of one, unlike TuneMyBG).
5. Deep-dive Timeline export omits basal delivery (server requests only cgmHigh/cgmNormal/
   cgmLow/deliveredBolus) while advertised "best for... long-term basal efficacy": the
   bolus-only trap one phase later.
6. Units: "mmol/L" hard-coded onto settings and averages; GMI formula assumes mmol; the
   mg/dl toggle converts only user-typed thresholds. An mg/dl account gets a
   self-contradictory prompt.
7. UTC/local mixing: Z-format mandated, hourly trends use browser getHours(), event times
   via toLocaleString with no zone.
8. Persona priming: asserts SmartAdjust 48-72h TDI weighting and a "2-hour DIA constraint"
   as premises; "tough love" register ordered.
9. Glooko credentials into a local scraper; fine self-hosted, hazardous deployed for others.
10. Default window 24 hours, too short for the pattern claims invited.

Better than TuneMyBG: complete TDD with basal/bolus split in the summary stats; README warns
users to disable chat training before pasting; free and open about what it is.

## Parameter responses an audit would plausibly return

| Parameter | Likely response | Variance risk |
|---|---|---|
| Target segments | raise/lower | high; O5 only allows 110 to 150 mg/dl in 10 mg/dl steps, proposals may not exist on the pump |
| ISF segments | strengthen/weaken corrections | highest (cf. TuneMyBG 30 to 180) |
| Carb ratios | adjust from post-meal spikes | high, confounded by unlogged carbs |
| DIA | shorten toward the asserted 2 h | high; assertion echoed (DeepSeek DIA-collapse pattern) |
| Max basal | lower as unused headroom | the max-IOB reflex; also mostly a manual-mode setting |
| Basal:bolus split | declare ratio wrong | medium; unauditable at deep-dive (no basal data) |
| Manual overrides | stop correcting, let it learn | medium, tone amplified by persona |
| Auto-mode % | urge more auto time | low |
| Critical Interest Window | different 48 to 72 h per run | structural; redirects the whole second phase |
