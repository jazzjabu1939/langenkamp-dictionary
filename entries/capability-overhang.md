---
layout: default
kind: reference
title: "Capability Overhang"
permalink: /entries/capability-overhang/
summary: "The gap between what existing AI systems can do and what practitioners have learned to do with them."
published: true
---

# Capability Overhang

## In one sentence

**Capability overhang is the gap between what existing AI systems can do and what practitioners have learned to do with them.**

## The structural problem

New model capabilities can arrive faster than organisations can test, integrate, and govern them. Demis Hassabis described the resulting application backlog in a May 2026 interview: *"even at the frontier labs we can only explore a fraction of what the applied things you could do with it... the opportunity space is getting huge."*

The delay is structural. Each release creates possible applications across many fields, while each real application requires domain knowledge, workflow design, testing, and institutional adoption. A later model may arrive before practitioners have explored the earlier one.

## Why it matters

The overhang identifies where applied value may still be available. Model capability is only one input. Practitioners must connect it to a specific domain, its data, and its constraints.

Hassabis drew a business implication: a practitioner who becomes skilled at applying frontier tools in an underserved domain may be able to build something that was previously impractical. Capability overhang does not guarantee that the application will be useful or profitable. It says that the possible uses of existing systems have not been exhausted.

## The practitioner's version

For an individual practitioner, capability overhang appears when available tools can perform useful work that the person's current workflows do not yet use. There is no reliable percentage for this gap. It has to be found through bounded experiments on real tasks.

## The operator's version

For the operator of an agentic system, capability overhang is also an architectural problem. Workflows built against last year's model capability may be leaving substantial capability on the table — either because they do not route tasks to the right models, or because the task decomposition was designed around older constraints that no longer apply. Auditing a workflow against current model capability is a form of maintenance that most operators do not do regularly enough.

## See also

[Move 37](move-37.md) · [Root Node Problems](root-node-problems.md) · [Opus Addict](opus-addict.md) · [Durable Workflow](durable-workflow.md) · [On Beginning](on-beginning.md) · [Implementation Layer War](implementation-layer-war.md)

---

[^1]: Hassabis named OpenClaw specifically: *"I think a kid these days could probably start a multi-billion dollar business in some ways using these tools in some new way that no one had thought about. And I think things like OpenClaw is a good example of that."* (Huge Conversations / Cleo Abram, May 2026.)

[^2]: Nate Jones placed OpenClaw at the *runtime and orchestration* layer of the emerging agentic stack in the same month. ("AI Agent Judge Layer: How to Control Agents in Production," Nate's Substack, May 11, 2026.) Hassabis used it as an example of unexplored application; Jones used it as an example of implementation architecture.

*Proposed May 9, 2026; expanded May 11, 2026 with the Nate Jones naming. Sources: Demis Hassabis interview, Huge Conversations / Cleo Abram, May 2026; Nate Jones, "AI Agent Judge Layer," Nate's Substack, May 11, 2026.*
