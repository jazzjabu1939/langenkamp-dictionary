---
layout: default
kind: reference
title: "Agentic Engineering"
permalink: /entries/agentic-engineering/
summary: "AI-assisted software work where the human owns the architecture, constraints, tests, security posture, maintainability, and final responsibility, even when agents write much of the code."
published: true
---

# Agentic Engineering

---

## In one sentence

**Agentic Engineering is AI-assisted software work in which the human operator owns the architecture, constraints, tests, security posture, maintainability, and final responsibility, even when agents write much of the code.**

## The corrective term

Vibe Coding is what happens when the model becomes a code fountain.

Agentic Engineering is what happens when the human takes responsibility for the fountain, the plumbing, the water pressure, the filtration system, and the people downstream.

The distinction is not whether AI writes code. In both cases, AI may write a great deal of code. The distinction is whether the human operator is merely accepting plausible output or actively designing the conditions under which that output can be trusted.

This is why Andrej Karpathy's move from "vibe coding" toward "agentic engineering" matters. It is not just a rebrand. It is a shift in the moral posture of the work.

Vibe coding says: *look what I can make the model produce.*

Agentic engineering says: *look what I can responsibly cause this system to do.*

Those are different claims.

## The engineer moves up a level

The old craft centered on writing implementation directly. That craft has not disappeared, and it should not be sentimentalized out of existence. Reading code, debugging code, naming functions, designing interfaces, understanding data structures, and knowing where systems fail remain real skills.

But the center of gravity is moving.

The new craft increasingly centers on specifying intent, bounding behavior, reviewing generated diffs, designing tests, controlling permissions, watching failure modes, and deciding when the model has produced something usable versus merely convincing.

This is why **Agentic Engineering** is a better term than "AI coding" or "prompting." Prompting is too small. Coding is too implementation-focused. Agentic engineering names the whole operating loop: task framing, tool access, context management, review, verification, deployment, rollback, and maintenance.

The agent may write the patch. The engineer owns the system.

## Ownership is the line

If a model writes authentication logic, the engineer owns the security implications.

If an agent edits a database migration, the engineer owns the data risk.

If generated code passes a weak test, the engineer owns the weakness of the test.

If a tool call deletes the wrong file, the engineer owns the permission design that allowed it.

This is not unfair to the engineer. It is what engineering means. Delegation does not remove responsibility; it changes the form of supervision.

The same principle applies outside professional software teams. A professor building a local grading helper, a researcher building a scraper, or an operator maintaining an OpenClaw workflow can practice agentic engineering. The question is not credential status. The question is whether the human remains accountable for the system's behavior.

That accountability is especially important because AI makes implementation abundant. What remains scarce is trustworthy implementation: code that does what it should, fails in known ways, exposes enough of its path to be reviewed, and can be maintained by someone who did not sit inside the original prompt session.

## The marks of the practice

Agentic engineering has visible habits.

The work is broken into clear task boundaries. The agent is asked to do one coherent thing, not to wander across the codebase looking industrious.

Constraints are explicit. The human tells the agent what files it may edit, what behavior must remain unchanged, what interfaces are stable, and what tests define success.

Diffs are small enough to review. A thousand-line patch may be impressive. It may also be camouflage. The engineer keeps the work inspectable.

Tests are meaningful. They do not merely prove that the happy path still smiles. They check the behavior the change is supposed to guarantee and the failure modes that matter.

Permissions are controlled. The agent does not receive broad destructive power merely because it is convenient.

Rollback paths exist. The engineer knows how to return to a known-good state.

The generated code can be explained. If the human cannot explain the architecture, the risks, and the tests, the work has not yet earned the name engineering.

## Not anti-AI

Agentic engineering is not a nostalgic defense of hand-coded purity. That would miss the point.

The agent is useful precisely because it can implement quickly, hold local context, search a codebase, propose changes, write boilerplate, refactor, summarize errors, and try fixes while the human stays at the level of intent and judgment.

The right objection to vibe coding is not that it uses AI. The right objection is that it asks too little of the human.

Agentic engineering asks more. It asks the human to become a better specifier, reviewer, tester, architect, and judge. It treats the model as a powerful but unreliable implementation system. The human's job is not to type every line. The human's job is to make the whole loop worthy of trust.

That is why this term belongs next to Vibe Coding. Vibe Coding names the intoxicating discovery. Agentic Engineering names the discipline that has to follow if other people are going to depend on the result.

## See also

*[Vibe Coding](vibe-coding.md)*, *Coding Solved*, *Claude Code*, *Verification Gap*, *Artifact Is Not Competence*, *Judge Layer*, *Approval Gating*, *Sovereign Compute*, *OpenClaw*, *Red Pill*.

## Source

Andrej Karpathy's public move from "vibe coding" toward "agentic engineering," including his X post naming the term and the Sequoia Capital conversation with Stephanie Zhan, "Andrej Karpathy: From Vibe Coding to Agentic Engineering," AI Ascent 2026.

- Karpathy X post on agentic engineering: <https://x.com/karpathy/status/2019137879310836075>
- Sequoia Capital / YouTube, "Andrej Karpathy: From Vibe Coding to Agentic Engineering w/ Stephanie Zhan": <https://www.youtube.com/watch?v=96jN2OCOfLs>
