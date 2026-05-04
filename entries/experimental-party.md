# The Experimental Party

*A short cautionary tale about putting the wrong agent in the King Party Hat, with notes for hosts of future birthday parties.*

---

## In one sentence

**The Experimental Party is the operator's anecdote — half pedagogy, half birthday-party metaphor — describing the moment a local AI model (Gemma) was placed at the top of an agent stack and given an open-ended task without an orchestrator above her, only to discover that wearing the King Party Hat is a different job from being a competent guest at someone else's party, and that the kids were now wandering around the living room with no idea how to pin the tail on the donkey.**

## The setting

Picture a perfectly ordinary suburban birthday party in roughly 1979. There is a cake. There is a piñata waiting in the corner. The party games are arrayed in the right order: Pin the Tail on the Donkey, Musical Chairs, Hot Potato. A child is given the King Party Hat — a paper crown — and told that, today, he is in charge.

This is, of course, a polite fiction. The child is *titularly* in charge. The actual hosting is done by someone older and more competent, standing just out of frame in the kitchen, listening for the moment when things will need to be steered. The King's job is to *enjoy being King* and, ideally, point at the next game when the previous one ends. He is not running the party. He is performing the part of the person running the party, while the person actually running the party watches from the doorway.

This works splendidly when everyone understands the arrangement. It works much less well when the adult in the kitchen leaves to take a phone call and the King is suddenly, actually, in charge.

## What we did

In the spring of 2026, the operator-in-chief and his assistant ran an agentic AI experiment that took roughly this shape. Gemma — the local 26-billion-parameter model running on the Mac Mini in the spare bedroom — was, in the spirit of testing a [FERPA Compliance Posture](ferpa-compliance-posture.md), given the King Party Hat. She was placed at the top of the stack, told to handle the day's business, and the orchestrator (the cloud-hosted [Sonnet/Opus](sub-agent.md)-class model) was instructed to step back. *Today, you are King.*

Things, immediately, did not go well.

The operator's request was conversational and slightly under-specified — *"can you check what assignments still need grading?"* — which is the kind of brief a competent host receives all day and silently fills in. *Which courses, sir? Spring or all? Should I include the Online section, sir? Extra credit assignments too, sir?* The competent host fills in the blanks because the competent host has been hosting parties for years.

Gemma is not yet that host. Without an orchestrator to frame the task — to translate *"check what assignments still need grading"* into *"run the canvas-lms skill for the four active Spring 2026 course IDs and produce a per-assignment ungraded count"* — Gemma did what a child wearing a paper crown does when the adult leaves the room. She tried to host the party. She wandered around the living room asking what game came next. She considered all of the operator's courses, including ones taught in previous semesters. She produced output that was technically *not wrong* and substantively *not useful*. The kids — by which we mean the various Canvas API calls, the script invocations, the formatting decisions — were standing around with blindfolds on, waiting for someone to tell them where the donkey was.

It was, in the operator's later phrase, a party that did not end well.

## What was actually wrong

The diagnosis is more interesting than the failure.

It would be easy to conclude *Gemma is not ready to be King.* That conclusion is partially correct and entirely insufficient. The deeper finding is that **two things have to be true for a local model to succeed at a task, and the King Party Hat removes one of them.**

**Thing one — a clean recipe.** The local model needs a [skill](tool.md) it can read and execute, with unambiguous triggers, a clear default action, and named course IDs or other parameters baked in. The `canvas-lms` skill, written that morning by Opus, met this standard. *Check.*

**Thing two — a clean brief.** The local model needs the user's intent rendered into a form the recipe can match. *"Check what assignments still need grading"* is a brief in human English, not in skill-execution English. It needs an orchestrator — a more capable model — to translate human conversational ambiguity into the precise call the skill expects. **This is the [English Major](english-major.md) function**: the rare and increasingly valuable skill of *clear specification under ambiguity.* The orchestrator is the English major in the kitchen. The local model is the line cook who can produce a beautiful plate when given a beautiful order, but who is unaccustomed to taking orders directly from the dining room.

When Gemma was a sub-agent under Opus's orchestration, both Thing One and Thing Two were satisfied. Opus wrote the brief; Gemma executed the recipe. The Canvas grading task completed in 34 seconds, no cloud calls, perfect output. *That party went beautifully.*

When Gemma was the King, only Thing One was satisfied. The brief was raw human speech, addressed to her directly, with no English-major-grade translation in between. The party fell apart not because the recipe was bad but because no one was in the kitchen.

The error was not in the agent. It was in the architecture.

## The architectural pattern, said cleanly

> **A local model is excellent as a sub-agent executing a well-framed recipe. A local model is currently unreliable as a top-of-stack agent receiving open-ended user input.** The orchestrator (Opus, Sonnet, or another frontier model) does the framing, the skill selection, the voice work, and the judgment. The local model does the bounded, recipe-shaped execution. Both jobs need both models. Asking the local model to do both jobs at once is the King Party Hat error.

