---
layout: default
kind: glossary
title: "Incremental Construction"
permalink: /entries/incremental-construction/
summary: "the workflow technique of building complex AI-assisted output one verified layer at a time — committing each working checkpoint before asking for the next — so that the model always reasons against a correct context rather than a poisoned one."
published: true
---

# Incremental Construction

## In one sentence

**Incremental construction is the workflow technique of building complex AI-assisted output one verified layer at a time — committing each working checkpoint before proceeding — so the model always reasons against correct context rather than a [poisoned one](kv-cache-poisoning.md).**

## The problem it solves

When you one-shot a complex task to a language model — ask for the whole thing in a single prompt — you are gambling that the model's cold-start routing (in a MoE architecture) or cold-start attention (in a dense architecture) will activate the right capabilities simultaneously for every dimension of the task. For simple tasks, this works. For tasks with multiple interacting requirements — a stateful animation that also needs correct terminal rendering and a precise algorithm — the probability of the cold start getting all of it right drops sharply. And when it goes wrong, [KV cache poisoning](kv-cache-poisoning.md) makes it hard to recover within the same session.

Incremental construction sidesteps this entirely.

## How it works

Break the task into the smallest verifiable unit that makes architectural sense. Ask the model for only that unit. Test it. If it works, commit the result to version control (or otherwise fix it as a checkpoint). Only then ask for the next unit, with the working checkpoint now forming the context.

The analogy Protorikis used: building a moon station brick by brick rather than asking for the whole structure at once. Each verified brick becomes the foundation the router reasons against for the next brick. The expert clusters activated for step N+1 are aimed by the correct output of step N, not by a cold start and not by a poisoned context.

## Why this is better than critique-and-revise

The standard alternative to incremental construction is: one-shot the task, receive a flawed result, ask the model to review and fix it. This fails more often than practitioners expect because the critique is running against the poisoned KV cache. The model sees what it already wrote and tends to patch it rather than rethink it.

Incremental construction eliminates the bad draft before it exists. There is no poisoned context to critique because the context only ever contains verified working output.

## The secondary benefit

Protorikis noted this in passing and it deserves emphasis: when you build incrementally, you understand what you are building. The step-by-step process forces the operator to engage with each layer — the coordinate system, the data structure, the physics propagation, the rendering — rather than receiving a black box. The resulting code or text is not just more likely to be correct; it is more likely to be understood, maintained, and extended by the operator who built it.

This connects to the broader argument in [Durable Workflow](durable-workflow.md): the value of an AI-assisted workflow is not just in the output, but in the operator's maintained understanding of what the system does.

## Applications beyond coding

Incremental construction is a coding technique in origin but applies wherever a task has multiple interacting requirements that a cold-start prompt might not satisfy simultaneously:

- **Long-form writing:** draft the argument structure, verify it, then fill each section, rather than asking for the full essay
- **Data analysis:** establish the data structure and schema first, verify it, then add transformations one at a time
- **Workflow design:** build one agent step at a time, testing handoffs, before composing the full pipeline

## See also

[KV Cache Poisoning](kv-cache-poisoning.md) · [Sparse Routing](sparse-routing.md) · [Durable Workflow](durable-workflow.md)

---

*Proposed May 9, 2026. Source: Protorikis, "The 90's Flame Challenges the Modern MoE Models," YouTube 2026.*
