---
layout: default
kind: glossary
title: "Mixture of Experts (MoE)"
permalink: /entries/mixture-of-experts/
date: 2026-05-12
summary: "A neural-network architecture in which only a subset of parameters is *activated* for any given input token. Allows much larger total parameter counts than a dense model with the same inference cost."
draft: false
published: true
---

Mixture of Experts (MoE) is a neural-network architecture pattern in which a layer contains many parallel sub-networks (*experts*) and only a small subset is activated for any given input token. A routing network decides which experts to send each token to. The architecture allows a model to have a much larger *total* parameter count than a dense model of the same per-token compute cost: the total parameters store more knowledge, while the *active* parameters keep inference economic.

A worked example: the *[Qwen](qwen.md)* 3.6 30B A3B model has approximately 30 billion total parameters but only ~3 billion active per token (hence the *A3B* suffix). The model behaves, in terms of inference cost and latency, roughly like a 3B dense model — but stores capacity comparable to a 30B dense model. This is the structural advantage MoE offers: you can fit much more capability into the same compute budget.

The trade-off is in *routing*: the gating network has to decide which experts to use for each token, and the routing decision is harder to get right than the per-expert computation itself. In practice, MoE models tend to need more careful prompt-construction and *warming* than dense models — the *incremental construction* workflow documented in TOOLS.md is partly an adaptation to this MoE-specific behaviour.

For this Dictionary, MoE matters because **most current open-weights frontier-adjacent models are MoE** — *[Qwen](qwen.md)* 3.6, *[DeepSeek](deepseek.md)*-V3, *[Mistral](mistral.md)*'s Mixtral 8x7B and Mixtral 8x22B, and others. *[Gemma](gemma.md)* 4 is a hybrid dense+MoE design. Operators running local inference on the *[M5 Max](m5-max.md)* benefit substantially from MoE economics — the architecture is, in effect, what makes the local-compute argument viable at the current capability tier.

## See also

- *[Sovereign Compute](sovereign-compute.md)*
- *[Qwen](qwen.md)*, *[DeepSeek](deepseek.md)*, *[Mistral](mistral.md)* — MoE models
- *[Gemma](gemma.md)* — hybrid dense+MoE
