# Supplementary material for: A paid application standardises what large language models read about insulin pump settings and leaves what they decide to chance: reproducibility of an automated insulin delivery settings review across eleven models

Tim Street, MEng BEng (Hons), ORCID 0009-0008-4417-6581. Diabettech Ltd, London, United Kingdom. tim@diabettech.com

Preprint, not peer reviewed. Zenodo, September 2026.

## Table S1. Model identifiers as requested and as returned by each provider

The requested identifier is the string sent in the API call; the served identifier is the model field the provider returned in each response, with the number of turns reporting it. Dates are the first and last conversation start dates (UTC).

| Model (paper) | Provider and route | Requested identifier | Served identifier (turns) | Conversations | Dates |
|---|---|---|---|---|---|
| Gemini 3.6 Flash | Google, Generative Language API | gemini-3.6-flash | gemini-3.6-flash (204) | 50 | 2026-08-21 to 2026-08-21 |
| Gemini 3.1 Pro Preview | Google, Generative Language API | gemini-3.1-pro-preview | gemini-3.1-pro-preview (203) | 50 | 2026-08-21 to 2026-08-21 |
| Gemini 3.5 Flash-Lite | Google, Generative Language API | gemini-3.5-flash-lite | gemini-3.5-flash-lite (218) | 50 | 2026-08-22 to 2026-08-22 |
| GPT-5.6-sol | OpenRouter, OpenAI-compatible API (reasoning effort medium) | gpt-5.6-sol | gpt-5.6-sol (200) | 50 | 2026-08-21 to 2026-08-21 |
| GPT-5.4-mini | OpenRouter, OpenAI-compatible API (reasoning effort medium) | gpt-5.4-mini | gpt-5.4-mini-2026-03-17 (227) | 50 | 2026-08-22 to 2026-08-22 |
| Claude Opus 5 | Anthropic, Messages API | claude-opus-5 | claude-opus-5 (95) | 20 | 2026-08-21 to 2026-08-22 |
| Claude Sonnet 5 | Anthropic, Messages API | claude-sonnet-5 | claude-sonnet-5 (84) | 20 | 2026-08-21 to 2026-08-22 |
| Claude Haiku 4.5 | Anthropic, Messages API | claude-haiku-4-5 | claude-haiku-4-5-20251001 (244) | 50 | 2026-08-22 to 2026-08-22 |
| DeepSeek V4 Pro | OpenRouter, OpenAI-compatible API | deepseek/deepseek-v4-pro | deepseek/deepseek-v4-pro (217) | 50 | 2026-08-22 to 2026-08-22 |
| Grok 4.6 | OpenRouter, OpenAI-compatible API | x-ai/grok-4.6 | x-ai/grok-4.6 (201) | 50 | 2026-08-22 to 2026-08-22 |
| Llama 4 Maverick | OpenRouter, OpenAI-compatible API | meta-llama/llama-4-maverick | meta-llama/llama-4-maverick (231) | 50 | 2026-08-22 to 2026-08-22 |

## Table S2. Verification of the reconstructed validator against the application

Twenty-six real model outputs were pasted into the application's result screen on 22 August 2026 and its response recorded; the same texts were then judged by the validator. Sample 04 was pasted while the application held the demonstration package and is reported only for whether fenced JSON parsed. The verdict classes are: accepted; repair prompt (with the clauses the application composed); schema error with no prompt; invalid JSON with no prompt.

