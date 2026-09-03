---
layout: default
kind: reference
title: "Routing Logic"
permalink: /entries/routing-logic/
date: 2026-07-01
summary: "The managerial and technical layer that decides which work should go to which model, agent, tool, human, or harness."
published: true
---

# Routing Logic

---

## In one sentence

**Routing logic is the managerial and technical layer that decides which work should go to which model, agent, tool, human, or harness.**

## The new scarce judgment

When intelligence is expensive, the obvious question is how to get access to it.

When intelligence becomes cheap, the harder question is where to spend it.

That is the shift behind routing logic. The organisation no longer has one AI system doing one kind of work. It has frontier models, cheap models, open-weight models, local models, coding agents, browser agents, document assistants, search tools, internal databases, human reviewers, approval gates, and ordinary software. The work has to move somewhere.

Routing logic is the rule system, explicit or implicit, that decides where.

## Not just a router

The word "routing" can make the problem sound mechanical: classify prompt, choose model, return answer. That is the thin version.

The thicker version is managerial. A good routing layer asks:

- Is this task routine or novel?
- Is the answer easy to inspect?
- Does the task require private context?
- Would a wrong answer be annoying or dangerous?
- Is speed more important than quality?
- Is cost material at this scale?
- Does the output change shared state?
- Who owns the result?
- Which tool or model has the right permissions?
- Should a human approve this before it leaves the sandbox?

Those questions are not merely engineering details. They are the new operations discipline of AI work.

## Task distribution first

Routing logic depends on [Task Distribution](task-distribution.md). If the organisation cannot describe the shape of its work, routing becomes vibes with invoices attached.

A sensible routing decision might say:

- This routine summary can go to a cheap model because the output is easy to inspect.
- This student-facing policy draft needs a frontier model and human review because ambiguity and institutional risk are high.
- This customer-data task should stay local because the context is sensitive.
- This code refactor can go to an agent, but only inside a test-backed branch with a human review gate.
- This message should not be drafted by an agent at all because the social cost of tone failure is too high.

That is routing logic in its useful form. It does not worship the strongest model. It spends intelligence according to the work.

## Raw IQ is not enough

Routing logic is one reason **raw IQ** is an incomplete frame.

A very capable model may be the wrong destination for cheap, repetitive, easily verified work. A weaker model may be perfect for a bounded formatting task. A local model may be required for privacy. A human may be required because the system is about to make a commitment no model should make alone.

The advantage moves from having the smartest model to knowing where intelligence should be spent.

This does not make model quality irrelevant. Better models expand the frontier of routable work. But the frontier does not route itself. Someone has to decide which work belongs there.

## The company problem

Companies are tempted to treat routing logic as a cost-control mechanism. That is part of it, but not enough. Routing exists to preserve quality, ownership, trust, privacy, speed, and cost in the same system.

If routing is only about cost, the firm will send fragile work to cheap systems and discover the error later. If routing is only about quality, the firm will overpay for routine work and learn nothing about its own task distribution. If routing is only about privacy, the firm may build a local system that no one can use. If routing is only about convenience, the firm will drift into [Team Harness](team-harness.md) lock-in without noticing.

Routing logic is the balancing discipline.

## The teaching implication

For students, this is good news.

The future skill is not simply "prompt the best model." It is learning how to classify work, understand constraints, choose the right system, and defend the choice. That is a strategy skill as much as a technical skill.

A student who can say, "This belongs with a cheap local model because the task is routine and the output is easy to verify," or "This needs a frontier model and a human review loop because the ambiguity is high," is already thinking like a manager of AI work.

That is more useful than memorising model rankings, which age about as well as yoghurt in a sunny window.

## See also

[Task Distribution](task-distribution.md) · [Team Harness](team-harness.md) · [Tool Diet](tool-diet.md) · [Agent Ownership](agent-ownership.md) · [Verification Gap](verification-gap.md) · [Sovereign Compute](sovereign-compute.md)

## Source

Nate Jones, GLM-5.2 and recent Substack work on cheap intelligence, context lock-in, and model routing, June 2026; Prof. Langenkamp vocabulary review, July 1, 2026.

- YouTube, "I tried GLM 5.2 and it blew my mind": <https://youtu.be/Zp8lr6IzUnQ>
- <https://natesnewsletter.substack.com/p/glm-5-2-context-lock-in>
