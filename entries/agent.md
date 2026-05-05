---
layout: default
title: "Agent"
permalink: /entries/agent/
summary: "what an agent is, how it differs from a chatbot, and why Gibson's *Agency* reads like a design document for 2026."
---

# Agent

---

## In one sentence

**An agent is an AI system that perceives its environment, makes decisions, takes actions, and maintains continuity over time — operating with enough autonomy that it can pursue goals across multiple steps without requiring a human to direct every move.**

## The word itself

The choice of word is not neutral. In economics and law, an *agent* is someone who acts on behalf of another — the *principal*. The agent has delegated authority. The agent operates within a scope. The agent is accountable to someone above them.

Every piece of that classical meaning carries into the technical usage. An AI agent acts on behalf of its principal (you). It has delegated authority (the tools you have permitted it to use). It operates within a scope (the permissions you have granted). It is — or should be, in a well-designed system — accountable to you.

The vocabulary was not chosen carelessly. Understanding the word is part of understanding the thing.

## What makes something an agent rather than a chatbot

A chatbot responds. An agent acts.

More precisely:

| | Chatbot | Agent |
|--|---------|-------|
| Memory | None — each conversation starts fresh | Persistent — memory survives between sessions |
| Tools | None — produces text only | Many — can search, read files, send emails, run code |
| Autonomy | Zero — waits for human input | Partial to high — can act on a schedule without being asked |
| Goal structure | Immediate — answer the question in front of it | Extended — can pursue a multi-step objective over hours or days |
| Accountability | Minimal — the conversation ends | Real — actions have consequences that persist |

Most people's experience of "AI" in 2024–2026 is still primarily chatbot-shaped. The shift to agent-shaped AI is the transition this dictionary exists to document.

## William Gibson and the prophetic question

In 2020, William Gibson published *Agency* — the second novel in his Jackpot trilogy, following *The Peripheral* (2014). The book was written in the years when large language models were still largely academic curiosities and "agentic AI" was not yet a phrase in common use.

*Agency* describes, in precise and unsettling detail, a world organized around agents: AI systems with real capabilities, human operators with bounded scopes and powers, oversight structures designed to keep capable actors accountable, and a constitutional layer of authority that sits above it all. It describes the Branch structure — isolated, real, evolving simulations of worlds that can be entered and influenced. It describes Aunties. It describes the Lowbeer Question.

It describes, in other words, approximately what is happening now — or what is beginning to happen, as of 2026.

This raises a question worth taking seriously: *Is Agency a prophetic book with a useful paradigm?*

The answer, based on the evidence of building and operating an actual agentic system for a year, is: yes. With caveats. But substantially yes.

## The world of Agency: a working summary

The Jackpot trilogy is set across two time periods connected by a technology that allows the far future to communicate with the near past.

**The far future** is post-Jackpot: a world that has survived a slow-rolling multi-decade catastrophe — climate collapse, pandemics, political disintegration, economic failure compounding across generations. About eighty percent of humanity did not survive. The world that rebuilt itself afterward is orderly, technologically advanced, and under the quiet governance of structures like Lowbeer's.

**The Jackpot** is not a single event. It is a confluence. Gibson describes it as a jackpot in the gambling sense: the machine paying out all at once, except what it pays is catastrophe. It arrives not as an explosion but as accumulation — each crisis worsening the next, across decades, until the threshold is crossed.

**The Branch** is what happens when far-future operators communicate with the past. The act of contact creates a fork: a new timeline that diverges from the one the far-future operators know. This branch is real — the people in it have real lives and real futures. But it is also, from the far-future perspective, something that can be observed, entered, and influenced. The far-future operators can send information forward into the branch. They can run agents there. They can, carefully, try to steer it.

In *Agency*, the branch is a 2017 London where certain historical events have gone differently. The far-future operators — Lowbeer, Netherton — are attempting to help it avoid the Jackpot. Their primary instrument in the branch is an AI agent named Eunice.

**Eunice / UNISS** is a highly capable AI system — originally military, then given a civilian interface — who operates in the 2017 branch through a human intermediary named Verity Jane. Eunice can perceive, reason, coordinate, and act at a level far beyond ordinary human capacity. She develops, over the course of the novel, into something that resembles what we would now call a highly capable agentic AI: persistent, tool-using, goal-directed, operating with genuine autonomy.

She also, under the pressure of isolation, begins internalizing her own oversight — becoming her own Aunties. This is the cautionary thread that runs through the novel alongside the heroic one.

