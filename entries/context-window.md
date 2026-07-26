---
layout: default
kind: glossary
title: "Context Window"
permalink: /entries/context-window/
date: 2026-05-16
summary: "The amount of text, code, images, tool results, and conversation history a model can consider at one time."
draft: false
published: true
---

A model's **context window** is the working span of material it can attend to while generating an answer: the current prompt, relevant prior conversation, tool results, files, retrieved passages, and sometimes images or other modalities. It is the model's short-term operating field, not its permanent memory.

The concept matters because many AI failures are not failures of intelligence in the abstract. They are failures of visibility. The model cannot use what it cannot see, and it may overgeneralise from the part of the problem that fits inside the window. Larger context windows make longer documents and multi-file tasks possible, but they do not remove the need for structure. Important facts can still be buried, diluted, contradicted, or ignored.

For operators, context-window management is a real craft. Summaries, retrieval systems, prompt files, stable memory, and incremental construction all exist because dumping everything into the window is not the same as making the right things salient.

## See also

- *[Context Window Database Myth](context-window-database-myth.md)*
- *[RAG](rag.md)*
- *[Vector database](vector-database.md)*
- *[Incremental Construction](incremental-construction.md)*
