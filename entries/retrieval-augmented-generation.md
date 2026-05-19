---
layout: default
kind: glossary
title: "Retrieval-Augmented Generation"
permalink: /entries/retrieval-augmented-generation/
date: 2026-05-16
summary: "The spelled-out form of RAG: generating answers with help from retrieved external documents or records."
draft: false
published: true
---

**Retrieval-Augmented Generation** is the full phrase behind **RAG**. A system retrieves relevant documents, chunks, memories, or database records and supplies them to a language model so the answer can be grounded in material outside the model's training weights.

The promise is simple: instead of asking the model to answer from memory, give it the relevant files. The reality is more delicate. Retrieval can fetch the wrong material, miss the right material, bury the important sentence, or combine sources in misleading ways. RAG improves groundedness, but it does not eliminate the need for provenance, evaluation, and human judgment.

This page is a spell-out companion to the shorter *RAG* entry.

## See also

- *[RAG](rag.md)*
- *[Vector database](vector-database.md)*
- *[Provenance](provenance.md)*
