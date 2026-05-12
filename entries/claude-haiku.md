---
layout: default
kind: glossary
title: "Claude Haiku"
permalink: /entries/claude-haiku/
date: 2026-05-12
summary: "The fast-and-cheap tier of Anthropic's *Claude* family. The default for high-volume routine tasks where latency and cost matter more than marginal capability."
draft: false
published: true
---

Claude Haiku is the smallest and fastest tier of *[Anthropic](anthropic.md)*'s *[Claude](claude.md)* model family. Where *[Opus](claude-opus.md)* prioritises capability and *[Sonnet](claude-sonnet.md)* balances capability and cost, Haiku is optimised for *speed and price* — typical token costs are roughly one-twelfth of Opus, with latencies low enough for genuinely interactive use cases (chat, real-time tool selection, sub-second classification). Major versions include Haiku 3 (March 2024), Haiku 3.5 (November 2024), Haiku 4, 4.5, 4.6, and 4.7.

For this Dictionary, Haiku is the **high-volume routine-work tier**. Use cases that the operator's workflows actually route to Haiku: image OCR triage, low-stakes classification, the first-pass annotation that gets refined by a higher tier later, vision tasks where the operator only needs a quick description, and sub-agent dispatch decisions where the model's job is to pick a tool, not to think hard. The Dictionary's *F* (Fast & Cheap) query-mode in AGENTS.md explicitly routes to Haiku for vision and reading tasks.

Haiku's capability ceiling is meaningfully below the frontier — operators who try to do agentic writing or complex coding with Haiku as the primary engine will be disappointed. But for high-volume routine work, the cost differential makes it the rational choice.

## See also

- *[Claude](claude.md)* — the model family
- *[Claude Opus](claude-opus.md)*, *[Claude Sonnet](claude-sonnet.md)* — peer tiers
- *[Sovereign Compute](sovereign-compute.md)*
