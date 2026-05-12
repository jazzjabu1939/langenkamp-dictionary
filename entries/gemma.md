---
layout: default
kind: glossary
title: "Gemma"
permalink: /entries/gemma/
date: 2026-05-12
summary: "Google DeepMind's open-weights model family, derived from the Gemini lineage. The operator runs Gemma 4 26B and 31B locally on Apple Silicon."
draft: false
published: true
---

Gemma is the open-weights model family released by *[Google DeepMind](google-deepmind.md)*, structured as a sibling to the proprietary *[Gemini](gemini.md)* line. The first Gemma generation was released in February 2024; subsequent generations (Gemma 2, Gemma 3, Gemma 4) have shipped at increasing scales and capabilities. As of May 2026, the operator of this Dictionary runs **Gemma 4 26B and Gemma 4 31B** locally on the M5 Max workstation as part of the practical *[Sovereign Compute](sovereign-compute.md)* setup — see TOOLS.md notes on hybrid dense+MoE architecture and sliding-window attention.

For this Dictionary, Gemma matters as **the open-weights family produced by an actor with frontier-lab resources and full-Gemini-team backing**. Where Mistral and Llama are produced by labs that have made the open-weights posture their primary strategic move, Gemma is produced by a lab with closed-weights frontier products that has chosen, deliberately, to release competitive open-weights alongside them. The behaviour is asymmetric to OpenAI (which has released essentially no open weights since GPT-2) and Anthropic (no open weights at all) and somewhat parallel to Meta's Llama posture.

Strengths of Gemma 4 relative to peer open-weights models (Hermes, Qwen) on local Apple Silicon: fast on contained tasks, punches above weight on moderate-context workloads. Weaknesses: the sliding-window attention pattern limits the model's behaviour on large-context multi-file tasks, where Qwen 3.6 currently outperforms.

## See also

- *[Google DeepMind](google-deepmind.md)*
- *[Gemini](gemini.md)* — the proprietary sibling line
- *[Sovereign Compute](sovereign-compute.md)*
- *[Hermes](hermes.md)*, *[Qwen](qwen.md)*, *[Llama](llama.md)* — peers in the local-compute tier
