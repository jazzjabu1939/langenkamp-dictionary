---
layout: default
title: "Open source"
permalink: /entries/open-source/
summary: "AI models whose trained weights are published publicly; one of the two large strategic camps in the model ecosystem."
---

# Open source

*One of the two large strategic camps in the contemporary AI model ecosystem; the term as it is used in 2026 carries some specific gotchas that the older free-software vocabulary did not.*

---

## In one sentence

**An *open-source* AI model is one whose weights — the trained parameter values — are published publicly so that anyone can download them, run them on their own hardware, modify them, and (usually) redistribute them; the term has accumulated some controversy because not every model labeled "open" actually meets the older free-software standards.**

## Why this term exists

The original "open source" movement, going back to the late 1990s, was about *source code* — the human-readable instructions that compile into running software. The user got the recipe, could read it, modify it, and rebuild the program from scratch.

Modern AI models break that model in interesting ways. The "source" of a language model is, arguably:

1. The training-time *code* (the algorithm that does the training)
2. The training *data* (the trillions of tokens fed in)
3. The trained *weights* (the resulting parameter blob)

Releasing the *weights* is the thing most labs mean when they say "open source." That is genuinely useful — you can run the model, modify it via fine-tuning, and use it commercially (often). But the *training data* is almost never released, and the *training code* is sometimes withheld. So the recipe is incomplete.

This has produced an ongoing argument in the AI community about whether models like Llama, Gemma, and Qwen are *really* open source, or just *open weights*. The older free-software purists say the latter is a marketing-friendly relabel that misses the point. The pragmatists argue that open weights provide most of the practical benefits to most users.

## What it actually does — concretely

When a model is published as open-weights, you typically get:

- The **model file** — the parameter blob, often hosted on Hugging Face or distributed via Ollama. Anywhere from 2 GB (a small 1B model) to several hundred GB (a frontier 405B model).
- A **license** — often permissive (Apache 2, MIT) but sometimes with restrictions (Meta's Llama license has some prohibitions on use by very large competitors; some "open" models have an acceptable-use policy).
- **Inference code** — open-source software like Ollama, llama.cpp, or vLLM that knows how to load and run the weights.

What you do *not* always get:

- The training data
- The training scripts
- The exact hyperparameters
- The intermediate model checkpoints
- The full safety-tuning recipe

That asymmetry is the modern open-source AI debate in one paragraph.

## Working example

Three open-weights models are the workhorses of the local-AI ecosystem in mid-2026:

- **Meta Llama 3.3 70B** — among the most capable open-weights models. License has some commercial restrictions but is usable for most academic and small-business contexts.
- **Google Gemma 4** (26B MoE, 31B dense) — fully released for commercial use; competitive on benchmarks. Available via Ollama, Hugging Face, and Google's own runtime.
- **Alibaba Qwen 2.5** (multiple sizes up to 72B) — strong general performance, especially on multilingual tasks; permissive license.

All three live on this MacBook's hard drive and can run without sending a single token to a cloud provider. None of the three released their full training data.

## Why this matters in a teaching context

For a BBA or MBA classroom, the open-source AI conversation is genuinely strategic. Three angles worth surfacing:

1. **Vendor independence.** An organization that builds critical workflows around a closed-source frontier model is at the mercy of price changes, terms-of-service updates, and API deprecations. Open weights are a hedge — you can always run the version you have, on hardware you control, indefinitely.

2. **The Llama bet.** Meta's strategy of releasing capable models open-weights is one of the clearest pieces of competitive AI positioning in the past three years. Worth working through with students: *why would Meta give away models that cost hundreds of millions of dollars to train?* (Hint: commoditize your complement.)

3. **The compliance puzzle.** Many regulated industries — healthcare, finance, defense — cannot use cloud-hosted closed models with sensitive data. Open-weights models on local hardware are the only viable path. This drives substantial enterprise adoption that does not show up in the trade press.

## Trade-offs

- **Inference cost is your problem.** With closed-source cloud APIs, the vendor handles the GPU bill. With open weights, you do.
- **Updates are not automatic.** When the lab releases an improved version, you must download and deploy it yourself.
- **Safety tuning may be lighter.** Some open models have noticeably less safety alignment than their closed counterparts.
- **Frontier capability lags.** As of mid-2026, the absolute top of the capability frontier (Claude Opus, GPT-5, Gemini Ultra) remains closed. Open-weights models are roughly 6-12 months behind on the hardest benchmarks. The gap is shrinking but real.
- **The "open" label is partial.** As discussed, the training data and full recipe are usually not included.

## Related and adjacent terms

- *Open weights* — the more accurate term for what most "open-source" AI models actually offer.
- *Closed source* — the strategic counterpart. See its own entry.
- *Hugging Face* — the public registry where most open-weights models live.
- *Llama license* / *Gemma license* — examples of "mostly open with some commercial restrictions."

---

*Related entries: [Closed source](closed-source.md), [Ollama](ollama.md), [Parameters](parameters.md).*
