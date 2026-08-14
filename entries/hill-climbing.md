---
layout: default
kind: glossary
title: "Hill Climbing"
permalink: /entries/hill-climbing/
date: 2026-08-14
seeded: 2026-08-14
first_published: 2026-08-14
last_revised: 2026-08-14
summary: "An optimization method that repeatedly makes a locally improving move—the technical ancestor of the AI-era habit of getting better by following a feedback signal step by step."
draft: false
published: true
---

**Hill climbing** is an optimization method that starts with a possible solution, tests a nearby alternative, and moves to it when the alternative is better. Repeat the procedure and the system climbs the landscape one locally improving step at a time. The childhood game of *hot and cold* gives the intuition: each move is judged by whether it brings you closer to the hidden object.

The phrase comes from early work in artificial intelligence, operations research, and cognitive science. Its virtue is method rather than foresight. The climber need not see the whole mountain or know the best route; it needs only a way to generate a neighbouring move and a feedback signal that says *better* or *worse*.

This is why the phrase remains useful in modern AI. Training a model means adjusting parameters in response to an objective or reward signal. Reinforcement learning makes the resemblance especially vivid: like an animal in a Skinner box learning which actions bring food or stop discomfort, an agent changes its behaviour according to reward. But the terms are not interchangeable. **Hill climbing is a particular search strategy; reinforcement learning is a broader framework for learning behaviour from rewards.** Modern neural-network training usually uses gradient descent and its descendants—mathematically more informed relatives that estimate which direction through an enormous parameter landscape should reduce error.

Hill climbing also names a characteristic failure. A method that accepts the next improving step may reach the top of the nearest hill and mistake it for the highest point in the range. This is the **local optimum** problem. In AI systems—and in institutions—the feedback loop can yield steady, measurable improvement against the chosen score while leaving the larger objective untouched or even making it worse.

## See also

- [RLHF](rlhf.md)
- [Reward Hacking](reward-hacking.md)
- [Scaling Laws](scaling-laws.md)
- [Big Blob of Compute](big-blob-of-compute.md)

