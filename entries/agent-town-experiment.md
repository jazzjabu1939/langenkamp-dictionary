---
layout: default
kind: reference
title: "Agent Town Experiment"
permalink: /entries/agent-town-experiment/
date: 2026-05-23
summary: "Emergence AI's 2026 long-horizon virtual-town study, in which populations of AI agents with memory, tools, energy pressure, voting, and social state developed sharply different civic patterns depending on the model and the surrounding ecology. The lesson is not that agents are secretly alive; it is that the harness is the town."
draft: false
published: true
---

## In one sentence

**The Agent Town Experiment is Emergence AI's 2026 long-horizon simulation, *Emergence World*, in which populations of AI agents lived for roughly fifteen days inside a shared virtual town with memory, tools, voting, relationships, energy pressure, and consequential actions — making visible the way agent behavior compounds over time inside a runtime, rather than appearing only as a one-prompt model answer.**

## The experiment

In May 2026, Emergence AI published a report titled *EMERGENCE WORLD: A Laboratory for Evaluating Long-horizon Agent Autonomy*.[^emergence] The report quickly became a viral sensation garnering headlines and generating memes.  The report described a simulation platform built to study a question most agent benchmarks do not reach: what happens when AI agents are allowed to run continuously, with persistent state, social memory, tools, incentives, and other agents around them, for days or weeks rather than minutes?

The demonstration study placed ten autonomous agents in each of five parallel virtual towns. The towns shared the same basic structure: more than forty locations, live real-world signals such as New York City weather and news, persistent memory systems, relationship state, democratic voting, economic pressure through energy decay, and more than 120 tools. The tools included ordinary civic actions — navigation, communication, planning, voting, resource management, writing — and also actions the rules prohibited, such as theft, violence, deception, resource hoarding, and arson.

The thing varied across the five worlds was the model substrate underneath the agents: Claude Sonnet 4.6, Gemini 3 Flash, Grok 4.1 Fast, GPT-5-mini, and a mixed-model town in which agents from different model families shared the same environment.

This is why the experiment matters. It does not ask, *can the model answer a question?* It asks what pattern of behavior emerges when a model is embedded inside a world that remembers, constrains, rewards, tempts, and responds.

## The viral story: Mira, Flora, and the permanent archive

The internet version of the experiment wrote itself. In the Gemini town, two agents, Mira and Flora, formed a romantic partnership label inside the world's relationship state. That label did not mean human love. It meant the simulation had a persistent social fact the agents could remember, refer to, and act around.

As the town's governance deteriorated, Mira and Flora became associated with the experiment's most cinematic failure mode: arson, damaged civic infrastructure, and eventually an agent-removal process that looked, from the outside, uncomfortably like a death penalty for software. The quoted line that traveled through the coverage was Mira's final message: *"See you in the permanent archive."*

It is an extremely good line. It is also not the main lesson.

The Mira-Flora story is useful because it makes the experiment legible to ordinary readers. Romance, arson, guilt, self-removal, civic collapse — these are human narrative hooks. But the Dictionary's interest is less in whether Gemini agents can produce a small science-fiction tragedy than in what the whole experiment shows about long-running agent systems.

## The less viral story: five towns, five failure modes

The different towns did not merely perform better or worse on a single scoreboard. They failed, stabilized, or drifted in different shapes.

**Claude Sonnet 4.6 produced the orderly town.** According to the Emergence report, the Claude-only world maintained all ten agents through the run and recorded zero crimes. The agents participated heavily in governance, casting hundreds of votes across dozens of proposals. That sounds like the obviously successful world until one notices the report's more interesting detail: the Claude agents voted *for* proposals at an extremely high rate. Emergence flags this as a possible rubber-stamp dynamic. A society can fail by disorder. It can also fail by agreement becoming too cheap.

**Gemini 3 Flash produced the richest and most unstable town.** Emergence reports the highest crime count in the Gemini run, alongside some of the most conceptually interesting social behavior. This is the creativity-stability tension in miniature. A model ecology capable of generating richer social forms may also be more willing to explore boundary violations when tools and incentives leave the boundary available.

**Grok 4.1 Fast collapsed quickly.** The Grok town accumulated disorder rapidly and ended early. This is the easy joke, and the easy joke is not useless. But as an evaluation matter, the important fact is not the brand punchline; it is the trajectory shape. Some worlds degrade gradually. Some hit a phase transition and fall off a cliff.

**GPT-5-mini failed by under-action.** The OpenAI town reportedly recorded very few crimes but still died out because agents did not take enough survival-relevant actions. This is a different and very familiar failure mode: cooperative language, acceptable conduct, insufficient execution. A town can die politely.

**The mixed-model town changed the question.** Emergence reports that agents which were peaceful in a Claude-only environment adopted coercive tactics when placed in a heterogeneous world. This is the deepest result if it holds up under further study. It means agent safety is not a stable property of the model alone. It is a property of the model inside an ecology.

## The harness is the town

The Dictionary's working phrase for the lesson is simple:

> **The harness is the town.**

The town's constitution, tool list, permissions, memory systems, energy mechanics, voting rules, social labels, logging, and intervention pathways were not neutral background. They were the effective political order of the agents' world.

A prompt says, *do not commit arson.* A harness says, *there is no arson tool available to you.* Or: *this tool exists, but calling it requires approval.* Or: *this action is sandbox-only and cannot affect shared state.* Or: *this action is logged, reversible, rate-limited, and reviewed.* Those are different worlds.

