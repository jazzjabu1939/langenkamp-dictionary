---
layout: default
kind: glossary
title: "Skill"
permalink: /entries/skill/
date: 2026-05-19
summary: "A packaged capability aimed at the agent: instructions, triggers, tools, and local knowledge for doing a class of work reliably."
draft: false
published: true
---

A **skill** is a packaged capability written for an agent rather than for an ordinary software user. It usually contains triggers, operating instructions, tool conventions, safety notes, and local knowledge for a repeatable class of work: using Canvas, handling Apple Notes, managing GitHub issues, querying email, transcribing audio, or maintaining the Dictionary.

A tool is something the agent can call. A skill is the larger recipe that tells the agent *when* to call it, *how* to interpret the result, and *what local conventions matter*. This distinction is important because many agent failures are not tool failures. The tool works; the agent used it in the wrong situation or without the surrounding judgment.

In the Dictionary's architecture, skills are one way to turn tacit operator knowledge into durable system behaviour.

The neighbouring terms do different jobs. A skill tells the agent **what procedure to follow**; *[MCP](/entries/mcp/)* gives it a standard way to reach tools and outside systems; *[RAG](/entries/rag/)* retrieves relevant documentary knowledge; and *[Agent Memory](/entries/agent-memory/)* carries facts, decisions, and lessons across sessions. A skill may instruct the agent to use all three, but is not interchangeable with any of them.

## See also

- *[Tool](/entries/tool/)*
- *[MCP (Model Context Protocol)](/entries/mcp/)*
- *[RAG (Retrieval-Augmented Generation)](/entries/rag/)*
- *[Agent Memory](/entries/agent-memory/)*
- *[System Prompt](/entries/system-prompt/)*
- *[Durable Workflow](/entries/durable-workflow/)*
