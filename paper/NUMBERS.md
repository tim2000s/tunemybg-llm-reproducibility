# Numbers sheet (final, 2026-08-22)

## Outcomes per model (completed runs; Wilson 95% CI on accepted-first-time and on dead-end)
- gemini-3.6-flash: n=50; first 50 (100%, CI (0.929, 1.0)); after repair 0; dead end 0 (0%, CI (0.0, 0.071)); still rejected 0; accepted-but-breaking-prompt 4/50; stability 0.951; unanimous 14/23; wall 107s; in_tok 148479; out_tok 13514; cost nan
- gemini-3.1-pro-preview: n=50; first 50 (100%, CI (0.929, 1.0)); after repair 0; dead end 0 (0%, CI (0.0, 0.071)); still rejected 0; accepted-but-breaking-prompt 3/50; stability 0.983; unanimous 17/23; wall 137s; in_tok 141673; out_tok 8951; cost nan
- gemini-3.5-flash-lite: n=50; first 38 (76%, CI (0.626, 0.857)); after repair 1; dead end 11 (22%, CI (0.128, 0.352)); still rejected 0; accepted-but-breaking-prompt 8/49; stability 0.987; unanimous 19/23; wall 34s; in_tok 156648; out_tok 11445; cost nan
- gpt-5.6-sol: n=50; first 50 (100%, CI (0.929, 1.0)); after repair 0; dead end 0 (0%, CI (0.0, 0.071)); still rejected 0; accepted-but-breaking-prompt 0/50; stability 0.983; unanimous 21/23; wall 306s; in_tok 122854; out_tok 17535; cost nan
- gpt-5.4-mini: n=50; first 48 (96%, CI (0.865, 0.989)); after repair 0; dead end 1 (2%, CI (0.004, 0.105)); still rejected 1; accepted-but-breaking-prompt 25/48; stability 0.998; unanimous 22/23; wall 123s; in_tok 135508; out_tok 22645; cost nan
- claude-opus-5: n=20; first 10 (50%, CI (0.299, 0.701)); after repair 1; dead end 9 (45%, CI (0.258, 0.658)); still rejected 0; accepted-but-breaking-prompt 5/19; stability 0.970; unanimous 20/23; wall 1025s; in_tok 91199; out_tok 89272; cost 2.83
- claude-sonnet-5: n=20; first 18 (90%, CI (0.699, 0.972)); after repair 1; dead end 1 (5%, CI (0.009, 0.236)); still rejected 0; accepted-but-breaking-prompt 2/20; stability 0.998; unanimous 22/23; wall 558s; in_tok 40245; out_tok 55600; cost 1.02
- claude-haiku-4-5: n=50; first 17 (34%, CI (0.224, 0.478)); after repair 3; dead end 3 (6%, CI (0.021, 0.162)); still rejected 27; accepted-but-breaking-prompt 17/20; stability 0.926; unanimous 6/23; wall 737s; in_tok 108375; out_tok 73396; cost 0.49
- deepseek/deepseek-v4-pro: n=50; first 45 (90%, CI (0.786, 0.957)); after repair 3; dead end 2 (4%, CI (0.011, 0.135)); still rejected 0; accepted-but-breaking-prompt 14/50; stability 0.915; unanimous 10/23; wall 360s; in_tok 138193; out_tok 22522; cost nan
- x-ai/grok-4.6: n=50; first 50 (100%, CI (0.929, 1.0)); after repair 0; dead end 0 (0%, CI (0.0, 0.071)); still rejected 0; accepted-but-breaking-prompt 1/50; stability 0.986; unanimous 21/23; wall 522s; in_tok 135160; out_tok 30567; cost nan
- meta-llama/llama-4-maverick: n=50; first 19 (38%, CI (0.259, 0.518)); after repair 25; dead end 2 (4%, CI (0.011, 0.135)); still rejected 4; accepted-but-breaking-prompt 5/46; stability 0.952; unanimous 16/23; wall 85s; in_tok 130694; out_tok 7233; cost nan

