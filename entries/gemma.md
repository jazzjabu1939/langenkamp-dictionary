---
layout: default
kind: glossary
title: "Gemma"
permalink: /entries/gemma/
date: 2026-05-12
summary: "Google DeepMind's family of open-weight models, designed for deployment and adaptation outside Google's hosted services."
draft: false
published: true
---

Gemma is the open-weight model family released by *[Google DeepMind](/entries/google-deepmind/)* alongside the proprietary *[Gemini](/entries/gemini/)* line. The first Gemma models appeared in February 2024. Gemma 4, released in March 2026, included dense and mixture-of-experts variants, multimodal input, and context windows of up to 256,000 tokens.

For this Dictionary, Gemma matters because a laboratory with a major closed-model business also releases weights that operators can run and adapt elsewhere. That makes the family useful for practical *[Sovereign Compute](/entries/sovereign-compute/)* experiments without pretending that “open weights” settles every question about training data, licensing, or reproducibility.

In the operator's May 2026 tests on Apple Silicon, Gemma 4 was fast on contained tasks, while *[Qwen](/entries/qwen/)* was more reliable on some large-context, multi-file work. That is a dated local observation, not a universal model ranking: quantisation, runtime, prompt construction, and hardware all affect the result.

## Sources

- Google, [Gemma releases](https://ai.google.dev/gemma/docs/releases).
- Google, [Gemma 4 model overview](https://ai.google.dev/gemma/docs/core).

## See also

- *[Google DeepMind](/entries/google-deepmind/)*
- *[Gemini](/entries/gemini/)* — the proprietary sibling line
- *[Sovereign Compute](/entries/sovereign-compute/)*
- *[Hermes](/entries/hermes/)*, *[Qwen](/entries/qwen/)*, *[Llama](/entries/llama/)* — peers in the local-compute tier
