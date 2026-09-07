---
layout: default
kind: glossary
title: "Quantization"
permalink: /entries/quantization/
date: 2026-05-16
summary: "Representing model weights or activations at lower numerical precision to reduce storage, memory use, and sometimes inference cost."
draft: false
published: true
first_published: 2026-05-16
last_revised: 2026-09-06
---

**Quantization** represents model weights, activations, or both with lower-precision numbers. In local language-model use, the word usually refers to storing trained weights with fewer bits than the original floating-point representation. This reduces the model file and its weight-memory requirement; speed may also improve when the hardware and runtime have efficient kernels for the chosen format.

A 70-billion-parameter model stored at four bits per parameter has a theoretical weight payload of about 35 GB. The running system needs more: quantization scales and metadata, activations, runtime buffers, and a key-value cache whose size grows with context and workload. A nominally 35 GB model therefore does not fit safely in 35 GB of available memory. Even so, quantization can turn a model that would require roughly 140 GB for 16-bit weights into one that fits on a high-memory consumer machine.

The quality trade-off is not one fixed percentage. It depends on the model, quantization method, bit width, calibration, runtime, and task. Four-bit and five-bit versions can be useful for everyday inference, but lower precision can also damage particular capabilities. The deployed model should be tested on the work that matters rather than judged from its filename alone.

For the Dictionary's sovereignty argument, quantization is one of the enabling technologies. It turns open-weights models from museum objects into working tools. Without it, local-first AI would remain mostly a datacenter story.

## Sources

- Hugging Face, *[Quantization](https://huggingface.co/docs/transformers/en/main_classes/quantization)*.
- Apple, *[Accelerate machine learning with Metal](https://developer.apple.com/videos/play/wwdc2024/10218/)*.
- NVIDIA, *[Model Quantization: Concepts, Methods, and Why It Matters](https://developer.nvidia.com/blog/model-quantization-concepts-methods-and-why-it-matters/)*.

## See also

- *[Parameters](/entries/parameters/)*
- *[Open source](/entries/open-source/)*
- *[Ollama](/entries/ollama/)*
- *[LM Studio](/entries/lm-studio/)*
- *[Sovereign Compute](/entries/sovereign-compute/)*
