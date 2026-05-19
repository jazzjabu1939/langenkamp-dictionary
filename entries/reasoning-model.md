---
layout: default
kind: glossary
title: "Reasoning Model"
permalink: /entries/reasoning-model/
date: 2026-05-19
summary: "A model or model mode optimised for harder multi-step work, usually spending more inference-time computation before answering."
draft: false
published: true
---

A **reasoning model** is a model, or model mode, designed to spend more computation on multi-step problems before producing an answer. In ordinary use, the phrase marks the difference between a fast conversational model and one better suited to coding, mathematics, planning, debugging, or careful synthesis.

The term should not be taken too literally. A reasoning model does not necessarily reason the way a human does, and its visible explanation may not be a transparent record of its internal process. What matters operationally is that the system has been trained or configured to perform better on tasks where intermediate structure, self-checking, and inference-time effort matter.

For operators, reasoning models belong in the expensive tier. Use them when the work justifies the latency and cost; do not waste them on routine formatting.

## See also

- *[Chain of Thought](chain-of-thought.md)*
- *[Model Tiering](model-tiering.md)*
- *[Hallucination](hallucination.md)*
