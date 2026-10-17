---
layout: default
kind: reference
title: "Thea Fleet"
permalink: /entries/thea-fleet/
summary: "Our experimental project for coordinating existing local computers and cloud resources through an AI assistant, with human direction and measured results."
seeded: 2026-10-17
first_published: 2026-10-17
last_revised: 2026-10-17
published: true
---

# Thea Fleet

**Thea Fleet is our experimental project for coordinating existing local computers and cloud resources through Thea, an AI assistant, to produce useful, checked results under Matthew Langenkamp's direction.** The starting question is practical: before buying a larger machine, what can the computers we already own accomplish together?

The name was adopted on October 17, 2026. It identifies this particular project, not an established industry standard, a new model, or a generally available software product.

## The operating rule

Thea coordinates inference, tools, and supporting services across authorised resources, checks their outputs, and returns actionable results to Matthew. Matthew sets direction, reviews findings, and approves consequential actions. Routine work already authorised does not require approval at every step.

This is the intended operating arrangement. Naming a coordinator does not establish that every proposed worker, model connection, or supervisory mechanism has been implemented.

## Three different ways to distribute computing

**Distribute the work.** Separate machines carry out independent tasks, possibly using different models. Each uses its own memory. The coordinator combines and checks the results. This can increase throughput, but dispatch, verification, and reconciliation also take time.

**Split one model.** Compatible machines hold and execute different parts of a model. This may accommodate a model that does not fit on one machine, but communication overhead and slow components can make it less responsive. Combining memory capacity is not the same as obtaining one larger pool of fast local RAM.

**Move supporting services.** Search, indexing, storage, or other suitable services run elsewhere, leaving more resources available on the main workstation. The benefit depends on how much local load is removed and what delay or operational complexity the remote service introduces.

These are complementary architectures, not three competing communication protocols. An agent worker also need not host its own model: it can use local tools while obtaining model responses from another authorised machine or a managed service.

## The first test

**Fleet Test 01 (FT-01)** is planned for October 24, 2026. It compares a single-workstation baseline with three bounded tracks: **FT-01A — Work**, **FT-01B — Model**, and **FT-01C — Services**.

Each track should produce a useful result from public or synthetic material and record correctness, elapsed time, memory use, reliability, cost, and required human intervention. A cloud virtual private server is included where suitable capacity permits. A VPS is hosting capacity; it is not automatically a GPU server or a managed model service.

The outcome for each track is a recommendation to adopt it, investigate further, or set it aside. A documented incompatibility is a result. Spending the entire weekend trying to make an unsuitable machine cooperate is not a necessary condition of scientific seriousness.

**Status at publication, October 17, 2026:** the charter and weekend reminders exist. The three distributed-computing experiments have not yet been run. No performance improvement or pooled-memory capability is claimed.

## Why share the name?

A name gives collaborators something they can remember, discuss, and revise. “Thea Fleet” retrieves the overall project; “FT-01B” identifies a particular experiment. The nomenclature keeps separate questions from collapsing into one vague ambition to “use all the computers.”

For students and colleagues, the transferable lesson is the method: define the work, inventory available resources, establish a baseline, test a bounded alternative, and retain evidence. Readers do not need to reproduce our hardware collection or adopt our names.

[TeachClaw](/entries/teachclaw/) is a separate teaching-platform project. It may eventually benefit from Fleet findings, but its classroom trials are not evidence that the Fleet architectures work.

## Trade-offs

Older machines can offer useful capacity while adding power consumption, maintenance, compatibility problems, and security-update obligations. Network links can become the bottleneck. A heterogeneous system may have more total memory and still finish a task more slowly.

The objective is useful capacity at an acceptable cost, not participation by every device. A computer that remains a reliable browser terminal may be contributing more than one pressed into an unsuitable inference role.

## See also

- [Naming](/entries/naming/) — shared vocabulary for remembering and coordinating work.
- [Zhengming](/entries/zhengming/) — keeping names and actual capabilities in agreement.
- [Big Blob of Compute](/entries/big-blob-of-compute/) — a distinct hypothesis about scaling learning systems, not a synonym for this distributed-computing project.
- [TeachClaw](/entries/teachclaw/) — our teaching platform in development.
