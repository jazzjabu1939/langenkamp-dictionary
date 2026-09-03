---
layout: default
kind: reference
title: "Sovereign Compute Calculator"
permalink: /entries/sovereign-compute-calculator/
summary: "a forthcoming Dictionary tool that estimates an individual operator's personal cash breakeven between rented closed-tier inference and home Sovereign Compute. Sister tool to the Consciousness Calculator. The point is to replace generic punditry about \"who needs a local model\" with a personal answer the user can actually act on."
published: true
---

# Sovereign Compute Calculator

*A forthcoming tool, sketched here as an entry so the concept can be referenced and the design argued before it is built. Companion to the [Consciousness Calculator](consciousness-calculator.md).*

---

## In one sentence

**The *Sovereign Compute Calculator* is a forthcoming tool that lets an individual operator plug in their actual subscription costs, expected workload, hardware-amortisation assumptions, and electricity rates, and returns a personal estimate of the cash breakeven point between continuing on the closed-tier rental escalator and migrating to home Sovereign Compute.**

## What it actually computes

The tool runs a simple, transparent comparison and shows the work. Inputs:

- Current monthly closed-tier spending (subscription tier, API token spend, both).
- Expected trajectory of that spending over the next three years, given the [Plan A escalator](sovereign-compute.md#the-market-has-split-the-split-is-structural-and-philosophical) and the user's rate of usage growth.
- Approximate workload class (light reading and writing assistance / serious project work / agentic loops / long-context analysis / sustained generation).
- Hardware option being considered (an existing [Dusty Laptop](dusty-laptop.md), a mid-range Mac, an M-series MacBook Pro at various memory configurations, a desktop with a recent NVIDIA card).
- Local electricity rate, typical hours-on per day, and expected useful life of the hardware.
- Optional: expected resale value of the hardware at end of useful life.

Outputs:

- A monthly cost-of-rental projection, escalator built in.
- A monthly amortised-plus-electricity cost-of-sovereignty projection.
- The crossover month — the month, if any, at which sovereign compute becomes cheaper in cash terms than rental.
- A non-cash sovereignty score that names what the user is buying with whatever cash difference exists, drawing on the arguments named in *The operator is not the product*, [FERPA Compliance Posture](ferpa-compliance-posture.md), and [GenXClaw](genxclaw.md).

## Why personal is the whole point

The Dictionary's standing position is that *most discussion of "who needs local AI" is performed at a level of abstraction that is useless to the individual operator.* Pundits make sweeping claims about whether "most people" need sovereign compute, with no reference to which people, doing what work, on which hardware, paying which electricity rates, growing their usage at which rate. The Sovereign Compute Calculator is an attempt to refuse that abstraction. The user's answer should be their answer, computed on their numbers, with the assumptions visible and editable.

The tool is also designed to handle the *escalator* honestly. The conventional analysis compares today's $20 subscription to the cost of buying hardware. That comparison flatters the closed tier because it treats the $20 as static when in fact it is one rung on a long upward ladder. The calculator builds the ladder in: $20 today, $25 next year, $30 the year after, whatever the user's plan is doing on its actual trajectory. Many users who currently look like "the closed tier is obviously cheaper" actually look, on a three-year escalator-aware horizon, like "the crossover is closer than the consultant said it was."

The output is paired with the [Consciousness Calculator](consciousness-calculator.md) for users who are weighing the free-tier option. The honest comparison is between *what the closed tier costs me in cash*, *what the closed tier costs me in attention*, and *what the open tier would cost me to operate.* The two calculators are designed to put those three figures in the same window.

## Status

Not yet built. The conceptual design is captured here so the [Sovereign Compute](sovereign-compute.md) entry can reference it as a real artifact-in-progress rather than a vague intention. When the tool exists, it will live at `/tools/sovereign-compute-calculator/` with this entry as its conceptual companion.

## See also

- [Sovereign Compute](sovereign-compute.md) — the entry this tool is designed to make actionable
- [Consciousness Calculator](consciousness-calculator.md) — the attention-side companion tool
- [Dusty Laptop](dusty-laptop.md) — the cheapest hardware input the calculator will model
- [Opus Addict](opus-addict.md) — a common reason an operator's actual closed-tier spending is higher than the $20-tier baseline most analyses assume
- [GenXClaw](genxclaw.md) and [FERPA Compliance Posture](ferpa-compliance-posture.md) — the non-cash justifications that the calculator surfaces alongside the cash answer
