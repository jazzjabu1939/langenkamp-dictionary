---
layout: default
title: "Tool Diet"
permalink: /entries/tool-diet/
date: 2026-07-01
summary: "The discipline of giving an AI agent the smallest useful set of tools rather than every capability the surrounding system can expose."
published: true
---

# Tool Diet

---

## In one sentence

**Tool diet is the discipline of giving an AI agent the smallest useful set of tools rather than every capability the surrounding system can expose.**

## Capability is not tool count

The naive agent design says: give the model more tools and it will be more capable.

Sometimes that is true. Often it is not.

Every tool adds possibility, but it also adds ambiguity, prompt load, security risk, error surface, and decision burden. A model that sees too many tools may choose the wrong one, call a tool too early, confuse overlapping capabilities, or take an action the surrounding system should never have made easy.

A good harness does not merely maximise available action. It curates action.

That curation is tool diet.

## The food metaphor

The metaphor works because tools are not abstract features. They feed the agent's behaviour.

An agent with a clean diet receives a small set of well-described, well-scoped tools. It knows what each tool is for. The tools match the task. Dangerous actions are gated. Redundant tools are removed. The agent is not asked to choose between five similar ways to do the same thing.

An agent with a bad diet receives everything. Search, shell, browser, email, calendar, database, file writes, deployments, memory edits, messaging, payment tools, and a few half-documented internal functions all arrive in one long tool list. The agent looks powerful. The harness has quietly become sloppy.

Too many tools can make the agent worse.

## Why deletion can improve performance

Nate Jones's recent discussion of Vercel cutting an agent's available tools is useful because it names a counterintuitive pattern: removing tools can improve the agent.

This should not surprise anyone who has managed humans. A clear job with the right tools is easier than a vague job with every possible tool. Constraints are not always anti-capability. Good constraints reduce noise.

For agents, the same principle applies technically. The model has less to parse, fewer wrong paths, fewer unsafe actions, and a clearer sense of what the surrounding system expects. The harness becomes more legible.

Subtraction is not failure. In agent design, subtraction may be the first adult move.

## Governance through subtraction

Tool diet is also governance.

Approval gates control whether a tool can be used. Tool diet asks whether the tool should be visible in the first place.

Those are different questions. A destructive tool with approval gating may be appropriate for an administrator agent. It may not belong in a writing assistant's diet at all. A database write tool may be essential for a production support agent and reckless for an exploratory research agent. A broad shell tool may be suitable in a sandbox and inappropriate in a shared business workflow.

The safest tool is not the one the agent nobly refuses to use. It is the one the agent never had for a task that did not need it.

## The operator's habit

Tool diet should become a normal review habit.

When an agent performs poorly, do not only ask whether the model is smart enough. Ask:

- Did it have too many tools?
- Were two tools semantically overlapping?
- Was a dangerous tool exposed for convenience?
- Was the tool description vague?
- Was a narrower tool available?
- Did the harness force the model to reason about infrastructure instead of the task?

This is one of the quiet places where agent reliability is won.

## Maintenance surface

Tool diet is not only a launch decision. It is a maintenance surface.

Nate Jones's agent-maintenance frame is useful here: agents drift because the world changes, the job changes, the model underneath them changes, and the harness built around yesterday's weakness becomes today's dead weight. A tool that was necessary in March may be redundant in July. A memory source that once helped may now pollute the task. A broad permission that was tolerable for a prototype may be reckless once the agent is part of real work.

The recurring question is not "What else can this agent do?" It is "What should this agent still be allowed to do?"

That question belongs beside the usual maintenance checks: job, diet, memory, tools, reach, proof, and value. Tool diet is the one that makes subtraction respectable.

## The management version

For teams, tool diet is the antidote to performative capability.

It is easy to impress a meeting by saying the new agent can search the web, read the CRM, update tickets, draft emails, query the database, post to Slack, create calendar events, and open pull requests. It is harder, and more useful, to say: this agent does three things, on these inputs, with these permissions, under this owner, and with this review rule.

The second agent may sound less magical. It is more likely to survive contact with real work.

## See also

[Tool](tool.md) · [Harness](harness.md) · [Approval Gating](approval-gating.md) · [Agent Ownership](agent-ownership.md) · [OpenClaw](openclaw.md) · [Grok Bot](/entries/grok-bot/)

## Source

Nate Jones, recent Substack discussion of agent tool reduction and harness design, June 2026; Prof. Langenkamp vocabulary review, July 1, 2026.

- YouTube, "I tried GLM 5.2 and it blew my mind": <https://youtu.be/Zp8lr6IzUnQ>
- <https://natesnewsletter.substack.com/p/ai-agent-maintenance>
