---
layout: default
title: "Task Distribution"
permalink: /entries/task-distribution/
date: 2026-07-01
summary: "The shape of the work an AI system is being asked to do: familiar or novel, inspectable or opaque, routine or edge-case, cheap to verify or expensive to trust."
published: true
---

# Task Distribution

---

## In one sentence

**Task distribution is the shape of the work an AI system is being asked to do: familiar or novel, inspectable or opaque, routine or edge-case, cheap to verify or expensive to trust.**

## The question before the model

The laziest AI argument in 2026 is still the most common one: which model is best?

It is not a stupid question. Model quality matters. Cost matters. Context length matters. Open weights matter. Latency matters. A model that cannot do the work cannot be rescued by a clever procurement memo.

But it is not the first question.

The first question is: **what kind of work are we asking the system to do?**

A model that is perfectly adequate for ten thousand routine summaries may be the wrong choice for a novel legal interpretation. A cheap local model may be excellent for cleaning data labels and dangerous for drafting a sensitive student accommodation policy. A frontier model may be wasteful for a standard formatting task and worth every penny for ambiguous strategy, unfamiliar code, or high-stakes reasoning.

The task has a distribution. The model has capabilities. Good AI work begins by matching the two.

## Center and edge

Nate Jones's useful distinction in the GLM-5.2 discussion is between **center-of-distribution** work and **edge-of-distribution** work.

Center-of-distribution work has familiar shapes. There are many examples in the model's training and in the world. The output pattern is normal. The human can check it quickly. A first-pass deck outline, a routine code refactor, a standard email, a clean product description, or a typical landing page may sit near the center.

Edge-of-distribution work is different. It is novel, ambiguous, poorly represented, high-risk, or hard to inspect. It may require hidden domain judgment. It may look plausible while being wrong. It may involve a one-off fact pattern, a fragile system, a legal or ethical constraint, or a decision where the cost of error is high.

The same model can be sensible for one and reckless for the other. The same team can be wise to use cheap intelligence for one class of work and unwise to use it for another.

## The missing map

Most organisations do not have a live map of their task distribution.

They have departments, job titles, budgets, software categories, approval paths, and job descriptions. They may have process maps, if someone once had the stamina to make them. But they usually do not have a practical classification of which tasks are routine, which are fragile, which are easily verified, which require deep context, which change shared state, and which should never be automated without explicit ownership.

That missing map is why model substitution looks easier in a spreadsheet than it is in practice.

The spreadsheet may say one model is 98 percent cheaper. It may be right. But the spreadsheet does not know whether the work is routine enough to move, whether the necessary context can travel with it, whether the output can be checked, whether the receiving team has built a harness around the cheaper model, or whether a cheap mistake becomes an expensive one three steps later.

The hidden question is not "Can GLM-5.2 answer this prompt?"

It is "Is this the kind of work we can safely send there, and can our system tell the difference?"

## Inspectability matters

The most useful practical axis is not glamour. It is inspectability.

Some AI outputs are easy to check. A cleaned CSV can be sampled. A revised paragraph can be read. A renamed file can be inspected. A formatted bibliography can be compared against sources. If the model is wrong, the error is visible and relatively cheap.

Other outputs are hard to check. A legal conclusion, a security patch, a medical interpretation, a strategic forecast, or a subtle grading recommendation can look polished while hiding the important failure. In those cases, the model's answer is not the end of the work. It is the beginning of the verification problem.

This is why task distribution belongs next to the Dictionary's [Verification Gap](verification-gap.md). Once polished artifacts become cheap, the responsible question shifts from "Does this look good?" to "What evidence would let us trust this?"

## The management implication

Task distribution turns model strategy into operations strategy.

The leader's job is not to crown a universal winner. It is to classify work. Which tasks are cheap to verify? Which tasks create expensive errors? Which tasks require private context? Which tasks can be batched? Which tasks should go to a local model? Which tasks should go to a frontier model? Which tasks should stay with a human?

This is where [Routing Logic](routing-logic.md) begins. Task distribution describes the shape of the work. Routing logic decides where that work should go.

The firms that learn to measure their task distribution will buy and build AI more intelligently. The firms that do not will either overpay for routine work or under-protect fragile work. Both errors are expensive. One shows up in the budget. The other shows up in the incident review.

## Teaching use

For students, task distribution is a better frame than model gossip.

Instead of asking "Which AI is best?", ask students to classify a bundle of tasks: which are routine, which are novel, which are inspectable, which are high-risk, which need private context, and which require human sign-off. Then ask them to defend a routing decision.

That exercise teaches the thing managers will actually need. It teaches students that AI adoption is not a popularity contest among models. It is a discipline of matching work, risk, context, cost, and accountability.

## See also

[Routing Logic](routing-logic.md) · [Team Harness](team-harness.md) · [Harness](harness.md) · [Verification Gap](verification-gap.md) · [Open Model Trust](open-model-trust.md) · [Sovereign Compute](sovereign-compute.md)

## Source

Nate Jones, GLM-5.2 video and Substack briefing on context lock-in, June 2026; Prof. Langenkamp vocabulary review, July 1, 2026.

- YouTube, "I tried GLM 5.2 and it blew my mind": <https://youtu.be/Zp8lr6IzUnQ>
- <https://natesnewsletter.substack.com/p/glm-5-2-context-lock-in>
