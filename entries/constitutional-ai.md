---
layout: default
kind: glossary
title: "Constitutional AI"
permalink: /entries/constitutional-ai/
date: 2026-05-12
summary: "Anthropic's approach to training language models to be helpful and harmless using a written *constitution* of behavioural principles — rather than purely relying on human-labelled preference data."
draft: false
published: true
---

Constitutional AI (often abbreviated *CAI*) is the training methodology developed by *[Anthropic](anthropic.md)* for producing language models that are helpful and avoid harms without relying solely on human-labelled preference data. The approach was introduced in the 2022 paper *Constitutional AI: Harmlessness from AI Feedback* (Bai et al.).

The mechanism: a written *constitution* — a list of principles drawn from sources including the UN Declaration of Human Rights, parts of Apple's terms of service, and Anthropic's own safety research — is used to guide the model's self-critique and revision during training. The model produces a response to a prompt, critiques the response against the constitution, revises it, and the revised response becomes the training target. This *Reinforcement Learning from AI Feedback* (RLAIF) layer is meant to complement rather than fully replace traditional *[RLHF](rlhf.md)*, and is one of the core differentiators Anthropic claims for the *[Claude](claude.md)* model family relative to pure-RLHF peers.

For this Dictionary, Constitutional AI matters as one of the **technical responses to the sycophancy diagnosis** developed in *[The Sincere Society](https://freedomtomato.substack.com/p/the-sincere-society)*. The essay argues that *cheng* — alignment of inner state with outer expression — must be designed into the feedback loop, or it will not appear. Constitutional AI is one attempt at that design: a structured set of principles that the model can apply to its own outputs at training time, rather than relying entirely on human-rater preferences (which produce sycophancy as a side effect). Whether the approach actually delivers more *cheng*-aligned models in practice is the kind of empirical claim the Dictionary tracks but does not settle.

## See also

- *[Anthropic](anthropic.md)*
- *[Claude](claude.md)* — the model family trained with this approach
- *[RLHF](rlhf.md)* — the broader category
- *[Sycophancy](sycophancy.md)*
- *[The Sincere Society](https://freedomtomato.substack.com/p/the-sincere-society)*
