---
layout: default
kind: glossary
title: "Hill Climb"
permalink: /entries/hill-climb/
date: 2026-05-16
summary: "An optimisation metaphor: improve by repeatedly moving toward better nearby states, even when the global optimum is unknown."
draft: false
published: true
---

A **hill climb** is an optimisation pattern: start where you are, make the best nearby improvement you can see, then repeat. You may not know the global optimum. You may not even know the landscape. But you can often tell whether the next step is higher than the current one.

In AI practice, hill climbing shows up everywhere. A prompt is revised after a weak answer. A draft is improved through critique. A local model is swapped for a better one. A workflow is made more durable after a failure. The operator does not solve the whole system in one leap; the operator climbs.

The danger is local maxima. A system can become better than its starting point while still trapped on the wrong hill. That is why hill climbing needs occasional reframing: change the objective, inspect the landscape, ask whether the current climb still points toward the real goal.

## See also

- *[Incremental Construction](incremental-construction.md)*
- *[The Path is The Goal](red-pill.md)*
- *[Sovereign Compute](sovereign-compute.md)*
