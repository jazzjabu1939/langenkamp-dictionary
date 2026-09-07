---
layout: default
kind: glossary
title: "Qwen"
permalink: /entries/qwen/
date: 2026-05-12
summary: "Alibaba's broad family of language, multimodal, coding, and specialist AI models, including many downloadable open-weight releases."
draft: false
published: true
first_published: 2026-05-12
last_revised: 2026-09-06
---

**Qwen** (通义千问, *Tōngyì Qiānwèn*) is Alibaba's family of language, multimodal, coding, audio, image, and specialist AI models. The family began with Qwen-7B in 2023 and includes both hosted products and many downloadable open-weight releases. *Qwen* is therefore a family name, not a reliable statement about one model's size, architecture, licence, or availability; the model card still has to be read.

As of September 2026, the Qwen 3.8 family shows the range. Alibaba released **Qwen3.8-27B**, a dense multimodal model under Apache 2.0 that can be quantized for consumer hardware. At the other end sits **Qwen3.8-2.4T-A95B**, a mixture-of-experts model with 2.4 trillion total and 95 billion active parameters. These are different deployment propositions. The 27B model is relevant to a local operator; the flagship requires infrastructure far beyond an ordinary workstation.

Qwen matters to this Dictionary because it joins local usefulness with ecosystem scale. Hugging Face's summer 2026 analysis counted Qwen models across a wide range of sizes and reported more than 151,000 derivative repositories. That supports a claim about adoption and distribution, not automatic superiority on every benchmark. Model quality remains dependent on the release, quantization, runtime, harness, language, and task.

It also complicates the old geopolitical map. A PRC-based company has supplied a large share of the downloadable model layer used by developers around the world. Running a Qwen release locally can provide operational control over inference, but it does not make the training data, post-training choices, or institutional origin disappear. Sovereignty and provenance remain separate questions.

## Sources

- Qwen Team, *[Introducing Qwen](https://qwenlm.github.io/blog/qwen/)*.
- Alibaba Cloud, *[Alibaba Unveils Qwen3.8-27B and Releases Weights of Qwen3.8 Flagship Model](https://www.alibabacloud.com/blog/alibaba-unveils-qwen3-8-27b-and-releases-weights-of-qwen3-8-flagship-model_603463)* (August 2026).
- Hugging Face, *[State of Open Models: Summer 2026 Observations](https://huggingface.co/blog/state-of-open-models-summer-2026)*.

## See also

- *[Open Weights](/entries/open-weights/)*
- *[Using the Empire’s Telescope](/entries/empires-telescope/)*
- *[Sovereign Compute](/entries/sovereign-compute/)*
- *[Mixture of Experts](/entries/mixture-of-experts/)*
- *[DeepSeek](/entries/deepseek/)* — PRC peer
- *[Gemma](/entries/gemma/)*, *[Hermes](/entries/hermes/)*, *[Llama](/entries/llama/)* — local-compute peers
