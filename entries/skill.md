---
layout: default
kind: glossary
title: "Skill"
permalink: /entries/skill/
date: 2026-05-19
last_revised: 2026-09-03
summary: "A packaged capability aimed at the agent: instructions, triggers, tools, and local knowledge for doing a class of work reliably."
draft: false
published: true
---

A **skill** is a packaged capability written for an agent rather than for an ordinary software user. It usually contains triggers, operating instructions, tool conventions, safety notes, and local knowledge for a repeatable class of work: using Canvas, handling Apple Notes, managing GitHub issues, querying email, transcribing audio, or maintaining the Dictionary.

A tool is something the agent can call. A skill is the larger recipe that tells the agent *when* to call it, *how* to interpret the result, and *what local conventions matter*. This distinction is important because many agent failures are not tool failures. The tool works; the agent used it in the wrong situation or without the surrounding judgment.

In the Dictionary's architecture, skills are one way to turn tacit operator knowledge into durable system behaviour.

The neighbouring terms do different jobs. A skill tells the agent **what procedure to follow**; *[MCP](/entries/mcp/)* gives it a standard way to reach tools and outside systems; *[RAG](/entries/rag/)* retrieves relevant documentary knowledge; and *[Agent Memory](/entries/agent-memory/)* carries facts, decisions, and lessons across sessions. A skill may instruct the agent to use all three, but is not interchangeable with any of them.

## Five practices for building a trustworthy skill

IBM Technology's useful formulation treats a skill as **procedural knowledge handed to an AI agent**. Because the format can be little more than a Markdown file plus supporting resources, the engineering discipline sits in what the author chooses to put inside it.

1. **Treat the description as the trigger.** An agent may initially see only a skill's name and description. The description therefore needs to say both **what the skill does** and **when the agent should use it**. A precise skill that never triggers is merely well-filed literature.
2. **Build from real expertise.** The valuable content is not generic advice the model already knows. It is the operator's actual procedure, examples, review history, local conventions, and especially the gotchas discovered when reasonable assumptions failed. Every repeated human correction is a candidate for the skill.
3. **Spend context carefully.** Keep the main instructions lean and place detailed references in supporting files that the agent reads only when required. This is *progressive disclosure*: enough information to act correctly now, with deeper material available on demand.
4. **Use deterministic scripts for fragile steps.** Where several approaches can produce an acceptable result, instructions leave room for judgment. Where arithmetic, formatting, parsing, validation, or another exact operation must behave consistently, the skill should call tested code. The compact rule is: **loose step, instructions; fragile step, code.** Deterministic does not mean infallible; the script still needs tests.
5. **Vet a skill before running it.** A downloaded skill may contain executable code with access to files, networks, or credentials. An open format does not make every package trustworthy. Third-party skills should be reviewed like any other software dependency: inspect the instructions, scripts, permissions, and external connections before execution.

The five practices point toward one larger principle: a good skill preserves the human's domain expertise while giving the agent the routine work. The agent supplies fluency and repetition; the skill supplies the parts that should not be improvised anew each time.

*Source: IBM Technology, [“5 Best Practices for Building AI Agent Skills”](https://www.youtube.com/watch?v=qYNs80FKIVc), YouTube, 2026.*

## See also

- *[Tool](/entries/tool/)*
- *[MCP (Model Context Protocol)](/entries/mcp/)*
- *[RAG (Retrieval-Augmented Generation)](/entries/rag/)*
- *[Agent Memory](/entries/agent-memory/)*
- *[System Prompt](/entries/system-prompt/)*
- *[Durable Workflow](/entries/durable-workflow/)*
