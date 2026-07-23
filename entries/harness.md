---
layout: default
title: "Harness"
permalink: /entries/harness/
date: 2026-06-30
summary: "The surrounding runtime, tools, permissions, memory, approval gates, logs, prompts, and operating rules that determine what an AI model can perceive, do, remember, refuse, and recover from."
published: true
---

A **harness** is the surrounding system that turns an AI model into a working agent: the runtime, tools, permissions, memory, prompts, approval gates, logs, schedules, recovery paths, and operating rules that determine what the model can perceive, do, remember, refuse, and repair.

The distinction matters because a model is not the whole agent. A model predicts, reasons, writes, plans, and calls tools. The harness decides which tools exist, which actions are possible, which actions need approval, what context is loaded, what memory survives, what gets logged, and how failure is noticed.

OpenClaw is the Dictionary's working example. In OpenClaw, the same underlying model becomes more than a chat window because it sits inside a harness: Telegram routing, local files, memory files, skills, shell access, cron jobs, subagents, approval rules, session history, and startup instructions all shape what the assistant can actually do. The model supplies intelligence; the harness supplies world, authority, continuity, and constraint.

This is why two agents using the same model can behave very differently. One may be a polite chatbot with no tools and no memory. Another may be a durable assistant that reads project files, checks calendars, drafts entries, runs builds, delegates work, and refuses external action without permission. The difference is not only personality or model quality. It is harness design.

A good harness does not assume the model will always be wise. It assumes the model may be stale, overconfident, too agreeable, confused by old instructions, tempted by available tools, or locally rewarded for the wrong thing. Then it makes dangerous actions harder, useful actions easier, and recovery possible.

Bad harnesses create bad agents. They mix current rules with obsolete notes, expose tools without authority boundaries, hide failures, let cron jobs rot, blur private and public contexts, or make the assistant carry too much stale text in every session. The model then looks unreliable, but the deeper failure may be architectural.

In management language, an organization is also a harness. Job descriptions, budgets, approval limits, dashboards, escalation paths, incentives, and audit trails are not paperwork around the work. They are the system that makes some behaviors easy, some difficult, and some impossible.

The harness is therefore where AI governance becomes practical. "Be careful" is a prompt. A harness is the system that decides whether the agent can send the email, delete the file, spend the money, access the record, remember the decision, and show its work afterward.

## See also

[OpenClaw](openclaw.md) · [Agent](agent.md) · [Tool](tool.md) · [Approval Gating](approval-gating.md) · [Gateway](gateway.md) · [Grep Architecture](grep-architecture.md) · [Agent Town Experiment](agent-town-experiment.md) · [Trust Layer](trust-layer.md)
