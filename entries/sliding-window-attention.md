---
layout: default
kind: reference
title: "Sliding Window Attention"
permalink: /entries/sliding-window-attention/
date: 2026-05-09
first_published: 2026-05-09
last_revised: 2026-09-07
summary: "An attention pattern in which a token attends directly to a limited neighbourhood rather than every token in the context."
published: true
---

# Sliding Window Attention

**Sliding window attention is an attention pattern in which each token attends directly to a limited neighbourhood of tokens rather than to the entire sequence.** In a causal language model, that usually means a fixed number of preceding tokens.

Full self-attention allows every token to attend to every earlier token, but its attention computation and memory grow rapidly with sequence length. A local window limits that work. This can make long sequences cheaper to process, at the cost of removing a direct attention path between tokens that are far apart.

That cost is not the same as saying that a model simply forgets everything outside the window. Modern systems often combine local and global layers, recurrence, retrieval, summaries, or other mechanisms that carry information across longer distances. The effective context of a complete model therefore cannot be inferred from the local-window size alone.

Google's Gemma 4 illustrates the distinction. Its technical report describes a hybrid schedule that interleaves local sliding-window attention with global self-attention. The earlier version of this entry treated Gemma 4 as if every layer used only a recent window and then attributed two benchmark outcomes to that single feature. The architecture does not support that explanation, and two anecdotal tasks cannot isolate an architectural cause.

## Practical operator rule

Sliding-window attention is one factor in model selection, not a task router by itself. For work that depends on distant parts of a large context, test the actual model on representative files and measure retrieval or recall at the relevant depth. A published context-window number tells you how much input the system accepts; it does not guarantee equal use of every part of that input.

## Sources

- Iz Beltagy, Matthew E. Peters, and Arman Cohan, *[Longformer: The Long-Document Transformer](https://arxiv.org/abs/2004.05150)*, 2020.
- Google DeepMind, *[Gemma 4 Technical Report](https://arxiv.org/abs/2607.02770)*, 2026.

## See also

*[Sparse Routing](/entries/sparse-routing/)* · *[Context Window](/entries/context-window/)* · *[KV Cache Explosion](/entries/kv-cache-explosion/)* · *[Incremental Construction](/entries/incremental-construction/)*
