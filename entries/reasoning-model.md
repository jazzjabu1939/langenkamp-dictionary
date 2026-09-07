---
layout: default
kind: glossary
title: "Reasoning Model"
permalink: /entries/reasoning-model/
date: 2026-05-19
first_published: 2026-05-19
last_revised: 2026-09-06
summary: "A model or model mode optimized for harder multi-step work, usually spending more inference-time computation on planning, checking, and search before answering."
draft: false
published: true
---

A **reasoning model** is a model, or model mode, optimized for harder multi-step problems by spending more inference-time computation on planning, checking, and search before answering.

The term became common after OpenAI's o-series and DeepSeek's R1 made the distinction visible to ordinary users. OpenAI describes o1 as trained with large-scale reinforcement learning to perform chain-of-thought reasoning; the visible product category now includes several training methods and inference-time budgets rather than one architecture. In ordinary use, it marks the difference between a fast conversational model and one better suited to coding, mathematics, planning, debugging, or careful synthesis.

The term should not be taken too literally. A reasoning model does not necessarily reason the way a human does, and its visible explanation may not be a transparent record of its internal process. What matters operationally is that the system has been trained or configured to perform better on tasks where intermediate structure, self-checking, search, and inference-time effort matter.

For operators, the practical question is routing. Use reasoning models where the work justifies the latency and cost: proof-like reasoning, hard debugging, strategy synthesis, complex planning, and tasks where a cheap wrong answer is expensive.

## See also

[Chain of Thought](/entries/chain-of-thought/) · [Watch AI Think Myth](/entries/watch-ai-think-myth/) · [Training Compute Myth](/entries/training-compute-myth/) · [Model Tiering](/entries/model-tiering/) · [Hallucination](/entries/hallucination/) · [GPT](/entries/gpt/) · [DeepSeek](/entries/deepseek/)

## Source

- OpenAI, *[OpenAI o1 System Card](https://openai.com/index/openai-o1-system-card/)*, December 2024.
