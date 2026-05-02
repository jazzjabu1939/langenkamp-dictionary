---
layout: default
title: Topic Index
---

# Topic Index

A thematic view of the dictionary. For the alphabetical list, see [`entries/`](entries/). To return to the front page, see [home](./).

---

## Foundations

These are the load-bearing concepts. Most other terms reference one or more of these.

- [Embedding](entries/embedding.md) — meaning as a list of numbers.
- [Tool](entries/tool.md) — the function call that lets an agent act in the world.
- [Naming](entries/naming.md) — why the choice of names is structural, not cosmetic.

## How an agentic system is put together

The architectural pieces of a running agent.

- [Gateway](entries/gateway.md) — the always-on coordinator process.
- [Sub-agent](entries/sub-agent.md) — delegated AI sessions for parallel or focused work.
- [Heartbeat](entries/heartbeat.md) — periodic, automated nudges that make agents proactive.
- [SOUL.md](entries/soul-md.md) — the agent persona file as architectural pattern.

## Knowledge & retrieval

How an agent uses information beyond its training data.

- [RAG (Retrieval-Augmented Generation)](entries/rag.md) — the dominant pattern for "AI that knows my stuff."
- [Vector database](entries/vector-database.md) — the storage and retrieval infrastructure for embeddings.
- [Fine-tuning](entries/fine-tuning.md) — when to retrain a model, and when not to.

## Standards & ecosystems

The shared protocols and runtimes that make agentic systems composable.

- [MCP (Model Context Protocol)](entries/mcp.md) — the open standard for connecting agents to tools.
- [Ollama](entries/ollama.md) — local LLM runtime for sovereignty and cost containment.

## Operations & economics

The ongoing reality of running an agent in production — the costs, the meters, and the feelings practitioners develop about them.

- [Token burn](entries/token-burn.md) — the cost-rate concept. *What is it costing?*
- [Token anxiety](entries/token-anxiety.md) — the capacity-bounded operational concept. *Will it fit?*
- [Token angst](entries/token-angst.md) — the existential concept. *Was it worth it?*

## Working with the agent (and not against your own brain)

The practitioner's craft of using AI assistants without breaking your own learning, your own thinking, or your own labor-market position.

- [English major](entries/english-major.md) — why the new bottleneck is specification, not syntax, and who that suddenly favors.
- [Can't help you understand](entries/cant-help-you-understand.md) — the hard limit on what an AI can do for your comprehension.
- [Descartes was wrong](entries/descartes-was-wrong.md) — a philosophical reframing of what is happening when an AI agent (or a human) thinks.

---

## Planned entries

The dictionary is a work in progress. Expected near-term additions:

- *Skill* — packaged capabilities aimed at the agent.
- *Context window* — the boundary of what a model can see at once.
- *Prompt* / *system prompt* — the input layer of an agentic system.
- *Token* — the unit of cost, throughput, and capacity.
- *Quantization* — why a 70-billion-parameter model can fit in 42 gigabytes.
- *Hallucination* — what it is, what it isn't, and why "hallucination" is itself an imperfect name.
- *Local-first / sovereignty* — running AI without sending data to a third party.
- *Model tiering* — using different models for different tasks to control cost.
- *Approval gating* — how to require human consent for sensitive agent actions.
- *Provenance* — knowing where an agent's output came from.

If a term you wish were here is missing, [open an issue](https://github.com/jazzjabu1939/langenkamp-dictionary/issues) and the maintainer will add it.

---

*Maintained by Matthew D. Langenkamp / 雷邁德.*
