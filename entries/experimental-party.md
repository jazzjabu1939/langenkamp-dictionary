---
layout: default
kind: reference
title: "The Experimental Party"
permalink: /entries/experimental-party/
summary: "a cautionary tale about putting a local model in the King Party Hat before the party has an adult in the kitchen — and the origin story of the Jindoo Process."
---

# The Experimental Party

*A short cautionary tale about putting the wrong agent in the King Party Hat, with notes for hosts of future birthday parties.*

---

## In one sentence

**The Experimental Party is the operator's birthday-party metaphor for a local-model failure mode: putting a capable local model at the top of an agent stack, giving it open-ended human speech, and then being surprised when it performs the role of host rather than actually hosting the party.**

The later cure is the **Jindoo Process**: frontier model as architect, local/open model as bounded contractor, and Thea/operator as general contractor, verifying each piece of work before the next one begins.

## Why it exists

Picture a suburban birthday party in roughly 1979. There is cake. There is a piñata waiting in the corner. Pin the Tail on the Donkey is ready. Musical Chairs is next. A child is given the King Party Hat — a paper crown — and told that, today, he is in charge.

This works because everyone understands the fiction. The child is *titularly* in charge. The actual hosting is being done by someone older and more competent, standing just out of frame in the kitchen, listening for the moment when the games need to be steered, the matches hidden, or the child in the paper crown gently redirected away from the dog.

The Experimental Party names what happens when the adult in the kitchen leaves and the child in the paper crown is suddenly, actually, in charge.

In the spring of 2026, the operator and his assistant ran exactly this experiment with local AI. Gemma — the local 26-billion-parameter model running on the household hardware — was given the King Party Hat. In the name of local sovereignty and FERPA-safe architecture, she was moved toward the top of the stack and asked to handle real work directly.

Things did not go well.

## What it actually does

The failure was not that Gemma was useless. That would have been a boring finding, and also false. Gemma was quite good when given a clean, bounded task. The failure was architectural.

The user's request was conversational and underspecified: *can you check what assignments still need grading?* A competent orchestrator silently translates that into something executable: use the Canvas LMS skill, target these active Spring 2026 course IDs, count ungraded submissions by assignment, ignore old courses, return a concise table.

That translation is not clerical. It is the [English Major](english-major.md) function: clear specification under ambiguity.

When Gemma ran as a sub-agent under a stronger orchestrator, the task worked. The orchestrator framed the request; Gemma executed the recipe. The party went beautifully.

When Gemma wore the King Party Hat, the raw human request reached the local model without enough framing. She considered too many courses, treated stale context as live, produced output that was technically adjacent but operationally wrong, and left the kids — Canvas calls, scripts, formatting decisions, context assumptions — wandering around the living room with their blindfolds on.

The error was not in the child. The error was in pretending the paper crown was a management system.

## A working example: before and after Jindoo

The original Experimental Party gave us the negative rule:

> **Do not put a local model at the top of the stack and hand it raw human ambiguity unless the task has already been reduced to a recipe.**

The newer Jindoo Process gives us the positive architecture:

1. **Architect pass.** A frontier or best-available model interviews the operator, inspects the files, and writes the work packet: goal, constraints, relevant context, build plan, task sequence, test plan, and escalation criteria.
2. **Contractor pass.** The local/open model receives one bounded task at a time. Not *build the app*. Not *finish the whole project*. One job, one context packet, one stop condition.
3. **General-contractor pass.** Thea or the operator dispatches the task, inspects the diff or output, runs the smallest meaningful test, and decides whether to continue, retry, or escalate.
4. **Verification gate.** Tests, lint, build, manual inspection, or live output decide whether the work is accepted. The model's confidence does not decide.
5. **Escalation.** If the local model gets stuck, only the failure packet is escalated: task, relevant files, error output, what was tried. The frontier model supplies a patch plan, not a full rewrite.

That is Master Jindoo's lesson, stated without the incense: **local models are excellent contractors when the job has been framed; they are unreliable party hosts when the job itself still needs framing.**

## Why it matters in a teaching context

The Experimental Party is useful for teaching because it separates three roles students and faculty often collapse into one word: *AI*.

There is the **architect**, who understands the assignment and designs the work.
There is the **contractor**, who executes a bounded portion of the work.
There is the **general contractor**, who sequences, checks, accepts, rejects, and escalates.

In human organisations, nobody sensible hires a subcontractor, hands them a vague hallway remark from the client, and then blames them for not delivering the building. We understand that scope, drawings, inspection, and punch lists matter. Agentic AI needs the same discipline.

For a management classroom, this is lovely material. The local model is not *bad labour*. It is mismanaged labour. The frontier model is not *magic*. It is an expensive architect whose time should not be wasted installing drywall. The operator is not a passive consumer. The operator is the client and, often, the general contractor.

That framing lets students see agent work as organisational design rather than toy prompting. Who writes the brief? Who owns quality? Who verifies completion? Who decides when to escalate? These are management questions wearing a technical costume.

## Trade-offs and warnings

- **The metaphor is generous.** The child in the paper crown is sympathetic. A local model is not a child, and the point is not sentimentality. The point is role clarity.
- **Local capability is moving.** The line between architect-class and contractor-class models will shift. Today's party-host failure may be tomorrow's ordinary local workflow. The architecture should be evidence-led, not sentimental.
- **Do not overcorrect into cloud dependency.** The lesson is not *use frontier models for everything*. That is expensive, brittle, and often unnecessary. The lesson is to use the expensive model where ambiguity, judgement, and voice matter — then route bounded execution locally when possible.
- **Do not pretend a checklist is a general contractor.** A task file helps. A build plan helps. But someone or something still has to inspect the work and decide whether it is acceptable.
- **Tests are the adult in the kitchen.** Without a verification gate, even a well-framed contractor task can drift. The birthday party still needs someone listening for broken glass.

## See also

- [English Major](english-major.md) — the source skill the orchestrator provides
- [GenXClaw](genxclaw.md) — the temperament that creates the temptation to make the local model King
- [FERPA Compliance Posture](ferpa-compliance-posture.md) — the legal frame for *why* local execution matters
- [Sub-agent](sub-agent.md) — the role the local model should typically play
- [Tool](tool.md) — recipe cards for bounded execution
- [Sovereign Compute](sovereign-compute.md) — why the local stack matters in the first place

---

*Entry drafted May 4, 2026, after the King Party Hat experiment. Revised May 19, 2026, after the Jindoo Process clarified the mature architecture: architect, contractor, general contractor, verification gate.*
