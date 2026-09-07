---
layout: default
kind: glossary
title: "Training Compute Myth"
permalink: /entries/training-compute-myth/
first_published: 2026-07-26
last_revised: 2026-09-07
date: 2026-07-26
summary: "The assumption that AI compute is mostly a one-time training expense, overlooking the continuing inference cost of deployed systems."
published: true
---

The **Training Compute Myth** is the belief that most AI compute is spent training the model once, after which ordinary use is comparatively cheap.

That picture misses the continuing cost of deployment. Training still matters, and frontier training is expensive. But every model invocation consumes inference compute, including the model calls used around tool execution, retrieval, reasoning, and agent loops. At sufficient usage, aggregate inference can rival or exceed training expenditure for a particular service. The balance varies by model, workload, utilisation, hardware, and accounting boundary; there is no universal crossover.

For students, the useful distinction is simple: **training builds the model; inference runs the model.** A trained model sitting idle is a sunk cost. A widely used model answering millions of questions is a continuing operating expense.

This matters for strategy because it changes where the bottleneck and margin pressure live. The AI business is not only a race to train the next frontier model. It is also a race to serve inference cheaply, route tasks intelligently, reduce wasted tokens, and decide when a smaller model is good enough.

## Source

Seeded by IBM Technology's July 2026 video **"5 AI Myths & The Truth Behind Them: ML, Context, Agents & More."** The video argues that inference is rising as a share of AI compute, especially as reasoning models and agentic harnesses generate more tokens per task. The entry keeps the narrower, workload-dependent claim rather than treating inference dominance as universal.

- IBM Technology / YouTube, "5 AI Myths & The Truth Behind Them: ML, Context, Agents & More": <https://www.youtube.com/watch?v=OWPRU_Pc4Ng>.

## See also

[Token Burn](/entries/token-burn/) · [Reasoning Model](/entries/reasoning-model/) · [Model Tiering](/entries/model-tiering/) · [Hyperscaler](/entries/hyperscaler/)
