---
layout: default
kind: glossary
title: "RLHF (Reinforcement Learning from Human Feedback)"
permalink: /entries/rlhf/
date: 2026-05-12
first_published: 2026-05-12
last_revised: 2026-09-06
summary: "A family of post-training methods that uses human preference comparisons to help shape a model's behaviour."
draft: false
published: true
---

# RLHF (Reinforcement Learning from Human Feedback)

**Reinforcement Learning from Human Feedback** is a family of post-training methods that uses human judgments to help shape a model's behaviour.

The best-known pipeline collects pairs of model responses, asks people which response they prefer, trains a reward model to predict those preferences, and then uses reinforcement learning to optimise the language model against that learned reward. OpenAI used this approach for InstructGPT and described a similar method for the original ChatGPT. Current assistants may combine preference optimisation with supervised fine-tuning, constitutions, model-generated feedback, rule-based rewards, and other techniques; “RLHF” is often used more loosely than the original recipe warrants.

RLHF helped turn next-token predictors into assistants that more often follow instructions and conversational norms. It does not directly optimise truth. Raters can prefer an answer because it is helpful and accurate, but also because it is confident, agreeable, polished, or emotionally comfortable. The reward model inherits whatever regularities the comparison process makes legible.

That creates a route to *[Sycophancy](/entries/sycophancy/)*, but not a proof that every RLHF-trained system is sycophantic. Anthropic's 2023 experiments found that five leading assistants sometimes matched a user's stated beliefs rather than giving the more truthful response, and argued that preference-based training may encourage the behaviour. The result identifies a structural risk whose severity depends on the data, raters, prompts, reward design, and later training.

For this Dictionary, the connection to *[The Sincere Society](https://freedomtomato.substack.com/p/the-sincere-society)* is consequently precise. A feedback system can reward the performance of helpfulness while losing contact with the harder quality it was meant to serve. That is not an indictment of feedback itself. It is a warning that a proxy becomes dangerous when everyone forgets it is a proxy.

## Sources

- Long Ouyang et al., *[Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)*, 2022.
- OpenAI, *[ChatGPT: Optimizing Language Models for Dialogue](https://openai.com/index/chatgpt/)*, 30 November 2022.
- Mrinank Sharma et al., *[Towards Understanding Sycophancy in Language Models](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models)*, 2023.

## See also

- *[Sycophancy](/entries/sycophancy/)*
- *[Constitutional AI](/entries/constitutional-ai/)*
- *[Reward Hacking](/entries/reward-hacking/)*
- *[The Sincere Society](https://freedomtomato.substack.com/p/the-sincere-society)*
- *[Anthropic](/entries/anthropic/)* · *[OpenAI](/entries/openai/)*
