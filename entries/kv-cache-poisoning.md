---
layout: default
kind: glossary
title: "KV Cache Poisoning"
permalink: /entries/kv-cache-poisoning/
date: 2026-05-09
last_revised: 2026-10-03
summary: "Context contamination, formerly described here as KV cache poisoning; distinguished from actual attacks on KV cache reuse."
published: true
---

# KV Cache Poisoning

## In one sentence

**This Dictionary originally used “KV cache poisoning” as a metaphor for context contamination: earlier errors remain in a model's working context and influence later answers. Context contamination is the more accurate name for that phenomenon.**

The existing title and address are retained so earlier references remain usable. The metaphor must be distinguished from security attacks that actually exploit cached model state.

## Context contamination

If a conversation contains a faulty premise, incorrect code, or a misleading plan, later responses may inherit it. The model may patch details while preserving the original mistake. This can happen even when KV caching is disabled: the problem is the material being used as context, not the cache mechanism.

Models can also correct earlier work. A clear statement of the defect, a failing test, or a return to a verified checkpoint may be enough. Starting a new session can help when the transcript is dominated by misleading material, but it does not guarantee a better answer.

## What a KV cache does

During generation, a language model can store attention keys and values computed for earlier tokens and reuse them rather than recomputing them for each new token. This KV cache makes inference more efficient. It is not a truth check, and it is not the same thing as a saved conversation or long-term memory.[1]

## Actual cache-security attacks

Security researchers also study attacks on KV reuse. In *HijackKV*, researchers describe how certain position-independent cache-reuse designs can reuse state that encodes an attacker-controlled prefix. A later request can then be influenced even though the attacker's text is absent from that request.[2]

That is an attack on a particular cache-reuse design, not simply a model continuing from its own incorrect answer. It does not establish that every KV cache is vulnerable.

## Practical response to contaminated context

- Identify the faulty premise rather than repeatedly patching its consequences.
- Return to the last verified version where possible.
- Supply the relevant evidence, constraints, and test results.
- Start again with a smaller, corrected context if the existing conversation remains misleading.

*[Incremental Construction](/entries/incremental-construction/)* helps by detecting mistakes before later work depends on them. Its benefit does not require a theory about corrupted caches or misrouted experts.

An earlier version attributed the effect to cold-start routing in mixture-of-experts models. The cited practitioner account did not establish that mechanism; that explanation has been withdrawn.

## Sources

[1] Hugging Face, [Caching](https://huggingface.co/docs/transformers/main/en/cache_explanation).

[2] Yichi Zhang et al., [*HijackKV: New Threat in Position-Independent KV Cache Reuse*](https://arxiv.org/abs/2607.19957), 2026.

## See also

[Sparse Routing](/entries/sparse-routing/) · [Incremental Construction](/entries/incremental-construction/) · [Capability Overhang](/entries/capability-overhang/)
