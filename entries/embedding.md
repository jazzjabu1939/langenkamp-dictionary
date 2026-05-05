---
layout: default
title: "Embedding"
permalink: /entries/embedding/
summary: "meaning as a list of numbers; the foundation of semantic search and RAG."
---

# Embedding


---

## In one sentence

**An embedding is a list of numbers — typically a few hundred to a few thousand of them — that represents the meaning of a piece of text in a way that lets you measure how similar two texts are by measuring the distance between their lists.**

## Why embeddings exist

Computers are good at matching exact words. If you search for "bank loan" on a website that does string matching, you will only find pages that contain the exact phrase "bank loan." You will miss "credit facility," "line of credit," and "borrowing arrangement," even though they mean the same thing.

For decades, this was the central limitation of search and document retrieval. The cure was a long line of clever tricks — stemming, synonym expansion, hand-built thesauri — that helped a little but never closed the gap.

Embeddings closed it.

A trained embedding model takes a piece of text and produces a vector (a list of numbers) such that **texts with similar meanings produce vectors that are close to each other in space.** The phrase "bank loan" and the phrase "credit facility" land near each other. "Bank loan" and "river bank" land far apart. The same model can do this across documents, sentences, even single words.

This single innovation underpins almost every modern AI search and retrieval system, including all of RAG.

## What it actually does — concretely

```
"the M5 Max has 128 GB of unified memory"
    │
    ▼   (embedding model)
    │
    ▼
[0.0214, -0.1893, 0.4471, 0.0902, ..., -0.3115]
    └── a vector of, say, 1024 numbers ──┘
```

That vector is the embedding. By itself it means nothing to a human. But two different vectors can be compared — most commonly using **cosine similarity**, which essentially measures the angle between the two vectors:

- Cosine similarity ≈ 1.0 → very similar meaning
- Cosine similarity ≈ 0.0 → unrelated
- Cosine similarity < 0 → opposite meanings (rarer, depends on the model)

If you embed a thousand documents and store the resulting thousand vectors, you can answer "which of these documents is most relevant to this query?" by embedding the query and finding the closest vectors. This is **semantic search**.

## Working example — what the agent on this machine uses

When the agent on this MacBook calls `memory_search("M5 Max benchmark token speed")`, what happens under the hood is:

1. The query string is embedded into a vector using a small, locally-cached embedding model.
2. Every chunk of `MEMORY.md`, `memory/*.md`, and indexed session transcripts has been pre-embedded and stored.
3. The query vector is compared against the chunk vectors.
4. The top-scoring chunks are returned with their text and source line numbers.
5. The agent reads those chunks and decides which to follow up on with `memory_get`.

This is the same architecture that powers customer-service knowledge bases, legal-document retrieval, internal handbooks, and academic literature search. Different scale, same pattern.

## Where embeddings come from

- **Cloud embedding APIs** — OpenAI's `text-embedding-3-large`, Anthropic, Google, Cohere. Easy to use, pay per million tokens, your text leaves your environment to be embedded.
- **Open-source embedding models** — `nomic-embed-text`, `bge-large-en`, `gte-large`. Run locally via Ollama, llama.cpp, or sentence-transformers. Slightly lower quality than top-of-the-line cloud, but free and private.
- **Domain-trained embeddings** — for specialized corpora (legal, medical, scientific) there are embedding models trained specifically on that domain that significantly outperform general-purpose ones for that field.

The choice of embedding model matters more than people expect. A bad embedding model will return results that *look* similar by surface keywords but miss the deeper relationships.

## Why embeddings made the modern AI stack possible

Before embeddings became cheap and good (roughly 2019 onward), the dominant pattern for "AI that understands my documents" was:

- Build a hand-tuned keyword search.
- Or build a complex pipeline of NLP heuristics.
- Or train a custom model from scratch on your corpus.

After embeddings became cheap and good, the dominant pattern became:

- Run every document through an off-the-shelf embedding model.
- Store the vectors.
- Embed queries the same way and look up by similarity.

This collapsed weeks of bespoke engineering into a single afternoon. It is one of the largest productivity unlocks in software in the last decade and is invisible to most end users because it works.

## Why this matters in a teaching context

For BBA and MBA students, embeddings are the technology that turned **unstructured text into a queryable asset.** Every email archive, every set of meeting notes, every PDF library, every Slack history, every customer-support transcript — all of it became analytically tractable in a way it had not been before.

The strategic implication: organizations that have been *accumulating* unstructured content for years now own a latent asset they can put to use cheaply. Organizations that have been losing or shredding their unstructured records are going to wish they had not.

A second implication: embeddings are also a privacy concern. A vector built from a sensitive document still encodes the document's meaning. An attacker who can recover the embeddings (and a few public clues about the embedding model) can reconstruct quite a bit. The right framing: **treat your vector store with the same security posture as the source documents themselves.**

## Trade-offs

- **Quality varies by model.** Some embedding models conflate different topics that should be distinct; others miss similarities a human would obviously see. Worth testing.
- **They go stale.** When the embedding model changes (e.g., you upgrade), all your stored vectors are invalidated and have to be re-embedded.
- **Multilingual support is uneven.** A model trained mostly on English may produce poor embeddings for Chinese, Arabic, or Hindi.
- **Bias is encoded.** Embeddings inherit biases from their training data — gendered associations, stereotyped pairings, etc. This shows up in surprising ways at retrieval time.
- **Privacy as a process.** As above, embeddings encode meaning. Storing them is non-trivial from a compliance perspective.

---

*Related entries: `rag.md`, `vector-database.md`, `fine-tuning.md`.*