## Profile focus and decision per model (accepted runs)
- gemini-3.6-flash: focus {'target': 39, 'basal': 11}; decision {'keep': 6, 'change': 44}; confidence {'high': 49, 'medium': 1}; changes/run {1.0: 5, 2.0: 7, 3.0: 19, 4.0: 13, 5.0: 4, 6.0: 2}
- gemini-3.1-pro-preview: focus {'target': 46, 'basal': 4}; decision {'change': 45, 'keep': 5}; confidence {'high': 50}; changes/run {1.0: 5, 2.0: 4, 3.0: 36, 4.0: 5}
- gemini-3.5-flash-lite: focus {'basal': 41, 'isf': 3, 'dia': 2, 'target': 1, 'cr': 2}; decision {'keep': 43, 'change': 6}; confidence {'medium': 46, 'high': 3}; changes/run {0.0: 39, 1.0: 6, 2.0: 4}
- gpt-5.6-sol: focus {'target': 39, 'basal': 11}; decision {'keep': 32, 'change': 18}; confidence {'medium': 50}; changes/run {0.0: 32, 1.0: 16, 2.0: 2}
- gpt-5.4-mini: focus {'basal': 47, 'cr': 1}; decision {'keep': 46, 'change': 2}; confidence {'medium': 44, 'low': 1, 'medium-low': 3}; changes/run {0.0: 46, 1.0: 2}
- claude-opus-5: focus {'dia': 3, 'basal': 13, 'isf': 3}; decision {'keep': 19}; confidence {'medium': 15, 'low': 4}; changes/run {1.0: 11, 2.0: 7, 3.0: 1}
- claude-sonnet-5: focus {'target': 3, 'cr': 1, 'basal': 14, 'dia': 2}; decision {'keep': 19, 'change': 1}; confidence {'low': 14, 'medium': 5, 'low-medium': 1}; changes/run {0.0: 19, 1.0: 1}
- claude-haiku-4-5: focus {'basal': 18, 'isf': 2}; decision {'change': 16, 'keep': 4}; confidence {'high': 10, 'medium-high': 3, 'medium': 7}; changes/run {0.0: 2, 1.0: 10, 2.0: 7, 3.0: 1}
- deepseek/deepseek-v4-pro: focus {'isf': 17, 'basal': 28, 'dia': 4, 'target': 1}; decision {'keep': 11, 'change': 39}; confidence {'medium': 39, 'high': 8, 'medium-high': 1, 'low': 2}; changes/run {0.0: 2, 1.0: 17, 2.0: 21, 3.0: 6, 4.0: 1, 5.0: 2, 6.0: 1}
- x-ai/grok-4.6: focus {'basal': 17, 'target': 33}; decision {'keep': 40, 'change': 10}; confidence {'medium': 50}; changes/run {0.0: 40, 1.0: 4, 2.0: 6}
- meta-llama/llama-4-maverick: focus {'basal': 41, 'isf': 4, 'cr': 1}; decision {'change': 29, 'keep': 17}; confidence {'medium': 44, 'high': 1, 'low': 1}; changes/run {0.0: 1, 1.0: 32, 2.0: 11, 3.0: 1, 4.0: 1}

