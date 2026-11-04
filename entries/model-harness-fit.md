---
layout: default
kind: glossary
title: "Model–Harness Fit"
permalink: /entries/model-harness-fit/
date: 2026-08-30
summary: "The degree to which a model's actual behavior suits the tools, context strategy, permissions, memory, verification, and recovery rules of the harness in which it works."
published: true
---

**Model–Harness Fit** is the degree to which a model's actual behavior suits the tools, context strategy, permissions, memory, verification, and recovery rules of the harness in which it works.

Model quality and harness quality are not simply additive. A strong model may perform poorly when tool descriptions are unclear to it, the context is arranged against its attention pattern, or the recovery loop assumes behavior it does not reliably exhibit. A less capable model may perform very well inside a narrow harness built around routine, inspectable work.

This is why model evaluation cannot stop at the naked model. The useful unit of analysis is the whole agent performing a real workflow: receiving the task, finding the right context, using the permitted tools, recognizing failure, producing evidence, and stopping appropriately.

Fit is also perishable. A harness built around yesterday's model weakness can become dead weight after a model upgrade. A model swap can quietly break tool use, memory retrieval, tone, or escalation even when benchmark scores improve. Every important change in model or harness therefore needs an end-to-end test.

## Source

The term crystallized in the Dictionary's August 2026 discussion of IBM Technology's **“AI Model vs Agentic Harness: What Actually Drives AI.”** IBM supplies the model/harness distinction; *Model–Harness Fit* names the interaction the distinction can otherwise hide.

- IBM Technology / YouTube, “AI Model vs Agentic Harness: What Actually Drives AI”: <https://www.youtube.com/watch?v=ZELPNFXJ4_o>.

## See also

[Harness](harness.md) · [Raw IQ](raw-iq.md) · [Agentic Loop](agentic-loop.md) · [Verification](verification.md) · [Routing Logic](routing-logic.md) · [Task Distribution](task-distribution.md)
