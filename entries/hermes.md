---
layout: default
kind: glossary
title: "Hermes"
permalink: /entries/hermes/
date: 2026-05-12
summary: "Open-weights LLM family from Nous Research, fine-tuned for instruction-following, tool use, and roleplay-style dialogue. The Dictionary's default local-model recommendation in the *Sovereign Compute* calculator."
draft: false
published: true
---

Hermes is a family of fine-tuned open-weights large language models produced by *[Nous Research](nous-research.md)*, the open-source AI collective. Hermes models start from existing open-weights base models — typically *[Llama](llama.md)*, occasionally *[Mistral](mistral.md)* — and are post-trained for instruction-following, tool use, and a more conversational register than the bare base models offer. The family includes versions ranging from approximately 7 billion parameters (suitable for laptops with 16+ GB of RAM) up to 405 billion parameters (requiring multi-GPU server hardware).

For this Dictionary, Hermes is the **practical default** in the *[Sovereign Compute](sovereign-compute.md)* calculator's Level-3 sovereignty tier — the recommendation for an operator who wants a known-quantity instruction-tuned model running locally on Apple Silicon hardware, without doing their own fine-tuning. The model's character is somewhat looser than the closed-weights frontier models (Claude Opus, GPT-5) but the gap is structurally manageable for most agentic workflows the Dictionary's audience runs.

Distribution is via *[Hugging Face](hugging-face.md)*; the standard local-inference runners (*[LM Studio](lm-studio.md)*, *[Ollama](ollama.md)*) ship Hermes presets out of the box.

## See also

- *[Nous Research](nous-research.md)* — the producer
- *[Sovereign Compute](sovereign-compute.md)*
- *[Llama](llama.md)* — the typical base
- *[LM Studio](lm-studio.md)*, *[Ollama](ollama.md)* — runners
