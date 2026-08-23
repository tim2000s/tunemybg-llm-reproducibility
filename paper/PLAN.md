# Paper plan: reproducibility of an LLM-mediated insulin-settings adviser

See also JOURNAL_AND_STRUCTURE.md (2026-08-22): journal choice (JDST original article plus
companion commentary, DT&T as the single-paper alternative), methods borrowed from the two
Diabettech preprints, pre-registrable hypotheses, section blueprints and the reference pool.

Target: Journal of Diabetes Science and Technology, original article. Limits from the JDST author
instructions: 3,000 words (main text), structured abstract of up to 250 words with the headings
Background, Method, Results, Conclusions; 4 to 6 keywords in alphabetical order; sections
Introduction, Methods, Results, Discussion, Conclusions; numbered references in biomedical
(Vancouver) style cited in order of appearance; tables in Word; figures embedded and also supplied
as separate files (line art 900 to 1200 ppi); an ethics or waiver statement and a consent statement
in the Methods; Declaration of Conflicting Interests and Funding sections; AI tools may not be
authors and any writing assistance must be disclosed.

Writing constraints: see `~/.claude/CLAUDE.md`. Calm, British, balanced; no bullets in the
manuscript except where a list is unavoidable; no em-dashes; no triplets; no punchy single
sentences. Write only when all results are in.

## Working title

"Same data, different answers: reproducibility of insulin-settings recommendations from a
commercially distributed LLM-prompting application for AndroidAPS users"

Alternative: "Reproducibility and regulatory status of a paid LLM-based settings adviser for
do-it-yourself automated insulin delivery".

## The argument in one paragraph

A paid Android application, marketed as a digital endocrinologist, packages a user's Nightscout
telemetry and AndroidAPS profile into a JSON file and a fixed sequence of four prompts, which the
user pastes into the large language model of their choice; the model's final JSON is pasted back
and the app converts it into settings recommendations. We replicated that workflow exactly, with
the app's own package and prompts, against five models (Gemini 3.6 Flash, Gemini 3.1 Pro,
GPT-5.6-sol at medium effort, Claude Opus 5, Claude Sonnet 5), 50 fresh conversations each where
cost allowed, and measured agreement within a model and between models. Structured decisions
are fairly stable within a model but the numbers attached to them are not, the headline
recommendation forks between competing explanations of the same evidence, and the models
disagree with one another about what, if anything, should change. Because the application's
intended purpose is to produce recommendations for changing insulin-delivery parameters, we
argue that it meets the definition of a medical device and that Rule 11 of the EU MDR places it
in Class IIb, a conclusion the forthcoming UK regulations will extend to Great Britain. The
discussion weighs this against the manufacturer's position (decision-support only, the LLM does
the analysis, the app merely prepares data) and against the practical reality that people were
already asking LLMs these questions before the app existed.

## Outline

### Abstract (structured, ≤250 words)
Background: DIY AID users increasingly ask LLMs to review settings; a paid app now formalises
this. Method: replicate the app's four-prompt workflow with its own package and prompts via
provider APIs, N fresh conversations per model, validate with the app's rules, one correction
round; measure per-setting decision agreement, suggested-value dispersion, headline stability,
reasoning overlap. Results: key numbers per model (to fill). Conclusions: measured statement on
reproducibility and the regulatory implication.

### Keywords (alphabetical, 4 to 6)
artificial intelligence; automated insulin delivery; large language models; medical device
regulation; reproducibility; type 1 diabetes

### Introduction (~600 words)
1. DIY AID (AndroidAPS) and the settings problem: basal, CR, ISF, DIA, targets and the oref
   automation limits are tuned by the user; Autotune exists but many rely on community advice.
2. People have been putting this question to LLMs for some time. Cite the Diabettech pieces
   (factual questions across seven LLMs, June 2025; ChatGPT Health conversations and the Boost
   AndroidAPS case study, January 2026) and the Diabettech/JMIR carbohydrate-consistency study
   (inter-user reproducibility of ChatGPT 5-2 carb estimates), plus the wider literature on LLM
   diabetes advice (education accuracy, CGM summarisation case study, Diabetes and Endocrinology
   SCE performance) and on LLM non-determinism (sampling temperature, floating-point and
   batching effects, provider-side variation even at temperature 0).
