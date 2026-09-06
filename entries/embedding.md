---
layout: default
kind: reference
title: "Embedding"
permalink: /entries/embedding/
date: 2026-05-02
summary: "A numerical representation that lets software compare and retrieve related items by their position in a learned vector space."
draft: false
published: true
---

# Embedding

## In one sentence

**An embedding is a numerical representation of an item—such as a word, passage, image, or user—that places related items near one another in a learned vector space.**

## Why embeddings exist

Exact-word search cannot by itself recognise that *credit facility* may be relevant to a query for *bank loan*. Search systems have long supplemented keywords with stemming, synonyms, statistical ranking, and other methods. Embeddings add another tool: they can retrieve material that is related in the model's representation even when the wording differs.

An embedding model converts an input into a vector, usually a list containing hundreds or thousands of numbers. Software can compare two vectors using a similarity measure. With a model trained for semantic retrieval, passages that are useful for the same query should generally receive more similar vectors than unrelated passages.

The qualification matters. An embedding is not meaning bottled as mathematics. It is a model's task-dependent representation, learned from particular data and judged by how well it performs on particular tests.

## What it does—concretely

```
"the M5 Max has 128 GB of unified memory"
    │
    ▼   (embedding model)
    │
    ▼
[0.0214, -0.1893, 0.4471, 0.0902, ..., -0.3115]
    └── a vector of, say, 1024 numbers ──┘
```

That vector is useful mainly in relation to other vectors produced by the same model. A common comparison is **cosine similarity**, which measures the angle between them. A higher score generally means greater similarity under that model. The score is not a universal semantic ruler: its range and interpretation depend on the model, its training, and the application. In particular, a negative cosine score does not automatically mean that two texts express opposite meanings.

To perform semantic search, a system can:

1. divide documents into passages;
2. embed and store those passages;
3. embed a user's query with the same model; and
4. return the passages whose vectors score as most similar.

This pattern is common in retrieval-augmented generation, though production search often combines vector retrieval with keywords, metadata filters, reranking, or other methods.

## A working example

When an agent runs a semantic memory search, the system can embed the query, compare it with previously indexed text chunks, and return the closest matches with their sources. The agent then reads the retrieved text and decides what is actually relevant. The precise index, model, and ranking pipeline vary by implementation; the durable idea is retrieval by learned similarity rather than exact wording alone.

The same broad pattern appears in customer-service knowledge bases, legal-document retrieval, internal handbooks, recommendation systems, and literature search.

## Where embeddings come from

- **Hosted embedding APIs.** Providers including OpenAI, Google, and Cohere expose models through paid APIs. They are convenient, but the text is sent to the provider under its applicable data terms.
- **Locally runnable models.** Families such as BGE, GTE, and Nomic can be run on local or controlled infrastructure. Quality, speed, language coverage, hardware needs, and licences vary; local does not automatically mean worse, free, or private.
- **Domain-specific models.** Legal, medical, scientific, and multilingual retrieval may benefit from models trained or tuned for those settings. Claims of superiority should be tested on the organisation's own queries and documents.

Changing models usually requires re-embedding the indexed collection because vectors from different embedding spaces are not safely interchangeable.

## Why this matters in a teaching context

Embeddings help turn unstructured material—emails, reports, transcripts, and document archives—into something that can be searched by approximate conceptual relevance. That can make an old document collection operationally useful. It does not make the collection clean, complete, lawful to use, or correct.

Embeddings also deserve the security posture of the source material. Research on **embedding inversion** has shown that text can sometimes be partially or substantially reconstructed from its vectors under favourable attack conditions. An embedding is therefore not anonymisation or encryption. Access controls, retention rules, and vendor review still matter.

## Trade-offs

- **Retrieval quality is empirical.** Test models on representative queries rather than trusting a leaderboard alone.
- **Similarity is not truth.** A close passage may be irrelevant, outdated, or wrong.
- **Migration has a cost.** A new model generally means re-embedding the collection and retesting retrieval.
- **Multilingual performance varies.** Strong English retrieval does not imply strong Chinese, Arabic, or Hindi retrieval.
- **Bias can enter retrieval.** Learned associations can affect which results are treated as close and therefore visible.
- **Vectors remain sensitive data.** Restrict access as though reconstruction or attribute inference may be possible.

## Sources

- OpenAI, [Vector embeddings](https://developers.openai.com/api/docs/guides/embeddings).
- Sentence Transformers, [Semantic Search](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html).
- John X. Morris et al., [*Text Embeddings Reveal (Almost) As Much As Text*](https://arxiv.org/abs/2310.06816), 2023.

## See also

*[Retrieval-Augmented Generation](/entries/rag/)* · *[Vector Database](/entries/vector-database/)* · *[Fine-Tuning](/entries/fine-tuning/)*
