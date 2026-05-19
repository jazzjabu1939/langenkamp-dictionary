---
layout: default
title: "Vector Database"
permalink: /entries/vector-database/
summary: "specialized storage and retrieval infrastructure for embeddings."
---

# Vector Database


---

## In one sentence

**A vector database is a specialized database designed to store millions of embeddings and answer the question "which of these are most similar to this one?" very quickly.**

## Why vector databases exist

Once embeddings became central to how AI systems retrieve information (see `embedding.md`), a new operational problem appeared: how do you search across a million vectors fast enough for a real-time chatbot?

A naive approach — comparing the query vector against every stored vector one by one — works for a thousand documents but breaks down at a million. The math is unforgiving: a million 1024-dimensional dot products per query is too slow.

Vector databases solve this with **approximate nearest-neighbor (ANN) algorithms**: index structures that can return the top 10 most similar vectors out of a million in tens of milliseconds, with very high but not perfect recall. The "approximate" part is a deliberate trade — exact-nearest-neighbor search is too slow at scale, and 99% accuracy on the top-10 is good enough for almost every real use case.

## What they actually do — concretely

A vector database typically offers four operations:

| Operation | What it does |
|-----------|--------------|
| `insert` | Add a new vector with metadata (source document, timestamp, tags, etc.) |
| `search` | Given a query vector, return the top-K most similar vectors |
| `update` | Replace an existing vector |
| `delete` | Remove a vector |

On top of these, modern vector databases add features like:
- **Hybrid search** — combine vector similarity with traditional keyword filters ("most relevant articles about taxes, but only ones from 2024")
- **Metadata filters** — narrow searches by tag, date range, source, user permission
- **Multi-tenancy** — separate vector spaces per customer, project, or user
- **Backup, replication, sharding** — the usual database operational concerns

## The major players (mid-2026)

- **Open-source, self-hosted**: ChromaDB (small projects, easy to run), Qdrant (Rust, fast), Weaviate (feature-rich), Milvus (large-scale), pgvector (Postgres extension — popular because you keep one database)
- **Hosted/cloud**: Pinecone (the original commercial player), Weaviate Cloud, Qdrant Cloud, Turbopuffer
- **Cloud platforms with vector features built in**: AWS OpenSearch, Azure AI Search, Google Vertex AI, Snowflake Cortex Search
- **In-process / "small" options**: SQLite with vector extensions, Apple FoundationDB, in-memory libraries like FAISS

The right choice is almost always **start small, scale later**. A research project or pilot can run perfectly well in pgvector or Chroma on a laptop. The need for Pinecone or Milvus shows up at multi-million-vector scale.

## Working example — what scaled-up RAG would look like for a teaching project

Suppose the Isenberg Management Department wanted to build a RAG-based teaching assistant that knows the department's syllabi, lecture transcripts, AACSB documents, and faculty research from the past five years. A reasonable architecture:

1. **Corpus** — roughly 10,000 documents (PDFs, transcripts, web pages).
2. **Chunking** — split each document into ~500-token chunks. Estimated ~200,000 chunks total.
3. **Embedding model** — `nomic-embed-text` or similar, run locally to keep student data on-premises.
4. **Vector database** — pgvector (because the department probably already runs Postgres), or Qdrant if a dedicated service is preferred.
5. **Storage** — 200,000 vectors at 1024 dimensions × 4 bytes ≈ 800 MB. Trivial.
6. **Query path** — a question goes in, gets embedded, top-15 chunks are retrieved, an LLM generates an answer with citations.

The vector database is one piece of an operational system that also requires document ingestion pipelines, periodic re-indexing as new documents arrive, monitoring, and access control. **The vector database itself is rarely the hard part. Data hygiene around it is.**

## Why this matters in a teaching context

For BBA and MBA students, vector databases are interesting because they sit at the intersection of three trends:

1. **The "AI-on-private-data" boom** — every organization wants to do this.
2. **The data infrastructure renaissance** — Postgres, ClickHouse, DuckDB, Snowflake, etc. are getting AI-native features.
3. **The embedded-AI pattern** — vector search is now showing up inside CRMs, knowledge bases, IDEs, email clients, and document editors as a standard feature, not an exotic add-on.

The strategic question worth raising in a class discussion: *for a given organization, is a vector database a strategic asset, an operational utility, or a commodity component?* The answer differs by industry. A law firm whose competitive edge depends on its archive of past matters has a strategic asset. A retail brand using vector search to recommend products has an operational utility. A small business adding semantic search to its internal handbook has a commodity component.

## Trade-offs

- **Operational overhead.** A separate database is a separate thing to monitor, back up, secure, and upgrade. The "use Postgres for vectors too" approach (pgvector) often wins on operational simplicity even if dedicated vector DBs win on raw performance.
- **Re-indexing is the real cost.** When the embedding model changes, every stored vector becomes useless and the whole corpus has to be re-embedded. At small scale this is a coffee-break job. At multi-million-vector scale it is a serious project.
- **Recall vs. latency vs. cost** — these three are always in tension. Different ANN algorithms (HNSW, IVF, ScaNN) trade them differently. Worth doing real measurements rather than trusting vendor claims.
- **Privacy.** As with embeddings themselves, the vectors encode meaning. The vector store is sensitive data. Worth treating it as carefully as the source documents.
- **Cost can sneak up.** Hosted vector services typically charge per stored vector and per query. A fast-growing app can produce a surprisingly large bill if no one is watching.

---

*Related entries: `embedding.md`, `rag.md`, *(planned)*.*
