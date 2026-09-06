---
layout: default
kind: glossary
title: "Hallucination"
permalink: /entries/hallucination/
date: 2026-05-16
summary: "The common but imperfect name for an AI system producing confident output unsupported by its sources, context, or the world."
draft: false
published: true
---

**Hallucination** is the standard term for an AI system producing an answer that sounds plausible but is not supported by the available evidence, context, or reality. The term is useful because everyone now recognises it. It is also imperfect, because it makes the error sound like a strange mental episode rather than a predictable property of a probabilistic text generator under uncertainty.

A model does not know the difference between *I have evidence for this* and *this continuation sounds likely* unless the system around it makes that distinction visible and valuable. Retrieval, citations, tool use, provenance records, and human review are all attempts to reduce hallucination by tying output back to external reality.

Not every wrong answer is a hallucination. Some are stale knowledge, ambiguous instructions, missing context, arithmetic failure, overconfident synthesis, or a user asking for something no one could know. The practical question is less *did the model hallucinate?* than *what evidence trail would have caught this before it mattered?*

## See also

- *[Hallucination Frequency Myth](/entries/hallucination-frequency-myth/)*
- *[RAG](/entries/rag/)*
- *[Provenance](/entries/provenance/)*
- *[Context Window](/entries/context-window/)*
