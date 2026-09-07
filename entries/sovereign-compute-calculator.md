---
layout: default
kind: reference
title: "Sovereign Compute Calculator"
permalink: /entries/sovereign-compute-calculator/
date: 2026-05-07
first_published: 2026-05-07
last_revised: 2026-09-07
summary: "A proposed Dictionary tool for comparing the cash costs of rented inference and home-controlled compute under explicit assumptions."
published: true
---

# Sovereign Compute Calculator

*A forthcoming tool, sketched here as an entry so the concept can be referenced and the design argued before it is built. Companion to the [Consciousness Calculator](/entries/consciousness-calculator/).*

---

## In one sentence

**The *Sovereign Compute Calculator* is a proposed tool for comparing rented inference with home-controlled compute using an operator's subscription costs, workload, hardware-amortisation assumptions, and electricity rates.** It would estimate a cash breakeven point when the inputs support one and show which assumptions drive the result.

## What it actually computes

The tool runs a simple, transparent comparison and shows the work. Inputs:

- Current monthly closed-tier spending (subscription tier, API token spend, both).
- Alternative three-year spending scenarios chosen by the user rather than one assumed subscription-price escalator.
- Approximate workload class (light reading and writing assistance / serious project work / agentic loops / long-context analysis / sustained generation).
- Hardware option being considered (an existing [Dusty Laptop](/entries/dusty-laptop/), a mid-range Mac, an M-series MacBook Pro at various memory configurations, a desktop with a recent NVIDIA card).
- Local electricity rate, typical hours-on per day, and expected useful life of the hardware.
- Optional: expected resale value of the hardware at end of useful life.

Outputs:

- A monthly cost-of-rental projection under the selected scenarios.
- A monthly amortised-plus-electricity cost-of-sovereignty projection.
- The crossover month — the month, if any, at which sovereign compute becomes cheaper in cash terms than rental.
- A separate qualitative checklist for control, portability, privacy, and continuity. It should not collapse unlike values into a spurious single score.

## Why personal is the whole point

The Dictionary's standing position is that *most discussion of "who needs local AI" is performed at a level of abstraction that is useless to the individual operator.* Pundits make sweeping claims about whether "most people" need sovereign compute, with no reference to which people, doing what work, on which hardware, paying which electricity rates, growing their usage at which rate. The Sovereign Compute Calculator is an attempt to refuse that abstraction. The user's answer should be their answer, computed on their numbers, with the assumptions visible and editable.

The tool is also designed to handle changing prices honestly. A comparison between today's subscription and a multi-year hardware purchase can mislead if it holds every price and workload constant. The calculator should show flat, rising, and user-defined scenarios without presenting any one of them as a forecast. For some users, rising usage will bring the crossover closer. For others, low utilisation, maintenance, and the value of continuing model upgrades will keep rental cheaper.

The output is paired with the [Consciousness Calculator](/entries/consciousness-calculator/) for users who are weighing the free-tier option. The honest comparison is between *what the closed tier costs me in cash*, *what the closed tier costs me in attention*, and *what the open tier would cost me to operate.* The two calculators are designed to put those three figures in the same window.

## Status

Not yet built. The conceptual design is captured here so the [Sovereign Compute](/entries/sovereign-compute/) entry can reference it as a real artifact-in-progress rather than a vague intention. When the tool exists, it will live at `/tools/sovereign-compute-calculator/` with this entry as its conceptual companion.

## See also

- [Sovereign Compute](/entries/sovereign-compute/) — the entry this tool is designed to make actionable
- [Consciousness Calculator](/entries/consciousness-calculator/) — the attention-side companion tool
- [Dusty Laptop](/entries/dusty-laptop/) — the cheapest hardware input the calculator will model
- [Opus Addict](/entries/opus-addict/) — a common reason an operator's actual closed-tier spending is higher than the $20-tier baseline most analyses assume
- [GenXClaw](/entries/genxclaw/) and [FERPA Compliance Posture](/entries/ferpa-compliance-posture/) — the non-cash justifications that the calculator surfaces alongside the cash answer
