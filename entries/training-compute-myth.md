---
layout: default
kind: glossary
title: "Training Compute Myth"
permalink: /entries/training-compute-myth/
date: 2026-07-26
summary: "The belief that AI compute is mostly spent on training, when inference is becoming the dominant operating cost for widely used AI systems."
published: true
---

The **Training Compute Myth** is the belief that most AI compute is spent training the model once, after which ordinary use is comparatively cheap.

That picture was more plausible when public attention centred on enormous one-time training runs. Training still matters, and frontier training remains astonishingly expensive. But the operating economics have shifted as AI use has scaled. Every prompt, tool call, reasoning trace, retrieval step, agent loop, and generated answer consumes inference compute. The more people use the systems, and the more reasoning and agentic workflows expand the number of generated tokens per task, the more inference becomes the live cost centre.

For students, the useful distinction is simple: **training builds the model; inference runs the model.** A trained model sitting idle is a sunk cost. A widely used model answering millions of questions is a continuing operating expense.

This matters for strategy because it changes where the bottleneck and margin pressure live. The AI business is not only a race to train the next frontier model. It is also a race to serve inference cheaply, route tasks intelligently, reduce wasted tokens, and decide when a smaller model is good enough.

## Source

Seeded by IBM Technology's July 2026 video **"5 AI Myths & The Truth Behind Them: ML, Context, Agents & More."** The video argues that inference is rising as a share of total AI compute, especially as reasoning models and agentic harnesses generate many more tokens per query.

- IBM Technology / YouTube, "5 AI Myths & The Truth Behind Them: ML, Context, Agents & More": <https://www.youtube.com/watch?v=OWPRU_Pc4Ng>.

## See also

[Token Burn](token-burn.md) · [Reasoning Model](reasoning-model.md) · [Model Tiering](model-tiering.md) · [Hyperscaler](hyperscaler.md)
