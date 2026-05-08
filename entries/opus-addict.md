---
layout: default
title: "Opus Addict"
permalink: /entries/opus-addict/
summary: "the operator who has come to depend on a single frontier closed-tier model to the point where its absence is felt as deprivation rather than inconvenience. Named for Anthropic's Claude Opus line, but the condition is general: a real form of cognitive dependency on a tool that is not, and cannot be, owned. The tension Sovereign Compute is one attempted answer to."
published: true
---

# Opus Addict

## In one sentence

**An *Opus Addict* is an operator who has come to rely on a single frontier closed-tier model — typically Anthropic's Claude Opus, but the term generalises — to the point where the model's absence is experienced as cognitive deprivation rather than as routine inconvenience.**

## What the dependency actually feels like

The pattern is recognisable to anyone who has it. The operator opens a new conversation, types a question of the kind they have been working on for months, and receives a response that is *almost* what they wanted but in a slightly thinner register. They notice the thinness. They check the model selector. They have, by accident, been routed to a smaller or earlier model. They switch back. The relief is small, fast, and slightly embarrassing.

Repeat that experience often enough, and the operator discovers that they have built a working relationship with a specific model rather than with "AI" in the abstract. The smaller model is not bad. The smaller model would have been astonishing in 2023. But the operator's standards have moved, and the standards moved because the frontier model was always there. The smaller model now reads as *insufficient*, the way a familiar restaurant's off-night reads as insufficient: it is fine, but it is not what was promised.

That displacement of standards is the addiction. The operator did not choose it. It happened by exposure.

## Why this matters

It matters because the addiction is leverage. The lab that supplies the frontier model knows that some non-trivial fraction of its paying users have built workflows that assume frontier capability and will not survive its removal. The lab can therefore reprice, reposition, deprecate, or condition access on whatever terms it likes — the addicted user will, in the short run, pay. That is not a moral failure on the lab's part. It is the natural shape of a market in which one party has built dependencies the other party can walk away from.

The Opus Addict's freedom of action is structurally limited. The freedom can be reclaimed, but it costs. The cost is some combination of: paying for hardware and electricity to run a sovereign substitute (see [Sovereign Compute](sovereign-compute.md)); accepting a meaningful capability gap during the migration; building workflows that route across models rather than depending on one; or staying on the closed tier with eyes open about the position.

## Why the addiction is rational, and why that makes it worse

There is a flippant way to describe the dependency — *I am hooked on Opus* — and an honest way. The honest way is darker and lands the operator's point harder: **the attachment is doing load-bearing prose work that the cheaper alternatives cannot yet do, the lab knows this, and the price reflects it.**

The Sequoia Ascent 2026 talk gave the framework a sharper edge. Capability spike, in Karpathy's compact formula, is roughly *verifiability × training attention × data coverage × economic value*.[^1] Coding, math, and benchmark tasks improve fast because they are *resettable, repeatable, and rewardable*: a test passes or fails, and the model can practice. Prose does not work that way. There is no unit test for whether a paragraph is alive. Taste is not verifiable. And it is precisely in the unverifiable, taste-driven register — what Ethan Mollick has been pointing at for over a year when he writes about aesthetics, voice, and the difference between a competent draft and one a reader will actually finish[^2] — that the frontier closed-tier model wins most decisively, and where the gap to open weights is widest.

This matters for an operator whose product *is* prose. A coding agent can tolerate a 70%-as-good local model: the test suite catches what the model misses. A Dictionary entry that is meant to be read in an armchair with a cup of coffee cannot tolerate a 70%-as-good model, because the failure mode is not a bug — it is *flatness*, and flatness is invisible until the reader closes the tab. The dependency on the frontier model is therefore not a weakness of will. It is rational. It is what the watchmaker's preference for the good Swiss escapement is. The escapement is the watch.

Which is also why it is worse than the flippant framing admits. The lab did not stumble into a moat; it priced one. The unverifiable, taste-driven, prose-heavy register is the region where Anthropic has trained hardest, where reinforcement-learning-from-human-feedback has the most signal, and where the resulting capability is least transferable to a 30-billion-parameter open-weight model running on a laptop. The price of admission to the register is structurally protected. An operator who tries to walk away discovers, often unhappily, that there is no clean substitute at any price below the closed-tier subscription.

The discipline that follows is not abstinence. It is *triage*. Reach for the frontier model where taste is the product — Dictionary openers, the *zhengming* prose, the warming-pass anecdotes, the careful philosophical entries — and demote everything else. Sub-agent triage runs, tool orchestration, invoice OCR, transcript ingestion, the structural body of an entry once the operator-voice opener is set: all of these can, and should, run on a cheaper tier or on a local model, because their failure modes are verifiable and the gap closes fast in that region. The honest operator pays for the escapement and uses it where it counts.

