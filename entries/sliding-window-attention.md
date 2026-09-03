---
layout: default
kind: reference
title: "Sliding Window Attention"
permalink: /entries/sliding-window-attention/
summary: "an attention mechanism in which each token attends only to a recent window of prior tokens rather than the full context history — trading long-range recall for speed and efficiency, with the consequence that models using it excel at contained tasks but lose coherence on large, complex, multi-file contexts."
published: true
---

# Sliding Window Attention

## In one sentence

**Sliding window attention is an attention mechanism in which each token attends only to a fixed recent window of prior tokens rather than the full context history — making the model faster and more memory-efficient, but causing it to lose coherence on tasks that require holding a large, complex context together simultaneously.**

## How standard attention works

In a standard transformer, every token attends to every previous token. This full attention is powerful — the model can, in principle, draw on any part of the context when generating each new token. But it is expensive: the compute cost grows quadratically with context length. A prompt of 128,000 tokens requires vastly more compute per token than a prompt of 1,000 tokens.

## What sliding window attention does differently

Sliding window attention restricts each token's attention to a recent window — say, the last 4,096 tokens — rather than the full history. Tokens outside the window are not attended to directly. This makes inference significantly faster and reduces memory requirements, because the attention matrix never grows beyond the window size regardless of total context length.

The trade-off is long-range recall. Information from early in a long context may fall outside the window by the time it is needed. The model cannot directly attend to it.

## Gemma 4's architecture and its consequences

Gemma 4 uses sliding window attention as part of its hybrid architecture (combined with a dense feed-forward network running in parallel, which is why it outperforms pure MoE models on cold-start tasks — see [Sparse Routing](sparse-routing.md)). This hybrid design explains two seemingly contradictory observations that Protorikis documented across three benchmark videos:

- **Gemma 4 26B outperformed a trillion-parameter MoE model on a cold one-shot flame animation challenge.** The task was contained: simulation logic, terminal rendering, colour algorithms — all visible within the window simultaneously. Gemma 4's dense parallel path gave it consistent access to everything it needed.

- **Gemma 4 26B failed a modem crawler challenge that Qwen 3.6 35B A3B completed.** The task required reverse-engineering login flows from thousands of lines of minified JavaScript across nineteen files. The full logic could not fit inside Gemma 4's attention window simultaneously. Critical connections between early files and later code fell outside the window before the model needed them. Coherence collapsed.

Qwen 3.6, by contrast, uses full MoE attention with gated delta mechanisms that maintain stronger long-range recall. Slower on prefill at large context, but able to hold the full picture together across hours of incremental work.

## The practical operator rule

This architectural difference produces a clear task-routing heuristic for operators running local models:

| Task type | Architecture fit |
|-----------|-----------------|
| Moderate context, contained, fast | Sliding window models (Gemma 4) |
| Large context, complex, multi-file | Full-attention MoE (Qwen 3.6) |
| Multi-dimensional cold-start | Either, with [incremental construction](incremental-construction.md) |

Knowing the architecture means knowing the failure mode before the task starts — and routing accordingly rather than discovering it after an hour of generation.

## The broader point

Sliding window attention is one instance of a general principle in local model design: every architectural decision that makes a model faster or more efficient creates a corresponding capability blind spot. The blind spot is not a bug; it is the designed trade-off. The operator who understands the trade-off routes tasks to the right model. The operator who treats all local models as interchangeable discovers the blind spot empirically, usually at an inconvenient moment.

## See also

[Sparse Routing](sparse-routing.md) · [KV Cache Poisoning](kv-cache-poisoning.md) · [Incremental Construction](incremental-construction.md) · [Capability Overhang](capability-overhang.md)

---

*Proposed May 9, 2026. Source: Protorikis, three-video local LLM benchmark series, YouTube 2026.*
