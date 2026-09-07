---
layout: default
kind: reference
title: "RAG (Retrieval-Augmented Generation)"
permalink: /entries/rag/
date: 2026-05-02
first_published: 2026-05-02
last_revised: 2026-09-06
summary: "A pattern for retrieving relevant external material at query time and supplying it to a generative model."
published: true
---

# RAG (Retrieval-Augmented Generation)

## In one sentence

**RAG is a pattern in which a system retrieves material relevant to a query and supplies that material to a generative model at answer time.**

The retrieved material can be private or public: company manuals, student work, case archives, current web pages, database records, or an agent's memory files. The model need not learn the material permanently; the application finds useful evidence and places it in the model's working context.

Patrick Lewis and colleagues introduced the name in a 2020 paper that combined a language model's parametric memory with retrieved passages from an external corpus. Modern systems use a wider range of retrieval methods, but the division of labour remains useful: **retrieve first; generate with the retrieved evidence second.**

## The basic loop

1. Receive a question.
2. Search a corpus for relevant passages or records.
3. Rank and select the results.
4. Supply them, with the question and instructions, to the model.
5. Generate an answer, ideally with citations back to the sources.

Vector embeddings are common, but not required. Keyword search, SQL, graph traversal, APIs, or combinations of these can perform retrieval. A vector database is therefore one possible component, not part of the definition.

The OpenClaw memory system on this machine is a small example. `memory_search` locates relevant passages in the authorised memory corpus; `memory_get` then retrieves the selected lines. *[Agent Memory](/entries/agent-memory/)* describes what is retained for continuity. RAG describes one way of finding and supplying it. A memory system can use RAG, and a RAG system can retrieve information that is not memory at all.

## RAG and fine-tuning

RAG and fine-tuning solve different problems and can be combined.

- **RAG** is usually the first tool when answers need current, attributable, or access-controlled information.
- **Fine-tuning** is usually considered when the model needs a different behaviour, format, style, or specialised task performance.

Neither is automatically cheap, fast, current, or private. Retrieval systems require ingestion, permissions, ranking, evaluation, and maintenance. Fine-tuning costs and timelines vary greatly. Supplying private documents to a hosted model can expose them to provider processing or retention rules even though the documents are not incorporated into the model's weights.

## Variants

- **Hybrid retrieval** combines semantic and keyword search.
- **Re-ranking** applies a second model or scoring stage to the candidates.
- **Agentic RAG** lets an agent issue several searches and follow leads.
- **GraphRAG** uses graph structure to help retrieve relationships spanning many documents.

## Why it matters

RAG makes an organisation's document discipline visible. A clean, current, permissioned corpus can become a useful operational asset. A contradictory archive with weak access controls becomes a faster way to distribute old mistakes.

The model call is only one part of the work. Operators must decide what belongs in the corpus, who may retrieve it, how passages are ranked, whether citations support the answer, and how the complete system is evaluated. RAG reduces one source of unsupported generation; it does not remove hallucination, source error, or the need for human judgment.

## Sources

- Patrick Lewis et al., *[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)*, 2020.
- Meta AI, *[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://ai.meta.com/research/publications/retrieval-augmented-generation-for-knowledge-intensive-nlp-tasks/)*.

## See also

- *[Retrieval-Augmented Generation](/entries/retrieval-augmented-generation/)*
- *[Embedding](/entries/embedding/)*
- *[Vector Database](/entries/vector-database/)*
- *[MCP (Model Context Protocol)](/entries/mcp/)*
- *[Agent Memory](/entries/agent-memory/)*
- *[Fine-Tuning](/entries/fine-tuning/)*