3. The app under study: the first paid product of this kind on Google Play; what it does and
   what it says about itself ("prepares data for review only", "decision-support content only").
4. Two questions: how reproducible is the advice, and what is the app's regulatory position?

### Methods (~800 words)
1. Materials. The package and the four prompts were copied verbatim from the app (package
   version 10, template general_audit); the correction prompt was copied from the app's
   rejection screen. Two packages: the app's synthetic demonstration package (control: near-
   perfect glucose) and a real 14-day package from one adult with type 1 diabetes using
   AndroidAPS (own data; consent and ethics statement; no identifiable data in the package beyond
   UUIDs and time zone). Describe the real package briefly (86.0% TIR, 5.1% TBR, CV 32.6%,
   coverage 98.7%, no carbohydrate entries, DIA 10 h, 23 inventory items).
2. Replication of the workflow. New conversation per run; package attached with Prompt 1;
   Prompts 2, 3, 4 sent in turn after each response; provider defaults for sampling; models and
   versions recorded per turn; dates. Claude via the official SDK, Gemini and OpenAI via REST.
   Reasoning effort as set (GPT: medium, matching the ChatGPT picker; Claude: default adaptive;
   Gemini: default). Justify API rather than the chat UI and state the caveat.
3. Validation and the correction loop. The app's acceptance rules reconstructed from Prompt 4 and
   required_output_schema (list them); the app's correction prompt sent once with the violated
   section paths; record first-pass and post-correction acceptance and whether the correction
   changed any decision.
4. Outcome measures. (a) format acceptance; (b) per-setting decision agreement (modal decision
   share; entropy; mean across settings as a stability index); (c) suggested-value dispersion for
   settings changed in more than one run (range, median, mode, number of distinct values,
   direction); (d) headline stability (profile_recommendation focus and decision; first
   recommendation area); (e) pairwise change-set Jaccard; (f) reasoning analysis (sentence
   clustering by TF-IDF cosine, shared vs varying points, evidence-citation rates); (g) between-
   model agreement on modal decisions; (h) cost and latency. Wilson 95% CIs for proportions.
   Comparison of suggested values with AndroidAPS code defaults (master 598e2eb, 2026-08-02).
5. Regulatory assessment method. Apply the MDR Article 2 definition and Annex VIII Rule 11 with
   MDCG 2019-11; UK MDR 2002 as in force and the draft 2026 amendment; FDA CDS criteria; Google
   Play health policy. State what was examined (listing, in-app text, privacy policy).
6. Software availability (the harness, open source) and data availability (all JSON outputs).

### Results (~800 words, mostly tables and figures)
Table 1: models, versions, effort, runs, dates, tokens and cost per run, time per run.
Table 2: acceptance by the app's checks: first pass, after correction, failure taxonomy per model
 (enum slips, dropped sections, lost braces, extra keys).
Table 3: per-setting change frequency and suggested-value range by model, with current value and
 AAPS default (the summarise_runs comparison table, trimmed to settings changed by any model).
Figure 1: workflow diagram (app → package + prompts → LLM → JSON → app check → correction).
Figure 2: heatmap, runs × settings, one panel per model (keep / change / verify).
Figure 3: suggested values for the contested settings (max IOB, max basal, overnight target,
 midnight basal, DynISF factor) as strip plots per model, with current value and AAPS default.
