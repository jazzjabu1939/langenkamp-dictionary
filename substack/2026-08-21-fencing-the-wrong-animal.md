---
layout: default
title: "Fencing the Wrong Animal"
permalink: /essays/fencing-the-wrong-animal/
date: 2026-08-21
description: "What eighteen days of American AI controls and a Chinese open-weight release teach about restraint asymmetry, control surfaces, and strategy."
published: true
---

# Fencing the Wrong Animal

### For eighteen days this summer, the United States restricted access to its most capable AI models. A Chinese lab gave away a comparable model for free. What that episode teaches about strategy when your competitor won't accept your constraints.

*Originally published at [Freedom Tomato](https://freedomtomato.substack.com/p/fencing-the-wrong-animal) on August 21, 2026.*

---

I raise Boer goats in northwestern Connecticut. Meat goats, South African breed, stocky and agreeable and smarter than they look. The fence around them does two jobs at once. It keeps the goats in, and it keeps the bears and coyotes out.

Those sound like the same job. They are not. Keeping the goats in works because the goats are mine and trained — I know where they are, I decide when they move, and the fence is a boundary they respect because I built their whole world around it. Keeping the coyotes out is a different proposition entirely. The coyotes were never mine or trained. They didn't agree to anything. My fence is not a rule they follow; it is an obstacle they evaluate, and if it isn't good enough, they go under it.

Every fence I own is really two instruments wearing one coat. And the failure mode is always the same: I spend my attention on the part I control, because that is where my work shows. But if coyotes are out on a full moon, I blow a battered antique Danish fog horn that scares them away. And if that doesn't work, I get my .22.

Washington built a fence in June. It was very good just at keeping the goats in. But the coyotes, who knows?

---

## Eighteen days

On June 12, 2026, the U.S. Department of Commerce restricted global access to Anthropic's two most capable models, Claude Fable 5 and Mythos 5. The stated concern was cybersecurity. Advanced models have gotten good at finding software vulnerabilities — flaws in code that let an intruder in — and that skill is the definition of dual use. The same capability that lets your security team audit your own systems lets someone else map them. Anthropic suspended access to comply.

The next day, a Beijing company called Zhipu AI, which sells internationally as Z.ai, started rolling out a new model called GLM-5.2 to its coding subscribers. Three days after that, it published the model's *weights* — the actual trained parameters, the thing itself — under an MIT license. That means anyone, anywhere, can download it, run it on their own hardware, modify it, and remove whatever safety behavior was trained into it. Free. Permanently.

The U.S. controls were lifted on June 30. Access was restored July 1.

Eighteen days.

---

## What the evidence actually shows

The tempting headline is *China caught up*. That is not what happened, and the real story is more useful.

The security firm Semgrep added GLM-5.2 to its evaluation suite after noticing it mentioned on social media. On one specific class of vulnerability — a common web flaw where an application fails to check whether you're allowed to see the record you just requested — GLM-5.2 scored about 39% on the standard accuracy measure. Claude Code scored 32%. A separate evaluation from Graphistry put GLM-5.2 near Opus 4.8 on cybersecurity investigation tasks. Researchers estimated it was surfacing findings at roughly seventeen cents each.

Now the correction. That is one vulnerability class and one test suite. On general capability, GLM-5.2 trails American models clearly. The U.S. government's own technical assessment, published in July, put its overall cyber capability near Opus 4.6 — a model four months older — and behind both Opus 4.8 and GPT-5.5.

So: not parity. Something narrower, and for policy purposes, arguably worse than parity. An attacker doesn't need a model that is good at everything. It needs one that is good at the specific thing, runs on hardware it already owns, and is cheap enough to run a million times. The relevant question was never *how close is China to the frontier*. It was *how much of the dangerous capability is already outside the fence* — and the answer arrived four days after the fence went up.

---

## Two kinds of control

Here is the distinction most of the coverage missed, and it is the one your strategy intuition should latch onto.

Controlling an API is like controlling a subscription. The customer never possesses the product. You host it, they rent access, and you can cut them off this afternoon. Revocable, monitorable, enforceable. This is the instrument Washington used, and it is a real instrument.

Publishing weights is like distributing the machine itself. The recipient may not know exactly how it was built, but it possesses the working artifact and can alter how it behaves. Once it's out, there is no recall, no version deprecation, no terms of service. You cannot un-give it. Every safety property built into the model becomes optional the moment someone with a GPU decides to fine-tune it away.

These are not two settings on the same dial. An export-control regime designed for the first has almost no purchase on the second. We called this an export control, but it controlled only the American route. The capability it was meant to contain was already circulating worldwide, for free, through a firm that was never subject to American law. Confucius, asked what he would do first if handed a state to govern, said he would rectify the names — 正名 — because an organization that misdescribes what it is doing cannot tell whether it is working. The only party whose behavior actually changed in June was the American defender who had been paying for legitimate access.

---

## The strategy problem, in familiar terms

Strip the geopolitics and this is a collective action problem, or a tragedy of the commons problem, of the kind that might be part of a business strategy class.

A restraint only produces the benefit it promises if the parties who could undercut it don't. That is why cartels are unstable, why price discipline collapses, and why voluntary industry standards fail whenever one player calculates that defecting is cheap. The restraint is not wrong; it is simply *unenforceable against a party who never joined*. In international relations the same idea travels under the offense-defense balance — Robert Jervis's argument that a competitive system's stability depends on whether the prevailing technology favors attackers or defenders, and on whether you can even tell offensive tools from defensive ones.

With bug-finding AI, you cannot tell. There is no defensive-only version. The tool that audits your code is the tool that maps mine.

So restraint by one side, on a capability the other side is publishing for free, does not close the gap between attacker and defender. It widens it — and it widens it specifically among the people who would have used the capability defensively, because those are the only people the restriction actually reached.

You can fence your goats. You cannot fence the coyotes.

---

## The honest case for the fence

I want to give the other side its real argument, because my conclusion is going to get borrowed by people who want it to mean “deregulate,” and it doesn't.

Friction is not futility. Controls raise cost and slow diffusion even when they leak. Running open-weight models at scale still takes compute, and compute is a chokepoint the U.S. genuinely holds. One benchmark result on one vulnerability class is thin evidence on which to dismantle a governance instrument — and if you would not let a student draw a strategic conclusion from a single data point, don't do it yourself. We also cannot observe the counterfactual: we don't know what didn't happen in those eighteen days, or what precedent the willingness to act sets for a future capability with a much steeper misuse curve.

All fair. None of it touches the structural problem. Friction works when the frictional surface is the only route in. Here there were two routes, the state could only put friction on one, and the one it couldn't touch was the one that can never be undone.

---

## What restraint is actually for

This is where it stops being a policy question and becomes the question a business school should care about.

There are two reasons an organization can give, in its own voice, for holding back from something it could legally and practically do.

The first is that holding back works. You restrain yourself because it produces a better result. Call it the practical reason.

The second is that holding back is who you are. You restrain yourself because doing otherwise would make you a different kind of organization. Call it the character reason.

Think of a company that refuses to use sweatshop labor. It can say *this protects our brand,* or it can say *this is wrong.* Both sound fine in a good year. They come apart the moment a competitor does the thing and takes share. The practical reason evaporates. The character reason doesn't.

June was that moment for AI restraint. The practical reason for restricting those two models was that it would keep dangerous capability away from people who shouldn't have it. A free download four days later meant the restriction did not actually keep you safe. And if the practical reason is the only one you have, your safety commitment lasts exactly as long as you are the only one holding the capability — and not a day longer. That is a race. The honest move is to say so out loud.

Here is the part I think matters most: you have to know which reason survives when the other fails.

What you cannot do is claim the practical reason in public — *this keeps you safe* — and then quietly switch to the character reason — *this is who we are* — once someone checks the numbers and finds that it did not keep anyone safe. That switch is how an institution loses its credibility. I have watched it when the values in mission statements only hold in good years.

Say the true thing instead. This restriction bought less safety than we claimed. We may keep it anyway, for reasons that don't depend on the arithmetic. And in the meantime we should stop admiring the gate and go walk the whole line — because for open-weight capability, nobody has built a fence yet, and eighteen days in June is what it cost us to find out. Should we buy ammo for our rifles instead?

The coyotes did not agree to anything.

---

### Terms used here

**Open weights** — a model whose trained parameters are published, so anyone can download, run, and modify it. Not the same as open source; the training data and code usually stay private.

**Fine-tuning** — additional training on top of a released model, which can add capability or strip out safety behavior.

**Dual use** — a capability that can serve both beneficial and harmful purposes. In cybersecurity, the same underlying ability to find a flaw may help a defender patch it or an attacker exploit it.

**Capability diffusion** — frontier ability spreading from a few well-resourced labs into cheap, widely available models.

**Restraint asymmetry** — the strategic condition in which one actor accepts a constraint that does not bind competitors, attackers, or systems outside the same control regime.

*Sources: Semgrep's June 2026 GLM-5.2 cyber evaluation; the NIST/CAISI assessment of Z.ai's GLM-5.2, July 2026; Anthropic's statement on the suspension and restoration of Fable 5 and Mythos 5 access; Zhipu AI's GLM-5.2 release notes.*

---

[← Other Writing](/other-writing/) · [Related Dictionary topics](/topics/#ai-capability-cyber-risk-and-strategic-restraint) · [Return to Dictionary](/)
