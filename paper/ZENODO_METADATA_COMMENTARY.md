# Zenodo record metadata for the commentary

Published 8 September 2026 as https://doi.org/10.5281/zenodo.22662770 (version 1.0; concept DOI 10.5281/zenodo.22662769, which always resolves to the latest version). Checked against the Zenodo API the same day: resource type Preprint, licence CC BY-NC-ND 4.0, open access, one file, related works as listed below except the study link, which awaits the study's DOI. What follows is the form content as prepared; the remaining actions are in the next section.

Prepared 8 September 2026. The commentary is the companion to the study preprint; the study's
form entries are in ZENODO_METADATA.md and the two records link to each other through Related
works. Publish the study first so that its DOI can go into this record and into the
commentary's reference 1; if the commentary must go first, publish it, then edit its metadata to
add the study's DOI once known.

Each heading below is a panel or field of the Zenodo upload form, in the form's order, with the
entry to make. The files are built by `build_zenodo.py` into `paper/zenodo/`.

## After publishing

1. Done: the cover letter carries 10.5281/zenodo.22662770 in place of `[DOI 2]`, and the study's record metadata links to it.
2. Once the study is published, add "Is supplement to" with the study's DOI to this record as a metadata edit, which needs no new version.
3. Reference 1 of the uploaded PDF cites the study by its repository URL because the study's DOI did not exist when the PDF was built. Changing it means a new version of the record with its own DOI; the URL resolves to the same material, so leaving it is reasonable.
4. The GitHub repository named in reference 1 was private on 8 September 2026. Make it public, since the published record now points readers to it.

## Files

| File | Contents |
|---|---|
| TuneMyBG_commentary_manuscript.pdf | Title page, abstract, body, references. No tables or figures. |

`TuneMyBG_commentary_abstract.txt` holds the description text below and is not uploaded.

## Basic information

Digital Object Identifier: leave "No" selected so Zenodo mints one.

Resource type: Publication, then Preprint. Zenodo has no commentary subtype; Preprint is the
type that matches an unrefereed manuscript under journal submission, and the description says
what kind of piece it is.

Title:

Is an application that prepares your data and prompts for a chatbot a medical device? Insulin settings advice mediated by large language models under the European and British device regulations

Publication date: the day of publishing, in YYYY-MM-DD.

Creators, one entry:

| Field | Entry |
|---|---|
| Family name | Street |
| Given names | Tim |
| Name identifiers | ORCID 0009-0008-4417-6581 |
| Affiliation | Diabettech Ltd, London, United Kingdom |

Description. Plain paragraphs, no markup:

Preprint, not peer reviewed. Commentary under submission to the Journal of Diabetes Science and Technology alongside the study it accompanies, which is a separate Zenodo record. Not legal advice.

A paid Android application prepares a user's AndroidAPS data and four prompts for any large language model, checks the returned file and presents it as a review of insulin pump settings. A companion article shows that eleven models read the record consistently and disagreed about what to change, and that the application's check cannot tell one answer from another. This commentary asks what such a product is in regulatory terms. On the definition in Regulation (EU) 2017/745 and Rule 11 as read in MDCG 2019-11, its stated purpose places it in Class IIb, or at the least IIa; the British, American and Google Play positions are set out, and the obligations that follow are the minimum a product of this kind should meet.

Additional descriptions. Add one of type "Other" carrying the declarations:

Ethics. The commentary analyses a product's public listing, in-app text and the regulations that apply to it. No participant data were collected. The companion study, cited as reference 1, used only the author's own health record with his written consent.

Competing interests. The author runs Diabettech Ltd, is a committee member of the Diabetes Technology Network UK and wrote its statement on large language models. He has no relationship with the developer of the application discussed and paid for its subscription. Three of the eleven models studied in the companion article are Anthropic's, as is the assistant used to produce this work; Anthropic had no role in the study, was not informed of it, and all model usage was paid for at list price. He is not a lawyer, and this commentary is not legal advice.

Funding. This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

Writing assistance. Claude (Anthropic), a large language model assistant, was used under the author's direction to draft and revise the text. The author made every decision of interpretation and is responsible for the content.

Licenses: Creative Commons Attribution Non Commercial No Derivatives 4.0 International (CC-BY-NC-ND-4.0), the same as the study and for the same reason: JDST (SAGE) is pending, and a licence cannot be narrowed after publishing.

## Recommended information

Contributors: none.

Keywords and subjects, one per entry:

AndroidAPS; automated insulin delivery; large language models; medical device regulation; software as a medical device; MDR 2017/745; MDCG 2019-11; Rule 11; type 1 diabetes

Languages: English.

Dates: none beyond the publication date.

Version: 1.0

Publisher: leave as Zenodo.

## Funding

None. Leave the panel empty.

## Alternate identifiers

None.

## Related works

| Relation | Identifier | Scheme | Resource type |
|---|---|---|---|
| Is supplement to | the study's Zenodo DOI, once known | DOI | Publication: Preprint |
| Is described by | https://www.diabettech.com/the-worlds-first-digital-endo-that-asks-ai-to-fix-your-aid-settings-and-why-you-should-keep-your-money/ | URL | Publication: Other |
| References | https://github.com/tim2000s/tunemybg-llm-reproducibility | URL | Software |

The study's record should carry the reverse link, "Is supplemented by" this DOI, added as a
metadata edit after both are published.

## References

Optional. The eleven entries from the manuscript's References section may be pasted in; they
are not required for the record.

## Publishing information

Leave the Journal, Imprint and Thesis panels empty until the piece is accepted somewhere.

## Conference and domain-specific fields

Leave empty.

## Visibility

Full record: Public. Files: Public. No embargo.

## Communities

Optional. Use the same community as the study if one was chosen, so the two records sit together.
