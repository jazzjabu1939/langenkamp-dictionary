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

Vibe coding and agentic engineering may use the same model and produce the same amount of generated code. They differ in the operator's responsibility for the result. Vibe coding accepts output mainly because it appears to work. Agentic engineering defines the architecture and constraints, examines the changes, tests the important behaviour, and remains accountable for deployment and maintenance.

Andrej Karpathy's move from *vibe coding* toward *agentic engineering* gives this difference a useful name. The term shifts attention from what the model can produce to the conditions under which other people can rely on the result.

## The engineer moves up a level

The old craft centered on writing implementation directly. That craft has not disappeared, and it should not be sentimentalized out of existence. Reading code, debugging code, naming functions, designing interfaces, understanding data structures, and knowing where systems fail remain real skills.

But the center of gravity is moving.

The new craft increasingly centers on specifying intent, bounding behavior, reviewing generated diffs, designing tests, controlling permissions, watching failure modes, and deciding when the model has produced something usable versus merely convincing.

**Agentic Engineering** is broader than "AI coding" or "prompting." It names the whole operating loop: task framing, tool access, context management, review, verification, deployment, rollback, and maintenance.

The agent may write the patch. The engineer owns the system.

## Ownership is the line

If a model writes authentication logic, the engineer owns the security implications.

If an agent edits a database migration, the engineer owns the data risk.

If generated code passes a weak test, the engineer owns the weakness of the test.

If a tool call deletes the wrong file, the engineer owns the permission design that allowed it.

Engineering responsibility includes delegated implementation. Delegation changes the form of supervision but does not remove it.

The same principle applies outside professional software teams. A professor building a local grading helper, a researcher building a scraper, or an operator maintaining an OpenClaw workflow can practise agentic engineering when the human remains accountable for the system's behaviour.

That accountability is especially important because AI makes implementation abundant. What remains scarce is trustworthy implementation: code that does what it should, fails in known ways, exposes enough of its path to be reviewed, and can be maintained by someone who did not sit inside the original prompt session.

## The marks of the practice

Agentic engineering has visible habits.

The work is broken into clear task boundaries. The agent is asked to do one coherent thing, not to wander across the codebase looking industrious.

Constraints are explicit. The human tells the agent what files it may edit, what behavior must remain unchanged, what interfaces are stable, and what tests define success.

Diffs are small enough to review. A thousand-line patch may be impressive. It may also be camouflage. The engineer keeps the work inspectable.

Tests cover the behaviour the change is supposed to guarantee and the failure modes that matter.

Permissions are controlled. The agent does not receive broad destructive power merely because it is convenient.

Rollback paths exist. The engineer knows how to return to a known-good state.

The generated code can be explained. If the human cannot explain the architecture, the risks, and the tests, the work has not yet earned the name engineering.

## Use of AI

Agentic engineering makes extensive use of AI. An agent can search a codebase, propose changes, write boilerplate, refactor, summarize errors, and test possible fixes while the human concentrates on intent and judgment.

This division of labour asks the human to become a better specifier, reviewer, tester, architect, and judge. The model is a powerful but fallible implementation system. The human need not type every line, but must make the development and review process reliable enough for the intended use.

The term therefore belongs next to *Vibe Coding*. Vibe coding names rapid creation through prompting. Agentic engineering names the additional discipline required when other people will depend on the result.

## See also

*[Vibe Coding](vibe-coding.md)*, *Coding Solved*, *Claude Code*, *Verification Gap*, *Artifact Is Not Competence*, *Judge Layer*, *Approval Gating*, *Sovereign Compute*, *OpenClaw*, *Red Pill*.

## Source

Andrej Karpathy's public move from "vibe coding" toward "agentic engineering," including his X post naming the term and the Sequoia Capital conversation with Stephanie Zhan, "Andrej Karpathy: From Vibe Coding to Agentic Engineering," AI Ascent 2026.

- Karpathy X post on agentic engineering: <https://x.com/karpathy/status/2019137879310836075>
- Sequoia Capital / YouTube, "Andrej Karpathy: From Vibe Coding to Agentic Engineering w/ Stephanie Zhan": <https://www.youtube.com/watch?v=96jN2OCOfLs>