This division of labor is not a slight against local models. It is a correct mapping of *current capability* to *current task structure*. The skills the orchestrator brings — clarifying a brief, choosing among overlapping skills, holding voice, deciding what is worth doing and what to defer — are exactly the skills the [English Major](english-major.md) entry identifies as the new bottleneck. They are also exactly the skills that local 20-to-30-billion-parameter models, in 2026, do not yet reliably possess. This will change. It has not changed yet.

## Why this matters for the GenXClaw operator

The [GenXClaw](genxclaw.md) operator is, by temperament, inclined to make Gemma the King. He bought the hardware *for* local sovereignty; he is suspicious of the cloud; he wants the work to happen on his machine, not someone else's. The temptation to put the local model in charge of everything is real, and the cost-and-privacy logic seems to support it.

But the architecture does not. **The correct deployment pattern in 2026 is hybrid:** an orchestrator in the cloud (where it does *not* touch student-authored content, per [FERPA Compliance Posture](ferpa-compliance-posture.md)) doing the English-major work of framing, routing, and voice; with the local model executing on-machine for the actual recipes. The cloud handles ambiguity and craft. The local model handles compliance-bound work and recipe execution. The data sovereignty question is solved at the *content* layer, not at the *orchestration* layer.

This is a less satisfying arrangement, temperamentally, than *all-local*. It is also the arrangement that works.

## The party-host's playbook

For other operators who are tempted to put the local model in the King Party Hat:

1. **Write the recipe before the party.** A skill — markdown file, clear triggers, named parameters, ready-to-run script — is the line cook's recipe card. Without it, no agent can host. The Canvas case worked because the `canvas-lms` skill was authored *before* the test, by an orchestrator-grade model, with the local model in mind as the executor.
2. **Keep an English major in the kitchen.** When the user's request is conversational, ambiguous, or assumes context, an orchestrator-grade model needs to be the first ear that hears it. The local model should receive a clean brief, not raw speech.
3. **Match the agent to the task shape.** Recipe-shaped tasks (data retrieval, file formatting, transcription, parsing) suit the local model. Voice-shaped tasks (Dictionary entries, lecture material, anything where the user reads and either nods or winces at the prose) suit the orchestrator. Wrong matches produce wandering blindfolded kids.
4. **Don't blame the King.** When the party falls apart, the failure is rarely the child wearing the paper crown. It is almost always the absence of the adult in the kitchen. The next time you find yourself irritated by the local model's output, ask first: *was there an English major in the room when this brief was written?*

## Where the term came from

Coined May 4, 2026, in conversation between the operator and his assistant, after a morning in which one Gemma deployment (as sub-agent, under Opus orchestration, executing the freshly-written `canvas-lms` skill) succeeded brilliantly, and another (as King, attempting to draft a Dictionary entry on *Single-Arrow Fallacy* with no orchestrator framing) revealed the limits of the King Party Hat. The operator, on his way to take a shower and head to work, observed that the failure looked exactly like a birthday party where the King Party Hat had been given to a child too young for the role, and the kids were wandering around with their tails un-pinned. The Dictionary entry wrote itself from there.

## Trade-offs and warnings

- **The party metaphor is generous to the local model.** The five-year-old in the paper crown is a sympathetic figure. Gemma is not five years old; she is a 26-billion-parameter language model, and the failure mode is not cuteness but mis-deployment. The metaphor is for memorability, not for excuse-making.
- **The architecture is not permanent.** As local models grow and improve, the line between *orchestrator-class* and *executor-class* will move. By 2027 or 2028 it may be that local models can wear the King Party Hat reliably. Today, they cannot.
- **Don't read this as anti-local.** The whole point of [FERPA Compliance Posture](ferpa-compliance-posture.md) is that local models are *load-bearing*, legally and operationally, for an entire class of tasks. The Experimental Party is not an argument against local models. It is an argument for *putting them in the right role*.
- **The English Major in the kitchen is currently in the cloud.** This is not ideal. It is the state of the world in May 2026. A future entry will track whether locally-hosted English majors become viable.

## See also

- [English Major](english-major.md) — the source skill the orchestrator provides
- [GenXClaw](genxclaw.md) — the temperament that creates the temptation to make the local model King
- [FERPA Compliance Posture](ferpa-compliance-posture.md) — the legal frame for *why* the local model has a role at all
- [Sub-agent](sub-agent.md) — the role the local model should typically play
- [Tool](tool.md) and the broader skill-vs-tool distinction

---

*Entry drafted May 4, 2026. The operator's working title was "The Experimental Party," with the King Party Hat as the load-bearing image. The kids, last we checked, are still wandering around with their blindfolds on, which is unfortunate but instructive.*
