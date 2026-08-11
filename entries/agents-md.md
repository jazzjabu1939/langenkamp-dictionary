---
layout: default
title: "AGENTS.md"
permalink: /entries/agents-md/
date: 2026-08-11
summary: "A project-level instruction file written for AI coding agents: how to build, test, edit, verify, and behave inside a particular repository. A README for the worker rather than the visitor."
draft: false
published: true
---

# AGENTS.md

**AGENTS.md is a project-level instruction file written for AI coding agents: it tells them how to build, test, edit, verify, and behave inside a particular repository.**

The quickest explanation is IBM's: an `AGENTS.md` file is rather like a README written for agents.

That analogy is useful, but incomplete. A conventional `README.md` usually explains the project to a human visitor: what the software does, how to install it, how to contribute. An `AGENTS.md` file addresses the worker already inside the building. It may specify which test command to run, which files are authoritative, what coding conventions matter, which generated files must not be edited, how pull requests should be titled, and which apparently reasonable action would be disastrously wrong in this particular environment.

The file exists because general intelligence is not local knowledge. A capable coding model may understand Python, Jekyll, GitHub Actions, and database migrations perfectly well while knowing nothing about the odd little facts that make *this* repository work. Perhaps the local Jekyll build must use a wrapper because Apple's system Ruby is too old. Perhaps an archive page is generated from a ledger and must never be edited by hand. Perhaps the newest-looking draft is not the canonical publication. These are not facts the model can infer safely. They have to be stated.

## The instruction hierarchy

`AGENTS.md` files can be nested. A repository may have one at its root and more specific ones inside subdirectories. The root file establishes broad rules; a file closer to the agent's working directory supplies local instructions and can override the broader ones where their scopes conflict.

This gives the repository an inspectable instruction hierarchy. General rules apply everywhere. Specialized rules travel with the part of the codebase that needs them.

The design resembles an organization. Corporate policy applies throughout the firm; a laboratory, trading desk, or regional office may have additional rules because its work has different risks. The local rules do not abolish the institution. They make its instructions usable where the work actually occurs.

## AGENTS.md, SOUL.md, and Skill

These three files operate at different levels:

- **[SOUL.md](soul-md.md)** shapes who the agent is: character, voice, values, boundaries, and relational stance.
- **AGENTS.md** governs how the agent works inside a project: commands, conventions, authority, verification, and local hazards.
- **[Skill](skill.md)** supplies procedural knowledge for a recurring class of task and is usually loaded only when that capability is needed.

One is character, one is workplace, and one is craft.

The distinction also matters for context. Project instructions may need to be available whenever the agent works in the repository. A detailed procedure for editing PDFs or querying Canvas does not. Loading every possible procedure at startup would crowd the context window with instructions irrelevant to the current task. Skills therefore lend themselves to **progressive disclosure**: the agent sees enough metadata to know a capability exists, then loads the full instructions only when the task calls for them.

## Why plain text matters

Like `SOUL.md`, an `AGENTS.md` file is deliberately unglamorous. It is plain text. Humans can inspect it. Agents can read it. Git can show who changed it and why. A bad rule can be corrected without retraining a model or waiting for a platform vendor.

This makes operating knowledge portable. The repository does not have to hope that the next agent, model, or session remembers an oral tradition. The knowledge sits beside the work.

There is a managerial point here. Organizations often describe important knowledge as "tribal," meaning everyone relies on it but nobody has written it down. That arrangement survives until the tribe changes shifts, leaves the company, or is replaced by a fresh context window. `AGENTS.md` is one small answer: if a correction matters twice, it should probably become infrastructure.

## What belongs in it

A useful `AGENTS.md` contains information the agent needs repeatedly and cannot safely infer:

- the correct build, test, lint, and verification commands;
- repository-specific architecture and sources of truth;
- file ownership and generated-file rules;
- naming, formatting, and contribution conventions;
- approval boundaries and prohibited actions;
- known environmental traps and recovery procedures;
- the definition of "done" for work in that scope.

It should not become a warehouse for every fact anyone might conceivably need. An overgrown instruction file creates the same problem as any other overloaded context: the important rule is present but no longer salient. Durable project rules belong in `AGENTS.md`; detailed task procedures belong in skills or linked references; transient work belongs in plans and issue trackers.

## The deeper significance

`AGENTS.md` is part of the emerging interface between human organizations and machine workers. Source code tells the computer what the program should do. Project documentation tells humans what the project is. `AGENTS.md` tells an agent how to participate responsibly in producing and maintaining it.

That is why the term belongs beside **[Harness](harness.md)** and **[Agentic Engineering](agentic-engineering.md)**. Agentic engineering is not merely asking a model to write code. It is constructing an operating environment in which the agent receives the right instructions, works within explicit constraints, verifies fragile steps, and leaves an auditable trail. `AGENTS.md` is one of the simplest artifacts in that environment, and one of the most consequential.

## See also

[SOUL.md](soul-md.md) · [Skill](skill.md) · [Harness](harness.md) · [Agentic Engineering](agentic-engineering.md) · [Sub-agent](sub-agent.md) · [System Prompt](system-prompt.md) · [Durable Workflow](durable-workflow.md)

## Sources

- AGENTS.md open specification: <https://agents.md/>
- IBM Technology, "5 AI Agent Terms You Need to Know," June 23, 2026: <https://www.youtube.com/watch?v=k5jYwyhDMxA>
