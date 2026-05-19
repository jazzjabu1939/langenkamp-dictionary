---
layout: default
kind: glossary
title: "Model Tiering"
permalink: /entries/model-tiering/
date: 2026-05-16
summary: "The practice of matching model capability, cost, speed, privacy, and context requirements to the task instead of using one model for everything."
draft: false
published: true
---

**Model tiering** is the operational practice of routing different tasks to different models based on what the work actually requires. A frontier model may be justified for high-stakes reasoning, delicate writing, or complex multi-file synthesis. A smaller or local model may be better for classification, formatting, triage, extraction, or privacy-sensitive routine work.

The point is not thrift for its own sake. It is fit. Using the most expensive model for everything creates cost blindness and dependency. Using a weak model for work that requires judgment creates false economy. Good operators learn the tiers: fast/cheap, standard, deep, local/private, frontier/expensive, and human-only.

Model tiering becomes especially important in agentic systems because background tasks, cron jobs, sub-agents, and recurring checks can quietly multiply token burn. Routing policy is therefore not an accounting afterthought. It is part of system design.

## See also

- *[Token burn](token-burn.md)*
- *[Opus Addict](opus-addict.md)*
- *[Sovereign Compute](sovereign-compute.md)*
