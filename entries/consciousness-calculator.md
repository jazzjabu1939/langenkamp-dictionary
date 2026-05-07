---
layout: default
title: "Consciousness Calculator"
permalink: /entries/consciousness-calculator/
summary: "a Dictionary tool that lets a user enter the name of a \"free\" closed-tier AI service and returns an estimated value of the consciousness — attention, intent, downstream-choice influence — the user is trading for the service. Companion tool to the Sovereign Compute Calculator. The point is not the precise number but the visibility of the trade."
published: true
---

# Consciousness Calculator

<p style="margin: 1.5rem 0; padding: 0.9rem 1.2rem; background: #f7f4ef; border-left: 3px solid #6b5b95; font-size: 1.05rem;">
→ <strong><a href="/tools/consciousness-calculator/">Use the Consciousness Calculator</a></strong> &middot; the live tool, free, open-access, runs in your browser, no tracking.
</p>

## In one sentence

**The *Consciousness Calculator* is a Dictionary tool that lets a user enter the name of a "free" closed-tier AI service — ChatGPT Free, Gemini Free, Meta AI, future ad-supported tiers — and returns an estimated value of the consciousness the user is trading for the service, on a per-hour, per-day, per-week, and per-month basis.**

## How much are your thoughts worth?

If I were to say *a nickel for your thoughts*, would that be enough? Probably not, but the question is the right one. The closed-tier "free" plan is selling something that has a price; the question is what that price actually is, and whether the price is being honestly named.

Consider two ads. Suppose, while you are querying ChatGPT about the oil-change procedure on a Chevy Silverado 2500HD, the platform places an advertisement for an oil filter from AutoZone next to the answer. You might think, *hmm, I don't usually go to AutoZone, but okay.* The ad is annoying. It is also forgettable. It does not follow you out of the conversation. The Silverado is in the driveway, the oil change is on the to-do list, the ad is information — mildly intrusive, commercially priced, structurally fine.

Now suppose, instead, that while you are chatting with ChatGPT about wishing you had a date on a Friday night, the platform places an advertisement for an anti-depressant medication via an online pharmacy next to the response. You might feel differently about that. The ad has not just observed your intent; it has read your loneliness, judged it as a sales opportunity, and delivered a chemical answer to a human question. It does not stay in the conversation. It lingers. It changes how you feel about your own situation, and possibly about your own mind.

Does the AutoZone oil-filter ad generate the same revenue for OpenAI as the online-pharmacy ad? And are they priced correctly? The oil filter can be forgotten in five minutes. The pharmacy ad takes a piece of you with it.

*That* is what the Consciousness Calculator is trying to make visible. Not just *attention rented from you* but *consciousness sold from you*. The economics of the mind, at the resolution where the mind actually lives — where loneliness is read as a market signal, where vulnerability is priced, where what you were thinking about a moment ago becomes what you are being sold to about right now.

We have tried to model this in the most approximate way — not to *get it right*, but to *illustrate the economics of the mind*. The point is not the precise number. The point is that there *is* a number. Selling your thoughts costs how much, exactly? The calculator does not pretend to give the final answer. It gives an answer-shaped object you can hold up against the $20-a-month subscription that would buy you out of the trade entirely, and you can look at the two figures and decide what kind of relationship you want to have with the assistant you are talking to.

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

Most users, presented with a credible estimate that their free-tier AI use is "costing" them more in sold attention than the $20-a-month paid plan would cost in cash, will discover that they had been making a poor trade by default. Some will switch to Plan A (honest rental). A smaller number will go further — to the [Sovereign Compute](sovereign-compute.md) architecture in which they are no longer in the merchandise category at all.

The tool is sister to the [Sovereign Compute Calculator](sovereign-compute-calculator.md), which estimates the *cash* breakeven against rented inference for an individual operator considering local-first architecture. Together, the two calculators are the Dictionary's attempt to give the operator the two numbers that matter most: *what is the closed tier costing me in attention*, and *what would the open tier cost me in cash*. The honest comparison is between those two figures.

## Status

**Live as of May 7, 2026.** The first version of the calculator is published at [/tools/consciousness-calculator/](/tools/consciousness-calculator/). It runs entirely in the browser, holds no state on any server, and has no analytics, no telemetry, and no outbound network requests after page load. The numbers it produces are illustrative, not precise; the point of the tool is not the exact figure but the visibility of the trade. The "How we computed this" section at the bottom of the tool shows the formulas and assumptions in full. The tool will be revised as the field evolves; the entry on this page is the conceptual companion that explains *why* it exists. Suggestions, corrections, and pull requests via the [Dictionary GitHub repo](https://github.com/jazzjabu1939/langenkamp-dictionary) are welcome.

## See also

- [Sovereign Compute](sovereign-compute.md) — the entry this calculator is designed to make legible at the point of decision
- [Sovereign Compute Calculator](sovereign-compute-calculator.md) — the cash-side companion tool
- [Mediation (a la Gibson)](mediation-a-la-gibson.md) — the philosophical frame for why making the mediation visible is the work
- [Inverted Funnel](inverted-funnel.md) and [Commercial Legibility](commercial-legibility.md) — the demand-side architecture in which "free" services compete for the user's intent
