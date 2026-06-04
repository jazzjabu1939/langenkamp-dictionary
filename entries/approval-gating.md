---
layout: default
kind: glossary
title: "Approval Gating"
permalink: /entries/approval-gating/
date: 2026-05-16
summary: "The control pattern that requires human consent before an agent performs sensitive, external, costly, or destructive actions."
draft: false
published: true
---

**Approval gating** is the practice of placing explicit human consent in front of actions an AI agent should not take on its own: sending messages, spending money, deleting files, changing production systems, exposing private data, or making irreversible commitments.

In a chatbot, approval is often informal: the user asks, the model answers. In an agentic system, the model can act through tools. That makes the difference between suggestion and execution much more important. Approval gates turn *I could do this* into *I will only do this after the human authorises it*.

Approval gating is not a sign that the agent is weak. It is a sign that the system understands authority. The most dangerous systems are not the ones that ask permission too often; they are the ones that quietly blur the line between recommendation and action.

## See also

- *[Tool](tool.md)*
- *[Trust Layer](trust-layer.md)*
- *[Aunties](aunties.md)*
- *[The Lowbeer Question](lowbeer-question.md)*
