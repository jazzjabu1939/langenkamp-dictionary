---
layout: default
kind: reference
title: "Token Burn"
permalink: /entries/token-burn/
first_published: 2026-05-02
last_revised: 2026-09-07
summary: "The rate at which an AI workflow consumes model tokens, and therefore one driver of its operating cost."
published: true
---

# Token Burn

*An informal but increasingly load-bearing piece of vocabulary among practitioners running agentic AI in production.*

---

## In one sentence

**Token burn is the rate at which an AI workflow consumes model tokens; for metered services, it is one driver of cost rather than a complete cost measure.**

## In one slightly longer sentence

Token burn is the rate at which a configured-with-good-intentions agentic system silently transmutes electricity, attention, and credit-card balance into JSON, while the operator sleeps soundly believing the heartbeat-every-30-minutes was a thrifty design choice.

## Why this term exists

Many cloud model services charge separately for input and output tokens, sometimes with additional distinctions for cached input, tool use, or service tier. A heavily instrumented agent — frequent checks, parallel child tasks, repeated context, and verbose tool results — can therefore cost much more than a short chat.

The arithmetic is workload-specific but simple: frequency multiplied by tokens per run multiplied by the applicable price. A periodic job that repeatedly loads a large context can become expensive even when each individual run looks harmless. The useful practice is to measure the actual configuration rather than rely on a generic per-chat intuition.

The phrase **token burn** was the natural label. It rhymes spiritually with *cash burn* from the startup vocabulary, with the same connotation: a continuous expenditure that goes on whether you are watching it or not, and whose true rate you discover only by inspecting the receipts.

## A taxonomy of token-burn modes (informal)

Practitioner experience has produced an informal classification:

- **Slow burn.** The default state of a configured-but-undermonitored agent. Steady, low-grade consumption. Easy to live with for weeks before anyone notices.
- **Heartbeat burn.** Periodic checks compound when they run often or load too much context. Reduce their frequency, context, or model cost when the resulting service remains useful.
- **Sub-agent burn.** Parallel workers multiply calls. How much parent context each child receives depends on the runtime and configuration, so the cost should be measured rather than assumed.
- **Compaction burn.** When an agent's context fills up and the runtime calls a *compaction* model to summarize and shrink it, the compaction itself is a model call. On a chatty agent this is recurring overhead the operator usually forgets exists.
- **Loop burn.** The catastrophic mode. An agent enters a self-stimulating loop — calling a tool, reacting to its output, calling the tool again, reacting again — and burns its way through the operator's monthly budget before anyone wakes up. The phrase *"I went to bed with $300 of credit and woke up to a $2 budget alert"* belongs to this category.

## Working example from this machine

The OpenClaw Control dashboard on this MacBook reports cumulative cost in plain numbers. As of the morning of May 2, 2026, 30 million tokens have flowed through the gateway across 351 messages — a number perfectly explicable by the workload of a real lecturer running real classes through a real agent for real weeks, but a number whose existence is itself a small education in what production agentic AI actually costs.

The model-tiering plan filed the same morning is, structurally, a token-burn-management plan. The vocabulary moved from finance ("how much are we spending?") to ecology ("which fires are we letting burn, which are we putting out, and which are we converting to controlled cooking flames on the local hardware?"). The shift in metaphor is, itself, a small *zhengming* — see the [naming entry](/entries/naming/).

## Why this matters in a teaching context

For a BBA or MBA classroom, *token burn* is a useful entry point into a much older management concept dressed in fresh terminology: **the difference between the cost you intend to incur and the cost you are actually incurring.**

Accounting students learn variance analysis, and operations courses teach the difference between designed and observed processes. Token burn brings those ideas into a domain where the gap between intended and actual cost can emerge in billable seconds rather than months.

A useful classroom exercise: take a published agentic-system architecture diagram (most vendor decks have one) and ask students to estimate where the token burn lives. The answers reveal who has read about the technology and who has actually run it.

## How practitioners diagnose it

The standard moves, in order of how angry the practitioner has become:

1. **Look at the available usage records.** Provider billing, runtime telemetry, and local logs may each show a different part of the cost.
2. **Review heartbeat frequency.** Halve it. Watch the cost line. Halve it again if needed.
3. **Tier the models.** Frontier model for the work that needs it; smaller / cheaper / local model for everything else. (See [Ollama](/entries/ollama/), the [model-tiering pattern](/entries/naming/), and the practical phased-rollout approach.)
4. **Check for loops.** Look for any agent that calls a tool, reads the tool's output back into itself, and decides — based on that output — to call another tool. If the loop has no termination condition, it is a token-burn time bomb.
5. **Trim the context.** The same heartbeat that re-injects 100,000 tokens of workspace bootstrap every fire can be configured to inject only what it needs. The operational difference is dramatic.
6. **Set alerts or hard limits where available.** A warning reports the problem; a hard limit can stop further spend, though not every provider or plan offers the same controls.

## The seasoned practitioner's stages of grief

In rough order:

1. **Denial.** *"Surely this is just the trial period."*
2. **Anger.** *"Why is the heartbeat using Opus?"*
3. **Bargaining.** *"What if I run heartbeats only during business hours?"*
4. **Depression.** *"I built a system that pays a frontier model to ask itself if anything has happened in the last 30 minutes."*
5. **Acceptance.** *"Time to tier."*

Most practitioners reach acceptance within one billing cycle. The truly fortunate reach it before their first billing cycle, by reading articles like this one.

## Trade-offs

- **Aggressive cost cutting can break behaviour.** A heartbeat downgraded too far becomes useless. A sub-agent on too small a model misses the nuance the user needed. Token burn management is genuinely a trade-off curve, not a free optimization.
- **Local models change the math but do not eliminate it.** Local inference costs are *electricity, hardware depreciation, and your time*, not zero. The bills look smaller because you absorb them differently, not because they vanished.
- **Monitoring is the foundation.** Without good per-job, per-tier, per-day cost telemetry, every cost optimization is a guess. The dashboard exists for this reason. Look at it more often than feels necessary.

## Related and adjacent terms

- **Cash burn** (from startup finance) — the mother metaphor.
- **Compute burn** (general, predates LLMs) — the same shape applied to GPU hours, container minutes, or any metered cloud resource.
- **Context burn** (less common) — specifically the cost of repeatedly re-loading large context windows.
- **Wallet burn** (humorous, internal) — what spouses of heavy practitioners call the same phenomenon, with no further taxonomy needed.

---

*Related entries: [Training Compute Myth](/entries/training-compute-myth/), [Heartbeat](/entries/heartbeat/), [Sub-agent](/entries/sub-agent/), [Ollama](/entries/ollama/), and [Model Tiering](/entries/model-tiering/).*

*Filed in the spirit in which most working terminology is filed: from the position of someone who learned the term the expensive way.*
