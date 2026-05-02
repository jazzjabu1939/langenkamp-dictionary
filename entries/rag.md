# RAG (Retrieval-Augmented Generation)


---

## In one sentence

**RAG (Retrieval-Augmented Generation) is the pattern of fetching relevant documents from a private corpus and pasting them into the AI model's prompt at query time, so the model can answer using your own data instead of relying solely on its frozen training knowledge.**

## Why RAG exists

A large language model knows a great deal about the world up to its training cutoff, but it does not know:

- Your company's internal handbook
- Your students' submitted work
- Your private research notes
- The contents of last week's emails
- Anything written after the model finished training

There are two ways to solve this:

1. **Fine-tune** the model — retrain it on your data. Expensive, slow, has to be redone whenever the data changes, and produces a model that "remembers" your data permanently (which can be a privacy and compliance problem).
2. **Retrieve** the relevant documents on demand and include them in the prompt — the model reads them in real time and answers from them. Cheap, fast, always up-to-date, and the data never permanently lives inside the model.

RAG is option 2. It has become the dominant pattern for "AI that knows my stuff" because it is dramatically simpler than fine-tuning for most use cases.

## What it actually does — the four-step loop

```
USER QUESTION
    │
    ▼
1. EMBED the question into a vector (a numerical fingerprint of meaning)
    │
    ▼
2. SEARCH a vector database for the chunks most similar to the question
    │
    ▼
3. ASSEMBLE a prompt that includes both the question and the retrieved chunks
    │
    ▼
4. SEND to the LLM, which generates an answer that draws on the chunks
    │
    ▼
ANSWER (with optional citations back to the source chunks)
```

The retrieval step is what makes it "augmented." The generation step is the normal LLM call. Together they let the model produce answers grounded in *your* corpus rather than its training data.

## The four standing pieces of a RAG system

1. **The corpus** — the source documents (PDFs, web pages, transcripts, notes).
2. **The embedding model** — a separate small model that converts text into vectors. (Local options exist; cloud options are common.)
3. **The vector store** — a database designed for fast similarity search across millions of vectors. Common choices: ChromaDB, Qdrant, Weaviate, Postgres with `pgvector`, Apple FoundationDB, or in-memory for small corpora.
4. **The retrieval logic** — code that takes a query, embeds it, searches the store, ranks results, and assembles the final prompt.

Each of these can be swapped without rewriting the others. That modularity is part of why RAG has spread so quickly.

## Working example from this machine

The OpenClaw setup on this MacBook uses a *lightweight, file-based* form of RAG via the **memory** system. When the agent needs to recall something, it does:

1. Calls `memory_search` with a query string.
2. The system performs a semantic search across `MEMORY.md`, `memory/*.md` daily files, and indexed session transcripts.
3. The most relevant chunks are returned with line numbers.
4. The agent then calls `memory_get` to read the specific lines it wants in detail.

This is RAG in miniature: a private corpus, semantic retrieval, and prompt-time augmentation. The corpus here is the user's own memory and notes, not a corporate document set, but the architecture is identical.

A scaled-up version of the same pattern would replace the markdown files with a vector database holding thousands of documents and add a more sophisticated ranking layer.

## RAG variants worth knowing

- **Naive RAG** — the simple loop described above. Good enough for many use cases.
- **Hybrid RAG** — combines vector search with traditional keyword search (BM25). Catches cases where exact terms matter (codes, acronyms, names).
- **Re-ranking RAG** — runs a second pass with a smaller model to reorder retrieved chunks by true relevance. Higher quality, slightly slower.
- **Agentic RAG** — the agent itself decides what to retrieve, can issue multiple searches, follows leads. More flexible, more expensive, harder to debug.
- **GraphRAG** — uses a knowledge graph layer on top of the documents to capture relationships between entities. Microsoft and others have published on this. Strong for analytical questions that need to "connect dots" across many documents.

## Why this matters in a teaching context

For an MBA classroom, RAG is the most consequential AI architectural pattern of 2024–2026 for one specific reason: **it lets organizations get useful AI value from their own private data without having to retrain the model.**

The economic and strategic implications:

- Every company sitting on a corpus of internal documents has a latent AI asset.
- The hard problem is not the model — it is the *data hygiene* (cleaning, chunking, indexing) and the *governance* (who can search what, audit logs, FERPA/HIPAA/GDPR compliance).
- The competitive advantage of a well-organized corpus shows up *only* when you put RAG on top of it. Companies that have neglected document management for a decade now find themselves at a disadvantage they did not realize they had.

This is the kind of operational point that translates well into strategy and operations courses. Classic question for a case discussion: *which functions inside a firm benefit most from RAG, and what does that imply about their data management investments over the next three years?*

## Trade-offs

- **Garbage in, garbage out.** If your corpus is poorly written, contradictory, or full of stale documents, RAG will surface that garbage and the model will dutifully repeat it.
- **Context-window cost.** Every retrieved chunk pasted into the prompt costs input tokens. Heavy retrieval = heavy bills. Hybrid approaches with re-ranking help.
- **Citation is not the same as truth.** A model can quote a retrieved chunk and still be wrong about what it means. RAG reduces hallucination but does not eliminate it.
- **Privacy is a process, not a checkbox.** Including private documents in the prompt sends them to the model provider. For sensitive data, the answer is to run RAG on top of a *local* model (e.g., Ollama) so nothing leaves your machine.
- **Chunking is hard.** Where you split documents, how big each chunk is, and what metadata you keep on each chunk all matter — and require iteration.

## RAG vs. fine-tuning — the simple version

|  | RAG | Fine-tuning |
|--|-----|-------------|
| Speed to set up | Days | Weeks to months |
| Cost per change | Cheap (re-index) | Expensive (re-train) |
| Stays current | Yes (always reads latest corpus) | No (frozen at training time) |
| Privacy | Documents leave at query time only | Documents permanently in model weights |
| Best for | Private knowledge bases, current data | Style, tone, domain-specific reasoning patterns |

In practice, most organizations should start with RAG. Fine-tuning is a later step for the small number of cases where the model needs to *behave* differently, not just know different things.

---

*Related entries: `embedding.md`, `vector-database.md`, *(planned)*.*
