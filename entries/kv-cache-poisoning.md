---
layout: default
kind: glossary
title: "KV Cache Poisoning"
permalink: /entries/kv-cache-poisoning/
date: 2026-05-09
last_revised: 2026-09-06
summary: "The Dictionary's metaphor for error compounding when flawed output remains in the context used for later generation; not a corruption of the KV cache itself."
published: true
---

# KV Cache Poisoning

## In one sentence

**KV cache poisoning is the Dictionary's metaphor for error compounding when a model's flawed output remains in the context used for later generation. It is not a claim that the cache itself has been corrupted.**

## What the KV cache is

When a language model generates text, it need not recompute all earlier attention keys and values for every new token. During inference, a KV cache stores those tensors and reuses them for later tokens. The cache is an efficiency mechanism: it faithfully represents the processed context according to the model. It does not judge whether that context is true, useful, or well designed.

## What the metaphor names

If a model produces a faulty premise, poor architecture, or incorrect block of code and the conversation continues from that draft, the flawed material remains part of the transcript. Later tokens may attend to it, and subsequent work may inherit its assumptions. Errors can then compound: a local patch preserves a bad structure, or a critique accepts the draft's framing rather than reconsidering it.

That is context contamination, not evidence of a damaged cache. Models can sometimes diagnose and repair their own work; sometimes a clear critique, a test failure, or a better specification is enough. Recovery becomes harder when errors interact, when the original framing is misleading, or when the transcript is too long and noisy for the important constraint to remain salient.

The original entry attributed the effect to cold-start routing in *[Mixture of Experts](/entries/mixture-of-experts/)* models and claimed that the wrong expert clusters poisoned the cache. The available sources do not establish that mechanism. The practical observation does not require it and applies to dense models as well: later work can depend on earlier mistakes.

## Why this matters in practice

When a session has become anchored to a bad premise, starting again can help because it removes the misleading transcript and rebuilds the cache from a new context. It does not “reset the router” in any demonstrated task-level sense. Often a cheaper remedy is to return to the last sound checkpoint, state the defect explicitly, and provide only the relevant working material.

*[Incremental Construction](/entries/incremental-construction/)* is a preventive workflow: build a small unit, test it, and checkpoint it before later work depends on it. Its advantage is earlier error detection, not protection against physical cache corruption.

## Naming boundary

“KV cache poisoning” is not used here as an established machine-learning diagnosis. It is a Dictionary coinage for an operator experience, and the cache language should not be mistaken for a verified explanation of why a particular model failed.

## See also

[Sparse Routing](/entries/sparse-routing/) · [Incremental Construction](/entries/incremental-construction/) · [Capability Overhang](/entries/capability-overhang/)

## Sources

- Hugging Face, *Caching*: <https://huggingface.co/docs/transformers/main/en/cache_explanation>

---

*Proposed 9 May 2026 after reviewing Protorikis, “The 90's Flame Challenges the Modern MoE Models,” YouTube, 2026. The technical mechanism formerly inferred from that practitioner account has been removed.*
