---
layout: default
kind: glossary
title: "KV Cache Poisoning"
permalink: /entries/kv-cache-poisoning/
summary: "the feedback loop in which a model's early flawed output contaminates the context against which all subsequent tokens are generated — making self-correction unreliable because the correction runs against the same bad context that caused the error."
published: true
---

# KV Cache Poisoning

## In one sentence

**KV cache poisoning is the feedback loop in which a model's early flawed output becomes part of the context all subsequent tokens are generated against — making self-correction unreliable, because the model is now trying to fix bad code by reasoning through the bad code.**

## What the KV cache is

When a language model generates text, it does not re-read the entire prompt from scratch for every new token. It stores the computed representations of previous tokens in a key-value cache (the KV cache) and attends to those stored representations efficiently. This is what makes long-context generation tractable. The KV cache is, in effect, the model's working memory for the current generation.

## How it gets poisoned

In a Mixture of Experts model (see [Sparse Routing](sparse-routing.md)), the router selects a small subset of expert sub-networks for each token based on what has come before. If the first several tokens of a complex generation go wrong — because the cold-start routing activated the wrong expert clusters for the task — the resulting flawed output enters the KV cache. Every subsequent token is now generated with that flawed output as part of its context.

The model is not stupid. It can often detect that something is wrong. But the detection and the attempted correction are both happening through the same routing mechanism, against the same poisoned context. The critique runs against the poisoned cache. The correction is itself routed through the contaminated context. The fix is often another variation on the original mistake, or a patch that introduces new inconsistencies.

This is why asking a model to "review and fix" its own sloppy output often produces either minor cosmetic changes or a different kind of broken. The problem is not that the model cannot write good code; it is that the model is now entangled in the context of the bad code it already wrote.

## Why this matters in practice

Practitioners who work with AI-assisted coding, writing, or analysis regularly experience this without having a name for it: the model starts poorly, and no amount of follow-up prompting brings it back to the quality level the task requires. The common response is to start a fresh session — which works, because it clears the KV cache entirely and gives the router a clean start. The less common but more efficient response is to use incremental construction (see [Incremental Construction](incremental-construction.md)) so that the cache never gets poisoned in the first place.

The phenomenon is more pronounced in Mixture of Experts architectures because the cold-start routing problem creates the initial flawed output; it exists in dense models too, but is less acute because all parameters are always engaged.

## See also

[Sparse Routing](sparse-routing.md) · [Incremental Construction](incremental-construction.md) · [Capability Overhang](capability-overhang.md)

---

*Proposed May 9, 2026. Source: Protorikis, "The 90's Flame Challenges the Modern MoE Models," YouTube 2026.*
