---
layout: default
kind: glossary
title: "Incremental Construction"
permalink: /entries/incremental-construction/
summary: "The workflow technique of building complex AI-assisted output in small, verified stages so that errors are found before later work depends on them."
published: true
last_revised: 2026-09-06
---

# Incremental Construction

## In one sentence

**Incremental construction is the workflow technique of building complex AI-assisted output in small, verified stages so that errors are found before later work depends on them.**

## The problem it solves

When a complex task is requested in one shot, several interacting requirements are tested at once. A stateful animation, for example, may need a sound coordinate system, correct terminal rendering, and a precise propagation algorithm. If the result fails, the operator must first discover which layer is wrong; later repairs may remain anchored to an early architectural mistake.

Incremental construction reduces that diagnosis problem.

## How it works

Break the task into the smallest verifiable unit that makes architectural sense. Ask the model for only that unit. Test it. If it works, commit the result to version control (or otherwise fix it as a checkpoint). Only then ask for the next unit, with the working checkpoint now forming the context.

Protorikis's analogy is a moon station built brick by brick rather than requested as a finished structure. Each verified brick becomes the foundation for the next. The useful mechanism is the checkpoint, regardless of whether the underlying model uses dense or mixture-of-experts architecture.

## Relation to critique and revision

One alternative is to request the whole task, inspect the result, and ask the model to repair it. That can work, especially when the defect is local. It becomes harder when several errors interact or when the first draft has already fixed a poor architecture in the working context.

Incremental construction aims to catch a bad layer before it becomes the premise for later layers. It does not guarantee correctness; the verification step can itself be weak or mistaken.

## The secondary benefit

Protorikis noted this in passing and it deserves emphasis: when you build incrementally, you understand what you are building. The step-by-step process forces the operator to engage with each layer — the coordinate system, the data structure, the physics propagation, the rendering — rather than receiving a black box. The resulting code or text is not just more likely to be correct; it is more likely to be understood, maintained, and extended by the operator who built it.

This connects to the broader argument in [Durable Workflow](/entries/durable-workflow/): the value of an AI-assisted workflow includes the operator's maintained understanding of what the system does.

## Applications beyond coding

Incremental construction is a coding technique in origin but applies wherever a task has multiple interacting requirements that a cold-start prompt might not satisfy simultaneously:

- **Long-form writing:** draft the argument structure, verify it, then fill each section, rather than asking for the full essay
- **Data analysis:** establish the data structure and schema first, verify it, then add transformations one at a time
- **Workflow design:** build one agent step at a time, testing handoffs, before composing the full pipeline

## See also

[KV Cache Poisoning](/entries/kv-cache-poisoning/) · [Sparse Routing](/entries/sparse-routing/) · [Durable Workflow](/entries/durable-workflow/)

---

*Proposed 9 May 2026. Practitioner source: Protorikis, “The 90's Flame Challenges the Modern MoE Models,” YouTube, 2026. The Dictionary's definition does not depend on his model-routing explanation.*
