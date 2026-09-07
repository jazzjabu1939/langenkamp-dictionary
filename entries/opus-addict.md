---
layout: default
kind: reference
title: "Opus Addict"
permalink: /entries/opus-addict/
summary: "the operator who has come to depend on a single frontier closed-tier model to the point where its absence is felt as deprivation rather than inconvenience. Named for Anthropic's Claude Opus line, but the condition is general: a real form of cognitive dependency on a tool that is not, and cannot be, owned. The tension Sovereign Compute is one attempted answer to."
published: true
date: 2026-05-07
first_published: 2026-05-07
last_revised: 2026-09-06
---

# Opus Addict

## In one sentence

**An *Opus Addict* is an operator who has come to rely on a single frontier closed-tier model — typically Anthropic's Claude Opus, but the term generalises — to the point where the model's absence is experienced as cognitive deprivation rather than as routine inconvenience.**

## What the dependency actually feels like

The pattern is recognisable to anyone who has it. The operator opens a new conversation, types a question of the kind they have been working on for months, and receives a response that is *almost* what they wanted but in a slightly thinner register. They notice the thinness. They check the model selector. They have, by accident, been routed to a smaller or earlier model. They switch back. The relief is small, fast, and slightly embarrassing.

Repeat that experience often enough, and the operator discovers that they have built a working relationship with a specific model rather than with "AI" in the abstract. The smaller model is not bad. The smaller model would have been astonishing in 2023. But the operator's standards have moved, and the standards moved because the frontier model was always there. The smaller model now reads as *insufficient*, the way a familiar restaurant's off-night reads as insufficient: it is fine, but it is not what was promised.

That displacement of standards is the addiction. The operator did not choose it. It happened by exposure.

## Why this matters

It matters because dependency creates leverage whether or not the supplier intended it. A lab can reprice, reposition, deprecate, or condition access to a hosted model. An operator whose workflow assumes that model then bears the migration cost. The vendor's knowledge of individual dependence and its pricing motives are not visible from outside; the exposure exists without either claim.

The Opus Addict's freedom of action is structurally limited. The freedom can be reclaimed, but it costs. The cost is some combination of paying for hardware and electricity to run a sovereign substitute (see [Sovereign Compute](/entries/sovereign-compute/)), accepting a capability gap during migration, routing across models, or staying on the closed tier with eyes open about the position.

## Why the addiction is rational, and why that makes it worse

There is a flippant way to describe the dependency—*I am hooked on Opus*—and a more precise one: **for this operator, the attachment is doing load-bearing prose work that the cheaper alternatives tested so far have not matched.** That is an operator report, not a universal model ranking or an account of the lab's pricing intent.

The Sequoia Ascent 2026 talk gave the framework a sharper edge. Capability spike, in Karpathy's compact formula, is roughly *verifiability × training attention × data coverage × economic value*.[^1] Coding, math, and benchmark tasks improve fast because they are *resettable, repeatable, and rewardable*: a test passes or fails, and the model can practice. Prose does not work that way. There is no unit test for whether a paragraph is alive. Taste is not verifiable. And it is precisely in the unverifiable, taste-driven register — what Ethan Mollick has been pointing at for over a year when he writes about aesthetics, voice, and the difference between a competent draft and one a reader will actually finish[^2] — that the frontier closed-tier model wins most decisively, and where the gap to open weights is widest.

This matters for an operator whose product *is* prose. Coding often supplies executable tests; prose supplies fewer decisive external checks. A Dictionary entry meant to be read in an armchair with a cup of coffee can fail through *flatness*, and flatness may be visible only when the reader closes the tab. Depending on the best tool one has actually tested can therefore be rational. It is what the watchmaker's preference for a good escapement is. The escapement is the watch.

Which is also why the flippant framing conceals the risk. Taste-driven, prose-heavy work is difficult to verify and benchmark. This operator has found a material gap between a preferred hosted model and the local models available on his machine. The size and durability of that gap are empirical questions, not properties that can be inferred from parameter count or training folklore.

