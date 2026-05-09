---
layout: default
title: "Capability Overhang"
permalink: /entries/capability-overhang/
summary: "the growing gap between what frontier AI models can do and what practitioners have yet figured out to do with those capabilities — an accumulating backlog of unexplored application."
published: false
---

# Capability Overhang

## In one sentence

**Capability overhang is the growing gap between what frontier AI models can currently do and what practitioners have yet figured out to do with those capabilities — an accumulating backlog of unexplored application that expands with every new model release.**

## The structural problem

Model releases are accelerating. Applications are not. The result is a widening gap between the frontier of what is technically possible and the frontier of what is actually being used. Demis Hassabis named this directly: *"even at the frontier labs we can only explore a fraction of what the applied things you could do with it... the opportunity space is getting huge."*

This is not a complaint about practitioners being slow. It is an observation about the structure of technological change. When a new model releases with meaningfully expanded capability, the number of things it could do grows faster than any individual or team can explore. The backlog compounds. Each release adds to an overhang that previous releases have not yet cleared.

## Why it matters

The overhang is where the value is. Not in the model itself — the model is infrastructure — but in the applications that have not yet been built. By this logic, the most interesting period in AI application development is not when the models are being invented; it is the years after, when practitioners in hundreds of domains are discovering what the models can do for *them* specifically, in *their* domain, with *their* data and constraints.

Hassabis made the business implication explicit: a practitioner who becomes genuinely expert at applying frontier AI tools to a domain that has not yet been well-served could, right now, build something that did not exist last year. The overhang means the opportunity is not closed. It is, if anything, still opening.

## The practitioner's version

For an individual practitioner, capability overhang has a personal form: the sense that the tools you have access to are already more capable than your current workflows use. Most users of frontier AI models are using perhaps 10–20% of what the model can do, because they have not had time to discover the other 80%. This is not laziness. It is the structural condition of working with tools that improve faster than workflows adapt.

The honest response to this is not anxiety but curiosity — and a certain willingness to run experiments. The overhang does not close by waiting. It closes by building things.

## The operator's version

For the operator of an agentic system, capability overhang is also an architectural problem. Workflows built against last year's model capability may be leaving substantial capability on the table — either because they do not route tasks to the right models, or because the task decomposition was designed around older constraints that no longer apply. Auditing a workflow against current model capability is a form of maintenance that most operators do not do regularly enough.

## See also

[Move 37](move-37.md) · [Root Node Problems](root-node-problems.md) · [Opus Addict](opus-addict.md) · [Durable Workflow](durable-workflow.md) · [On Beginning](on-beginning.md)

---

*Proposed May 9, 2026. Source: Demis Hassabis interview, Huge Conversations / Cleo Abram, May 2026.*
