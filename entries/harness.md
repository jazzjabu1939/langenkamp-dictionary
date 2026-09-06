---
layout: default
kind: glossary
title: "Harness"
permalink: /entries/harness/
date: 2026-06-30
summary: "The surrounding runtime, tools, permissions, memory, approval gates, logs, prompts, and operating rules that determine what an AI model can perceive, do, remember, refuse, and recover from."
published: true
last_revised: 2026-09-06
---

A **harness** is the surrounding system that turns an AI model into a working agent: the runtime, tools, permissions, memory, prompts, approval gates, logs, schedules, recovery paths, and operating rules that determine what the model can perceive, do, remember, refuse, and repair.

A model supplies only part of the agent. It predicts, reasons, writes, plans, and calls tools. The harness decides which tools exist, which actions are possible, which actions need approval, what context is loaded, what memory survives, what gets logged, and how failure is noticed.

OpenClaw is the Dictionary's working example. In OpenClaw, the same underlying model becomes more than a chat window because it sits inside a harness: Telegram routing, local files, memory files, skills, shell access, automations, subagents, approval rules, session history, and startup instructions all shape what the assistant can actually do. The model supplies intelligence; the harness supplies world, authority, continuity, and constraint.

This is why two agents using the same model can behave very differently. One may be a polite chatbot with no tools and no memory. Another may be a durable assistant that reads project files, checks calendars, drafts entries, runs builds, delegates work, and refuses external action without permission. The difference is not only personality or model quality. It is harness design.

A good harness anticipates that the model may be stale, overconfident, too agreeable, confused by old instructions, tempted by available tools, or locally rewarded for the wrong thing. It makes dangerous actions harder, useful actions easier, and recovery possible.

Bad harnesses create bad agents. They mix current rules with obsolete notes, expose tools without authority boundaries, hide failures, let background tasks rot, blur private and public contexts, or make the assistant carry too much stale text in every session. The model then looks unreliable, but the deeper failure may be architectural.

## Harness engineering

**Harness engineering** is the deliberate design and maintenance of this surrounding system. It begins where *prompt engineering* becomes too small a description of the work. A prompt tells the model what is wanted. The harness determines what the model can see, which tools it can use, how results return to context, what persists between sessions, where approval is required, how success is tested, and what happens after failure.

Latent Space describes harness engineering as the systems subset of **agent engineering** and frames the current argument as **Big Model versus Big Harness**. The Big Model position holds that stronger models absorb elaborate scaffolding: give a capable reasoning model a clear task and a thin loop, then stay out of its way. The Big Harness position holds that useful performance still depends heavily on context construction, tool design, repository legibility, permissions, evaluation, observability, and recovery.

Both positions have evidence. A stronger model can make yesterday's intricate scaffold unnecessary, and stale scaffolding can obstruct intelligence rather than support it. Yet the same model can perform very differently across harnesses because the harness controls its working world. The task, the model, and the consequences of failure determine how much harness is useful.

OpenClaw makes the distinction concrete. Changing the model changes the system's cognitive ceiling. Improving the harness changes whether that intelligence can work repeatedly, safely, and legibly. A brilliant model inside a confused harness may fail ordinary work; a well-designed harness can help a modest model complete bounded work reliably. The two are complementary levers.

As agents move from demonstrations into durable roles, the engineering problem shifts from producing an impressive answer to arranging the conditions under which useful work can continue tomorrow, be inspected by someone else, survive a model change, and recover when something goes wrong.

In management language, an organization is also a harness. Job descriptions, budgets, approval limits, dashboards, escalation paths, incentives, and audit trails are part of the system that makes some behaviors easy, some difficult, and some impossible.

The harness is therefore where AI governance becomes practical. "Be careful" is a prompt. A harness is the system that decides whether the agent can send the email, delete the file, spend the money, access the record, remember the decision, and show its work afterward.

## Sources

- Latent Space, [“Is Harness Engineering real?”](https://www.latent.space/p/ainews-is-harness-engineering-real), 4 March 2026.
- OpenAI, [“Harness engineering: leveraging Codex in an agent-first world”](https://openai.com/index/harness-engineering/).

## See also

[OpenClaw](/entries/openclaw/) · [Agent](/entries/agent/) · *Agentic Loop* (draft) · *Model–Harness Fit* (draft) · *Verification* (draft) · [Covert Channel](/entries/covert-channel/) · [Tool](/entries/tool/) · [Approval Gating](/entries/approval-gating/) · [Gateway](/entries/gateway/) · [Grep Architecture](/entries/grep-architecture/) · [Agent Town Experiment](/entries/agent-town-experiment/) · [Trust Layer](/entries/trust-layer/)
