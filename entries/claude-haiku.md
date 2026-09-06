---
layout: default
kind: glossary
title: "Claude Haiku"
permalink: /entries/claude-haiku/
date: 2026-05-12
summary: "The small, fast tier of Anthropic's Claude family, intended for work where latency and cost matter more than maximum capability."
draft: false
published: true
---

Claude Haiku is the small, fast tier of *[Anthropic](anthropic.md)*'s *[Claude](claude.md)* model family. Where *[Opus](claude-opus.md)* prioritises capability and *[Sonnet](claude-sonnet.md)* balances capability and cost, Haiku is designed for lower latency and lower-priced inference.

Typical uses include classification, extraction, routing, and other high-volume tasks whose answers can be checked cheaply. A harness may also use a smaller model for a first pass before sending harder cases to a stronger tier.

The trade-off is lower capability on difficult reasoning, writing, and coding tasks. Whether Haiku is economical depends on the task, the required reliability, and the cost of retries or escalation.

## See also

- *[Claude](claude.md)* — the model family
- *[Claude Opus](claude-opus.md)*, *[Claude Sonnet](claude-sonnet.md)* — peer tiers
- *[Sovereign Compute](sovereign-compute.md)*
