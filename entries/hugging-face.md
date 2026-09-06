---
layout: default
kind: glossary
title: "Hugging Face"
permalink: /entries/hugging-face/
date: 2026-05-12
summary: "An AI collaboration platform and hub for models, datasets, and applications; a central distribution layer for open-weight machine learning."
draft: false
published: true
---

**Hugging Face** is an AI company and collaboration platform founded in 2016 by Clément Delangue, Julien Chaumond, and Thomas Wolf. Its Hub hosts versioned repositories for models, datasets, and applications called Spaces. Repositories may be public, private, open, gated, or distributed under licences that impose important limits; presence on the Hub does not by itself make an artefact open source.

For this Dictionary, Hugging Face is a central distribution layer for the open-weight ecosystem. Models from [Llama](/entries/llama/), [Hermes](/entries/hermes/), [Mistral](/entries/mistral/), [Gemma](/entries/gemma/), [Qwen](/entries/qwen/), and many other families are commonly downloaded from the Hub for local inference. The company's `transformers` and `datasets` libraries are also widely used to load and work with machine-learning artefacts programmatically.

The Hub's scale makes it infrastructure, though "neutral" would be too strong. Hugging Face sets platform rules, offers paid storage, compute, inference, and enterprise services, and must make moderation and access decisions. At the same time, competing labs, companies, researchers, and hobbyists can distribute artefacts through the same interface. That shared layer makes open-weight models easier to find, compare, version, and download.

The [Sovereign Compute](/entries/sovereign-compute/) argument does not require one commercial hub to last forever. It does require weights and documentation to remain obtainable, licensable, verifiable, and runnable outside a single vendor's hosted product. Hugging Face currently makes that path much easier.

## Sources

- Hugging Face, [Hub documentation](https://huggingface.co/docs/hub/index), accessed 6 September 2026.
- Hugging Face, [pricing](https://huggingface.co/pricing), accessed 6 September 2026.

## See also

- *[Sovereign Compute](/entries/sovereign-compute/)*
- *[Llama](/entries/llama/)*, *[Hermes](/entries/hermes/)*, *[Mistral](/entries/mistral/)*, *[Gemma](/entries/gemma/)*, *[Qwen](/entries/qwen/)* — model families distributed through the platform
