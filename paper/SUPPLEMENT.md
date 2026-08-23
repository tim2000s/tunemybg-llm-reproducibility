# Supplementary material

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