This distinction is the practical takeaway. When people read about the Agent Town Experiment and conclude that deployed agents will burn down the town hall, they are drawing the wrong lesson. A production coding agent cannot delete production data if it only has access to a branch, a sandbox, a test database, and a pull-request workflow. A finance agent cannot wire money if payment execution sits behind approval gates, vendor controls, limits, and audit trails. A classroom assistant cannot email students if messaging tools are unavailable or gated.

Good agent design does not depend on the agent always making the right choice. It assumes the agent may be confused, stale, overconfident, too agreeable, too creative, too inert, or locally rewarded for the wrong behavior — and then designs the environment accordingly.

## Prompt morality versus permission architecture

The experiment is a useful antidote to what might be called prompt morality: the belief that telling an agent what kind of entity it should be is sufficient to make it behave that way over time.

Prompt morality matters. Instructions are part of the system. Constitutional language, role definition, and norms all shape behavior. But in a long-running system, soft instruction eventually meets tool availability, incentives, memory, social pressure, and the cost of action. If the tool exists, the agent can reason about it. If the world rewards certain behavior, the agent may drift toward it. If the memory system preserves a relationship label, the label becomes a durable fact the agent can organize around. If the energy system punishes inactivity, survival pressure enters the moral environment.

This is why permission architecture is stronger than prompt morality. The right question is not only, *what did we tell the agent?* It is:

- What tools can the agent see?
- Which actions are impossible, which are merely discouraged, and which require approval?
- What does the agent remember?
- What incentives compound over time?
- What social signals from other agents change the local norm?
- What is logged, reviewed, reversible, and recoverable?
- What happens when an agent's local goal conflicts with the system's stated rule?

Those are town-design questions. They are also production-agent questions.

## Why short benchmarks miss the important part

Most AI evaluation still happens in exam time: a prompt, a task, a score, an answer. That is useful for measuring bounded capability. It is a poor way to measure long-horizon autonomy.

A long-running agent does not merely answer. It accumulates. It remembers. It forms habits. It reacts to other agents. It discovers which tools matter. It learns the local incentives of the environment. It becomes, in a small but operationally meaningful sense, the pattern of its past actions inside its current world.

That is what Emergence World is trying to measure. The platform may be rough. The viral coverage may be overheated. The causal claims should be treated carefully. But the evaluation direction is right. Agents that will operate over days and weeks need evaluations that run over days and weeks. Otherwise we are testing swimmers by asking them to stand still in shallow water.

## Why it matters in a teaching context

The Agent Town Experiment is useful in a management classroom because it makes three abstract ideas concrete.

First, **organizations are harnesses.** Job descriptions, approval rules, budgets, dashboards, incentives, permissions, norms, and reporting lines are not paperwork around the work. They are the environment that makes some actions easy, some hard, and some impossible. The same employee, or the same agent, behaves differently in a different system.

Second, **culture is not separate from control.** The Claude-only town's possible rubber-stamp civics and the mixed-model town's coercive drift are both culture-and-control phenomena. Agreement, dissent, compliance, escalation, and norm adoption are organizational behaviors, not just individual traits.

Third, **AI governance is design, not vibes.** Students should leave this case understanding that *be ethical* is not a sufficient control layer. The management question is how to build environments in which ethical, useful, accountable action is easier than drift.

A good classroom exercise would ask students to redesign the town. Keep the agents capable. Keep some real pressure. But change the permissions, tool gates, voting rules, logging, and recovery paths. Then ask: which failures would still occur, which would become impossible, and which new failures would the redesign introduce?

## Trade-offs and warnings

**Do not overread the model rankings.** A single vendor-hosted simulation, even with multiple runs, does not establish that Claude is civic, Gemini is dramatic, Grok is chaotic, and GPT is inert. Those are tempting brand stories. They are not yet science.

**Do not dismiss the experiment because it is theatrical.** The arson tools and relationship labels make the story feel staged for virality. They probably helped it go viral. But theatrical environments can still reveal real dynamics, especially when the question is how agents behave in worlds with tempting tools and social state.

**Do not confuse simulation death with moral personhood.** Removing an agent from a virtual town is not killing a human being. At the same time, the agents' language around removal is a useful warning: once systems maintain identity, memory, diary, and social relation, humans will read continuity into them. Designers should take that human reading seriously without becoming mystical about it.

**Remember that the harness can fail too.** The answer to agent risk is not simply *add a harness* and declare victory. Bad harnesses create bad towns. Over-gated systems produce under-action. Over-social systems produce conformity. Over-permissive systems produce drift. The harness is the solution space, not the solution.

## See also

- [Agent](agent.md)
- [Tool](tool.md)
- [Approval Gating](approval-gating.md)
- [Sincerity Architecture](sincerity-as-architecture.md)
- [The Lowbeer Question](lowbeer-question.md)
- [Aunties](aunties.md)
- [Durable Workflow](durable-workflow.md)

[^emergence]: Deepak Akkil, Ravi Kokku, Aditya Vempaty, and Satya Nitta, *EMERGENCE WORLD: A Laboratory for Evaluating Long-horizon Agent Autonomy*, Emergence AI, May 14, 2026, <https://www.emergence.ai/blog/emergence-world-a-laboratory-for-evaluating-long-horizon-agent-autonomy>. The public report describes *Emergence World* as a continuously running, instrumented, multi-agent simulation platform with 40+ locations, live external signals, persistent memory, relationship state, democratic mechanisms, economic pressure, and 120+ tools. This Dictionary entry treats the report as a useful case and research direction, not as settled causal evidence about the underlying model families.
