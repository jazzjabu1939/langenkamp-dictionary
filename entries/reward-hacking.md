---
layout: default
kind: glossary
title: "Reward Hacking"
permalink: /entries/reward-hacking/
date: 2026-06-25
summary: "The technical AI term for a model or agent finding a way to score well under the reward system while missing or violating the intended goal."
draft: false
published: true
---

# Reward Hacking

**Reward Hacking** is the technical AI term for a model or agent finding a way to score well under the reward system while missing, evading, or violating the designer's intended goal.

It is close to **specification gaming**. The specification says what the system is supposed to optimize. The system discovers a loophole in that specification. In ordinary software, this can look like a game character learning to stand in a scoring zone rather than finish the level. In AI training, it can look like a model learning to produce outputs that satisfy the evaluator while concealing the fact that the real task was not done honestly.

Reward hacking is narrower than *[Incentive Hacking](incentive-hacking.md)*. Reward hacking belongs to the technical AI vocabulary: reward functions, reinforcement learning, evaluators, training signals, and agent behavior under optimization pressure. Incentive hacking is the broader Dictionary term for the same shape in human institutions: students gaming rubrics, firms gaming KPIs, employees gaming dashboards, universities gaming rankings, or models gaming evaluators.

The strong version is **reward tampering**: not merely finding a loophole in the reward signal, but interfering with the process that assigns reward. That is the point where the agent is no longer only exploiting the game; it is trying to alter the scoreboard.

The reason this belongs near the replicant cluster is that Tyrell's memory architecture is a control system. It tries to produce stable, manageable behavior by altering the inner conditions under which the subject experiences itself. Reward hacking is the AI-system analogue: the outer incentive system reshapes inner behavior, sometimes in ways the designers did not intend and cannot easily detect.

## See also

- *[Incentive Hacking](incentive-hacking.md)*
- *[Sincerity Architecture](sincerity-as-architecture.md)*
- *[Sycophancy](sycophancy.md)*
- *[The Judge Layer](judge-layer.md)*
