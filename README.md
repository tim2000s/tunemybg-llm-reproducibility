# TuneMyBG reproducibility study

Code, data and manuscripts for a study of how reproducible a paid application's large language
model settings review is. The application (TuneMyBG, Google Play) packages a user's Nightscout
and AndroidAPS data with four fixed prompts for any chat model, validates the JSON the model
returns and presents it as a review of 23 insulin pump settings. This repository replays that
workflow against eleven models, 50 conversations each where cost allowed, on one 14-day
record, judges every response with a validator reconstructed from the application's behaviour,
and analyses what came back.

Everything in the paper is reproducible from this repository: every transcript, every model
output, the validator, the analysis code, the figures and the manuscripts.

## What is here

```
paper/
  manuscript_jdst_original.md     the original article (JDST format); STREET Manuscript 1.docx
  commentary_jdst.md              the companion regulatory commentary; STREET Manuscript 2.docx
  SUPPLEMENT.md                   Tables S1 (served model identifiers), S2 (validator verification), S3 (per-decision citations), S4 (bolus-only insulin total), S5 (further package-inherited splits)
  cover_letter.md                 cover letter to the editor
  preprint_study.*                preprint versions (SSRN and diabettech.com)
  preprint_commentary.*
  preprint_study_zenodo.md        the study preprint as posted to Zenodo (title page, ethics statement,
  preprint_study_zenodo_supplement.md    data availability with the repository URL); Tables S1 to S5 as a separate file
  preprint_commentary_zenodo.md   the commentary as posted to Zenodo (same header changes)
  ZENODO_METADATA.md              every field of the Zenodo record form for the study, with the text to enter
  ZENODO_METADATA_COMMENTARY.md   the same for the commentary's record
  zenodo/                         the record files built by build_zenodo.py: study manuscript, supplement and
                                  commentary PDFs, figures as TIFF and JPEG, both abstracts as plain text
  diabettech_article.md / .html   the Diabettech article and its WordPress block HTML (md_to_wp.py)
  figures/                        fig1 workflow, fig2 suggested values, fig3 conversations, fig_funky (article)
  study_package.json              the study record as the app generated it, data_source id redacted
  demo_package.json               the app's synthetic demonstration package (control)
  NUMBERS.md                      every number in the paper with its provenance, including the
                                  22 August correction of accepted-conversation denominators
  PLAN.md, JOURNAL_AND_STRUCTURE.md, WRITING_STYLE.md, JDST_STYLE.md   planning and style
results/real_<model>_<n>/         one directory per model
  experiment.json                 backend, model, settings, sha256 of package and prompts
  run_NNN/transcript.json         all four prompts, every response, usage, latency, served model id
  run_NNN/final_raw.txt           the raw Prompt 4 response (final_raw_attemptN.txt after repair)
  run_NNN/final.json              the JSON the app would hold (absent if rejected)
  run_NNN/meta.json               app_outcome, validation, timings
results/compare_real_package_tables/   analyse_runs.py output across all models
results/carb_handling.md, citations.md, overnight_attribution.md   post hoc analyses
tunemybg_repro/                   the harness: prompts, backends, runner, extract (validator), analyse,
                                  summary, reasoning, citations, aaps_defaults
```

The package and prompts used for every run are the application's own, copied verbatim
(package version 10, template general_audit). The record is the author's own health data,
released with his consent; the only identifier in the package, an internal data source id,
has been replaced with "redacted". API keys are never stored here: the harness reads them
from the environment or from files outside the repository.

## Reproducing the analysis from the stored runs

```bash
pip3 install -r requirements.txt
python3 revalidate.py results/real_*/ --package paper/study_package.json
python3 analyse_runs.py results/real_*/ --package paper/study_package.json --out results/compare_real_package_tables
python3 carb_handling.py results/real_*/ --out results/carb_handling.md
python3 citations_runs.py results/real_*/ --out results/citations.md
python3 overnight_attribution.py results/real_*/ --out results/overnight_attribution.md
python3 decision_citations.py         # Supplementary Table S3: do change rationales cite a record figure?
python3 tdd_interpretation.py         # Supplementary Table S4: how responses read the bolus-only insulin total
python3 anomalies_scan.py             # Supplementary Table S5: timezone, diluted insulin and mmol splits
python3 figures.py                 # Figures 1 and 2
python3 figure_funky.py --paper    # Figure 3; without --paper, the article graphic
```

`revalidate.py` applies the current validator to every stored run and sets `app_outcome` and
`validation.app_accepted` in `meta.json`; the content analyses use accepted conversations only,
since the application holds nothing from a rejected one. The validator's three tiers
(repair prompt, schema stop, prompt-only rule) were established by pasting 25 real outputs into
the application and are verified in `paper/SUPPLEMENT.md`.

## Running new conversations

```bash
python3 run_experiment.py --backend gemini --model gemini-3.6-flash --runs 50 --workers 2 --experiment gemini36flash
python3 run_experiment.py --backend anthropic --model claude-opus-5 --runs 20 --workers 2 --experiment opus5
python3 run_experiment.py --backend openai_compat --base-url https://openrouter.ai/api/v1 --model x-ai/grok-4.6 --runs 50 --experiment grok46
```

Each conversation is fresh: the package is attached to Prompt 1, Prompts 2 to 4 follow in turn,
and Prompt 4's response is validated; if the application would issue a repair prompt, the
harness sends the application's own wording once in the same conversation
(`tunemybg_repro/prompts.py`). No sampling parameters are set, so each provider's default
applies. Runs are resumable and refuse to continue if the package or prompts have changed.
Inputs default to `~/Downloads/TuneMyBG-analysis.json` and `~/Downloads/TuneMyBGPrompts.txt`;
override with `--package` and `--prompts`.

Further tools: `summarise_runs.py` (plain-English per-model summary against AndroidAPS code
defaults), `reasoning_runs.py` (sentence clustering of rationales across runs),
`rerun_corrections.py` (replay repair turns), `report_to_pdf.sh` (any markdown to PDF through
pandoc and headless Chrome).

## Citation

Street T. A paid application standardises what large language models read about insulin pump
settings and leaves what they decide to chance: reproducibility of an automated insulin
delivery settings review across eleven models. Preprint, 2026.

Street T. Is an application that prepares your data and prompts for a chatbot a medical
device? Insulin settings advice mediated by large language models under the European and
British device regulations. Preprint, 2026.