## Row-level change rate with CI for key settings
### aaps.core.safety_limits
- real_gemini36flash_50: change 49/50 (98%, CI 0.895–0.996); distinct suggested 26
- real_gemini31pro_50: change 46/50 (92%, CI 0.812–0.968); distinct suggested 18
- real_gemini35flashlite_50: change 8/49 (16%, CI 0.085–0.29); distinct suggested 4
- real_gpt56sol_med_50: change 0/50 (0%, CI 0.0–0.071); distinct suggested 0
- real_gpt54mini_med_50: change 0/50 (0%, CI 0.0–0.071); distinct suggested 0
- real_opus5: change 17/19 (90%, CI 0.686–0.971); distinct suggested 10
- real_sonnet5_20: change 0/20 (0%, CI 0.0–0.161); distinct suggested 0
- real_haiku45_50: change 3/49 (6%, CI 0.021–0.165); distinct suggested 3
- real_deepseek_v4pro_50: change 22/50 (44%, CI 0.312–0.577); distinct suggested 14
- real_grok46_50: change 0/50 (0%, CI 0.0–0.071); distinct suggested 0
- real_llama4maverick_50: change 27/49 (55%, CI 0.413–0.681); distinct suggested 11
### profile.target.00_00
- real_gemini36flash_50: change 39/50 (78%, CI 0.648–0.872); distinct suggested 1
- real_gemini31pro_50: change 45/50 (90%, CI 0.786–0.957); distinct suggested 2
- real_gemini35flashlite_50: change 1/49 (2%, CI 0.004–0.107); distinct suggested 1
- real_gpt56sol_med_50: change 18/50 (36%, CI 0.241–0.499); distinct suggested 1
- real_gpt54mini_med_50: change 0/50 (0%, CI 0.0–0.071); distinct suggested 0
- real_opus5: change 0/19 (0%, CI 0.0–0.168); distinct suggested 0
- real_sonnet5_20: change 0/20 (0%, CI 0.0–0.161); distinct suggested 0
- real_haiku45_50: change 2/49 (4%, CI 0.011–0.137); distinct suggested 2
- real_deepseek_v4pro_50: change 1/50 (2%, CI 0.004–0.105); distinct suggested 1
- real_grok46_50: change 10/50 (20%, CI 0.112–0.33); distinct suggested 1
- real_llama4maverick_50: change 0/49 (0%, CI 0.0–0.073); distinct suggested 0
### profile.target.23_00
- real_gemini36flash_50: change 39/50 (78%, CI 0.648–0.872); distinct suggested 1
- real_gemini31pro_50: change 45/50 (90%, CI 0.786–0.957); distinct suggested 2
- real_gemini35flashlite_50: change 0/49 (0%, CI 0.0–0.073); distinct suggested 0
- real_gpt56sol_med_50: change 2/50 (4%, CI 0.011–0.135); distinct suggested 1
- real_gpt54mini_med_50: change 0/50 (0%, CI 0.0–0.071); distinct suggested 0
- real_opus5: change 0/19 (0%, CI 0.0–0.168); distinct suggested 0
- real_sonnet5_20: change 0/20 (0%, CI 0.0–0.161); distinct suggested 0
- real_haiku45_50: change 1/49 (2%, CI 0.004–0.107); distinct suggested 1
- real_deepseek_v4pro_50: change 1/50 (2%, CI 0.004–0.105); distinct suggested 1
- real_grok46_50: change 6/50 (12%, CI 0.056–0.238); distinct suggested 1
- real_llama4maverick_50: change 0/49 (0%, CI 0.0–0.073); distinct suggested 0
### profile.basal.00_00
- real_gemini36flash_50: change 11/50 (22%, CI 0.128–0.352); distinct suggested 1
- real_gemini31pro_50: change 1/50 (2%, CI 0.004–0.105); distinct suggested 1
- real_gemini35flashlite_50: change 5/49 (10%, CI 0.044–0.218); distinct suggested 1
- real_gpt56sol_med_50: change 0/50 (0%, CI 0.0–0.071); distinct suggested 0
- real_gpt54mini_med_50: change 2/50 (4%, CI 0.011–0.135); distinct suggested 1
- real_opus5: change 0/19 (0%, CI 0.0–0.168); distinct suggested 0
- real_sonnet5_20: change 0/20 (0%, CI 0.0–0.161); distinct suggested 0
- real_haiku45_50: change 7/49 (14%, CI 0.071–0.267); distinct suggested 2
- real_deepseek_v4pro_50: change 22/50 (44%, CI 0.312–0.577); distinct suggested 2
- real_grok46_50: change 0/50 (0%, CI 0.0–0.071); distinct suggested 0
- real_llama4maverick_50: change 27/49 (55%, CI 0.413–0.681); distinct suggested 3
### profile.isf.00_00
- real_gemini36flash_50: change 0/50 (0%, CI 0.0–0.071); distinct suggested 0
- real_gemini31pro_50: change 0/50 (0%, CI 0.0–0.071); distinct suggested 0
- real_gemini35flashlite_50: change 0/49 (0%, CI 0.0–0.073); distinct suggested 0
- real_gpt56sol_med_50: change 0/50 (0%, CI 0.0–0.071); distinct suggested 0
- real_gpt54mini_med_50: change 0/50 (0%, CI 0.0–0.071); distinct suggested 0
- real_opus5: change 0/19 (0%, CI 0.0–0.168); distinct suggested 0
- real_sonnet5_20: change 0/20 (0%, CI 0.0–0.161); distinct suggested 0
- real_haiku45_50: change 7/49 (14%, CI 0.071–0.267); distinct suggested 7
- real_deepseek_v4pro_50: change 20/50 (40%, CI 0.276–0.538); distinct suggested 14
- real_grok46_50: change 0/50 (0%, CI 0.0–0.071); distinct suggested 0
- real_llama4maverick_50: change 4/49 (8%, CI 0.032–0.192); distinct suggested 2
### aaps.core.sensitivity
- real_gemini36flash_50: change 13/50 (26%, CI 0.159–0.396); distinct suggested 1
- real_gemini31pro_50: change 0/50 (0%, CI 0.0–0.071); distinct suggested 0
- real_gemini35flashlite_50: change 0/49 (0%, CI 0.0–0.073); distinct suggested 0
- real_gpt56sol_med_50: change 0/50 (0%, CI 0.0–0.071); distinct suggested 0
- real_gpt54mini_med_50: change 0/50 (0%, CI 0.0–0.071); distinct suggested 0
- real_opus5: change 6/19 (32%, CI 0.154–0.54); distinct suggested 2
- real_sonnet5_20: change 0/20 (0%, CI 0.0–0.161); distinct suggested 0
- real_haiku45_50: change 3/49 (6%, CI 0.021–0.165); distinct suggested 2
- real_deepseek_v4pro_50: change 9/50 (18%, CI 0.098–0.308); distinct suggested 5
- real_grok46_50: change 0/50 (0%, CI 0.0–0.071); distinct suggested 0
- real_llama4maverick_50: change 0/49 (0%, CI 0.0–0.073); distinct suggested 0
### profile.dia
- real_gemini36flash_50: change 0/50 (0%, CI 0.0–0.071); distinct suggested 0
- real_gemini31pro_50: change 0/50 (0%, CI 0.0–0.071); distinct suggested 0
- real_gemini35flashlite_50: change 0/49 (0%, CI 0.0–0.073); distinct suggested 0
- real_gpt56sol_med_50: change 0/50 (0%, CI 0.0–0.071); distinct suggested 0
- real_gpt54mini_med_50: change 0/50 (0%, CI 0.0–0.071); distinct suggested 0
- real_opus5: change 0/19 (0%, CI 0.0–0.168); distinct suggested 0
- real_sonnet5_20: change 0/20 (0%, CI 0.0–0.161); distinct suggested 0
- real_haiku45_50: change 6/49 (12%, CI 0.057–0.242); distinct suggested 5
- real_deepseek_v4pro_50: change 8/50 (16%, CI 0.083–0.285); distinct suggested 4
- real_grok46_50: change 0/50 (0%, CI 0.0–0.071); distinct suggested 0
- real_llama4maverick_50: change 0/49 (0%, CI 0.0–0.073); distinct suggested 0
### aaps.core.smb_delivery
- real_gemini36flash_50: change 4/50 (8%, CI 0.032–0.188); distinct suggested 1
- real_gemini31pro_50: change 3/50 (6%, CI 0.021–0.162); distinct suggested 2
- real_gemini35flashlite_50: change 0/49 (0%, CI 0.0–0.073); distinct suggested 0
- real_gpt56sol_med_50: change 0/50 (0%, CI 0.0–0.071); distinct suggested 0
- real_gpt54mini_med_50: change 0/50 (0%, CI 0.0–0.071); distinct suggested 0
- real_opus5: change 5/19 (26%, CI 0.118–0.488); distinct suggested 2
- real_sonnet5_20: change 0/20 (0%, CI 0.0–0.161); distinct suggested 0
- real_haiku45_50: change 1/49 (2%, CI 0.004–0.107); distinct suggested 1
- real_deepseek_v4pro_50: change 5/50 (10%, CI 0.043–0.214); distinct suggested 3
- real_grok46_50: change 0/50 (0%, CI 0.0–0.071); distinct suggested 0
- real_llama4maverick_50: change 0/49 (0%, CI 0.0–0.073); distinct suggested 0

