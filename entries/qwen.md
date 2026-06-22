---
layout: default
kind: glossary
title: "Qwen"
permalink: /entries/qwen/
date: 2026-05-12
summary: "Open-weights language model family from Alibaba Cloud's DAMO Academy. Strong on Chinese-language tasks and long-context recall; current leaderboard performer in the local-compute tier."
draft: false
published: true
---

Qwen (通义千问, *Tōngyì Qiānwèn*) is the open-weights large language model family released by Alibaba Cloud's DAMO Academy, the research arm of Alibaba Group. The first Qwen generation was released in mid-2023; subsequent generations (Qwen 1.5, Qwen 2, Qwen 2.5, Qwen 3, Qwen 3.5, Qwen 3.6) have shipped at a faster cadence than most peer open-weights labs, with each generation expanding the parameter range from small (~0.5B) to large (~110B and beyond). The 2026-era flagship for local Apple Silicon use is **Qwen 3.6 30B A3B** — a Mixture-of-Experts model with ~30 billion total parameters and ~3 billion active per token, optimised for the kind of long-context tool-using agentic work the Dictionary's audience runs.

For this Dictionary, Qwen matters at two levels. First, **technically**: the model is the current local-compute-tier leader on long-context-recall benchmarks (the kind of test where Gemma 4's sliding-window attention pattern starts to hurt). The operator's TOOLS.md routing rule pairs Qwen with large-context multi-file tasks, while Gemma 4 covers moderate-context contained tasks. Second, **strategically**: Qwen is the most-distributed example of a PRC-produced open-weights frontier-adjacent model. Its sustained competitiveness with Western open-weights families is one of the structural facts the *zhengming* (正名) project takes as load-bearing.

## See also

- *[Open Weights](open-weights.md)*
- *[Using the Empire’s Telescope](empires-telescope.md)*
- *[Sovereign Compute](sovereign-compute.md)*
- *[Mixture of Experts](mixture-of-experts.md)*
- *[DeepSeek](deepseek.md)* — PRC peer
- *[Gemma](gemma.md)*, *[Hermes](hermes.md)*, *[Llama](llama.md)* — local-compute peers
