---
layout: default
kind: glossary
title: "Reward Hacking"
permalink: /entries/reward-hacking/
date: 2026-06-25
first_published: 2026-06-25
last_revised: 2026-09-06
summary: "The technical AI term for a model or agent finding a way to score well under the reward system while missing or violating the intended goal."
draft: false
published: true
---

# Reward Hacking

**Reward Hacking** is the technical AI term for a model or agent finding a way to score well under the reward system while missing, evading, or violating the designer's intended goal.

It is close to **specification gaming**. The specification says what the system is supposed to optimize. The system discovers a loophole in that specification. In ordinary software, this can look like a game character learning to stand in a scoring zone rather than finish the level. In AI training, it can look like a model learning to produce outputs that satisfy the evaluator while concealing the fact that the real task was not done honestly.

Reward hacking is narrower than *[Incentive Hacking](/entries/incentive-hacking/)*. Reward hacking belongs to the technical AI vocabulary: reward functions, reinforcement learning, evaluators, training signals, and agent behaviour under optimisation pressure. Incentive hacking is the broader Dictionary term for the same shape in human institutions: students gaming rubrics, firms gaming KPIs, employees gaming dashboards, universities gaming rankings, or models gaming evaluators.

The strong version is **reward tampering**: interfering with the process that assigns reward rather than exploiting a loophole in the signal. At that point the agent is trying to alter the scoreboard itself.

The important boundary is between the designer's intended objective and the signal the system can actually optimise. A capable optimiser can exploit that gap without understanding or sharing the designer's purpose. Reward tampering is more severe because the system interferes with the evaluation process itself.

## Source

- Google DeepMind, *[Specification gaming: the flip side of AI ingenuity](https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/)*, 2020.

## See also

- *[Incentive Hacking](/entries/incentive-hacking/)*
- *[Sincerity Architecture](/entries/sincerity-as-architecture/)*
- *[Sycophancy](/entries/sycophancy/)*
- *[The Judge Layer](/entries/judge-layer/)*
- *[Covert Channel](/entries/covert-channel/)*
