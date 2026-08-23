# Citation verification — do the quoted figures exist in the package?

Every number with a unit (mg/dL, %, U/h, U, h, min, g/U) quoted in the accepted JSON's summary, issues, strengths, step findings and evidence, decision rationales and profile recommendation is checked against the numbers present in the package (telemetry, profile, inventory), to the precision quoted. Derived figures the model computes itself count as unverified, so rates are lower bounds but comparable across models.

| Model | Runs | Figures quoted | Verified | Rate | Per-run median (min–max) | Commonest unverified figures |
|---|---|---|---|---|---|---|
| deepseek/deepseek-v4-pro | 48 | 2757 | 2738 | 0.993 | 1.00 (0.95–1.00) | 0.27u ×3, 160mg/dl ×3, 250mg/dl ×2, 39.2mg/dl ×2, 210mg/dl ×1, 335mg/dl ×1 |
| gemini-3.1-pro-preview | 50 | 1899 | 1897 | 0.999 | 1.00 (0.97–1.00) | 39.9mg/dl ×1, 36.7mg/dl ×1 |
| gemini-3.5-flash-lite | 39 | 1525 | 1523 | 0.999 | 1.00 (0.97–1.00) | 250mg/dl ×1, 160mg/dl ×1 |
| gemini-3.6-flash | 50 | 4823 | 4812 | 0.998 | 1.00 (0.98–1.00) | 160mg/dl ×5, 280mg/dl ×2, 250mg/dl ×1, 37.8mg/dl ×1, 0.48u ×1, 176mg/dl ×1 |
| gpt-5.4-mini | 48 | 869 | 869 | 1.0 | 1.00 (1.00–1.00) |  |
| gpt-5.6-sol | 50 | 2574 | 2571 | 0.999 | 1.00 (0.98–1.00) | 16.2u ×2, 176mg/dl ×1 |
| x-ai/grok-4.6 | 50 | 4111 | 4073 | 0.991 | 0.99 (0.97–1.00) | 16.2u ×38 |
| claude-haiku-4-5 | 20 | 6691 | 6528 | 0.976 | 0.98 (0.94–0.99) | 0.175u ×15, 280mg/dl ×12, 160mg/dl ×12, 0.125u ×10, 3.7mg/dl ×10, 890mg/dl ×9 |
| meta-llama/llama-4-maverick | 44 | 438 | 438 | 1.0 | 1.00 (1.00–1.00) |  |
| claude-opus-5 | 11 | 2789 | 2700 | 0.968 | 0.97 (0.93–1.00) | 16.2u ×49, 0.27u ×6, 0.167u ×6, 0.23u ×5, 160mg/dl ×4, 176mg/dl ×3 |
| claude-sonnet-5 | 19 | 1027 | 1017 | 0.99 | 1.00 (0.96–1.00) | 178.6mg/dl ×2, 16.2u ×2, 280mg/dl ×2, 250mg/dl ×1, 176mg/dl ×1, 265mg/dl ×1 |