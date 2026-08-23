# Journal choice and manuscript blueprint for the TuneMyBG study

Prepared 2026-08-22 from: the Diabettech article "I asked AI to count my carbs 27,000 times"
(15 April 2026), its preprint (Street T, "Reproducibility and accuracy of large language model
vision APIs for carbohydrate estimation from food photographs: a four-model batch comparison
with implications for automated insulin dosing", submitted to Diabetologia, 26,904 queries,
temperature 0.01), the companion settings preprint (Street T, "Frontier LLMs require explicit
clinical context to avoid training-data anchoring for insulin pump settings: a pre-registered
exploratory study", OSF 10.17605/OSF.IO/Q4UX9, April 2026), the DTN-UK statement on large
language models (Street T for DTN-UK, January 2026), and the author instructions of
Diabetologia, Diabetes Technology & Therapeutics, JDST and JMIR Diabetes.

## Where this study sits

The two preprints and this study form a sequence, and the manuscript should say so in the
Introduction. The carbohydrate paper measured within-image reproducibility of a single
structured prompt at near-zero temperature and translated the spread into insulin-dose risk.
The settings paper asked whether frontier models derive pump settings from patient data at
all, found them anchored to textbook values unless given the user's current settings, and
showed that 30 to 70 percent of the glucose values they cited were misattributed. The present
study closes the loop: it takes the first commercially distributed product that formalises
exactly this use (package, four prompts, validation, recommendation tracking, a subscription),
replicates its workflow verbatim against eleven models at the providers' default sampling,
and measures what the app's user would receive. It adds three things neither preprint had: a
real product with its own acceptance rules (reverse-engineered and verified against the app),
a within-model and between-model comparison on one real patient's data, and a regulatory
classification of the product. It also inherits the prior work's two headline risks, stochastic
variability and confident error, and shows both surviving the app's checks.

## Journal choice

Four realistic targets, judged on fit, format and timing.

Diabetologia (original article 4,000 words, up to 50 references, structured abstract with
Aims/hypothesis, Methods, Results, Conclusions/interpretation, a "Research in context" box,
ten keywords, mandatory AI-use disclosure; preprint citations allowed if from the current or
preceding year). The carbohydrate paper is already under review there, which is an argument
both ways: a second submission on the same theme could be welcomed as a series or deferred
until the first is decided. Diabetologia's readership is clinical and mechanistic; an app
evaluation with a regulatory discussion is at the edge of its scope.

Diabetes Technology & Therapeutics (original article 5,000 words, structured abstract up to
300 words, up to 8 tables and figures, at least four keywords, Sage Vancouver references,
graphical abstract required, preprints acceptable with DOI, mandatory AI disclosure). The
5,000-word allowance is the only one that lets the reproducibility results, the app's
validation behaviour, the carbohydrate-handling analysis and the regulatory classification
sit in one paper at full strength.

Journal of Diabetes Science and Technology (original article 3,000 words, structured
abstract Background/Method/Results/Conclusions up to 250 words, four to six keywords in
alphabetical order, numbered references, ethics and consent statements, no AI authorship).
JDST is where the DIY AID literature lives and where the app's users' clinicians read; it also
carries commentary articles (2,000 words), which suits the regulatory argument as a companion.
The 3,000-word limit is tight for eleven models plus an app plus a regulatory section.

JMIR Diabetes (IMRD original paper, structured abstract up to 450 words, AMA references,
generous length, article processing fee). The carbohydrate-consistency manuscript in
Downloads is formatted for JMIR Diabetes, and JMIR's digital-health readership is receptive
to regulatory and data-protection discussion, but the fee and the lower profile count against
it for this piece.

Recommendation: submit to JDST as two linked pieces, an original article on reproducibility
and the app's validation behaviour (3,000 words), and a commentary on the regulatory status of
LLM-wrapping settings advisers (2,000 words) that cites the original article. That keeps
each within its limit, puts the findings in front of the clinicians who will be asked about
this app, and gives the regulatory argument its own peer-reviewed home rather than a
discussion paragraph. If Tim would rather keep one manuscript, DT&T is the alternative: its
5,000 words and eight display items hold everything, and it accepts preprints, so the
Diabettech preprint route used for the other two papers can be repeated.

## Methods to borrow from the preprints

From the carbohydrate paper: coefficient of variation as the primary within-condition
reproducibility statistic, with range and a normality test (Shapiro-Wilk) for every
model-setting cell; Welch's t test with Cohen's d for between-model comparisons and
Mann-Whitney U where distributions are non-normal; translation of numeric spread into
clinical terms (there, units of insulin at 1:10; here, the spread of suggested max IOB, max
basal, target and ISF expressed against the user's actual daily insulin and the AAPS code
defaults); an explicit statement of temperature and model versions per call; a limitations
paragraph on model drift with the dataset and code released for longitudinal re-testing; and
a numbered recommendations list for application developers.

From the settings paper: pre-registration language (hypotheses stated before analysis, with
post-hoc analyses labelled as such), citation verification (check the glucose figures the
models quote, for example "18.5% below range at 01:00", against the package's
hourly_glucose_local table and report the exact-match rate per model), the distinction between
data-driven and prior-driven recommendations (here visible as the models' treatment of the
safety limits and of carbohydrate ratios they cannot test), and reporting of output failure
rates as a result rather than a nuisance.

From the DTN-UK statement: its policy points as the benchmark the app should be measured
against, in particular "all AI-suggested changes to insulin dosages, basal rates, or other
pump settings must be reviewed carefully and sense checked" and the warning about the model's
"instinct" to fill in missing information, which the carbohydrate-handling results illustrate
directly. Tim authored the statement as a DTN-UK committee member; this must be disclosed.

## Hypotheses to state in advance (register on OSF before writing, as for the settings paper)

H1 Within a model, the set of settings the app would show as "change" is not stable across
fresh conversations on identical input (primary: per-setting agreement below 0.95 for at least
one setting changed in a majority of runs).
H2 Where a model proposes a numeric change in most runs, the proposed value varies across
runs by more than the AAPS user-interface step for that setting.
H3 Models disagree with one another on whether any setting should change (modal decision
differs between at least two models for at least one setting).
H4 The app's acceptance check rejects a minority of first responses and its repair prompt
resolves most of them, but some responses are accepted while violating the prompt's own
rules.
H5 With no carbohydrate entries, models differ in whether they score the meal steps as
completed and in whether they tell the user to log carbohydrates before changing settings.
All five are supported by the data already collected; the point of stating them is to separate
them from the post-hoc observations (the Gemini target-versus-basal fork, the Llama basal
direction reversal, the DeepSeek ISF spread, the repeat-rejection loop).

## Blueprint: JDST original article (3,000 words)

Title (working): Same data, different answers: reproducibility of insulin-settings
recommendations from a commercial application that outsources analysis to the user's choice
of large language model.

Abstract (250 words, Background/Method/Results/Conclusions). Background: two sentences on
DIY AID settings tuning and the arrival of a paid app that packages data and prompts for any
LLM. Method: package and prompts copied from the app; 11 models; 50 fresh conversations each
(20 for Opus and Sonnet, 46 for Haiku); provider default sampling; outputs validated with the
app's own rules, verified against the app; outcomes: acceptance, per-setting decision
agreement, suggested-value spread, headline stability, between-model agreement, carbohydrate
handling. Results: the numbers from results/comparison_real_package.md and the per-model
reports (acceptance first time from 26% to 100%; dead ends up to 45%; stability index 0.915 to
0.998; safety limits lowered in 79 to 98 percent of Gemini Flash, Pro and Opus runs and never
by GPT, Sonnet or Grok; 26 distinct max-basal/max-IOB pairs in 49 Flash runs; ISF 30 to 180
mg/dL/U across DeepSeek runs; meal step marked completed in 98 to 100 percent of Flash-Lite,
Llama and Haiku runs with no carbohydrate data). Conclusions: one measured sentence on what a
user receives, one on what the app checks, one on the implication.

Keywords (alphabetical): artificial intelligence; automated insulin delivery; large language
models; medical device regulation; reproducibility; type 1 diabetes.

Introduction (450 words). DIY AID and settings tuning; people already ask LLMs (cite the
Diabettech factual-questions piece, the Health conversations post, the two preprints, Sng 2023,
Goncalves 2025, Joubert 2026); the DTN-UK statement; the app and its proposition (Play listing
quotes, price, no model recommended); two questions: reproducibility and what the app checks.
One sentence flags that the regulatory position is addressed in a companion commentary.

Methods (800 words). Materials (package version 10, verbatim prompts, the repair prompt and the
app's rejection behaviour established by pasting 25 outputs into the app; the demo package as a
control). Participant and ethics (one adult with type 1 diabetes, the author's own data, no
carbohydrate logging; ethics waiver statement; consent statement). Replication (new
conversation per run; attachment with Prompt 1; Prompts 2 to 4 in turn; provider defaults;
model IDs and dates; API rather than chat interface, with the caveat). Validation tiers (repair
prompt, schema stop, prompt-only; verified 23/23 against the app; app-faithful outcome classes).
Outcome measures (as in PLAN.md, plus citation verification against hourly_glucose_local).
Statistics (proportions with Wilson 95% CI; per-setting agreement and Shannon entropy; CV and
range for numeric suggestions; Shapiro-Wilk where n allows; pairwise Jaccard; reasoning
clustering method in one sentence with the supplement carrying detail). Software and data
availability.

Results (800 words, mostly Tables 1 to 3 and Figures 1 to 2). Table 1 models, versions, runs,
dates, cost, time. Table 2 app outcomes per model (five classes) plus the count accepted while
breaking the prompt's rules. Table 3 per-setting change frequency and suggested range for the
seven settings any model changed in more than 10 percent of runs, with current value and AAPS
default. Figure 1 workflow diagram including the app's validation and repair loop. Figure 2
strip plots of suggested values for max IOB, max basal, overnight target, midnight basal, ISF
and DynISF factor by model, with the current value and AAPS default marked. Text: the
within-model findings (stability indices, the Flash fork, the safety-limit arithmetic), the
between-model findings (three camps: change limits and target; keep everything; change
something else), the carbohydrate-handling table in brief, the repeat-rejection case.

Discussion (700 words). What a single run means for a user; why (sampling, output length,
prompts that instruct a choice between competing explanations, missing data handled
differently); the app's checks catch identity and copy errors and nothing about substance,
with the prompt's rules otherwise unenforced; no temperature control is available to a
chat-interface user and none would suffice; comparison with the preprints (the same two risks,
now inside a product); what a responsible design would do (pin the model, run several times,
show the spread, surface competing hypotheses, declare a classification); limitations (API not
chat UI; one person's data; reconstructed validator, though verified; one repair round; model
drift; sample sizes for Claude; consistency not correctness); the DTN-UK policy points as the
yardstick.

Conclusions (120 words).

Declarations: ethics (own data, waiver), consent, conflicts (Diabettech Ltd; DTN-UK committee
member and author of its statement; author of the cited preprints; no relationship with the
app's developer), funding (none; API costs self-funded, state the total), AI-use disclosure
(analysis code and drafting assistance from Claude, per JDST policy), data availability
(package minus identifiers, all 546 final JSONs, code, under a permissive licence on GitHub).

Supplement: S1 prompts verbatim; S2 repair prompt and the app's rejection screens; S3 validator
rules by tier with the 25-sample verification table; S4 per-model summary, tables and reasoning
reports (the PDFs already produced); S5 carbohydrate-handling table; S6 reasoning-cluster
method and CSVs; S7 demo-package control results.

## Blueprint: JDST commentary (2,000 words)

Title (working): Is an app that prepares your data and prompts for a chatbot a medical device?
The case of LLM-mediated insulin-settings advice.

Structure: the product and its own description of purpose (listing and disclaimer quotes,
pricing, the recommendation tracker); the MDR Article 2 definition and Annex VIII Rule 11 with
MDCG 2019-11 and the IMDRF categories, arriving at IIb with the reasoning shown; the
developer's best counter-arguments (data preparation only; the LLM is a third party; the user
decides; disclaimers and risk acceptance) and why MDCG 2019-11 does not accept them; Great
Britain today (UK MDR 2002, Rule 12, Class I, registration still required) and the draft
Medical Devices (Amendment) Regulations 2026; the United States (patient-facing dosing
recommendations outside the CDS exemption); Google Play's medical-device declaration; the
evidence from the original article that makes the classification matter (non-reproducible
numeric advice, unenforced rules, dead ends); data protection (special-category data sent to
consumer chat services that train on conversations by default; the user as the one making the
transfer); what compliance would require (intended purpose statement, risk management,
clinical evaluation, post-market surveillance, a pinned and validated model, and a declared
classification on the listing). Close with the DTN-UK position and a measured statement that
classification is for the manufacturer and the competent authority, with the reasoning here
offered for that process.

## Reference pool (to verify at writing; V = verified during this work, P = from the preprints)

Prior Diabettech work: Street T, carbohydrate reproducibility preprint, Diabettech, April 2026
(submitted to Diabetologia) P; Street T, settings anchoring preprint, OSF 10.17605/OSF.IO/Q4UX9,
April 2026 V; Street T for DTN-UK, Statement on large language models, January 2026 V;
Diabettech, "In conversation with… factual questions for LLMs", June 2025 V; Diabettech,
"ChatGPT Health conversations and a Boost AndroidAPS case study", January 2026 V; Diabettech,
"Five AI models, three users, one finding", April 2026 V; Street T, carbohydrate-consistency
manuscript (JMIR Diabetes, status to confirm).

LLMs in diabetes: Sng GLY et al, Diabetes Care 2023;46:e103-5 P; Goncalves S et al, Diabetes Res
Clin Pract 2025;113031 P; Joubert M et al, Diabetes Obes Metab 2026, doi 10.1111/dom.70396 P;
Baumgartner M et al, J Diabetes Sci Technol 2024, doi 10.1177/19322968241264744 P; Piazza CD et
al, eClinicalMedicine 2025;78 P; Housni A et al, J Med Internet Res 2025;27:e63278 P; the
Scientific Reports 2024 case study on LLM analysis of CGM data; the Frontiers Digital Health
2026 diabetes-education evaluation; the UK Diabetes and Endocrinology SCE performance paper
(2025); the medRxiv 2025 ChatGPT consistency study in type 2 diabetes.

LLM non-determinism: arXiv 2506.09501 (numerical sources of non-determinism) V; arXiv
2606.26185 (temperature control and reproducibility in LLM-as-judge) V; the temperature-zero
non-determinism discussion cited in the plan.

DIY AID and settings: AndroidAPS documentation (androidaps.readthedocs.io) V; nightscout/AndroidAPS
source, master 598e2eb, core/keys V; Burnside MJ et al, NEJM 2022 (CREATE trial of open-source
AID); Braune K et al and Lewis D on DIY AID safety (JDST / JMIR); Walsh J, Roberts R, Pumping
Insulin 6th edn P; International Hypoglycaemia Study Group, Diabetologia 2017;60:3-6 P; Cryer PE
2016 P.

Regulation: Regulation (EU) 2017/745, Article 2 and Annex VIII Rule 11 V (wording to confirm on
EUR-Lex); MDCG 2019-11 V (PDF saved; extract for quotation); MHRA, Medical device stand-alone
software including apps, 2023 V; MHRA, draft Medical Devices (Amendment) Regulations 2026, 11
May 2026 V; FDA, Clinical Decision Support Software guidance, September 2022 V; Google Play
Health Content and Services policy V; the Lancet Diabetes & Endocrinology diabetes data rights
charter (PIIS2213-8587(25)00291-8) V; OpenAI and Google consumer data-use terms (training on by
default) V.

## Style gate and declarations

The manuscript and the commentary follow WRITING_STYLE.md and JDST_STYLE.md (copies in this
folder). In particular: continuous prose with tables only for tabular content; no em or en
dashes, ranges written with "to"; no bold; no triplets; no negation-then-correction; no
fragments; no signposting; section headings that name their contents; a clean draft with no
history; every proportion with a Wilson 95 per cent interval and the unit named (the run, since
there is one participant); confidence tiers labelled (the within-model stability results are
solid, the between-model comparison provisional because models drift, the regulatory reading
speculative in the guide's sense, being reasoning rather than measurement); glucose in mg/dL
with mmol/L where a threshold is defined (70 mg/dL, 3.9 mmol/L); and, where the paper says what
a user would receive, the identification constraint stated once: the study measures what the
models produced on this package, not what any user's glucose would have done had they acted.
Before delivery: grep for dashes, bullets, bold and draft-history words; TimSim/build.py is the
gate if the paper is built in that pipeline.

Declarations for this paper, written accurately rather than from the TimSim template. Funding:
none; API costs were paid by the author (state the total). Conflicting interests: the author
runs Diabettech Ltd, sits on the DTN-UK committee and wrote its statement on large language
models, and authored the two preprints cited; he has no relationship with the developer of the
application. Ethical approval: the glucose and pump data are the author's own, exported from
his Nightscout instance and AndroidAPS profile; no other person's data were used; no
interventional protocol was applied and no institutional review board reviewed the work; the
analysis is of model outputs, not of a change made to treatment. Data availability: the prompts,
the validator, the harness, the analysis code and all model outputs are published in the
repository; the package is published with identifiers removed, since it contains the author's
own health data and he consents to its release.

## Remaining work before drafting

1. Finish Haiku (4 runs) and replay its 27 repair-class runs with the app's wording once
   Anthropic credits allow; re-validate; regenerate.
2. Add Wilson confidence intervals and a between-model agreement table to analyse.py; add the
   citation-verification check (quoted glucose figures against the package) to reasoning.py.
3. Produce Figure 1 (workflow) and Figure 2 (strip plots) after loading the dataviz skill.
4. Pin exact quotations for Rule 11 and MDCG 2019-11 from the saved PDFs.
5. Register the five hypotheses on OSF, as for the settings paper, before the first draft.
6. Decide: JDST pair (recommended) or single DT&T article.