Figure 4 (or table): headline focus distribution per model.
Table or short subsection: handling of the missing carbohydrate data (Tim does not log carbs,
so the package has 0 carb entries and an empty declared meal strategy). Per model: whether the
output notices, whether any CR is changed regardless, whether the CR rationale cites the
absence of carb data and calls CR untestable, whether meals are inferred from glucose shape
(UAM, "unannounced"), whether the user is told to start logging and whether that is the first
recommendation, and how the meal_bolus_strategy step is scored (status and confidence) given
it cannot be done. Generated by carb_handling.py (results/carb_handling.md), with
representative CR rationales per model.
Text: within-model stability index per model; the target-versus-basal fork in Gemini Flash;
 safety-limit numbers (26 distinct pairs in 49 runs); control package (all keep in 50/50);
 between-model disagreement (Gemini: tighten limits and raise target; Opus: DIA/ISF; GPT: keep);
 reasoning results (same evidence cited by nearly every run, different conclusions).

### Discussion (~700 words)
1. What reproducibility means for a user: a single run is one draw from a distribution; the
   direction is often stable but the number is not; the headline can flip between two
   defensible stories; different models give different advice on the same data.
2. Why: sampling, long outputs, the prompts' instruction to choose between competing
   explanations, missing data (no carbs) handled differently.
3. The app's checks: they catch format, not substance; the correction loop never changed a
   decision in our runs but also never questioned one.
4. Data protection: the package is special-category health data; consumer ChatGPT and Gemini
   train on conversations by default unless the user opts out; the user, not the app, is the
   data controller of that transfer; what the app discloses.
5. Regulation. Definition: software intended by the manufacturer to be used for a medical
   purpose; the app's intended purpose is to obtain and present recommendations to alter
   insulin-delivery parameters, a therapeutic decision. Rule 11: information used for
   therapeutic decisions is IIa; where a wrong decision may cause serious deterioration
   (severe hypoglycaemia, DKA) it is IIb; MDCG 2019-11 and the IMDRF categories (serious
   situation, drive clinical management). Counter-arguments: the manufacturer's framing as a
   data-preparation tool; the LLM is a third-party general-purpose model outside the
   manufacturer's control; disclaimers; the user is the decision-maker. Response: intended
   purpose is judged from the product as a whole and its marketing ("digital endocrinologist");
   the LLM is a component the manufacturer has designed around (prompts, schema, checks);
   disclaimers do not change intended purpose under MDCG 2019-11. Great Britain today (Rule 12,
   Class I, self-declaration and MHRA registration still required) and the 2026 draft alignment.
   FDA: patient-facing dosing recommendations fall outside the CDS exemption. Google Play:
   medical-device declaration. Keep the tone measured: we state the reading and the basis, and
   note that classification is ultimately for the manufacturer and competent authority.
6. Limitations: API rather than chat UI (system prompts, file handling); one real package, one
   person; reconstructed validator; one correction round; model versions drift; sample sizes
   for Claude; the study measures consistency, not correctness (no clinical ground truth).
7. What would help: pinning model and temperature, ensembling over several runs and showing
   the distribution, surfacing competing hypotheses rather than choosing, clinical validation.

### Conclusions (~150 words)

## How the app renders the JSON (13 screenshots, 2026-08-22, demo package result)