The discipline that follows is not abstinence. It is *triage*. Reach for the frontier model where taste is the product — Dictionary openers, the *zhengming* prose, the warming-pass anecdotes, the careful philosophical entries — and demote everything else. Sub-agent triage runs, tool orchestration, invoice OCR, transcript ingestion, the structural body of an entry once the operator-voice opener is set: all of these can, and should, run on a cheaper tier or on a local model, because their failure modes are verifiable and the gap closes fast in that region. The honest operator pays for the escapement and uses it where it counts.

## The hardware-class divide

There is a layer underneath this that an essayist from the *spasmodic court jester* school—Alex Fin, prophetic in his way—saw early.[^3] Access to capable models, paid subscriptions, hardware, and the knowledge required to use them is uneven. It is plausible that repeated access advantages will compound through university. How large that effect will be, and whether it exceeds earlier digital divides, remain predictions rather than measured facts.

The author's analogy comes from arriving at George Washington University in 1986 with a Macintosh on the desk, then watching a minority tool become ordinary. The proposed repetition is worth watching: an early-adopter cohort may arrive with sovereign agents or established cloud-agent workflows, and institutions may eventually treat that advantage as a normal baseline. The autumn 2026 class is the beginning of the test, not proof of the forecast.

The pedagogical implication is useful even before the forecast resolves. A faculty member should not assume equal access to paid models, modern hardware, or practiced agent workflows. Course design should make the expected capability floor explicit and decide what access the institution will guarantee.

[^1]: Andrej Karpathy, *Sequoia Ascent 2026 summary*, 30 April 2026, [karpathy.bearblog.dev/sequoia-ascent-2026/](https://karpathy.bearblog.dev/sequoia-ascent-2026/). Karpathy's framework is engineer-facing — it explains why coding agents got dramatically better in late 2025 and why "jagged intelligence" is the right description for what frontier models actually are. The Dictionary borrows the formula but applies it where Karpathy did not: to prose, where verifiability collapses and the moat widens.

[^2]: Ethan Mollick has been the most consistent public voice making the *aesthetics matters* argument for AI work since at least 2024. His distinction between a draft that is *competent* and one that has *taste* — the latter being what frontier models do meaningfully better than open weights — is the editorial premise the Dictionary is built on. We owe him the citation; we also owe him the acknowledgment that the gap he was naming early is the gap we have, two years later, organised our entire production stack around.

[^3]: Alex Fin's *hardware-class divide* argument — that access to high-end consumer compute would, within a few years, separate a *permanent* underclass from a *non-permanent* one — read in 2024 as the kind of overheated claim a court jester makes for clicks. By 2026 it reads as a load-bearing observation about how the frontier-model economy actually distributes its outputs. The court jester, sometimes, is the one who tells the truth the room is not ready to hear plainly. *The street finds its own uses for attachment.*

## What Sovereign Compute does about it

Sovereign Compute does not cure the addiction. The frontier closed-tier model is, today, materially more capable than the best openly available weights for many tasks, and an honest operator will admit that they still reach for the closed model when the work matters most. What Sovereign Compute does is *change the relationship*. The operator who runs a competent open-weight model on their own hardware has built a fallback that the lab cannot withdraw. They are still an Opus Addict. They are no longer an Opus Addict *without options*.

This is the underlying tension a substantial portion of the operator's recent hardware spending is trying to resolve. (See [Sovereign Compute](/entries/sovereign-compute/) footnote 2, where the unresolved-breakeven question is named directly.) The MacBook Pro with the M5 Max chipset and 128 GB of unified memory is, among other things, an attempt to walk the Opus Addict back from the edge of being structurally captive. Whether the math works on cash terms is an open question. Whether it works on *sovereignty* terms is a much easier one.

## See also

- [Sovereign Compute](/entries/sovereign-compute/) — one architectural answer to the dependency
- [GenXClaw](/entries/genxclaw/) — the temperamental case for owning the machine, which the Opus Addict is most likely to feel acutely
- [Mediation (a la Gibson)](/entries/mediation-a-la-gibson/) — the philosophical frame for why dependency on a mediating tool is the structural problem the Dictionary keeps returning to
