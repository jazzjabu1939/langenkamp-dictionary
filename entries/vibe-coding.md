---
layout: default
kind: reference
title: "Vibe Coding"
permalink: /entries/vibe-coding/
summary: "AI-assisted software development by conversational drift: fast, playful, often productive, and dangerous when the artifact outruns the operator's understanding."
published: true
---

# Vibe Coding

---

## In one sentence

**Vibe Coding is software development by conversational drift: describe what you want, accept what the model gives back, run it, patch the obvious breakage, and keep moving by feel.**

## Why the phrase worked

Andrej Karpathy coined the phrase in early 2025, and it spread because it was funny, self-indicting, and true. It named a thing programmers were already doing but did not yet have a socially acceptable way to describe.

The user is not quite programming in the old sense. The model is not quite programming in the accountable sense. The work happens in the space between: prompt, output, run, error, paste, shrug, try again, ship the demo before the coffee gets cold.

That is why the word **vibe** is doing real work. It does not flatter the operator. It admits the person is moving by feel rather than by complete comprehension. The code may work. The operator may not know why. This is both the charm and the danger.

Vibe coding is not fake productivity. That would be too easy a dismissal. It can produce useful prototypes, scripts, dashboards, experiments, and one-off tools at a speed that would have seemed indecent a few years earlier. It lowers the activation energy for building. It lets people who are not professional programmers express intent in software-shaped form. It lets professional programmers explore faster than they can type.

The problem is not that vibe coding produces nothing. The problem is that it produces something plausible faster than judgment catches up.

## The artifact outruns the operator

The central risk is not ugliness. It is misplaced confidence.

With vibe coding, the artifact arrives before the operator has earned the artifact. A working interface appears. A script completes. A test passes, or appears to pass. A dependency installs. A database writes. A permission boundary is crossed. The demo looks alive.

But the operator may not know the failure modes. Where are the secrets stored? What happens on malformed input? Which files can this script delete? Is the generated authentication logic real or theatre? Did the model silently remove the constraint that mattered? Did the test confirm behavior, or merely confirm that the happy path still smiles?

This is where vibe coding becomes a cousin of the AI Produced Artifact. The output may be useful, but it is not self-authenticating evidence of competence. A produced app does not prove the operator understands the app any more than a polished AI-assisted memo proves the student understands the recommendation.

The visible thing has become cheaper than the invisible judgment behind it.

## The honest amateur mode

There is a humane version of vibe coding. It is the amateur mode, and the word amateur should be taken in its older sense: someone who does the work out of love, curiosity, or immediate need.

A historian builds a small archive tool. A professor makes a grading helper. A parent creates a script to organize photographs. A student prototypes a club website. A farmer builds a price tracker for equipment auctions. None of these people needs to cosplay as a senior software engineer. They need a small tool, a tolerance for rough edges, and enough humility not to trust the output beyond its verified use.

In that setting, vibe coding is delightful. It gives ordinary people a way to make software-shaped things without first passing through the old gatekeeping rituals. The Dictionary should not sneer at that. Much of useful computing has always come from people using tools in ways the professionals did not anticipate.

The boundary appears when the artifact becomes consequential.

If the code handles money, grades, private data, safety, security, compliance, institutional records, or other people's time, vibe coding is no longer enough. The operator may still use AI. Of course the operator may use AI. But the posture has to change.

The work has to become engineering.

## Karpathy's correction

Karpathy's later move toward **[Agentic Engineering](agentic-engineering.md)** matters because it is a public self-correction. He did not merely add a new phrase to the pile. He named the next step: the same broad activity, but done with professional responsibility rather than consumer-mode drift.

Vibe coding is the phase where the human treats the model as a magical code fountain. Agentic engineering is the phase where the human designs the workflow, constrains the agent, reviews the diff, tests the behavior, understands the failure modes, and owns the result.

The difference is not whether AI writes code. In both cases, AI may write much of the code. The difference is whether the human has remained accountable for the architecture.

That distinction is why both terms belong in the Dictionary. Vibe coding names the intoxicating discovery. Agentic engineering names the discipline required after the intoxication wears off.

## The local test

The useful test is simple:

Can you explain what the code does?

Can you explain where it can fail?

Can you explain why the test proves what you think it proves?

Can you safely modify it tomorrow without asking the model to rediscover the whole system from scratch?

Can someone else maintain it after you?

If the answer is no, you may still have made something useful. But you have not engineered it yet.

That is not a moral failure. It is a category distinction. Vibe coding is a way to get something moving. Engineering is what begins when other people, future-you, money, records, security, or trust have to depend on it.

## See also

*AI Writing*, *AI Produced Artifact*, *Artifact Is Not Competence*, *Coding Solved*, *Claude Code*, *Capability Overhang*, *Sovereign Compute*, *OpenClaw*, *Red Pill*, *[Agentic Engineering](agentic-engineering.md)*.

## Source

Andrej Karpathy's original public coinage of "vibe coding" in early 2025; Karpathy's later X post naming "agentic engineering" as his current preferred term; and the Sequoia Capital conversation with Stephanie Zhan, "Andrej Karpathy: From Vibe Coding to Agentic Engineering," AI Ascent 2026.

- Karpathy X post on agentic engineering: <https://x.com/karpathy/status/2019137879310836075>
- Sequoia Capital / YouTube, "Andrej Karpathy: From Vibe Coding to Agentic Engineering w/ Stephanie Zhan": <https://www.youtube.com/watch?v=96jN2OCOfLs>
