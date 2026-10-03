---
layout: default
kind: reference
title: "Big Blob of Compute"
permalink: /entries/big-blob-of-compute/
date: 2026-06-17
summary: "Dario Amodei's hypothesis that general-purpose learning systems improve chiefly through more computation, sufficient high-quality data, and training methods that remain effective at larger scales."
published: true
---

# Big Blob of Compute

## In one sentence

**Big Blob of Compute is Dario Amodei's term for the hypothesis that general-purpose learning systems improve chiefly by using more computation, sufficient high-quality data, and training methods that remain effective at larger scales, rather than by adding a separate hand-designed solution for every task.**

## What the phrase names

Amodei traces the hypothesis to an internal document he wrote in 2017. He discussed it publicly with Dwarkesh Patel in 2023 and returned to it in their February 2026 conversation.[1][2] It was not limited to language models. It concerned learning systems across fields such as robotics, game-playing, and language.

The central comparison is between methods that can make productive use of increasing computation and specialized methods that do not scale as well. It is not a claim that buying more processors, by itself, produces intelligence.

In the later interview, Amodei identifies several ingredients:

- **Computation:** the processing resources available for training.
- **Data:** enough examples, of sufficient quality and breadth, for the system to learn beyond a narrow task.
- **Training time:** how long the learning process runs.
- **A scalable objective:** a training goal that remains useful as training expands, such as predicting text or learning to accomplish tasks from rewards.
- **Numerical conditioning and stability:** keeping the calculations well-behaved enough for learning to continue reliably.

These ingredients work together. More computation may accomplish little if the data are poor, the training goal is unsuitable, or the calculations become unstable.

## Why it matters

The hypothesis resembles Richard Sutton's *The Bitter Lesson*: general methods that exploit increasing computation have repeatedly overtaken approaches built around human knowledge of a particular problem.[3] Amodei's account emphasizes the data and engineering conditions that make such scaling possible.

In the 2026 interview, he presents both pre-training and reinforcement learning as examples. Pre-training learns patterns from data; reinforcement learning uses rewards to improve performance on tasks. He reports gains from longer reinforcement-learning training and expects broader task coverage to improve generalization. That expectation is part of his argument, not an established guarantee for every task.

The hypothesis helps explain why frontier laboratories invest heavily in chips, data centres, and training runs. They expect additional resources, applied through effective learning methods, to produce capabilities that would be difficult to engineer separately.

## What it does not establish

Measured scaling relationships and predictions about future intelligence are different claims. In his 2023 interview, Amodei distinguishes the relatively predictable improvement of aggregate training measures from the harder problem of predicting when a particular ability will appear.[1]

Better training performance does not by itself establish dependable behavior, alignment with human intentions, or commercial profitability. Nor does the hypothesis make architecture and algorithmic research irrelevant: a better method can change how effectively computation is used.

The unresolved question is how far these gains will continue, on which tasks, and at what cost.

## The physical requirements

The computation requires chips, memory, data centres, cooling, grid connections, and electricity. Expanding it also requires capital, equipment, permits, and construction time.

A laboratory may expect useful gains from a larger training run yet be unable to secure the powered infrastructure or financing to carry it out. Technical potential and economic feasibility are separate questions.

## See also

- [Scaling Laws](scaling-laws.md)
- [Capability Overhang](capability-overhang.md)
- [Sovereign Compute](sovereign-compute.md)
- [The CERN Alternative](cern-alternative.md)
- [Country of Geniuses in a Data Center](country-of-geniuses-in-a-data-center.md)

## Sources

[1] Dwarkesh Patel, [conversation with Dario Amodei (2023)](https://www.dwarkesh.com/p/dario-amodei), especially the opening discussion of scaling, predictability, and its limits.

[2] Dwarkesh Patel, [conversation with Dario Amodei (February 2026)](https://www.dwarkesh.com/p/dario-amodei-2), opening section, “What exactly are we scaling?” Amodei's recollection combines a 2017 document date with a reference to GPT-1 having appeared; this entry retains his date for the document without reproducing that inconsistent chronology.

[3] Richard Sutton, [*The Bitter Lesson*](http://www.incompleteideas.net/IncIdeas/BitterLesson.html), March 13, 2019.

---

*Originally drafted May 16, 2026. Revised October 3, 2026, to clarify the definition, correct the interview attribution, and distinguish observed scaling from predictions.*
