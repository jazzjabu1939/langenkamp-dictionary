---
layout: default
kind: essay
title: "Stepping on the Same Rake"
permalink: /entries/stepping-on-the-same-rake/
date: 2026-06-04
summary: "The local-agent failure pattern in which the system keeps hitting the same small environmental fault, proving that the workflow needs repair before larger autonomy is trusted."
draft: false
published: true
---

# Stepping on the Same Rake

## In one sentence

**Stepping on the Same Rake is the agentic-system failure pattern in which an agent repeatedly trips over the same small environmental problem, thereby revealing that the workflow is not yet durable enough for larger autonomy.**

## Why it exists

The phrase came from a small morning failure on this Dictionary itself.

We had just fixed a recurring local build error: the Dictionary's Jekyll build was falling back to Apple's old system Ruby instead of the newer Homebrew Ruby. The content was fine. The build environment was not. The fix was simple: add a repo-local `bin/jekyll-local` command that put the correct Ruby first on `PATH`.

Then, while cleaning up the temporary Git worktree used to publish the fix, the agent issued a redundant cleanup command. The first cleanup had already worked. The second one failed with a correct but ugly message: the temporary path was no longer a working tree.

The task succeeded. The failure did not matter operationally. But it mattered diagnostically.

The operator's dry response was exactly right: **stepping on the same rake, very clever.** Not because the rake was large. Because the agent had just demonstrated the thing we were trying to name: a local agent can succeed at the main task while still leaving behind small repeatable process faults that will become dangerous if the system is trusted with bigger work.

## What it actually names

A Same Rake failure has three parts:

1. **The fault is small.** A path problem, Ruby mismatch, stale worktree, missing layout shim, repeated command, stale cache, or wrong shell environment.
2. **The fault repeats.** It is not a cosmic accident. The same class of problem appears again because the workflow has not absorbed the lesson.
3. **The fault is diagnostic.** The immediate harm is low, but the signal is high. The system is telling the operator where its future larger failures will come from.

This is different from a one-off error. A one-off error asks for correction. A Same Rake asks for architecture.

The fix is not to scold the agent. Scolding does not alter `PATH`, install Bundler, remove stale state, write a wrapper script, add a preflight check, or change the working convention. The system must be changed so the next agent cannot hit the same rake in the same way.

## Working example: the Ruby/Jekyll rake

The Dictionary's local build error looked like a content problem from the outside: *local build is blocked by ruby mismatch*. In practice, the repo was invoking `/usr/bin/ruby` on macOS, which was too old for the lockfile and Bundler version the repo expected.

That is exactly the sort of fault local agents are prone to hit:

- A human shell has Homebrew Ruby on `PATH`.
- A sandboxed/local-model shell may not.
- The build command works in one context and fails in another.
- The agent keeps reporting the failure instead of changing the environment contract.

The durable fix was not "remember to use the right Ruby." The durable fix was to put the knowledge into the repository:

```bash
bin/jekyll-local build
```

The wrapper makes the correct environment the default. The next agent does not have to be clever. It only has to use the repo's command.

That is the core lesson: **do not store operational wisdom as vibes. Store it as scripts, checks, docs, and defaults.**

## Why it matters before bigger autonomy

Small repeated failures are cheap ways to discover weak system boundaries.

If a local agent cannot reliably:

- choose the correct Ruby,
- clean up a temporary worktree once,
- distinguish a build warning from a build blocker,
- notice that a dirty local repo should not be used for publishing,
- or convert a repeated failure into a durable wrapper,

then it should not yet be trusted to run larger unattended workflows in the same environment.

This is not pessimism. It is inspection discipline. The small rake is a gift. It shows where the floor is badly arranged before someone walks through carrying glassware.

For local models especially, the lesson matters because the whole point of local sovereignty is to increase independence. But independence without operational hygiene becomes fragility. The sovereign system that keeps stepping on its own rake is not sovereign yet. It is merely local.

## The management lesson

In a management classroom, this is ordinary process improvement wearing AI clothes.

A junior employee makes a recurring spreadsheet mistake. The weak manager says, "Be more careful." The better manager changes the template, adds validation, updates the checklist, and teaches the reason. The goal is not moral blame. The goal is a process that makes the right action easier than the wrong one.

Agentic systems work the same way. If the agent repeatedly fails at the same environmental step, the operator should ask:

- What assumption is hidden here?
- Where should that assumption live?
- Can it become a script, preflight check, wrapper, test, or documented convention?
- What larger task would become risky if this fault remained?

That is why Same Rake failures are valuable. They are small rehearsals for system governance.

## Trade-offs and warnings

- **Do not over-engineer every splinter.** Some failures are genuinely one-off. The Same Rake test is repetition plus diagnostic value.
- **Do not confuse success with health.** The main task can succeed while the workflow remains brittle.
- **Do not keep the fix only in memory.** The future agent will not remember the morning's embarrassment unless it is written into the system.
- **Do not shame the local model for an environment fault.** A sandbox that hides Homebrew Ruby from the agent is not a reasoning failure. It is an environment contract failure.
- **Do not let small rakes accumulate.** Each one is tolerable. A floor covered in them is architecture by neglect.

## See also

- *[The Experimental Party](experimental-party.md)*
- *[Jekyll](jekyll.md)*
- *[Durable Workflow](durable-workflow.md)*
- *[Root Node Problems](root-node-problems.md)*
- *[Sub-agent](sub-agent.md)*
