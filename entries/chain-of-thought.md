---
layout: default
kind: glossary
title: "Chain of Thought"
permalink: /entries/chain-of-thought/
date: 2026-05-16
summary: "A model’s stepwise reasoning trace, or the prompted imitation of such a trace; useful, contested, and not identical to reliable explanation."
draft: false
published: true
---

**Chain of thought** refers to stepwise reasoning written out by a model, or prompted from a model, while solving a problem. It became important because models often perform better when encouraged to reason through intermediate steps rather than jump directly to an answer.

The phrase is slippery. Sometimes the visible chain is useful work: decomposing a problem, tracking assumptions, catching arithmetic, or making a decision auditable. Sometimes it is a post-hoc rationalisation: fluent explanation after the model has already landed on an answer. Modern systems may also hide internal reasoning while providing a shorter summary, for safety, privacy, or product reasons.

For operators, the practical lesson is modest. Stepwise reasoning can improve work, but it should not be treated as a guaranteed window into the model's mind. The proof remains in the answer, the evidence, the checks, and the result.

## See also

- *[Reasoning Model](reasoning-model.md)*
- *[Approximate Turing Machine](approximate-turing-machine.md)*
- *[Hallucination](hallucination.md)*
