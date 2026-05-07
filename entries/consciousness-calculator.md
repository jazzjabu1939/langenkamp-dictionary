---
layout: default
title: "Consciousness Calculator"
permalink: /entries/consciousness-calculator/
summary: "a forthcoming Dictionary tool that lets a user enter the name of a \"free\" closed-tier AI service and returns an estimated value of the consciousness \u2014 attention, intent, downstream-choice influence \u2014 the user is trading for the service. Companion tool to the Sovereign Compute Calculator. The point is not the precise number but the visibility of the trade."
published: true
---

# Consciousness Calculator

*A forthcoming tool, sketched here as an entry so the concept can be cross-referenced from other Dictionary work and so the design can be argued before it is built.*

---

## In one sentence

**The *Consciousness Calculator* is a forthcoming tool that lets a user enter the name of a "free" closed-tier AI service \u2014 ChatGPT Free, Gemini Free, Meta AI, future ad-supported tiers \u2014 and returns an estimated value of the consciousness the user is trading for the service, on a per-hour, per-day, per-week, and per-month basis.**

## What it actually estimates

The tool does not pretend to measure consciousness in any philosophically rigorous sense. What it estimates is the *commercial value of the user's attention, intent, and downstream-choice influence* during the time the service is being used. The inputs are mundane:

- Hours per day spent in the service.
- Approximate sessions per week.
- Demographic and economic profile relevant to advertiser bidding (geography, age range, household income bracket, professional category).
- The advertising rates the service's most likely buyers are paying in adjacent attention markets (Google search ads, Meta ads, programmatic display).
- A multiplier for the service's *intent-shaping* premium: an AI assistant does not just observe intent the way a search engine does; it can shape what the user does next, and that shaping is worth more per impression than passive observation.

The output is a dollar figure: *this is what your consciousness is worth to the platform, per hour, per day, per week, per month.* The figure is approximate. It is also almost always larger than the cost of the paid plan that would buy the user out of the trade.

## Why the visibility matters more than the precision

The point of the tool is not to produce an exact number. The point is to make the trade *visible*. Most users on free-tier AI services do not consciously think of themselves as having sold anything. The trade was implicit at the moment of signup and has remained invisible since. The Consciousness Calculator is an attempt to do for AI what the early online-privacy-cost calculators did for browsing data: make the cost legible enough that the user can decide whether the trade is one they would, on reflection, choose.

Most users, presented with a credible estimate that their free-tier AI use is "costing" them more in sold attention than the $20-a-month paid plan would cost in cash, will discover that they had been making a poor trade by default. Some will switch to Plan A (honest rental). A smaller number will go further \u2014 to the [Sovereign Compute](sovereign-compute.md) architecture in which they are no longer in the merchandise category at all.

The tool is sister to the [Sovereign Compute Calculator](sovereign-compute-calculator.md), which estimates the *cash* breakeven against rented inference for an individual operator considering local-first architecture. Together, the two calculators are the Dictionary's attempt to give the operator the two numbers that matter most: *what is the closed tier costing me in attention*, and *what would the open tier cost me in cash*. The honest comparison is between those two figures.

## Status

Not yet built. The conceptual design is captured here so that future Dictionary entries can reference it as a real artifact-in-progress rather than a vague intention. When the tool exists, it will live at `/tools/consciousness-calculator/` with this entry as its conceptual companion.

## See also

- [Sovereign Compute](sovereign-compute.md) \u2014 the entry this calculator is designed to make legible at the point of decision
- [Sovereign Compute Calculator](sovereign-compute-calculator.md) \u2014 the cash-side companion tool
- [Mediation (a la Gibson)](mediation-a-la-gibson.md) \u2014 the philosophical frame for why making the mediation visible is the work
- [Inverted Funnel](inverted-funnel.md) and [Commercial Legibility](commercial-legibility.md) \u2014 the demand-side architecture in which "free" services compete for the user's intent
