---
layout: default
kind: glossary
title: "System Prompt"
permalink: /entries/system-prompt/
date: 2026-05-16
summary: "The instruction layer that defines how an AI system should behave before it receives a user’s immediate request."
draft: false
published: true
---

A **system prompt** is the high-priority instruction layer that tells an AI system how to behave: its role, constraints, available tools, safety boundaries, preferred style, and sometimes the identity or workflow it should maintain. In an agentic system, the system prompt is not mere decoration. It is part of the operating architecture.

The user sees the answer, but the answer is shaped by instructions that come before the user request. Those instructions may tell the model to be concise, refuse certain actions, use tools before answering, preserve privacy, or follow a particular persona. In OpenClaw terms, files such as `SOUL.md`, `USER.md`, skills, and runtime policies can all function as parts of the broader prompt environment, even when they are not literally one monolithic prompt.

The system prompt is powerful but not magical. It can be ignored, confused, attacked, or diluted by conflicting context. That is why serious agent design eventually needs judge layers, approval gates, and external checks rather than relying on prompt wording alone.

## See also

- *[SOUL.md](soul-md.md)*
- *[Prompt](prompt.md)*
- *[Approval Gating](approval-gating.md)*
