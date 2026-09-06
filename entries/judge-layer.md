---
layout: default
kind: reference
title: "The Judge Layer"
permalink: /entries/judge-layer/
date: 2026-06-17
first_published: 2026-06-17
last_revised: 2026-09-06
summary: "The production-architecture layer that evaluates an agent's proposed actions and decides which may proceed, which need human approval, and which must stop."
published: true
---

# The Judge Layer

---

## In one sentence

**The Judge Layer is the part of an agentic system that evaluates proposed actions and decides which may proceed, which need human approval, and which must stop.**

## Where the name comes from

Nate B. Jones used the term in his Substack essay *AI Agent Judge Layer: How to Control Agents in Production* (11 May 2026). His central architectural claim is narrow and useful: once an agent can take consequential action, a separate judge should sit between the actor and execution.

Jones's builder toolkit includes action classification, proposals, specialist judges, evaluation, and memory governance. This entry uses *judge layer* for that control tier; it does not treat the term as a complete taxonomy of agent infrastructure.

## What belongs in the layer

A judge need not be another large model. The layer may combine:

- deterministic rules, schemas, and permission checks;
- a classifier or model that evaluates a proposed action;
- a human approval gate at a high-risk boundary;
- logging and post-action evaluation for conduct that cannot be judged fully in advance.

The placement depends on consequence. A formatting validator can run after generation. A payment limit, publication gate, or deletion policy must intervene before the irreversible action.

Self-critique inside the worker may improve quality, but it is not independent control. The worker and its self-critic share context, incentives, and failure modes. External checks become more important as permissions and consequences increase.

## The literary version: the Aunties

The Dictionary reads William Gibson's Aunties as a literary analogue. In the *Jackpot* novels, Lowbeer operates with specialised background intelligences that observe, advise, and exercise forms of authority. Gibson was not specifying a production-agent architecture. The mapping is the Dictionary's extension: the Aunties give the engineering pattern moral and organisational texture.

This analogy asks questions that a validator schema cannot answer by itself. Who grants the judge authority? What evidence can it see? Can its decision be appealed? Who notices when the judge fails? The engineering term identifies a control boundary; the literary vocabulary keeps the governance problem visible.

## Separation without theatre

Naming a judge layer does not make a system safe. A judge can share the worker's blind spots, approve by habit, or optimise for the same misleading reward. A human confirmation dialog can also become theatre when every prompt receives an automatic click.

The useful design question is concrete: **what proposed action crosses this boundary, what evidence is inspected, and what can prevent execution?** The answer should be observable in logs and tests.

For a small, low-risk workflow, one checking component may be enough. Higher-risk systems benefit from separating functions that demand different evidence or authority: policy validation, budget control, security review, human approval, and recovery. This is a design preference, not a universal rule that every verb requires its own agent.

The separation also matters after deployment. Monitoring, evaluation, reward, permissions, and remediation are related, but they should not collapse into one opaque score. See [Monitor–Reward Separation](/entries/monitor-reward-separation/) for the incentive problem.

## A checklist for builders

For each new worker capability, ask:

1. What consequential action can this capability produce?
2. Which checks run before execution?
3. Which decisions require a person?
4. What evidence is retained?
5. How can a mistaken approval be stopped or reversed?

If the answer to the second question is only *the prompt tells the worker to be careful*, the system has instructions, not a judge layer.

## Related entries

[Aunties](/entries/aunties/) · [Approval Gating](/entries/approval-gating/) · [Human Judgment Layer](/entries/human-judgment-layer/) · [Monitor–Reward Separation](/entries/monitor-reward-separation/) · [Provenance](/entries/provenance/) · [Verification Gap](/entries/verification-gap/) · [Jailbreak](/entries/jailbreak/)

## Source

Nate B. Jones, [*AI Agent Judge Layer: How to Control Agents in Production*](https://natesnewsletter.substack.com/p/agent-judge-layer-production-control), 11 May 2026.
