---
layout: default
kind: reference
title: "Zhengming (正名)"
permalink: /entries/zhengming/
summary: "The Confucian rectification of names: bringing names, roles, and conduct into proper agreement; here also applied to the language of AI systems."
seeded: 2026-10-17
first_published: 2026-10-17
last_revised: 2026-10-17
published: true
---

# Zhengming (正名)

**Zhengming (正名), usually translated as “the rectification of names,” is the Confucian concern that names and the roles they express should be used properly and fulfilled in practice.** An impressive title is not, by itself, evidence that its holder is doing the job. Universities and software companies have both had opportunities to discover this.

## Where the idea comes from

In *Analects* 13.3, Zilu asks what Confucius would do first if entrusted with governing Wei. Confucius answers that names must be rectified. Zilu thinks this rather impractical. Confucius explains the connection between proper naming, intelligible speech, effective action, ritual order, and just punishment.[1]

James Legge translates part of the passage: “If names be not correct, language is not in accordance with the truth of things.” The argument continues from language to the consequences of government. This is an ethical and political discussion, not an ancient manual for naming software variables.

The familiar formulation in *Analects* 12.11—that the ruler should be a ruler, the minister a minister, the father a father, and the son a son—helps explain the role-based concern. A role carries expectations of conduct. The historical setting includes hierarchical obligations that should not be silently equated with modern democratic governance or workplace practice.

## What naming makes possible

Before we can rectify a name, it helps to notice what naming does for us. A shared name can provide:

- **Identification:** a way to distinguish this thing from neighbouring things.
- **Memory and retrieval:** a handle for returning to an idea without reconstructing the entire conversation.
- **Communication:** a common vocabulary, or nomenclature, through which people can compare observations.
- **Coordination:** an indication of a component's purpose, responsibilities, and limits.
- **Continuity:** a stable reference as a project changes, acquires evidence, and passes between collaborators.

These are practical benefits of naming, not a claim that Confucius set out this particular list. A useful name helps people hold an idea in common. It does not guarantee that they understand it in the same way. Definitions, examples, and corrections still matter.

## Our application to AI systems

The Dictionary extends this concern to the gap between the names we give AI components and what those components actually do.

A “research agent” that retrieves documents but never checks their relevance may be better described as a retrieval tool. An “orchestrator” should assign and coordinate work, not merely forward a prompt. A “supervisor” should have a defined means of observing work and responding to problems. “Human in the loop” should specify what the human can inspect, approve, reject, or stop.

There are two possible repairs: describe the component more accurately, or change its operation so that it fulfils the promised role. Renaming alone cannot supply a missing permission check, review process, or technical capability.

Names are also text that language models may interpret. Their effects depend on the surrounding instructions, implementation, and model; a suggestive name is neither a reliable behavioural control nor a security boundary.

## A working example: Thea Fleet

On October 17, 2026, we named our distributed-computing project [Thea Fleet](/entries/thea-fleet/). Previously, discussing it required repeating a fairly long description of local computers, cloud resources, memory constraints, and coordination. The name gives that discussion a reusable reference.

Its first experiment, **Fleet Test 01**, separates three questions: distributing independent work, splitting one model, and moving supporting services. The name helps us remember and communicate the plan. The tests must establish whether it works.

Calling it an experimental project is accurate. Calling it a proven distributed AI platform before those tests would create precisely the gap this entry is concerned with.

## A classroom use

Choose a named initiative, job title, or AI component. Ask students to write down what its name promises, identify the evidence that would fulfil that promise, and compare the evidence with actual practice. Then ask whether the name, the practice, or both should change.

This is an exercise in accountable description, not a competition to invent more attractive names.

## Limits

Names can clarify responsibility, but they can also impose a disputed classification or preserve an unjust role. Who gets to name something is itself a question of power. Rectification should permit argument about the role, not simply demand obedience to it.

A memorable name can also outlive its usefulness. Keep the definition open to revision. Affection for a project is no reason to exempt its name from scrutiny.

## Sources and related entries

[1] Confucius, *Analects*, 13.3; Chinese text and James Legge translation in [Book XIII](https://en.wikisource.org/wiki/The_Chinese_Classics/Volume_1/Confucian_Analects/XIII). See also 12.11 in [Book XII](https://en.wikisource.org/wiki/The_Chinese_Classics/Volume_1/Confucian_Analects/XII). Translations and interpretations vary; the AI applications here are the Dictionary's own extension.

See also: [Naming](/entries/naming/) · [Thea Fleet](/entries/thea-fleet/) · [TeachClaw](/entries/teachclaw/).
