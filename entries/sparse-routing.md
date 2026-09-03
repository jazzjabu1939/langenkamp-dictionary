---
layout: default
kind: reference
title: "Sparse Routing"
permalink: /entries/sparse-routing/
summary: "the mechanism in Mixture of Experts models by which a learned router activates only a small fraction of the model's total parameters for each token — trading consistency for speed, and creating the cold-start vulnerability that incremental construction is designed to address."
published: true
---

# Sparse Routing

## In one sentence

**Sparse routing is the mechanism in Mixture of Experts (MoE) models by which a learned router activates only a small subset of the model's total expert sub-networks for each token — making MoE models faster and larger than dense models at equivalent cost, while introducing a cold-start vulnerability that does not exist in dense architectures.**

## How it works

A standard dense language model activates all of its parameters for every token it generates. A Mixture of Experts model divides its parameters into a large number of specialist sub-networks (experts) and trains a router to decide, for each token, which small subset of experts to activate. The Qwen3 30B A3B model, for example, has approximately 256 experts but activates only 10 of them per token — hence "30 billion total parameters, 3 billion active." The routing decision is made fresh for each token, based on the accumulated context.

The economic logic is straightforward: by keeping most parameters inactive at any given moment, MoE models can be much larger in total parameter count (and therefore more capable on tasks that benefit from scale) without requiring proportionally more compute per token. This is why many of the largest and fastest local models are MoE architectures.

## The cold-start problem

The router's decisions are only as good as the context it routes against. On the first token of a generation, the context is essentially the input prompt alone — there is no prior output to inform the routing. This cold-start routing is where MoE models are most vulnerable. If the task requires simultaneous competence across multiple distinct knowledge domains (stateful simulation *and* terminal rendering *and* colour algorithms, in Protorikis's flame example), the router must happen to activate the right expert clusters across all dimensions from the very first token. Miss one dimension early, and [KV cache poisoning](kv-cache-poisoning.md) can compound the error across the rest of the generation.

Dense models do not have this problem because they are not routing at all — all parameters engage with every token. This makes dense models slower and more expensive per token but more consistent, especially on complex cold-start tasks.

## Gemma 4's unusual architecture

Gemma 4 is technically a MoE model but runs a dense feed-forward network in parallel with the sparse routing layer. This hybrid design means it never fully loses the consistency of a dense model, even when the sparse routing makes suboptimal choices. In Protorikis's flame benchmark, this is why Gemma 4 26B (4B active parameters) outperformed much larger pure-MoE models on a cold one-shot prompt: the dense parallel path provided a floor that the pure-MoE models lacked.

## What this means for local model selection

The choice between MoE and dense local models is not simply "bigger vs. smaller." It is a question of task structure:

- **Cold-start, multi-dimensional, complex tasks** → dense models or Gemma 4's hybrid; or use [incremental construction](incremental-construction.md) with a MoE model to avoid the cold-start problem
- **Simpler, narrower tasks where context is established** → MoE models perform well and are faster
- **Speed-critical applications** → MoE models (more total capability per unit of inference compute)

The operator who understands sparse routing can route tasks to the right local model rather than treating all local models as interchangeable.

## See also

[KV Cache Poisoning](kv-cache-poisoning.md) · [Incremental Construction](incremental-construction.md) · [Capability Overhang](capability-overhang.md) · [Opus Addict](opus-addict.md)

---

*Proposed May 9, 2026. Source: Protorikis, "The 90's Flame Challenges the Modern MoE Models," YouTube 2026.*
