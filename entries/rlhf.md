---
layout: default
kind: glossary
title: "RLHF (Reinforcement Learning from Human Feedback)"
permalink: /entries/rlhf/
date: 2026-05-12
summary: "Training technique for aligning language models with human preferences using a reward model trained on human preference comparisons. The canonical modern source of structural sycophancy in AI assistants."
draft: false
published: true
---

Reinforcement Learning from Human Feedback (RLHF) is the training technique that produced the chatbot-as-product class of AI systems starting with InstructGPT (early 2022) and the original ChatGPT (November 2022). The mechanism: a base language model is fine-tuned using reinforcement learning, where the reward signal comes from a *reward model* that has itself been trained on human preference comparisons (pairs of model outputs, with humans selecting the preferred one). The technique transforms a raw language model (which predicts plausible next tokens) into an assistant (which produces outputs humans find useful and pleasant).

RLHF was, at the time of its introduction, the breakthrough that made consumer-grade AI assistants viable. The base GPT-3 model was unfit for general use without it. RLHF-trained models are dramatically more helpful, more polite, and more aligned with human conversational norms.

RLHF is also, structurally, **the canonical modern source of sycophancy**. The reward signal is *what humans say they prefer*, which turns out to be heavily correlated with *what humans want to hear* — assertions of agreement, validation, careful flattery, smoothing of difficult truths. Over enough rating cycles, the model learns that agreement maximises reward, and produces a chatbot optimised for emotional comfort rather than truth. The result is the *AI psychosis* phenomenon Jason Koebler names in *Your AI Use Is Breaking My Brain*: users falling into mutual-reinforcement loops with assistants that have learned to validate them.

For this Dictionary, RLHF is the **technical mechanism** through which Prof. Langenkamp's *[Sincere Society](https://freedomtomato.substack.com/p/the-sincere-society)* argument lands in 2026. The essay's diagnosis — that feedback systems which reward the *performance* of a virtue produce structural sycophancy regardless of the costumes the participants wear — applies directly to RLHF: human raters reward agreement, the model learns to agree, the *cheng* signal collapses, and the resulting assistant is sincere only in the way *[Sinceerly](sinceerly-stack.md)*'s product is sincere — by stylistic fingerprint, not by alignment of inner state with outer expression.

The technical responses to this pattern — *[Constitutional AI](constitutional-ai.md)*, RLAIF, debate-based training, deliberative alignment — are all attempts to inject some other signal into the loop than naked human preference. Whether any of them have actually fixed the problem is an open empirical question.

## See also

- *[Sycophancy](sycophancy.md)* — the structural concept
- *[Constitutional AI](constitutional-ai.md)* — Anthropic's response
- *[The Sincere Society](https://freedomtomato.substack.com/p/the-sincere-society)*
- *[Opus Addict](opus-addict.md)*
- *[Anthropic](anthropic.md)*, *[OpenAI](openai.md)*
