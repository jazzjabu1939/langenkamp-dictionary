---
layout: default
kind: reference
title: "Aunties"
permalink: /entries/aunties/
date: 2026-05-02
summary: "specialized, single-verb oversight agents that prevent any one component from accumulating unchecked authority. Named after Gibson's Jackpot trilogy."
draft: false
published: true
---

# Aunties

---

## In one sentence

**Aunties are specialized, single-purpose oversight agents — each with exactly one job — that sit around a more capable worker-agent to authenticate, monitor, approve, or intervene, so that no single component accumulates unchecked authority.**

## Where the name comes from

The concept comes from William Gibson's Jackpot trilogy — *The Peripheral* (2014), *Agency* (2020), and the unfinished third volume. In Gibson's near-future and far-future settings, Lowbeer — a detective working for a shadowy enforcement body — operates with the assistance of AI systems she calls "Aunties." Her name for them is a pet name: intimate, not condescending. They are not her equals, but they are not her tools either. They are figures of quiet, persistent authority who sit in the background of her work and do things she needs done without requiring her to manage them directly.

In the novels, the Aunties are contextual (bound to their time-fork; new branches may need new Aunties), semi-sentient by design (powerful but deliberately not autonomous), and *friction by design* — Netherton, who interacts with them indirectly, finds them slightly unpleasant. That is the point. An oversight agent that everyone finds perfectly pleasant is probably not doing its job.

## The architectural insight

Gibson's Aunties, extracted from fiction, become an architectural pattern:

**The function of oversight, in a multi-agent system, should be decomposed into named, specialized, single-verb components — not concentrated in a single all-powerful guardian.**

The alternative — one big supervisor watching everything — is itself an unaccountable concentration of power. The Aunties pattern avoids it by making each oversight function a separate, named entity with a clearly bounded job.

The verb test is the core discipline: each Auntie has *one verb*. Assign a function to an Auntie only if it passes the test.

## The current roster and their verbs

| Auntie | Verb | What it does |
|--------|------|--------------|
| **Gate** | *authenticate, classify, scope* | Checks identity, determines what a session or requester is allowed to do, assigns scope at entry |
| **Tool** | *permit, restrict, allowlist* | Governs which tools a worker can call; enforces per-context tool policies |
| **Memory** | *store, retrieve, validate, quarantine* | Manages what the worker writes to persistent storage; validates incoming data; quarantines suspect content |
| **Approval** | *estimate, gate, require approval* | Estimates cost and risk before an action; triggers human approval for actions above a threshold |
| **Watch** | *observe, log, alert, detect anomalies* | Observes the system continuously; writes logs; fires alerts when thresholds are crossed; never intervenes directly |
| **Provenance** | *sign, attribute, record provenance* | Tags every significant output with who produced it, when, and why; makes the audit trail possible |
| **Recovery** | *stop, rollback, kill, restore* | The enforcer; terminates runaway sessions, kills degrading iteration loops, rolls back bad state |

A worked example of how they compose: suppose you want to control costs. You do not assign cost control to a single "Cost Auntie." You decompose it:

- **Watch Auntie** *sees* daily spend, alerts when it crosses a threshold (observe-only)
- **Approval Auntie** *estimates* cost before each action, gates expensive calls at tier boundaries
- **Recovery Auntie** *enforces* hard caps when spending has already exceeded them, kills the runaway session

Three Aunties, three verbs, no overlap. The anti-pattern is any one of those absorbing another's verb. The moment Watch starts enforcing, or Approval starts killing, the household has collapsed back into one all-powerful agent under a different name.

## The versioning rule

An Auntie graduates from `v0` to `v1` only when it is **named, monitored, and externally observable**. A function that exists only in code with no name, no logging, and no external visibility is not yet an Auntie — it is an aspiration. The version number is not a marketing claim; it is an accountability contract.

## Working example from this machine

As of May 2026, one Auntie is live: **Watch Auntie v0.5**.

It runs as two cron jobs — one at 7:00 AM EDT, one at 7:00 PM EDT — that execute a security audit, format the output to distinguish new findings from baseline, and deliver the report to a private Telegram group. It observes only; it does not intervene.

Version 0.5 rather than 1.0, because it is not yet monitored by another layer — there is no Auntie watching Watch Auntie. Version 1.0 requires external observability in both directions.

The remaining Aunties (Gate, Tool, Memory, Approval, Provenance, Recovery) are designed but not yet implemented. The registry lives in `security/AUNTIES_REGISTRY.md`.

## Why this matters in a teaching context

The Aunties pattern is, at bottom, an organizational design problem wearing technical clothes. The architectural question — *how do you prevent any single component from accumulating unchecked authority?* — is the same question that produced the separation of powers in constitutional government, the audit-and-compliance function in large corporations, and the checks-and-balances structure in family governance.

For a BBA or MBA classroom, the productive framing is this: every organization eventually faces the question of what to do when a capable actor — a person, a team, or a system — becomes inconvenient to supervise. The Aunties pattern answers by decomposing oversight, distributing it across named entities with bounded scopes, and making each entity externally observable.

Useful classroom questions:
- Which Auntie is missing in most organizations, and why?
- What happens when Approval absorbs Recovery? (You get a body that both sets the rules and enforces them — a common corporate governance failure mode.)
- Is the "one verb" principle achievable in human organizations, or only in code?

## A note on the name

One reason to keep Gibson's name rather than choosing a more technical one: the slightly whimsical, slightly unnerving quality of "Auntie" does useful work. The Aunties are not neutral infrastructure. They are authority-bearing, persistent, slightly formidable — the way a good aunt can be. The technical name would flatten that. The literary name carries the right emotional payload.

## Trade-offs

- **Friction is the product.** An Auntie that never inconveniences anything is probably not watching carefully enough. Expect the Aunties to generate friction; build for it rather than optimizing it away.
- **The verb test requires discipline.** Scope creep is natural. Every Auntie will eventually be proposed as the right place to add one more function. The test ("what is this Auntie's one verb?") is the only guard against it.
- **Capability lag is structural.** The Aunties' ability to supervise a worker lags behind the worker's frontier capability by default — the more capable the worker, the harder the Aunties' job. Auntie capability must be deliberately scaled with worker capability, not left to catch up.
- **New contexts need new Aunties.** An Auntie bound to one context (one time-fork, in Gibson; one deployment environment, in practice) may not reach across to a new one. Audit the Auntie coverage whenever a new context is added.
- **The Principal-of-Principals remains human.** The Aunties execute; they do not make constitutional decisions. Commissioning a new Auntie, retiring the worker, terminating an actor entirely — these authorities belong to the human at the top of the structure, not to any Auntie.

---

*Related entries: `gateway.md`, `sub-agent.md`, `heartbeat.md`, `branches.md` *(planned)*, `approval-gating.md` *(planned)*.*
