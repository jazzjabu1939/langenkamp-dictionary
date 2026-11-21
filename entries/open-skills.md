---
layout: default
kind: reference
title: "Open Skills"
permalink: /entries/open-skills/
date: 2026-11-21
summary: "Procedures for AI agents, written in portable files the person or firm controls, so that the way work is done can move between models and vendors instead of being rented back from one."
published: true
seeded: 2026-06-19
first_published: 2026-11-21
last_revised: 2026-11-21
---

# Open Skills

This entry was drafted by following a procedure. It lives in a two-page text file called `dictionary-entry-editor`: read the style guides, check whether the entry already exists, define before interpreting, separate fact from tradition, run the checks, publish, confirm the page is live. The file was written for one AI assistant. It now works with several, from different companies, because it is plain text in a format they all read.

## In one sentence

**Open skills are procedures for AI agents, written in portable files that the person or firm controls, so that the way work is done can move between models and vendors instead of being rented back from one.**

## Why it exists

The first ownership fight over AI assistants was about memory: who keeps the record of what the assistant knows about you. The next one is about procedure.

When people work with agents, their methods get written down. How we grade a case write-up. How we reconcile the monthly accounts. How we check a contract before signing. Those instructions become prompts, templates, scripts, and [skill](/entries/skill/) files. That writing-down is valuable: it turns habits that lived in one person's head into something a colleague or an agent can follow. Michael Polanyi observed that *we can know more than we can tell*.[1] Skill files are an attempt to tell more of it.

The risk is where the writing lands. If the procedures are built inside one vendor's product, the firm's know-how becomes part of that product. Nate Jones's June 2026 warning was that skills were *leaving people's hands*, and that a firm could end up renting its own methods back.[2] The [Borrowed Brain](/entries/borrowed-brain/) entry describes the individual version of the same problem.

## The standard

The portable format now exists. Anthropic introduced Agent Skills in October 2025 as folders containing a `SKILL.md` file of instructions plus any scripts or reference material the procedure needs.[3] In December 2025 it published the format as an open standard, and in October 2026 handed the standard to the Agentic AI Foundation, a Linux Foundation project, reporting that more than seventy agent platforms had adopted it.[4]

A standard format makes open skills possible. It does not make them automatic. A skill written in the open format but stored only in a vendor's cloud, editable only through its interface, is still a rented skill.

## What makes a skill open

Four tests:

1. **Readable.** A person can open the file and understand the procedure without the agent.
2. **Held.** The canonical copy lives somewhere the owner controls, such as a shared drive or a code repository.
3. **Portable.** It runs, with little change, on more than one model or product.
4. **Maintained.** Someone revises it when the work changes. An abandoned skill is a stale instruction with good formatting. (See [Agent Maintenance](/entries/agent-maintenance/).)

## Why this matters in a teaching context

Business schools teach that a firm's capabilities, its routines and know-how, are a source of advantage that rivals find hard to copy. Skills files make those routines explicit, which makes them easier to improve, to teach, and to lose. A student who learns to write a clear procedure for an agent is learning to articulate how good work is done, which is most of what a manager does anyway. The ownership question then follows naturally: once the routine is written down, who holds the page?

## Trade-offs and warnings

- **Writing it down is not the same as knowing it.** A skill captures the steps someone could articulate. The judgment that tells a good result from a bad one may still live only in a person.
- **Integrated products are convenient.** A vendor's built-in skill library may be easier to use and share. Keeping the canonical copy elsewhere is extra work.
- **Open skills can leak.** A procedure portable enough to move between vendors is also easy to copy out of the firm. Openness to tools is a different question from openness to competitors.
- **A shared skill is a shared risk.** A skill downloaded from a public library is code and instructions from a stranger, and deserves the same caution as any other untrusted input ([Prompt Injection](/entries/prompt-injection/)).

## See also

[Skill](/entries/skill/) · [Context Lock-In](/entries/context-lock-in/) · [Team Harness](/entries/team-harness/) · [Borrowed Brain](/entries/borrowed-brain/) · [SOUL.md](/entries/soul-md/) · [AGENTS.md](/entries/agents-md/) · [Workspace](/entries/workspace/) · [Agent Maintenance](/entries/agent-maintenance/)

## Sources

[1] Michael Polanyi, *The Tacit Dimension* (University of Chicago Press, 1966), p. 4.

[2] Nate Jones, "Your skills are leaving your hands. Don't let a rent-a-brain keep them," *Nate's Newsletter*, June 19, 2026.

[3] Anthropic, ["Equipping agents for the real world with Agent Skills"](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills), October 16, 2025; updated December 18, 2025, on publication of the open standard at [agentskills.io](https://agentskills.io).

[4] Anthropic, ["Donating Agent Skills to the Agentic AI Foundation"](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation), October 22, 2026.

---

*First published November 21, 2026.*