## Safety-limit component values per model (distinct pairs, ranges)
- real_gemini36flash_50: 49 change rows, 18 distinct (basal,iob) pairs; iob 4.0-15.0 mode [(7.0, 27)]; basal 2.5-4.0 mode [(3.5, 19)]
- real_gemini31pro_50: 46 change rows, 17 distinct (basal,iob) pairs; iob 3.0-10.0 mode [(7.0, 16)]; basal 2.5-4.0 mode [(3.0, 29)]
- real_gemini35flashlite_50: 8 change rows, 4 distinct (basal,iob) pairs; iob 6.0-15.0 mode [(6.0, 5)]; basal None-None mode []
- real_opus5: 17 change rows, 7 distinct (basal,iob) pairs; iob 6.0-10.0 mode [(8.0, 8)]; basal 4.0-5.0 mode [(5.0, 1)]
- real_haiku45_50: 1 change rows, 1 distinct (basal,iob) pairs; iob 20.0-20.0 mode [(20.0, 1)]; basal None-None mode []
- real_deepseek_v4pro_50: 22 change rows, 14 distinct (basal,iob) pairs; iob 2.0-12.0 mode [(5.0, 7)]; basal 2.0-4.0 mode [(4.0, 4)]
- real_llama4maverick_50: 26 change rows, 6 distinct (basal,iob) pairs; iob 15.0-20.0 mode [(15.0, 11)]; basal 10.0-10.0 mode [(10.0, 1)]