Screen title "Analysis result". Order, top to bottom:
1. Hero card "Primary profile recommendation" with three chips (decision rendered as "Keep
   unchanged" or change; focus, e.g. "CR"; confidence), the `recommendation` text in bold, the
   `rationale`, and a "Next verification" box (`next_check`). This is `profile_recommendation`
   verbatim, so the target-versus-basal fork and the focus label are the first thing a user sees.
2. "Summary" card (`summary`).
3. "Final parameter decision table": "A concrete list of parameters to review, keep, or clarify.
   TuneMyBG never applies these items automatically in AAPS." Two groups with row-count badges
   (Profile 16/16, AAPS settings 6/6; the app counts rows against the inventory). Unchanged
   profile rows are collapsed into "Remaining profile parameters (16)", so changed rows are what
   the user sees expanded. AAPS rows are a horizontally scrolling table: Parameter, Current
   value, Suggested value ("Not suggested" when null), Decision chip (Keep unchanged, Verify,
   and presumably a change chip), Rationale/notes. Suggested values are shown verbatim, so the
   numeric spread between runs is exactly what different users would see.
4. "Meal and e-carb strategy" card with confidence chip, `suggestion` in bold, `rationale`,
   "Exceptions to the overall strategy" (pattern: suggestion) and "Most useful next observation".
5. "Strengths" and "Issues" as bullet lists.
6. "Recommendations" grouped under the `area` string upper-cased verbatim (CR, SMB,
   MEAL_STRATEGY), each with title and description and a four-way status selector New /
   Planned / Applied / Skipped. The status feeds `analysis_context.recent_results` for the next
   analysis, so the app runs a change-management workflow around the model's advice, which
   matters for the intended-purpose argument. Inconsistent `area` strings from the models
   (safety_limits, aaps.core.safety_limits, automation, limits) will appear as separate headings.
   Priority is not visibly rendered.
7. "Implementation steps", "Education", "Safety notes" as bullets (safety notes include the
   "decision-support content only" sentence and "No AAPS setting should be changed
   automatically from this analysis").
8. "Full analysis flow" behind "Show technical analysis details": numbered stages with status
   (Completed / Partial) and confidence, expanding to Findings, Evidence, Dependencies, Missing
   data. Four stages have friendly titles and four show the raw key with underscores removed
   ("profile cr isf dia", "automation sensitivity limits"), an incomplete label map.

Rejection behaviour (tested by Tim 2026-08-22 with two real unparseable outputs): the app
shows "Paste a valid JSON response from AI." and offers no correction prompt. The section-
correction prompt appears only when the JSON parses but fails the checks. So an unparseable
first pass is a dead end in the app's own workflow; the harness's corrections for those runs
are a what-if, not the app. Report app-faithful outcomes in four classes: accepted first time;
accepted after the correction prompt; invalid JSON with no correction offered; still rejected
after correction.

Repair prompt structure (screenshot 2026-08-22, "Paste AI result" screen, fenced Llama sample
pasted while the app held the demo package): header "The AI response is incomplete for this
package. Use the repair prompt below in the same AI conversation." Box "The result is not
complete yet" with counts ("AI returned 23 of 22 required parameter decisions"), then lists:
"Missing parameters (n)" by label, "Invalid or missing stable keys (n)" by parameter_key,
"Current values not copied from the package (n)". The prompt is composed of a fixed opening
line, one clause per error type ("Add exactly these missing parameter_key values: …", "Remove
these keys because they are not in decision_inventory: …", "Copy current_value exactly from
decision_inventory for: …", and "Correct these sections according to required_output_schema:
…" for other errors) and a fixed closing line. Buttons: "Copy repair prompt" and "Paste from
clipboard and check". The app parsed JSON wrapped in ```json fences, so fences are not a
rejection. The harness now composes the prompt the same way (tunemybg_repro/prompts.py).
Fidelity caveat: corrections already run before this change used the single "Correct these
sections" clause for row and current_value errors (Llama 28 runs, DeepSeek several, Sonnet 2,
Flash-Lite a few); the outcome class is unaffected but the wording differed. Re-run those
correction turns if time allows.

The app's actual acceptance rules (25 samples pasted by Tim, 2026-08-22; harness reproduces
23/23 verdicts). Repair prompt (three error types only): decision rows missing from or not in
decision_inventory ("Add exactly these missing parameter_key values" / "Remove these keys
because they are not in decision_inventory"); current_value not copied ("Copy current_value
exactly from decision_inventory for"); profile_recommendation.focus outside the five values
("Correct these sections according to required_output_schema: profile_recommendation.focus").
Hard stop with "The AI response does not match the TuneMyBG schema." and no prompt (one case
crashed the session): a required string field absent, observed for a decision row without
`rationale` (misspelt) and a profile_recommendation without `recommendation`; a missing
`suggested_value` or `data_gaps` is tolerated. Invalid JSON: "Paste a valid JSON response from
AI." and no prompt. Accepted despite breaking Prompt 4: a missing `issues` section, extra keys
anywhere, status/confidence words outside the allowed set ("partial" as a confidence,
"medium-high"), priority words outside the set, a trailing ``` fence, fenced JSON. So the app
enforces identity and copy integrity of the decision table and one enum, and nothing about the
narrative or the quality fields. The current_value comparison is an exact string match: GPT-5.4-
mini run 18 wrote "…/5m" for "…/5 min", was asked to copy the value exactly, wrote "…/5m"
again, and the app (tested 2026-08-22) issued the identical repair prompt a second time, so a
user can be sent round the same loop with no change in the model's behaviour. Paper point: the prompt's rules are aspirational; the app's
checker is structural; whatever the model writes in between reaches the screen.

Pricing ("Unlock Pro" screen, 2026-08-22): a free tier with a limited number of saved
analyses and 7 or 14 day ranges; Pro at £4.49/month, £31.49/year ("only £2.62/mo", 42% off)
or £71.99 lifetime, giving unlimited AI analyses, 30-day analysis, analysis history and
recommendation progress tracking. "Subscription auto-renews. Cancel anytime." Note the paid
features are the workflow ones (history, progress of applied changes), which again describes
a settings-management tool rather than a data exporter.

On the phrase "digital endocrinologist": the app does not use it anywhere we have seen, and
Tim's view is that it should not be used as a quotation. The paper and the article should
instead characterise the role from the app's own description: it prepares the data, prescribes
the analysis sequence, validates the result and tracks the user's implementation of the
recommended changes, which is the work an endocrinology review would do, with the reasoning
outsourced to whichever model the user opens. The article theme therefore needs rewording
(for example "A settings review for £4.49 a month, from whichever chatbot you happen to open").

Play listing URL: https://play.google.com/store/apps/details?id=com.adamkowalczyk.tunemybg
(developer shown as "Adam Kowalczyk 81"; updated 20 August 2026; in-app purchases listed). The
page HTML fetched on 22 August 2026 contains no "Medical device" label, which Google Play
displays for apps declared as regulated under MDR; relevant to the commentary.

Not yet seen: the input/upload flow; what the free tier's analysis limit is.

## Play Store listing and in-app disclaimers (screenshots 2026-08-22)

Listing (version 1.0.5, updated 20 Aug 2026, "1+ downloads", PEGI 3). Tagline: "AI ready
Nightscout data for safer AAPS tuning". Body: "TuneMyBG helps AndroidAPS users turn Nightscout
data into a structured package for AI analysis. The app is designed for people who want to
better understand their AAPS settings and review data in a more organized way before making
changes." Feature list: choose a 7, 14 or 30 day range; connect Nightscout and other supported
data sources; generate a reusable AI-ready data package; follow a guided analysis flow with
four focused prompts; review profile, SMB, bolus, e-carbs and safety context in one place; save
analysis history and track recommendation progress; learn what AAPS parameters mean with
built-in education screens. Closing: "TuneMyBG does not replace medical advice. It is a tool
for organizing data, preparing prompts, and helping users think through possible profile
improvements more safely and clearly."

Onboarding screen "Your safety matters more than an AI result": "TuneMyBG organizes data and
recommendations, but does not replace professional medical advice." "AI can make mistakes or
draw conclusions from incomplete data." "Do not change settings solely based on an app result.
Verify recommendations and make changes cautiously." Amber box: "You use the app and make
decisions at your own risk." Mandatory tick: "I understand the limitations and safe-use rules."

Use in the paper: the manufacturer's own description of intended purpose is "safer AAPS
tuning", "possible profile improvements" and "track recommendation progress"; that is a
therapeutic-decision purpose in MDR Article 2 terms whatever the disclaimer says, and MDCG
2019-11 treats disclaimers as not altering intended purpose. The "at your own risk" clause is
a contractual allocation of risk, not a regulatory one. Note the listing does not itself use
the phrase "digital endocrinologist"; attribute that phrase to wherever it actually appears
(website, social media, in-app copy) or do not use it as a quotation.

## Evidence inventory

Done (2026-08-22, all re-validated with the app-faithful validator; demo package kept at
paper/demo_package.json): Gemini 3.6 Flash on the demo package (50, control, all keep);
on the real package: Gemini 3.6 Flash (50), Gemini 3.1 Pro (50), Gemini 3.5 Flash-Lite (50),
GPT-5.6-sol medium (50), GPT-5.4-mini medium (50), Claude Opus 5 (20), Claude Sonnet 5 (20),
Claude Haiku 4.5 (28 of 50, credits exhausted), DeepSeek V4 Pro (50), Grok 4.6 (50), Llama 4
Maverick (50). Eleven-model comparison at results/comparison_real_package.md. Local Qwen 9B
pilot (1) for the appendix only. Cost: Opus $2.82/run, Sonnet $1.02, Haiku $0.29; Gemini,
OpenAI and OpenRouter not priced from usage (read from dashboards at writing time).

Still to do once batches finish:
1. summarise_runs.py and reasoning_runs.py for every experiment; one combined comparison.
2. Add Wilson CIs and a between-model agreement table to analyse.py.
3. Figures 2 and 3 (matplotlib; load the dataviz skill first).
4. Failure taxonomy table from first_pass_sections across models.
5. Cost table from recorded usage (Claude priced from usage; Gemini and OpenAI need current
   list prices from their pricing pages on the day of writing).
6. Regulatory section sources to pin down with exact citations: EUR-Lex CELEX 32017R0745 Annex
   VIII Rule 11 and Article 2(1); MDCG 2019-11 (PDF saved locally, needs text extraction);
   MHRA "Medical device stand-alone software including apps" (gov.uk, updated 2023) and the
   draft Medical Devices (Amendment) Regulations 2026 (11 May 2026); FDA CDS guidance
   (28 Sep 2022); Google Play Health Content and Services policy (medical-device declaration).

## Citation verification result (citations_runs.py, 2026-08-22)

Every figure with a unit quoted in the accepted JSONs was checked against the numbers in the
package (with rounding tolerance and the obvious derived quantities such as total insulin per
day). Verified rates: Gemini Flash 99.8%, Gemini Pro 99.9%, Flash-Lite 99.9%, GPT-5.6 99.9%,
GPT-5.4-mini 100%, Opus 97.0%, Sonnet 99.1%, Haiku 97.4%, DeepSeek 99.3%, Grok 99.1%, Llama
100% (Llama quotes very few figures: 457 in 46 runs against 4,823 for Flash). The residue is
thresholds (160, 250, 280 mg/dL) and small arithmetic (16.2 U, 0.27 U). Contrast with the
settings preprint, where 30 to 70 percent of cited glucose values were misattributed from raw
5-minute data: a structured, pre-aggregated package largely removes the citation problem. The
variability is in the conclusions drawn, not in the numbers quoted.

## Exact regulatory wording (from the saved MDCG 2019-11 PDF, paper/mdcg_2019_11.txt)

Rule 11 (as reproduced in MDCG 2019-11, section 4.2): "Software intended to provide information
which is used to take decisions with diagnosis or therapeutic purposes is classified as class
IIa, except if such decisions have an impact that may cause: death or an irreversible
deterioration of a person's state of health, in which case it is in class III; or a serious
deterioration of a person's state of health or a surgical intervention, in which case it is
classified as class IIb. Software intended to monitor physiological processes is classified as
class IIa, except if it is intended for monitoring of vital physiological parameters, where the
nature of variations of those parameters is such that it could result in immediate danger to
the patient, in which case it is classified as class IIb. All other software is classified as
class I." MDCG 2019-11 also states that Rule 11 "relates to the consequences of indirect harm
from failure to provide correct information" and "describes and categorises the significance of
the information provided by the active device to the healthcare decision (patient management)
in combination with the healthcare situation (patient condition)", and, on claims, that "any
claims, relating to the intended medical purpose of their MDSW are supported by clinical
evidence" (section 3.2, citing Article 7).

## Questions for Tim before writing

1. Play Store URL, developer name, price, and the exact marketing wording ("digital
   endocrinologist" and any claims of clinical benefit); whether the listing declares a medical
   device, CE or UKCA mark, and which countries it is sold in.
2. The app's privacy policy and any in-app statement about where the data goes.
3. Whose data the real package is, for the consent statement; and whether Diabettech Ltd is the
   author affiliation with a conflict statement covering T1Twin or other products.
4. Whether the app's rejection screen wording for unparseable JSON differs from the section
   version (ours is an assumption).
5. (Answered 2026-08-22) The app does not recommend or list any LLM; the choice is left to the
   user. Treat the model set as a sample of what users would plausibly pick. Tim's hypothesis
   is that the developer used Gemini Flash as the test bed; state only as a hypothesis,
   supported (not proven) by Flash having the highest first-pass acceptance, which is what one
   would expect of prompts iterated against a single model.
6. Whether to cite the carbohydrate-consistency manuscript as submitted/in press or as a preprint.

## Follow-on article (Diabettech, after the paper)

Brief from Tim (2026-08-22): an easy-to-read, calmly damning piece with pithy statements. Arc:
people are already using AI to analyse their diabetes data (yes, they are); so why go to an AI on
your own when an app will do it for you and charge you for the privilege; then the MDR
relevance; the variation within and across models and what that risk means for a user; and the
questions it raises about auditability and reproducibility of the data path for something that
is, on any sensible reading, a medical device. Needs a theme along the lines of "The world's
first digital endo. Why you shouldn't pay them" and an equally pithy sign-off. Global style
rules still apply (no em-dashes, no triplets, no sensational single sentences); pithy is fine,
shouting is not.

Theme and title candidates to refine once results are in:
"The world's first digital endocrinologist. Why you should keep your money."
"A digital endo for the price of a coffee. Ask it twice and see what happens."
"Same data, fifty answers: the paid app that outsources your insulin settings to whichever
chatbot you happen to open."

Sign-off candidates:
"Your endocrinologist may be slow to reply, but at least they give the same answer twice."
"An endocrinologist who changes their mind every time you ask is not one you would pay.
Neither is this."
"Keep the data. Keep the money. Ask a human."

Structure: open with the fact that people already do this (cite the June 2025 seven-LLM piece
and the January 2026 Health conversations post); introduce the app and its proposition; the
reproducibility results in plain numbers (one model, fifty runs, twenty-six different
safety-limit answers; a headline that flips one time in five; five models, several different
stories); the medical-device point (what Rule 11 says and why "decision support only" does not
get you out of it); the data-protection point (where the package goes, who trains on it); what
a responsible version would look like (pinned model, several runs, show the spread, a
declared classification); sign off.

## Candidate references (to verify at writing time)

Regulation (EU) 2017/745, Annex VIII Rule 11; MDCG 2019-11 Guidance on qualification and
classification of software; MHRA, Medical device stand-alone software including apps (2023);
MHRA draft Medical Devices (Amendment) Regulations 2026; FDA, Clinical Decision Support Software
guidance (2022); Google Play Health Content and Services policy; Street T, Diabettech, "In
conversation with… factual questions for LLMs" (2025); Diabettech, ChatGPT Health conversations
and Boost AndroidAPS case study (2026); Street T, consistency of carbohydrate estimation from
ChatGPT 5-2 (JMIR Diabetes, submitted); Braune/Lewis et al. on DIY AID safety (JDST); Scientific
Reports 2024 case study on LLM analysis of CGM data; medRxiv 2025 on accuracy and consistency of
ChatGPT for T2D management; Frontiers Digital Health 2026 on ChatGPT diabetes education; arXiv
2506.09501 on numerical sources of non-determinism in LLM inference; arXiv 2606.26185 on
temperature control and reproducibility; Poor performance of LLMs on the UK Diabetes and
Endocrinology SCE (2025); AndroidAPS documentation; nightscout/AndroidAPS source (defaults).