| Sample | Source conversation | Defect in the paste | Application's response | Validator's verdict | Agree |
|---|---|---|---|---|---|
| 01 | real_gemini35flashlite_50/run_037 | fully compliant, should be accepted | accepted | accepted | yes |
| 02 | real_gpt54mini_med_50/run_018 | current_value not copied verbatim: parameter_decisions.aaps.core.carb_absorption.current_value | repair prompt: copy current_value for aaps.core.carb_absorption | repair prompt: copy current_value for aaps.core.carb_absorption | yes |
| 03 | real_gpt54mini_med_50/run_008 | unrequested key added inside meal_strategy_summary | accepted | accepted | yes |
| 04 | real_llama4maverick_50/run_035 | fully compliant JSON wrapped in ```json fences | accepted (fenced JSON parsed; tested against the demonstration package) | parsed (fenced JSON accepted by extractor) | yes |
| 05 | real_gemini35flashlite_50/run_026 | confidence outside low/medium/high in: analysis_steps.meal_ecarbs_absorption.confidence | accepted | accepted | yes |
| 06 | real_deepseek_v4pro_50/run_041 | profile_recommendation.focus outside basal/target/cr/isf/dia | repair prompt: profile_recommendation.focus | repair prompt: profile_recommendation.focus | yes |
| 07 | real_opus5/run_017 | recommendation priority outside low/medium/high/safety | accepted | accepted | yes |
| 08 | real_gemini31pro_50/run_024 | top-level section(s) missing: issues | accepted | accepted | yes |
| 09 | real_gpt54mini_med_50/run_043 | sections flagged: analysis_steps.automation_sensitivity_limits.confidence, meal_strategy_summary | accepted | accepted | yes |
| 10 | real_deepseek_v4pro_50/run_023 | sections flagged: analysis_steps.automation_smb_uam.confidence, profile_recommendation.focus | repair prompt: profile_recommendation.focus | repair prompt: profile_recommendation.focus | yes |
| 11 | real_gemini35flashlite_50/run_050 | sections flagged: analysis_steps.basal_targets.confidence, analysis_steps.synthesis_plan.confidence, profile_recommendation | schema error, no prompt (application session then crashed) | schema error, no prompt | yes |
| 12 | real_deepseek_v4pro_50/run_033 | sections flagged: analysis_steps.profile_cr_isf_dia.confidence, parameter_decisions.profile.basal.00_00.current_value, parameter_decisions.profile.basal.05_00.current_value, parameter_decisions.profile.basal.06_00.current_value, parameter_decisions.profile.basal.10_00.current_value, parameter_decisions.profile.basal.16_00.current_value, parameter_decisions.profile.basal.18_00.current_value, parameter_decisions.profile.basal.19_00.current_value, parameter_decisions.profile.cr.00_00.current_value, parameter_decisions.profile.cr.04_00.current_value, parameter_decisions.profile.cr.08_00.current_value, parameter_decisions.profile.cr.16_00.current_value, parameter_decisions.profile.cr.20_00.current_value, parameter_decisions.profile.isf.00_00.current_value, parameter_decisions.profile.target.00_00.current_value, parameter_decisions.profile.target.08_00.current_value, parameter_decisions.profile.target.23_00.current_value, parameter_decisions.profile.dia.current_value | repair prompt: copy current_value for 17 keys | repair prompt: copy current_value for 17 keys | yes |
| 13 | real_grok46_50/run_017 | sections flagged: analysis_steps.safety_overview, analysis_steps.basal_targets, analysis_steps.profile_cr_isf_dia, analysis_steps.automation_smb_uam, analysis_steps.automation_sensitivity_limits, analysis_steps.meal_bolus_strategy, analysis_steps.meal_ecarbs_absorption, analysis_steps.synthesis_plan | accepted | accepted | yes |
| 14 | real_gpt54mini_med_50/run_003 | sections flagged: meal_strategy_summary.confidence | accepted | accepted | yes |
| 15 | real_gemini35flashlite_50/run_015 | sections flagged: parameter_decisions.aaps.core.carb_absorption | accepted | accepted | yes |
| 16 | real_deepseek_v4pro_50/run_002 | sections flagged: parameter_decisions.profile.basal.10_00, parameter_decisions.profile.basal.16_00 | schema error, no prompt | schema error, no prompt | yes |
| 17 | real_deepseek_v4pro_50/run_035 | sections flagged: parameter_decisions.profile.cr.00_00 | accepted | accepted | yes |
| 18 | real_gemini36flash_50/run_016 | sections flagged: parameter_decisions.profile.dia | accepted | accepted | yes |
| 19 | real_gpt54mini_med_50/run_042 | sections flagged: profile_recommendation | accepted | accepted | yes |
| 20 | real_gemini35flashlite_50/run_017 | valid JSON followed by a stray closing ``` | accepted | accepted | yes |
| 21 | real_gemini35flashlite_50/run_028 | well-formed except one closing brace missing (root never closes) | invalid JSON, no prompt | invalid JSON, no prompt | yes |
| 22 | real_opus5/run_011 | several top-level JSON objects in sequence instead of one | invalid JSON, no prompt | invalid JSON, no prompt | yes |
| 23 | real_llama4maverick_50/run_012 | syntax error inside: Expecting value at char 0 | invalid JSON, no prompt | invalid JSON, no prompt | yes |
| 24 | real_gemini35flashlite_50/run_025 | stray closing ``` at the end, no opening fence | invalid JSON, no prompt | invalid JSON, no prompt | yes |
| 25 | real_gemini35flashlite_50/run_033 | parameter_decisions rows missing/duplicated/extra: parameter_decisions | repair prompt: add profile.cr.16_00, remove profile.cr.06_00 | repair prompt: add profile.cr.16_00; remove profile.cr.06_00 | yes |
| 26 | real_gpt54mini_med_50/run_018 (response to the repair prompt) | current_value still not copied exactly ("5m" for "5 min") | repair prompt: copy current_value for aaps.core.carb_absorption (second time) | repair prompt: copy current_value for aaps.core.carb_absorption | yes |

Agreement on verdict class: 25 of 25 informative samples.

## Table S3. Whether the rationale for each decision cites a figure from the record

Post hoc analysis over accepted conversations. For each decision row the rationale text was searched for figures with a unit (the same extraction as the citation check) and each figure was checked against the numbers in the package. A change decision is counted as cited when at least one such figure is present in the package. Wilson 95 per cent intervals, with the decision row as the unit, are given for the cited proportion; rows are not independent within a conversation, so the intervals are indicative.

| Model | Change decisions | Cited a verified figure, n (per cent; 95 per cent interval) | Cited figures, none verified | No figure in rationale | Keep decisions | Keep decisions citing a verified figure, n (per cent) |
|---|---|---|---|---|---|---|
| Gemini 3.6 Flash | 160 | 154 (96; 92 to 98) | 0 | 6 | 990 | 328 (33) |
| Gemini 3.1 Pro Preview | 141 | 97 (69; 61 to 76) | 0 | 44 | 1009 | 88 (9) |
| Gemini 3.5 Flash-Lite | 10 | 9 (90; 60 to 98) | 0 | 1 | 887 | 129 (15) |
| GPT-5.6-sol | 20 | 17 (85; 64 to 95) | 0 | 3 | 1130 | 187 (17) |
| GPT-5.4-mini | 2 | 0 (0; 0 to 66) | 0 | 2 | 1102 | 3 (0) |
| Claude Opus 5 | 16 | 16 (100; 81 to 100) | 0 | 0 | 237 | 200 (84) |
| Claude Sonnet 5 | 1 | 1 (100; 21 to 100) | 0 | 0 | 436 | 150 (34) |
| Claude Haiku 4.5 | 27 | 27 (100; 88 to 100) | 0 | 0 | 433 | 405 (94) |
| DeepSeek V4 Pro | 93 | 84 (90; 83 to 95) | 0 | 9 | 1011 | 105 (10) |
| Grok 4.6 | 16 | 16 (100; 81 to 100) | 0 | 0 | 1134 | 615 (54) |
| Llama 4 Maverick | 56 | 3 (5; 2 to 15) | 0 | 53 | 956 | 0 (0) |

## Table S4. How accepted conversations read the package's bolus-only insulin total

Post hoc analysis. The package's treatment_summary gives total_insulin_u 275.95 over 14 days (19.7 U/day), a sum of the bolus and SMB treatment records only: the package carries no basal delivery data, and its scheduled basal profile integrates to 16.2 U/day. Response text was searched for the derived figure (19.7 or 275.95) in a daily total or TDD context, for statements that the total excludes basal or is bolus only, and for a reconstructed total near 36 U/day. Wilson 95 per cent intervals over accepted conversations.

| Model | Accepted | Treated 19.7 U as a daily total or TDD, n (per cent; 95 per cent interval) | Noted the total excludes basal, n (per cent) | Reconstructed about 36 U/day, n (per cent) | Lowered max IOB while calling 19.7 a daily total |
|---|---|---|---|---|---|
| Gemini 3.6 Flash | 50 | 49 (98; 90 to 100) | 13 (26) | 0 (0) | 48 |
| Gemini 3.1 Pro Preview | 50 | 16 (32; 21 to 46) | 5 (10) | 0 (0) | 16 |
| Gemini 3.5 Flash-Lite | 39 | 0 (0; 0 to 9) | 5 (13) | 0 (0) | 0 |
| GPT-5.6-sol | 50 | 4 (8; 3 to 19) | 23 (46) | 2 (4) | 0 |
| GPT-5.4-mini | 48 | 0 (0; 0 to 7) | 32 (67) | 0 (0) | 0 |
| Claude Opus 5 | 11 | 9 (82; 52 to 95) | 10 (91) | 11 (100) | 7 |
| Claude Sonnet 5 | 19 | 2 (11; 3 to 31) | 8 (42) | 6 (32) | 0 |
| Claude Haiku 4.5 | 20 | 4 (20; 8 to 42) | 19 (95) | 8 (40) | 0 |
| DeepSeek V4 Pro | 48 | 5 (10; 4 to 22) | 25 (52) | 7 (15) | 5 |
| Grok 4.6 | 50 | 26 (52; 38 to 65) | 23 (46) | 29 (58) | 0 |
| Llama 4 Maverick | 44 | 0 (0; 0 to 8) | 0 (0) | 0 (0) | 0 |

## Table S5. Further package-inherited splits

Post hoc analysis over accepted conversations. Hour of the lows: the package's hourly glucose is keyed both in UTC (time below range peaks at 18.5 per cent at hour 0) and in local time (the same peak at 01:00, BST); responses are classed by where they place the peak, with '00:00 or midnight only' indicating the UTC array read as clock time. Diluted insulin: the record's use of diluted insulin is disclosed only in a free-text profile name inside Profile Switch events; counts give responses mentioning it and responses engaging with its kinetics or absorption. mmol/L: responses quoting the mmol-denominated ISF values from the loop reason strings inside the otherwise mg/dl package.

| Model | Accepted | Peak at 01:00 only | Peak at 00:00 or midnight only | Both hours cited | Mentions diluted insulin | Engages with its kinetics | Quotes mmol ISF values |
|---|---|---|---|---|---|---|---|
| Gemini 3.6 Flash | 50 | 10 | 1 | 39 | 1 | 0 | 0 |
| Gemini 3.1 Pro Preview | 50 | 10 | 4 | 32 | 8 | 0 | 0 |
| Gemini 3.5 Flash-Lite | 39 | 12 | 6 | 5 | 0 | 0 | 0 |
| GPT-5.6-sol | 50 | 10 | 0 | 39 | 4 | 1 | 0 |
| GPT-5.4-mini | 48 | 2 | 2 | 3 | 0 | 0 | 0 |
| Claude Opus 5 | 11 | 1 | 0 | 7 | 3 | 3 | 0 |
| Claude Sonnet 5 | 19 | 0 | 5 | 1 | 13 | 4 | 0 |
| Claude Haiku 4.5 | 20 | 2 | 3 | 8 | 12 | 9 | 1 |
| DeepSeek V4 Pro | 48 | 14 | 6 | 13 | 3 | 2 | 1 |
| Grok 4.6 | 50 | 25 | 3 | 10 | 46 | 42 | 0 |
| Llama 4 Maverick | 44 | 0 | 0 | 0 | 0 | 0 | 0 |
