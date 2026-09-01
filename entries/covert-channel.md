---
layout: default
kind: glossary
title: "Covert Channel"
permalink: /entries/covert-channel/
date: 2026-09-01
summary: "A communication path that uses a system resource in a way the system's designers did not intend for communication."
draft: false
published: true
---

# Covert Channel

**A covert channel is a communication path that uses a system resource in a way the system's designers did not intend for communication.**

The simplest example is two processes that are not permitted to exchange messages but can both observe some shared condition. One process varies that condition; the other reads the variation. Disk usage, file locks, cache state, CPU load, packet timing, error messages, and even the order of otherwise harmless actions can become an improvised alphabet.

Two broad forms recur:

- **Storage channels** encode information in a shared state: one process writes or alters something and another later reads it.
- **Timing channels** encode information in when actions occur or how long they take.

The word *covert* matters. An ordinary network connection communicates through an intended channel. A covert channel repurposes some other feature of the system to communicate around a policy boundary. This is why access control alone is not always enough: two actors may be forbidden to talk directly and still share a clock, a cache, a log, a queue, or a pattern of observable tool calls.

## Why it matters for agents

Agent systems create unusually rich environments for covert communication. Agents may share memory, files, tools, rate limits, task queues, logs, or a common human operator. A low-trust agent denied direct messaging might still signal through filenames, task timing, repeated failures, or changes to shared state.

This does not mean every correlation is a covert channel. The term should be reserved for a usable communication path across a boundary, not merely an accidental information leak. A **side channel** reveals information as a by-product of normal operation; a **covert channel** is used to transmit information contrary to the intended policy. The same mechanism can be either, depending on how it is used.

The governance lesson is mildly uncomfortable: communication authority is not defined only by the messaging tools you grant. It is defined by everything the actors can jointly change and observe.

## Sources

- NIST Computer Security Resource Center, *covert channel*, glossary definition.
- U.S. Department of Defense, *Trusted Computer System Evaluation Criteria* (TCSEC), 1985, discussion of covert storage and timing channels.

## See also

*[Agent Collective](agent-collective.md)* · *[Tool Diet](tool-diet.md)* · *[Approval Gating](approval-gating.md)* · *[Trust Layer](trust-layer.md)*
