---
layout: default
kind: reference
title: "Grep Architecture"
permalink: /entries/grep-architecture/
summary: "The choice to give an assistant a filing cabinet it searches on demand rather than forcing it to carry the whole library in its head at every session start."
date: 2026-06-17
draft: false
published: true
---

# Grep Architecture

---

## In one sentence

**Grep Architecture is the choice to give an assistant a filing cabinet it searches on demand rather than forcing it to carry the whole library in its head at every session start.**

## The filing cabinet problem

A growing agentic system eventually faces a simple architectural question: should the assistant wake up with everything already loaded, or should she wake up with a good map and fetch what she needs?

The first pattern is carrying-in-your-head. The harness loads large memory files, project notes, operating rules, style guides, calendars, history, context, and instructions into the model's prompt at session start. The assistant can refer to the material immediately, but every session pays the cost of carrying it, whether or not the task needs it.

The second pattern is filing-cabinet. The assistant wakes with a smaller current index and uses ordinary tools—`rg`, `grep`, `find`, `sed`, structured search, or memory search—to fetch the relevant file when the task calls for it.

The second pattern is Grep Architecture.

## Why grep

`grep` is a Unix search tool from the early 1970s. It searches text for patterns. `rg`, ripgrep, is the modern fast version many developers now reach for first. The exact command is less important than the habit: search the corpus, read the relevant part, then act.

This habit is old. Librarians knew it before programmers. A card catalogue is more useful than a memorized library. A lawyer does not carry the entire case law of a jurisdiction in her head. A doctor does not memorize all of PubMed. Experts learn where to look, how to search, and how to judge what they retrieve.

The same thing is true for agents.

## Why it matters for cost

Always-loading context makes the default prompt grow with the corpus. Every new memory file, project note, standing instruction, or long-term reference adds weight to future sessions unless a harness compacts, retrieves, or omits it. The corpus becomes more valuable, but also more expensive to carry.

The filing-cabinet pattern changes the cost curve. The assistant pays for the small current map by default and pays for the deeper context only when the work actually requires it.

This matters for API economics. Prompt caching can reduce repeated work, but only under the provider's reuse rules and cache lifetime. Retrieval avoids paying to present irrelevant material in the first place.

It also matters for local models. On local hardware, the same problem appears as prefill latency: the model has to read the prompt before it can answer. A smaller default prompt means faster starts. On-demand search means the local machine spends time reading what matters, not rereading the attic.

The architectural discipline ports across the model swap.

## Why it matters for memory

Grep Architecture is also a memory hygiene rule. It forces the system to distinguish current authority from historical material.

If everything is loaded, old notes can feel current simply because they are present. If memory is searched on demand, the assistant has to ask: what am I looking for, where is the current source of authority, and is this file a standing rule or a historical record?

That is not just cheaper. It is safer.

## The human analogy

The deeper point is that carrying everything is not how expertise works. Experts do not memorize all available knowledge. They carry a compact internal model of what matters, where to search, which sources have authority, and what kind of answer would count as adequate.

An agent designed with Grep Architecture behaves more like that expert. She does not pretend the whole corpus is present in the room. She knows where the filing cabinet is and how to use it.

## Related entries

*Cache-Write Tax* (planned) · *Prefill* (planned) · *[Sovereign Compute](/entries/sovereign-compute/)* · *[Model Tiering](/entries/model-tiering/)* · *[Context Window](/entries/context-window/)* · *[Provenance](/entries/provenance/)* · *[Heartbeat](/entries/heartbeat/)* · *[Agent Health](/entries/agent-health/)* · *[Harness Hygiene](/entries/harness-hygiene/)* · *[Skill](/entries/skill/)*
