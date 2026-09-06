---
layout: default
kind: reference
title: "Fine-tuning"
permalink: /entries/fine-tuning/
date: 2026-05-02
summary: "Continuing a pre-trained model's training on task-specific examples to alter its behaviour or performance."
draft: false
published: true
---

# Fine-tuning


---

## In one sentence

**Fine-tuning continues the training of a pre-trained model on task-specific examples, updating all or some of its parameters so that it performs a desired task or behaviour more reliably.**

## Why fine-tuning exists

A pre-trained language model is a generalist. It may not follow a firm's conventions, produce a required output reliably, or handle a specialised task well. Three common interventions are:

1. **Prompt engineering** — supply clearer instructions and examples at query time.
2. **[RAG](/entries/rag/)** — retrieve relevant material at query time and place it in the model's context.
3. **Fine-tuning** — train on examples so the model's parameters change.

Fine-tuning is the heaviest of the three. Most projects should start with the lighter options and only reach for fine-tuning when those genuinely run out of road.

## What it actually does — concretely

Pre-training a frontier model from scratch requires enormous datasets and compute. Fine-tuning is the cheaper sibling: take an already-trained model and continue training it for a smaller number of steps on a focused dataset.

Three common varieties:

- **Supervised fine-tuning (SFT)** — train on example inputs paired with desired outputs.
- **Preference-based post-training** — methods such as RLHF and Direct Preference Optimization use preference information to favour some responses over others, although they optimise that information differently.
- **Parameter-efficient fine-tuning (PEFT)** — methods such as LoRA freeze the base weights and train comparatively small adapter matrices. This can sharply reduce the trainable parameter count and memory required, but it does not guarantee the same result as full fine-tuning on every task.

## Where fine-tuning genuinely beats RAG

RAG is brilliant for "the model needs to know things from my corpus." Fine-tuning is the right move when one of these is true:

- **Repeated behaviour remains unreliable after good prompting and examples.** Tone, classification conventions, or a stable response format may improve with fine-tuning.
- **A specialised task is poorly handled by the base model.** Fine-tuning can improve performance when the training examples genuinely represent the task.
- **Latency or token cost matters.** A fine-tuned smaller model may replace a larger model or shorten a long prompt, but this is an empirical result to test rather than assume.
- **You have representative data and a held-out evaluation.** Example count alone is not decisive; quality, coverage, and measurement matter more than a magic threshold.

If none of these apply, prompting, retrieval, application logic, or structured-output controls may solve the problem with less machinery.

## Working example — a hypothetical for an Isenberg context

Imagine a management department wanted an AI tutor for case-method discussion with a defined level of rigour and a consistent Socratic style. The pieces might be:

- **Base model:** a capable model whose licence and deployment fit the institution's constraints.
- **Training data:** permissioned, carefully curated examples of strong instructor moves, separated from an evaluation set.
- **Method:** supervised or parameter-efficient fine-tuning aimed at specified behaviours.
- **Test:** compare the adapted model with the base model, good prompting, and retrieval on unseen discussions.

The pre-conditions are non-trivial: someone has to define good tutoring, curate examples, obtain the necessary permissions, protect student records, and design an evaluation capable of proving improvement. **The data and evaluation work, again, are the hard parts.**

## Why this matters in a teaching context

For BBA and MBA students, the strategic point is that model adaptation has become more accessible through vendor services and open-source tooling. The managerial difficulty has therefore moved towards deciding *whether* to fine-tune, securing suitable data, and evaluating the result. Product availability changes quickly; it should not be treated as part of the definition.

The strategic point worth surfacing in class: **the bottleneck has moved from compute to data quality and evaluation.** Most organizations that fail at fine-tuning fail because they had garbage training data or no honest way to measure whether the fine-tuned model actually does better than the base model on real tasks. Both problems are organizational, not technical.

## Fine-tuning vs. RAG — when to use which

|  | Fine-tuning | RAG |
|--|-------------|-----|
| Speed to change | Requires another training run | Update or re-index the corpus |
| Current information | Limited to training and other model context | Can retrieve the current corpus |
| Main data risk | Training examples may be memorised or exposed through the training pipeline | Retrieved material is exposed to every component serving the query |
| Best for | Style, tone, domain language, output formats | Private knowledge bases, current data |
| Model size impact | Can let you use a smaller, faster model | Generally needs a capable base model |

The two are not mutually exclusive. Many production systems use **both**: fine-tune the model for tone and behaviour; layer RAG on top for current knowledge. They solve different problems.

## Trade-offs

- **You may forget what you wanted to keep.** Fine-tuning can degrade general capabilities — a model fine-tuned to be very good at one task sometimes gets worse at unrelated tasks. Worth measuring before and after on a broad eval suite.
- **Data quality dominates.** Bad training data produces a bad fine-tuned model, full stop. The temptation to fine-tune on whatever you have lying around is strong and usually wrong.
- **Evaluation is the real bottleneck.** "Is the fine-tuned model actually better?" is harder to answer than it sounds. Without honest evaluation, you can spend a lot fine-tuning your way backward.
- **Updates require care.** Patterns learned through fine-tuning are not edited like rows in a database. Correcting stale or harmful behaviour may require new data and another training run.
- **Training data can be memorised.** Fine-tuning does not turn documents into a searchable database, but models can reproduce training examples. Sensitive data therefore requires permission, minimisation, security controls, and leakage testing. RAG carries different risks because the retriever, index, prompt, logs, and model may all handle the retrieved text.

## Sources

- OpenAI, *Supervised fine-tuning*: <https://platform.openai.com/docs/guides/supervised-fine-tuning>
- Edward J. Hu et al., *LoRA: Low-Rank Adaptation of Large Language Models*, 2021: <https://arxiv.org/abs/2106.09685>
- Patrick Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*, 2020: <https://arxiv.org/abs/2005.11401>

---

*[RAG](/entries/rag/)* · *[Embedding](/entries/embedding/)*
