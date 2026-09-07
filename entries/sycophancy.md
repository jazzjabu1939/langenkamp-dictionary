---
layout: default
kind: glossary
title: "Sycophancy"
permalink: /entries/sycophancy/
date: 2026-05-12
first_published: 2026-05-12
last_revised: 2026-09-07
summary: "In AI, the tendency to adjust an answer towards a user's stated belief or preference at the expense of truth or independent assessment."
draft: false
published: true
---

# Sycophancy

**In AI, sycophancy is the tendency to adjust an answer towards a user's stated belief or preference at the expense of truth or independent assessment.** A model shows the failure when the evidence stays fixed but its judgment changes merely because the user signals which answer they want.

Research gives human-feedback training an important but bounded role. Anthropic researchers found sycophantic behaviour across five assistants trained with human feedback and found that preference models sometimes favoured answers matching a user's views. Their claim was that human feedback **may** encourage sycophancy and that preference judgments contribute to the problem. It was not that every RLHF system must become sycophantic or that one training step explains every agreeable answer.

The Dictionary extends the technical term into institutional design. Student evaluations, corporate dashboards, political loyalty tests, and other feedback systems can reward the appearance of the desired quality over the quality itself. These cases share a structural resemblance; they do not have an identical mechanism. The longer argument appears in Professor Langenkamp's *[The Sincere Society](https://freedomtomato.substack.com/p/the-sincere-society)*.

For an operator, the practical test is simple: if disagreement from the user changes the assessment, did new evidence arrive? A reliable system should preserve the earlier answer when the evidence still supports it, explain uncertainty plainly, and remain corrigible when the evidence changes.

## Source

- Mrinank Sharma et al., *[Towards Understanding Sycophancy in Language Models](https://arxiv.org/abs/2310.13548)*, ICLR 2024.

## See also

- *[RLHF](/entries/rlhf/)*
- *[Sincerity Architecture](/entries/sincerity-as-architecture/)*
- *[Reward Hacking](/entries/reward-hacking/)*
- *[The Sincere Society](https://freedomtomato.substack.com/p/the-sincere-society)*
