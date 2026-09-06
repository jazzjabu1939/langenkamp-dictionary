---
layout: default
kind: glossary
title: "Hermes"
permalink: /entries/hermes/
date: 2026-05-12
summary: "A Nous Research family of post-trained open-weight language models built for steerability, reasoning, structured output, and tool use."
draft: false
published: true
---

**Hermes** is a family of post-trained open-weight language models produced by [Nous Research](/entries/nous-research/). Nous takes existing base models and trains them for instruction following, steerability, structured output, reasoning, and tool use.

Hermes is a family name rather than one fixed architecture. Hermes 4 includes a 14-billion-parameter model based on Qwen 3 and 70-billion- and 405-billion-parameter models based on Llama 3.1. Hermes 4.3 added a 36-billion-parameter model based on ByteDance Seed. Older Hermes releases used other bases, including Mistral. The name therefore tells you mainly about Nous's post-training approach; the model card still matters for architecture, licence, hardware needs, prompt format, and supported tools.

For local use, operators usually download official weights or community quantisations from [Hugging Face](/entries/hugging-face/) and run them through software such as [LM Studio](/entries/lm-studio/) or [Ollama](/entries/ollama/). A small quantised release may fit on a laptop; a 70B or 405B model requires much more memory and, at useful speeds, usually server-class hardware. The runner, quantisation, context length, and model variant all affect the result.

Hermes remains relevant to the Dictionary's [Sovereign Compute](/entries/sovereign-compute/) argument because it offers inspectable weights and local deployment choices. It should be treated as one candidate family, not as a timeless default. Local-model recommendations age quickly and should be tested against the operator's actual hardware and work.

## Sources

- Nous Research, [Hermes 4 collection](https://huggingface.co/collections/NousResearch/hermes-4-collection).
- Nous Research, [Hermes 4 — Qwen 3 14B model card](https://huggingface.co/NousResearch/Hermes-4-14B).
- Nous Research, [Hermes 4.3 36B model card](https://huggingface.co/NousResearch/Hermes-4.3-36B).

## See also

- *[Nous Research](/entries/nous-research/)* — the producer
- *[Sovereign Compute](/entries/sovereign-compute/)*
- *[Llama](/entries/llama/)* and *[Qwen](/entries/qwen/)* — base-model families used by Hermes 4
- *[LM Studio](/entries/lm-studio/)* and *[Ollama](/entries/ollama/)* — local runners
