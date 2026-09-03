---
layout: default
kind: reference
title: "Fine-tuning"
permalink: /entries/fine-tuning/
summary: "when to retrain a model on your own data, and when not to."
---

# Fine-tuning


---

## In one sentence

**Fine-tuning is the process of taking a pre-trained large language model and continuing its training on a smaller, specific dataset so the model permanently learns new behaviour, style, or domain knowledge that lives inside its own weights rather than being passed in at query time.**

## Why fine-tuning exists

A pre-trained language model is a generalist. It has read a great deal but knows nothing about the specifics of your firm, your tone of voice, or the quirks of your domain. There are three ways to address that:

1. **Prompt engineering** — write better instructions in the prompt. Fast, free, but limited.
2. **RAG** — fetch relevant documents at query time and paste them into the prompt. Fast to set up, stays current, no model retraining required. (See `rag.md`.)
3. **Fine-tuning** — actually retrain the model on your data so it learns the patterns directly. Slower, more expensive, but produces a model that *behaves* differently, not just one that *knows* differently.

Fine-tuning is the heaviest of the three. Most projects should start with the lighter options and only reach for fine-tuning when those genuinely run out of road.

## What it actually does — concretely

Pre-training a frontier model from scratch is a months-long, billion-token, millions-of-dollars effort. Fine-tuning is the much cheaper sibling: take an already-trained model and continue its training for a relatively small number of steps on a focused dataset.

Three common varieties:

- **Supervised fine-tuning (SFT)** — show the model thousands of input-output pairs ("here is a customer email; here is the ideal reply"). The model learns to produce outputs that look like the training answers.
- **Reinforcement learning from human feedback (RLHF) / Direct Preference Optimization (DPO)** — show the model pairs of better and worse outputs and let it learn the preference. Used heavily by frontier labs to align their models.
- **Parameter-efficient fine-tuning (PEFT) / LoRA** — instead of updating all model weights, train a small set of *adapter weights* that bolt onto the base model. Much cheaper, similar effect for most use cases. The dominant approach in practice.

## Where fine-tuning genuinely beats RAG

RAG is brilliant for "the model needs to know things from my corpus." Fine-tuning is the right move when one of these is true:

- **You need a specific behaviour, not specific knowledge.** Speak in our company tone. Always answer in this format. Never use these forbidden phrases. Behaviour lives in weights, not in prompts.
- **You have a domain language the base model handles poorly.** Niche legal terminology, medical shorthand, your company's internal acronyms. Fine-tuning can teach the model the language properly.
- **You need consistent output schemas.** A fine-tuned model will reliably emit JSON in your exact shape; a prompted base model is more variable.
- **Latency matters.** Fine-tuning lets you use a smaller model that has been specialized to your task, which is faster and cheaper to run than a big general model with a long RAG prompt.
- **You have lots of data.** Tens of thousands of high-quality examples is when fine-tuning starts to outperform pure prompting.

If none of these apply, RAG plus good prompting is almost always the right choice.

## Working example — a hypothetical for an Isenberg context

Imagine the Management Department wanted an AI tutor for case-method discussion that *talks like Isenberg faculty do* — same level of rigour, same vocabulary, same Socratic style. The pieces:

- **Base model**: a capable open-weights model, e.g., Llama 3.3 70B or Qwen 2.5 72B.
- **Training data**: ~5,000 well-curated case-discussion transcripts, with each turn labeled by role (instructor / student) and quality.
- **Method**: LoRA fine-tuning on the instructor turns, optimizing for the rigour and style markers that distinguish good case discussion from generic chatter.
- **Result**: a specialized model that does case-method tutoring noticeably better than the base model with a clever prompt.

The cost of doing this in 2026 is no longer prohibitive — a one-time LoRA fine-tune on a 70B model can be run for a few thousand dollars, and the resulting adapter weights are tiny (megabytes) and easy to share among colleagues.

The pre-conditions, though, are non-trivial: someone has to *curate* those 5,000 transcripts, with quality labels, with permissions, with FERPA-clean handling. **The data work, again, is the hard part.**

## Why this matters in a teaching context

For BBA and MBA students, fine-tuning is interesting because of where the cost has moved over the past three years:

- 2022: fine-tuning a useful model required a team of researchers and serious infrastructure.
- 2024: fine-tuning was straightforward for any competent developer with a credit card.
- 2026: fine-tuning is increasingly a self-service product (OpenAI fine-tuning, Anthropic fine-tuning, AWS Bedrock fine-tuning, on-prem with LoRA). The skill is shifting from *how to fine-tune* to *whether you should and how to evaluate the result*.

The strategic point worth surfacing in class: **the bottleneck has moved from compute to data quality and evaluation.** Most organizations that fail at fine-tuning fail because they had garbage training data or no honest way to measure whether the fine-tuned model actually does better than the base model on real tasks. Both problems are organizational, not technical.

## Fine-tuning vs. RAG — when to use which

|  | Fine-tuning | RAG |
|--|-------------|-----|
| Speed to deploy | Days to weeks | Hours to days |
| Cost per change | Expensive (re-train) | Cheap (re-index) |
| Stays current | No (frozen at training time) | Yes (always reads latest corpus) |
| Privacy | Documents permanently in weights | Documents leave at query time only |
| Best for | Style, tone, domain language, output formats | Private knowledge bases, current data |
| Model size impact | Can let you use a smaller, faster model | Generally needs a capable base model |

The two are not mutually exclusive. Many production systems use **both**: fine-tune the model for tone and behaviour; layer RAG on top for current knowledge. They solve different problems.

## Trade-offs

- **You may forget what you wanted to keep.** Fine-tuning can degrade general capabilities — a model fine-tuned to be very good at one task sometimes gets worse at unrelated tasks. Worth measuring before and after on a broad eval suite.
- **Data quality dominates.** Bad training data produces a bad fine-tuned model, full stop. The temptation to fine-tune on whatever you have lying around is strong and usually wrong.
- **Evaluation is the real bottleneck.** "Is the fine-tuned model actually better?" is harder to answer than it sounds. Without honest evaluation, you can spend a lot fine-tuning your way backward.
- **Permanence cuts both ways.** Knowledge fine-tuned in is hard to update. If your training data contains a mistake or stale info, that mistake is now baked into the model.
- **Privacy lives in the weights.** Once private data is fine-tuned in, it is in the weights. If those weights leak or are sold or are subpoenaed, the data is in there. RAG keeps the data outside the model.

---

*Related entries: `rag.md`, `embedding.md`, *(planned)*.*
