---
layout: default
kind: glossary
title: "Quantization"
permalink: /entries/quantization/
date: 2026-05-16
summary: "The compression technique that stores model weights with fewer bits, making large open-weights models practical on consumer hardware."
draft: false
published: true
---

**Quantization** is the process of representing a model's weights with fewer bits than were used during training or full-precision inference. Instead of storing each weight as a large floating-point number, a quantized model stores an approximation. The result is smaller memory use and often faster local inference, at some cost to precision.

This is why a model with tens of billions of parameters can run on a high-end consumer machine. A 70-billion-parameter model at full precision is too large for ordinary local hardware; a 4-bit or 5-bit quantized version may fit into unified memory and become usable. The tradeoff is not binary. Some quantizations are excellent for everyday use; others degrade reasoning, coding, or long-context recall noticeably.

For the Dictionary's sovereignty argument, quantization is one of the enabling technologies. It turns open-weights models from museum objects into working tools. Without it, local-first AI would remain mostly a datacenter story.

## See also

- *[Open source](open-source.md)*
- *[Ollama](ollama.md)*
- *[LM Studio](lm-studio.md)*
- *[Sovereign Compute](sovereign-compute.md)*
