# Zenodo record metadata for the study preprint

Prepared 8 September 2026. medRxiv was the first choice and was dropped because its ethics
declaration asks for the institutional body that approved or exempted the work, and this study
has none: the only data subject is the author. SSRN rejected both pieces at screening on
24 August 2026 and OSF Preprints is closed to new submissions, so Zenodo, where the companion
commentary is posted, is the venue for the study as well. Zenodo assigns a DOI on publication,
applies no ethics gate, supports versioning under a concept DOI, and is accepted by SAGE's prior
posting policy for JDST.

Each heading below is a panel or field of the Zenodo upload form, in the form's order, with the
entry to make. The files named in the first section are built by `build_zenodo.py` into
`paper/zenodo/`.

## Before publishing

1. The data availability statement names the GitHub repository
   `tim2000s/tunemybg-llm-reproducibility`. It was private on 8 September 2026. Make it public
   before publishing the record, or the statement is untrue on the day of posting.
2. A Zenodo record cannot be deleted once published; files are fixed per version and a new
   version gets its own DOI under the same concept DOI. Metadata can be edited after publishing.
3. The commentary was published on Zenodo on 8 September 2026 as 10.5281/zenodo.22662770; it is linked below and in the cover letter. After the study is published, add the reverse link ("Is supplement to" the study's DOI) to the commentary record as a metadata edit.
4. After publishing, put the study's version DOI into `[DOI 1]` in the JDST cover letter and
   into the "Also available at" line of the Diabettech article if one is added.

## Files

Upload all of the following. Zenodo does not distinguish manuscript from supplement, so the
file names carry the distinction.

| File | Contents |
|---|---|
| TuneMyBG_preprint_manuscript.pdf | Title page, abstract, body, references, three tables, three figures. 11 pages. |
| TuneMyBG_preprint_supplement.pdf | Supplementary Tables S1 to S5. 5 pages, landscape. |
| Figure1.tiff, Figure2.tiff, Figure3.tiff | The figures at 900 dpi, LZW compressed, for anyone reusing them. |

The JPEG copies and the abstract text file are for the form and for other venues; they need not
be uploaded.

## Basic information

Digital Object Identifier: leave "No" selected so Zenodo mints one. Use "Get a DOI now" only if
the DOI is needed in the PDF before publishing; it is not, since the PDF carries no DOI.

Resource type: Publication, then Preprint.

Title:

A paid application standardises what large language models read about insulin pump settings and leaves what they decide to chance: reproducibility of an automated insulin delivery settings review across eleven models

Publication date: the day of publishing, in YYYY-MM-DD.

Creators, one entry:

| Field | Entry |
|---|---|
| Family name | Street |
| Given names | Tim |
| Name identifiers | ORCID 0009-0008-4417-6581 |
| Affiliation | Diabettech Ltd, London, United Kingdom |
| Role | (leave unset; Zenodo lists creators without a role) |

Description. Zenodo renders this on the record page; plain paragraphs, no markup. The same text
is in `TuneMyBG_preprint_abstract.txt`, preceded by the one-line note.

Preprint, not peer reviewed. Under submission to the Journal of Diabetes Science and Technology. The companion commentary on the product's regulatory position is at https://doi.org/10.5281/zenodo.22662770. Code, prompts, every transcript and the study package with identifiers removed are at https://github.com/tim2000s/tunemybg-llm-reproducibility.

Background. A paid Android application prepares a user's AndroidAPS data and four prompts for any large language model, checks the returned file and presents it as a settings review.

Method. The application's package and prompts were replayed verbatim against eleven models, 50 conversations per model (20 for two), on one adult's 14-day record. Responses were judged by a validator verified against the application's behaviour. Outcomes were whether quoted figures were in the record, agreement on 23 settings within and between models, and what the check accepted, with Wilson 95 per cent intervals.

Results. The models quoted the record accurately: 96.8 to 100 per cent of cited figures were in it. Three models lowered the maximum insulin on board limit in 73 to 98 per cent of accepted conversations, proposing 5 to 18 distinct value pairs; four left it alone throughout. One model proposed sensitivity factors from 30 to 180 mg/dl per unit against a current 56. Acceptance at first paste ranged from 34 per cent (22.4 to 47.8) to 100 per cent, and up to 17 of 20 accepted responses broke rules the prompts state but the check does not enforce.

Conclusions. A sensitivity factor three times the current value and a meal step marked completed on a record with no meals both passed the application's check. Which settings a user is told to change depended more on the model opened than on the data, and the user is given no means of telling which answer they have.

Additional descriptions. Add one of type "Other" carrying the declarations, since Zenodo has no
fields for them:

Ethics. The data analysed are the author's own health record, released with his written consent. No other person's data were involved, no participant was recruited, no treatment was changed, and no institutional review board approval was sought because the only data subject is the author. Not a clinical trial; not registered.

Competing interests. The author runs Diabettech Ltd, is a committee member of the Diabetes Technology Network UK and wrote its statement on large language models, and is the author of the two SSRN preprints cited. He has no relationship with the developer of the application studied and paid for its subscription. Three of the eleven models studied are Anthropic's, as is the assistant used to produce this work; Anthropic had no role in the study, was not informed of it, and all model usage was paid for at list price.

Funding. No specific grant. Model usage for the study, $158.42 plus £19.73, was paid for by the author.

Writing assistance. Claude (Anthropic), a large language model assistant, was used under the author's direction to write the harness and analysis code, run the analyses, prepare the figures and draft and revise the text. The author specified the study, made every decision of design and interpretation, checked each reported number against the stored outputs, and is responsible for the content.

Licenses: replace the default CC BY 4.0 with Creative Commons Attribution Non Commercial No Derivatives 4.0 International (CC-BY-NC-ND-4.0). Reason: the manuscript is under submission to JDST (SAGE), whose policy permits prior posting; the no-derivatives term keeps the posted text from being redistributed in altered form while the journal version is pending. A licence cannot be narrowed after publishing, so the restrictive choice is the safe first one. CC BY 4.0 is the alternative if maximum reuse is wanted.

## Recommended information

Contributors: none.

Keywords and subjects, one per entry:

AndroidAPS; artificial intelligence; automated insulin delivery; large language models; reproducibility; type 1 diabetes; medical device software; Nightscout

Languages: English.

Dates: add one of type "Collected", 2026-08-21 to 2026-08-22, description "Model conversations run".

Version: 1.0

Publisher: leave as Zenodo.

## Funding

None. Leave the panel empty; the funding statement is in the additional description.

## Alternate identifiers

None.

## Related works

| Relation | Identifier | Scheme | Resource type |
|---|---|---|---|
| Is supplemented by | https://github.com/tim2000s/tunemybg-llm-reproducibility | URL | Software |
| Is described by | https://www.diabettech.com/the-worlds-first-digital-endo-that-asks-ai-to-fix-your-aid-settings-and-why-you-should-keep-your-money/ | URL | Publication: Other |
| Is supplemented by | 10.5281/zenodo.22662770 | DOI | Publication: Preprint |
| Continues | 10.2139/ssrn.6619638 | DOI | Publication: Preprint |
| Continues | 10.2139/ssrn.6577780 | DOI | Publication: Preprint |

## References

Optional. Zenodo accepts free-text references; paste the twelve entries from the References
section of the manuscript if wanted. They are not required for the record.

## Publishing information

Leave the Journal, Imprint and Thesis panels empty. The manuscript is under submission and has
no journal, volume or pages yet; add the journal fields as a metadata edit after acceptance.

## Conference and domain-specific fields

Leave empty.

## Visibility

Full record: Public. Files: Public. No embargo.

## Communities

Optional. None required. If one is wanted, search for a diabetes technology or open-source
automated insulin delivery community; do not create one for a single record.
