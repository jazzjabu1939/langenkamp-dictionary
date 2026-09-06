---
layout: default
kind: glossary
title: "Llama"
permalink: /entries/llama/
date: 2026-05-12
last_revised: 2026-09-06
summary: "Meta's family of downloadable model weights, beginning with LLaMA in 2023 and distributed under Meta's own community licences rather than a standard open-source licence."
draft: false
published: true
---

Llama is Meta's family of downloadable AI model weights. The name began as LLaMA — *Large Language Model Meta AI* — with a research release in February 2023. Llama 2 expanded commercial access in July 2023, Llama 3 followed in 2024, and Llama 4 introduced natively multimodal mixture-of-experts models in April 2025.

The family helped normalize a practical alternative to closed APIs: download weights, run them on infrastructure you control, fine-tune them, or build derivative models. Meta reported more than one billion cumulative Llama downloads by March 2025. That figure is a vendor count, not proof that Llama underlies most open-weight systems, as the former entry claimed; the ecosystem also includes major families such as *[Qwen](/entries/qwen/)*, *[DeepSeek](/entries/deepseek/)*, Gemma, and Mistral.

Llama is **open-weight**, but its licence is not a standard open-source software licence. The Llama 4 Community License requires attribution and compliance with an acceptable-use policy, imposes naming conditions on some derivative models, and requires services above 700 million monthly active users to seek a separate licence. Those restrictions may not burden an individual local operator, but they still matter when describing what “open” means.

For the Dictionary, Llama matters because it made capable local and self-hosted inference easier to obtain. It supports the practical case for *[Sovereign Compute](/entries/sovereign-compute/)* without settling the larger argument over whether access to weights is enough.

## See also

- *[Meta AI](/entries/meta-ai/)* — the producer
- *[Hermes](/entries/hermes/)* — a Llama-derived fine-tune family
- *[Sovereign Compute](/entries/sovereign-compute/)*
- *[Open Weights](/entries/open-weights/)*
- *[Hugging Face](/entries/hugging-face/)* — a distribution channel

## Sources

- Meta AI, *The Llama 4 herd*, 5 April 2025: <https://ai.meta.com/blog/llama-4-multimodal-intelligence/>
- Meta, *Celebrating 1 Billion Downloads of Llama*, 18 March 2025: <https://about.fb.com/news/2025/03/celebrating-1-billion-downloads-llama/>
- Meta, *Llama 4 Community License Agreement*: <https://github.com/meta-llama/llama-models/blob/main/models/llama4/LICENSE>
