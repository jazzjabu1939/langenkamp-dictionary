---
layout: default
kind: reference
title: "Sparse Routing"
permalink: /entries/sparse-routing/
date: 2026-05-09
first_published: 2026-05-09
last_revised: 2026-09-07
summary: "The learned selection process that activates only part of a mixture-of-experts model for each token."
published: true
---

# Sparse Routing

**Sparse routing is the learned selection process that activates only a small subset of a mixture-of-experts model's expert networks for each token.** The model may contain many more parameters than it uses for any one token, which is why model cards often report both total and active parameter counts.

In a typical sparse mixture-of-experts (MoE) layer, a router scores the available experts from the token's hidden representation. The system selects the highest-scoring experts, combines their outputs, and leaves the others inactive for that token. Training also needs mechanisms that prevent a few experts from receiving nearly all the traffic.

Sparse activation can increase total model capacity without multiplying computation in direct proportion to the total parameter count. It does not make the inactive weights free: they still require storage and memory bandwidth, and routing, communication, and expert imbalance create overhead.

The earlier version of this entry claimed that sparse MoE models have a general **cold-start vulnerability** because the first generated token has no previous output, and that incremental construction repairs this by steering the router towards the right experts. That was an attractive explanation for a small set of benchmark observations, but it was not established by the cited evidence. Routing uses the prompt and the model's internal representations; benchmark differences among models cannot be assigned to routing alone without controlled tests.

Architectures also combine mechanisms. Qwen3.6-35B-A3B, for example, pairs MoE feed-forward layers with a repeating mixture of Gated DeltaNet and attention layers. Gemma 4 includes dense and MoE variants and uses hybrid local/global attention. Labels such as *MoE*, *dense*, *local attention*, and *full attention* describe parts of a system rather than a complete performance forecast.

## Practical operator rule

Use total and active parameters to understand memory and compute requirements, then test the actual model on the actual task. Sparse routing helps explain how capacity is organised. It does not, by itself, tell an operator whether a model will code well, preserve long-range context, or recover from a bad first attempt.

## Sources

- Noam Shazeer et al., *[Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/abs/1701.06538)*, 2017.
- Qwen, *[Qwen3.6-35B-A3B model card](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)*, 2026.
- Google DeepMind, *[Gemma 4 Technical Report](https://arxiv.org/abs/2607.02770)*, 2026.

## See also

*[Parameters](/entries/parameters/)* · *[Sliding Window Attention](/entries/sliding-window-attention/)* · *[Incremental Construction](/entries/incremental-construction/)* · *[Quantization](/entries/quantization/)*
