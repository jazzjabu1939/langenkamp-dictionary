---
layout: default
kind: reference
title: "Agent Maintenance"
permalink: /entries/agent-maintenance/
date: 2026-11-21
summary: "The ongoing work of keeping an AI agent accurate, safe, and useful after it has been built: checking its instructions, tools, memory, permissions, and results as models, data, and the work itself change."
published: true
seeded: 2026-07-01
first_published: 2026-11-21
last_revised: 2026-11-21
---

# Agent Maintenance

In May 2026 several of our scheduled agent jobs began failing overnight. Nothing in the jobs had changed, and that turned out to be the problem. Each job had a model name written into it, and we had since moved our billing away from that provider. The jobs kept asking for models we were no longer paying for. The agents had been built correctly. Nobody had looked after them since.

## In one sentence

**Agent maintenance is the ongoing work of keeping an AI agent accurate, safe, and useful after it has been built: checking its instructions, tools, memory, permissions, and results as models, data, and the work itself change.**

## Why it exists

Building an agent has become easy. A capable person can write instructions, connect a few tools, and have something useful running in an afternoon. The demonstration works, people start relying on it, and the builder moves on to the next thing.

Then the world moves. The model provider releases a new version that follows instructions slightly differently. A colleague renames the folder the agent reads from. The policy the agent summarises is revised. A tool it depends on changes its login. None of these breaks the agent loudly. Most of them make it quietly worse, and a confident agent that is quietly worse is harder to notice than one that has stopped.

Nate Jones put the point in the title of a June 2026 essay: building agents is easy, and maintaining them is the real skill.[1] The observation is older than agents. Google engineers made the same argument about machine-learning systems in 2015: the code that trains a model is a small part of the system, and the surrounding data, configuration, and dependencies accumulate a maintenance debt that compounds unless someone pays it down.[2]

## What gets maintained

Jones's checklist, lightly adapted, gives seven things to inspect:

- **Job.** Is the agent still doing the task people now expect of it, or has its use drifted beyond what it was built for?
- **Diet.** Are its instructions and reference documents current? Old guidance stays in force until someone removes it.
- **Memory.** Has it accumulated notes that are stale, wrong, or private in ways nobody intended?
- **Tools.** Does it still need every tool it has? Does every tool still work? (See [Tool Diet](/entries/tool-diet/).)
- **Reach.** Have its permissions grown as people added "just one more" access?
- **Proof.** How would anyone know it is wrong? Is there a check, a sample review, or a log someone actually reads?
- **Value.** Is it still worth running, or would retiring it be the better maintenance?

## A working example

The failures in the opening were fixed in a day once someone looked. The lasting fix was a maintenance rule rather than a repair: scheduled jobs no longer name a model. They name which agent should do the work, and that agent's configuration, kept in one place, decides the model. When the model changes, one setting changes, and every job follows.

A second rule came from the same episode. A twice-daily check now lists every scheduled job and flags any that has picked up a model name again. That check is itself maintenance, and it is the part that keeps the first fix from decaying.

## Why this matters in a teaching context

Students learn to build things in courses. They rarely learn to keep things running, because a semester ends before upkeep starts. Yet most of the value, and most of the risk, of an agent in a real organisation comes after the demonstration.

The management lesson is the familiar one about any asset: the purchase price is the smaller cost. An organisation that counts how many agents it has built, but not who maintains each one, is counting liabilities as assets. [Agent Ownership](/entries/agent-ownership/) asks who is responsible for an agent. Agent maintenance is what that person actually does each week.

## Trade-offs and warnings

- **Maintenance competes with building.** The new agent is exciting; checking the old one is not. Without a schedule, upkeep loses every time.
- **More agents, more upkeep.** Each new agent adds a recurring cost. Sometimes the best maintenance decision is to retire two agents and keep one.
- **Checks decay too.** A review nobody reads is not a check. The proof step needs to produce something a person will notice.
- **Model upgrades are not free improvements.** A better model may follow old instructions in new ways. Treat a model change as a change to every agent that uses it, and look at results afterward.

## See also

[Agent Ownership](/entries/agent-ownership/) · [Agent Health](/entries/agent-health/) · [Tool Diet](/entries/tool-diet/) · [Harness](/entries/harness/) · [Heartbeat](/entries/heartbeat/) · [Verification Gap](/entries/verification-gap/) · [Prompt Injection](/entries/prompt-injection/)

## Sources

[1] Nate Jones, ["Agent Maintenance: The AI Skill That Keeps Agents Useful"](https://natesnewsletter.substack.com/p/ai-agent-maintenance), June 17, 2026. The seven-part checklist above is adapted from his.

[2] D. Sculley et al., ["Hidden Technical Debt in Machine Learning Systems"](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems), *Advances in Neural Information Processing Systems* 28 (2015).

---

*First published November 21, 2026.*