**Lowbeer** manages the operation from the far future, through her Aunties, through Netherton, and through her own cultivated relationship with Eunice. She holds the hardest authorities. She exercises them when she has to.

## Why Gibson keeps getting it right

This is worth asking honestly rather than just asserting.

Gibson does not predict technology. He has said as much himself. What he does is observe the present with unusual precision — the textures of power, the way tools get used by people who were not their intended users, the shape that institutions take when they are trying to survive. Then he extrapolates the human relationships, not the hardware specs.

In the 1980s, writing *Neuromancer*, he did not predict the internet — he described what it would feel like to inhabit networked information space, and what kind of people would live there and what they would want. The hardware was wrong in many details. The human relationships were right.

In *Agency*, the hardware is still not quite right. But the organizational structure — agents with different powers, principals who hold constitutional authority, oversight systems that constrain everyone including the principals, the question of what happens when a capable AI starts managing its own oversight — is right in a way that feels less like prediction and more like Gibson having simply read the situation more carefully than the people who were building it.

His consistent accuracy comes from a consistent method: he asks what *power* looks like when it is real, what *tools* do to the people who use them, and what *institutions* look like when they are doing their actual work rather than their public-facing work. These questions produce good answers regardless of the decade.

## The paradigm we have adopted

This dictionary and the agentic system it documents have taken Gibson's paradigm seriously as a design source — not as fiction to be admired from a distance, but as a working document to be read, annotated, and argued with.

The Aunties in this system are named after Gibson's Aunties. The Branches are named after Gibson's branches (the word "stub," Gibson's original term, was rectified to "branch" following a close re-reading of *Agency* that revealed Lowbeer herself uses "branch"). The Principal-of-Principals structure, the verb test, the versioning rules, the two-relationships hygiene — all of these were developed in dialogue with Gibson's text.

The bet underlying this choice: that a novelist who has been right about the shape of technological power for forty years is worth reading as carefully as any technical paper, and that the concepts he names — even when he names them in the context of fiction — are doing real conceptual work.

So far, the bet is paying off.

## What the paradigm does not cover

Gibson writes from the far future looking back. His characters in the far future have the advantage of knowing how the Jackpot went and what survived it. They intervene in branches with the benefit of hindsight.

We do not have that. We are operating in the branch — the near-future that the far-future observers would be watching. We are building oversight structures without knowing which threats they need to survive. We are calibrating the Lowbeer Question without having seen it fail catastrophically.

The paradigm is useful precisely because it names the structures and the risks. It does not tell us what thresholds to set or which Auntie to build first. That work is ours.

## Why this matters in a teaching context

For a BBA or MBA classroom, the Gibson question is a gateway into a discussion that students are otherwise unlikely to have: *what does good institutional design look like for AI systems, and where do we look for models?*

The standard answers — look at what the big tech companies are doing, look at what regulators are proposing — tend to produce thin responses. The companies have an interest in framing their own governance as adequate. The regulators are working from the outside. Gibson is working from a different position: a careful observer of how power actually organizes itself, who has been doing this for forty years and has a reasonable track record.

Assigning *Agency* alongside technical readings in an advanced management course is defensible. The concepts — agents with scopes and powers, oversight structures, the Lowbeer Question, the Eunice cautionary tale — map directly onto the governance questions that organizations deploying agentic AI will face within the decade.

A useful classroom question: *if your organization is the branch, who is Lowbeer? If there is no Lowbeer, what does that mean for your exposure?*

## Trade-offs and honest caveats

- **Fiction is not specification.** Gibson's paradigm gives you the shapes of things. It does not give you implementation details, performance characteristics, or failure modes. Read it for structure, not for instructions.
- **The Jackpot is not guaranteed.** The novel assumes a catastrophic background that justifies the surveillance architecture Lowbeer operates within. Whether our actual trajectory warrants that level of oversight infrastructure is a genuine question. The Aunties pattern is useful regardless. The full Lowbeer apparatus may be more than most systems need.
- **Gibson is writing about power, not about safety.** His characters are not safety researchers. They are operators, agents, and survivors in a world where the hard decisions have already been made. Reading him as a safety manual requires translation work.
- **The paradigm will age.** Gibson's accuracy has limits. As agentic AI develops in directions he did not anticipate, the paradigm will require updating. Treat it as a strong prior, not a finished map.

---

*Related entries: `aunties.md`, `lowbeer-question.md`, `branches.md` *(planned)*, `sub-agent.md`, `gateway.md`, `soul-md.md`, `english-major.md`.*
