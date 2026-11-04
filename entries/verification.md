---
layout: default
kind: glossary
title: "Verification"
permalink: /entries/verification/
date: 2026-08-30
summary: "The act of testing an agent's claim, artifact, or action against evidence outside the process that produced it."
published: true
---

**Verification** is the act of testing an agent's claim, artifact, or action against evidence outside the process that produced it.

The outside evidence may be a test suite, source document, calculation, schema, screenshot, second implementation, physical observation, independent reviewer, or human judgment. What matters is that the system does not treat confidence, fluency, or successful completion of a tool call as proof that the work is correct.

Verification belongs inside the [agentic loop](agentic-loop.md), not merely at its end. A long workflow built on an early mistake can produce a polished final artifact whose entire coherence rests on the wrong premise. Small checks made while the work is still reversible are usually cheaper and more informative than one grand inspection after completion.

Self-review can help, but it is not independence. The same model may reproduce the same blind spot when asked to judge its own work. Consequential tasks therefore need evidence with some structural separation from the worker: executable tests, primary sources, a differently prompted or different model, a judge component, or a human who retains authority over the result.

[Verification Gap](verification-gap.md) names the distance between what can be shown and what can reliably be known. [The Judge Layer](judge-layer.md) names an architectural tier that performs or enforces judging functions. **Verification** is the underlying discipline both entries require.

## See also

[Verification Gap](verification-gap.md) · [The Judge Layer](judge-layer.md) · [Agentic Loop](agentic-loop.md) · [Covert Channel](covert-channel.md) · [Incremental Construction](incremental-construction.md) · [Approval Gating](approval-gating.md) · [Trust Layer](trust-layer.md)
