---
layout: default
kind: glossary
title: "Agent Memory"
permalink: /entries/agent-memory/
date: 2026-09-03
summary: "Persistent information an agent can carry across sessions or tasks: facts, decisions, preferences, unfinished work, and lessons from prior outcomes."
draft: false
published: true
---

**Agent memory** is persistent information that an agent system can retain and retrieve across sessions or tasks. It may include facts about the operator, earlier decisions, preferences, unfinished work, summaries of past interactions, and lessons extracted from previous successes or failures. Memory gives an agent continuity beyond the model's training data and the contents of its current context window.

Without memory, an agent may still be capable, but each session begins without information from the last one.

The useful distinction from *[RAG](/entries/rag/)* is one of role, not necessarily machinery. **Memory names the information kept for continuity; RAG names a way of retrieving outside information into the current prompt.** An agent may retrieve its memories using semantic search and therefore use RAG-like machinery. Memory may also be kept in plain files, a database, or structured records and fetched by exact lookup. Nor must every memory be autonomously learned: people may deliberately curate, correct, or construct it.

In a four-part agent architecture, a *[Skill](/entries/skill/)* supplies procedure and judgment, *[MCP](/entries/mcp/)* supplies a standard connection to external systems, RAG supplies relevant documentary context, and memory carries forward experience and continuity. The four work together; they are not competing product categories.

Memory is therefore useful and dangerous for the same reason: the agent may act on it later. Good memory systems need provenance, correction, expiry, and some way to distinguish an observed fact from an inference or an operator-authored instruction.

## See also

- *[Skill](/entries/skill/)*
- *[MCP (Model Context Protocol)](/entries/mcp/)*
- *[RAG (Retrieval-Augmented Generation)](/entries/rag/)*
- *[Intentional Memory Construction](/entries/intentional-memory-construction/)*
- *[Memory Artifact](/entries/memory-artifact/)*
- *[Provenance](/entries/provenance/)*
