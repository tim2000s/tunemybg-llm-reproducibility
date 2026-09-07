# medRxiv submission metadata

Prepared 7 September 2026 for the study preprint. Each heading below is a field or panel of
the medRxiv submission form, in the form's order, with the text to enter. The files named in
the last section are built by `build_medrxiv.py` into `paper/medrxiv/`.

## Before submitting

1. The data availability statement names the GitHub repository
   `tim2000s/tunemybg-llm-reproducibility`. It was private on 7 September 2026. Make it public
   before submitting, or the statement is untrue on the day of posting.
2. medRxiv does not accept commentary or opinion pieces, so only the study goes here. The
   companion commentary stays on Zenodo; the manuscript header says so without a DOI. Add the
   Zenodo DOI to the header line if it exists by the time of submission.
3. Once posted the preprint cannot be removed and the DOI is permanent. Revised versions can
   be posted under the same DOI at any time before journal publication.
4. The JDST cover letter carries the placeholder `[DOI 1]` for this preprint's DOI.

## Manuscript basics

Subject area: Endocrinology (including Diabetes Mellitus and Metabolic Disease)

Alternative if the form's list offers it and the primary fit is questioned at screening:
Health Informatics.

Title:

A paid application standardises what large language models read about insulin pump settings and leaves what they decide to chance: reproducibility of an automated insulin delivery settings review across eleven models

## Abstract

Plain text, no special characters beyond ASCII apart from the pound sign, which does not
appear. The same text is in `TuneMyBG_medRxiv_abstract.txt`.

Background. A paid Android application prepares a user's AndroidAPS data and four prompts for any large language model, checks the returned file and presents it as a settings review.

Method. The application's package and prompts were replayed verbatim against eleven models, 50 conversations per model (20 for two), on one adult's 14-day record. Responses were judged by a validator verified against the application's behaviour. Outcomes were whether quoted figures were in the record, agreement on 23 settings within and between models, and what the check accepted, with Wilson 95 per cent intervals.

Results. The models quoted the record accurately: 96.8 to 100 per cent of cited figures were in it. Three models lowered the maximum insulin on board limit in 73 to 98 per cent of accepted conversations, proposing 5 to 18 distinct value pairs; four left it alone throughout. One model proposed sensitivity factors from 30 to 180 mg/dl per unit against a current 56. Acceptance at first paste ranged from 34 per cent (22.4 to 47.8) to 100 per cent, and up to 17 of 20 accepted responses broke rules the prompts state but the check does not enforce.

Conclusions. A sensitivity factor three times the current value and a meal step marked completed on a record with no meals both passed the application's check. Which settings a user is told to change depended more on the model opened than on the data, and the user is given no means of telling which answer they have.

## Author approval

Yes. The manuscript has a single author, who has seen and approved it.

## Competing interests

The author runs Diabettech Ltd, is a committee member of the Diabetes Technology Network UK and wrote its statement on large language models, and is the author of the two SSRN preprints cited. He has no relationship with the developer of the application studied and paid for its subscription. Three of the eleven models studied are Anthropic's, as is the assistant used to produce this work; Anthropic had no role in the study, was not informed of it, and all model usage was paid for at list price. The author has received no payments or services from any third party in the past 36 months in connection with this work.

## Declarations

The form asks four questions. Tick each, and enter the text given where the form provides a
field.

Ethical guidelines and IRB or ethics committee approval. Confirm. Details field:

The study analysed a single 14-day record of the author's own glucose, insulin and pump settings, which he released with his written consent. No other person's data were involved, no participant was recruited, and no treatment was changed. No institutional review board approval was sought because the only data subject is the author.

Participant consent and identifiers. Confirm. The author is the sole data subject and consented in writing. The only identifier in the published package, an internal data source id, was replaced with the word "redacted".

Clinical trial registration. Confirm. Trial ID field: Not applicable. The study is a computational replay of a software workflow, not a clinical trial or a prospective interventional study, and no treatment was changed.

Research reporting guidelines. Confirm. No EQUATOR Network checklist covers a reproducibility study of a language model workflow. The Methods section states which analyses were specified before the runs and which were added after inspection of the outputs, reports Wilson 95 per cent intervals with the conversation as the unit, and records the served model identifier for every turn (Supplementary Table S1).

## Data availability statement

The prompts, the harness, the validator, the analysis code, every transcript and model output for all 490 conversations, and the study package with identifiers removed are published in the study repository at https://github.com/tim2000s/tunemybg-llm-reproducibility. The package is the author's own health data and is released with his written consent. The application's synthetic demonstration package, used as the control, is included. The supplementary tables give the model identifier each provider returned for every conversation, the full validator verification, a per-decision citation check, and analyses of how each model read the package's bolus-only insulin total and its other partial fields.

Data availability links:

https://github.com/tim2000s/tunemybg-llm-reproducibility

## Clinical protocols

None. Not applicable: no clinical procedure was performed.

## Author list

One author.

| Field | Entry |
|---|---|
| First name | Tim |
| Last name | Street |
| Email | tim@diabettech.com |
| Institution | Diabettech Ltd |
| Department | (leave blank) |
| City | London |
| Country | United Kingdom |
| ORCID | 0009-0008-4417-6581 |
| Corresponding author | Yes |
| Degrees | MEng BEng (Hons) |

## Funding information

Funders: none. Statement for the form:

This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors. Model usage for the study, $158.42 plus £19.73, was paid for by the author.

## Distribution and reuse option

Select: CC BY-NC-ND 4.0.

Reasoning. The manuscript is under submission to the Journal of Diabetes Science and Technology (SAGE), whose policy permits prior posting of preprints; the no-derivatives term keeps the posted text from being redistributed in altered form while the journal version is pending, and the non-commercial term is consistent with the author's disclosure that he has no commercial relationship with the product studied. CC BY is the alternative if maximum reuse is wanted; it cannot be narrowed later, so the more restrictive licence is the safer first choice.

## Files

Manuscript file, single complete PDF with figures included, so no separate image upload is
required at initial submission:

| File | Label on the form |
|---|---|
| TuneMyBG_medRxiv_manuscript.pdf | Manuscript |

Supplemental file (not converted by medRxiv):

| File | Label on the form |
|---|---|
| TuneMyBG_medRxiv_supplement.pdf | Supplementary Tables S1 to S5 |

Image files, kept ready for a revision, where medRxiv asks for source files. TIFF is the
first choice; JPEG is provided as a fallback.

| File | Label on the form |
|---|---|
| Figure1.tiff | Figure 1. The application's workflow as replicated |
| Figure2.tiff | Figure 2. Suggested values in accepted conversations that proposed a change |
| Figure3.tiff | Figure 3. Every conversation as one cell |

Filenames use only letters, digits, underscores and the extension, as the form requires.