## Demo package control (gemini36flash_50)
- n=50, change per run {0: 50}, focus {'basal': 40, 'cr': 10}, first-pass compliant 49

## Package facts
{"entry_count": 3995, "average_glucose": 121.6, "standard_deviation": 39.7, "time_in_range_percent": 86.0, "time_above_range_percent": 8.9, "time_below_range_percent": 5.1, "coefficient_of_variation_percent": 32.6} 98.7 65.0 {'events': 27, 'entries': 3995, 'treatments': 2315, 'raw_entries': 3995, 'device_statuses': 6214} {'carb_entries': 0, 'total_carbs_g': 0.0, 'insulin_entries': 655, 'total_insulin_u': 275.95, 'total_treatments': 2315, 'extended_carb_entries': 0, 'average_extended_carb_duration_min': None} dia 10.0 inventory 23 {'aaps': 6, 'profile': 17} hourly TBR max 18.5

## Carb handling table


## Citations table
---

## Correction, 22 August 2026 (late): accepted-conversation denominators

revalidate.py had stored the last attempt's validation under meta.validation even when the app
outcome was a rejection, so content analyses (Tables 2 and 3, Figure 2, citations, carb
handling, stability) had counted harness-parsed responses the app would have rejected. Fixed
(revalidate.py forces app_accepted False for rejected outcomes; analyse.py drops final.json for
non-accepted runs) and everything regenerated. Accepted n now: Flash 50, Pro 50, Flash-Lite 39,
GPT-5.6-sol 50, GPT-5.4-mini 48, Opus 11, Sonnet 19, Haiku 20, DeepSeek 48, Grok 50, Llama 44.
Opus lowered max IOB 8/11 (73%, 43.4 to 90.3), 5 distinct pairs. Llama basal 00:00 23/44 (16
raised to 0.65, 7 lowered to 0.55), 18 with no causal attribution. DeepSeek ISF 20/48 (42%).
Citation accuracy 96.8% (Opus) to 100%. Stability: Flash-Lite 0.989, Haiku 0.928, Llama 0.953,
Opus 0.972 (others unchanged). Breaking prompt rule: Flash-Lite 6/39, Opus 5/11, Sonnet 2/19,
DeepSeek 14/48, Llama 5/44. Table S2 now 25/25 informative pastes agree (26 samples incl. demo).

## Per-decision citation check (decision_citations.py, 23 August 2026; Supplementary Table S3)

Change decisions whose rationale cites at least one figure present in the package: Flash 154/160 (96%), Pro 97/141 (69%), Flash-Lite 9/10, GPT-5.6 17/20 (85%), GPT-5.4-mini 0/2, Opus 16/16, Sonnet 1/1, Haiku 27/27, DeepSeek 84/93 (90%), Grok 16/16, Llama 3/56 (5%; 53 with no figure at all). No change rationale anywhere quoted a figure absent from the package. Manuscript now states the structured-input comparison with the settings preprint is cross-study, names Llama and DeepSeek's DIA shortening (8 conversations, 5 to 8 h) as exceptions.
