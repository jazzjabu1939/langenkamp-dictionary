---
layout: default
kind: glossary
title: "Hugging Face"
permalink: /entries/hugging-face/
date: 2026-05-12
summary: "Open-source AI platform and model hub, founded 2016. The de facto distribution channel for open-weights language models and adjacent ML artifacts."
draft: false
published: true
---

Hugging Face is a French-American AI company founded in 2016 by Clément Delangue, Julien Chaumond, and Thomas Wolf. The company operates the most-used open-source AI model hub on the internet: a platform where labs, independent researchers, and hobbyists upload pretrained model weights, datasets, training scripts, and demos under various licences. As of 2026, more than a million models and a comparable number of datasets are hosted on the platform.

For this Dictionary, Hugging Face is the **infrastructure layer the open-weights ecosystem runs on**. When the Dictionary's *[Sovereign Compute](sovereign-compute.md)* calculator recommends downloading *[Llama](llama.md)*, *[Hermes](hermes.md)*, *[Mistral](mistral.md)*, *[Gemma](gemma.md)*, *[Qwen](qwen.md)*, or any other open-weights model for local inference, the actual download is in nearly every case from Hugging Face. The company's *transformers* and *datasets* Python libraries are the standard tooling for working with these models programmatically.

Hugging Face's strategic position is unusual: it competes with no major lab directly, charges only for hosted enterprise services and compute, and has consequently become the *neutral platform* that even commercial-rival labs (Anthropic, Meta, Google) use for some artefact distribution. Its sustained existence is a non-trivial precondition for the *[Sovereign Compute](sovereign-compute.md)* argument as currently formulated.

## See also

- *[Sovereign Compute](sovereign-compute.md)*
- *[Llama](llama.md)*, *[Hermes](hermes.md)*, *[Mistral](mistral.md)*, *[Gemma](gemma.md)*, *[Qwen](qwen.md)* — models distributed via the platform
