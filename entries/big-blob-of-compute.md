---
layout: default
kind: reference
title: "Big Blob of Compute"
permalink: /entries/big-blob-of-compute/
date: 2026-06-17
summary: "Dario Amodei's name for the scaling worldview: intelligence progress as the result of large amounts of compute, broad data, scalable objectives, and numerical stability rather than hand-designed cleverness."
published: true
---

# Big Blob of Compute

## In one sentence

**The Big Blob of Compute is Dario Amodei's name for a scaling hypothesis: AI capability advances when large amounts of compute can be applied effectively to broad data, scalable objectives, and numerically stable training.**

## What the phrase names

In his May 2026 conversation with Dwarkesh Patel, Amodei described a document he wrote in 2017 called *The Big Blob of Compute Hypothesis*. The point was not originally about language models alone. GPT-1 had only just appeared. The AI world still had separate tribes for robotics, reinforcement learning, game-playing systems, reasoning systems, and language models.

The hypothesis applied across these domains. Amodei expected systems able to absorb larger useful amounts of compute without becoming unstable to outperform more bespoke methods that did not scale as well.

Amodei lists the ingredients roughly as:

1. raw compute;
2. quantity of data;
3. quality and breadth of data distribution;
4. training duration;
5. an objective function that can scale very far;
6. numerical conditioning;
7. numerical stability.

The last two conditions determine whether a large training run remains usable. Computation must pass through the system without exploding, collapsing, or drifting into uselessness. Amodei describes the desired flow as *laminar*.

## Why it matters

The hypothesis resembles Richard Sutton's *Bitter Lesson*, which argues that general methods able to use increasing computation tend to outperform methods built mainly from human domain knowledge. The Big Blob formulation adds the engineering conditions needed to apply computation at scale.

Compute by itself is insufficient. The hypothesis also requires data, objectives, architecture, training procedure, numerical stability, and the engineering discipline to keep a run operating. Its stronger claim is that capability will continue to emerge from scale before theory fully explains it.

This is why Amodei treats both pre-training and reinforcement learning as instances of the same phenomenon. Pre-training was the first public curve. RL is now, in his telling, showing similar log-linear returns on verifiable tasks such as math and code, then expanding outward into broader task distributions.

## The useful warning

The phrase emphasizes the material and industrial character of this account of intelligence. Progress depends on physical infrastructure and repeatable training processes as well as research insight.

If the hypothesis is right, frontier capability can continue advancing through more compute, better data, scalable objectives, and sufficient engineering stability. If returns flatten, laboratories may commit very large resources to an approach with declining gains.

The hypothesis is not proven in its strongest form. It is nevertheless an important operating belief among frontier laboratories and helps explain large investments in chips, data centres, power, and training runs. Its economic effects are therefore observable even while its technical limits remain uncertain.

## The missing wall socket

The blob sounds abstract but requires chips, memory, packaging, data centres, cooling, transformers, substations, permits, capital, and electricity. Cloud computation depends on physical facilities and power contracts.

This is where Amodei's compute framing meets arguments about power and data-centre supply. The possible gains from more compute depend on whether powered infrastructure can be financed, permitted, built, and operated.

## See also

- [Scaling Laws](scaling-laws.md)
- [Capability Overhang](capability-overhang.md)
- [Sovereign Compute](sovereign-compute.md)
- [The CERN Alternative](cern-alternative.md)
- [Country of Geniuses in a Data Center](country-of-geniuses-in-a-data-center.md)

---

*Drafted May 16, 2026, from Dario Amodei's May 2026 conversation with Dwarkesh Patel, especially the section in which Amodei describes his 2017 document, "The Big Blob of Compute Hypothesis."*