## The hardware-class divide

There is a layer underneath this that an essayist from the *spasmodic court jester* school — Alex Fin, prophetic in his way — saw early.[^3] The Opus Addict is not an evenly distributed condition. It correlates with hardware. A student arriving at university in autumn 2026 with a Mac Studio in the dorm room and a paid Anthropic subscription is operating in a measurably different cognitive universe than a student arriving with a Chromebook and the free tier of whatever frontier chatbot has chosen, this quarter, to ration its best register to paying users. The gap is not subtle. It compounds. Over four years, it produces graduates whose capacity to *do work that involves taste* — writing, judgment, synthesis, the unverifiable middle of professional life — has diverged from their peers' to a degree that the older hardware divides (laptop versus no laptop, fast internet versus slow) never quite produced.

This is not a hypothetical. The author arrived at George Washington University in 1986 with a Macintosh on the desk, one of a small minority in the dormitory. Within four years that small minority had become routine. The pattern repeats: an early-adopter cohort arrives with a tool that confers a real, measurable capability advantage; the early advantage looks like privilege, then looks like normalcy, then becomes the floor that everyone is assumed to have. Expect the autumn 2026 incoming class to include a meaningful minority of students arriving with sovereign agents already running on their laptops, or cloud-based agents that have been doing work *for* them through high school. The gap with their peers — at the moment they walk into a freshman seminar — will not be small. By graduation it will be structural.

The pedagogical implication is uncomfortable but worth naming. A faculty member who teaches as if every student in the room has equal access to the frontier register is teaching a course that does not exist. The honest course design now has to assume a divided room, and to think hard about what *floor* of capability the institution is willing to guarantee. That is a different conversation from the one most universities are currently having. It is a conversation the Dictionary thinks is overdue.

[^1]: Andrej Karpathy, *Sequoia Ascent 2026 summary*, 30 April 2026, [karpathy.bearblog.dev/sequoia-ascent-2026/](https://karpathy.bearblog.dev/sequoia-ascent-2026/). Karpathy's framework is engineer-facing — it explains why coding agents got dramatically better in late 2025 and why "jagged intelligence" is the right description for what frontier models actually are. The Dictionary borrows the formula but applies it where Karpathy did not: to prose, where verifiability collapses and the moat widens.

[^2]: Ethan Mollick has been the most consistent public voice making the *aesthetics matters* argument for AI work since at least 2024. His distinction between a draft that is *competent* and one that has *taste* — the latter being what frontier models do meaningfully better than open weights — is the editorial premise the Dictionary is built on. We owe him the citation; we also owe him the acknowledgment that the gap he was naming early is the gap we have, two years later, organised our entire production stack around.

[^3]: Alex Fin's *hardware-class divide* argument — that access to high-end consumer compute would, within a few years, separate a *permanent* underclass from a *non-permanent* one — read in 2024 as the kind of overheated claim a court jester makes for clicks. By 2026 it reads as a load-bearing observation about how the frontier-model economy actually distributes its outputs. The court jester, sometimes, is the one who tells the truth the room is not ready to hear plainly. *The street finds its own uses for attachment.*

## What Sovereign Compute does about it

Sovereign Compute does not cure the addiction. The frontier closed-tier model is, today, materially more capable than the best openly available weights for many tasks, and an honest operator will admit that they still reach for the closed model when the work matters most. What Sovereign Compute does is *change the relationship*. The operator who runs a competent open-weight model on their own hardware has built a fallback that the lab cannot withdraw. They are still an Opus Addict. They are no longer an Opus Addict *without options*.

This is the underlying tension a substantial portion of the operator's recent hardware spending is trying to resolve. (See [Sovereign Compute](sovereign-compute.md) footnote 2, where the unresolved-breakeven question is named directly.) The MacBook Pro with the M5 Max chipset and 128 GB of unified memory is, among other things, an attempt to walk the Opus Addict back from the edge of being structurally captive. Whether the math works on cash terms is an open question. Whether it works on *sovereignty* terms is a much easier one.

## See also

- [Sovereign Compute](sovereign-compute.md) — one architectural answer to the dependency
- [GenXClaw](genxclaw.md) — the temperamental case for owning the machine, which the Opus Addict is most likely to feel acutely
- [Mediation (a la Gibson)](mediation-a-la-gibson.md) — the philosophical frame for why dependency on a mediating tool is the structural problem the Dictionary keeps returning to
