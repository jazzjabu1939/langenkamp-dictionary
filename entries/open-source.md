---
layout: default
kind: reference
title: "Open source"
permalink: /entries/open-source/
date: 2026-05-02
summary: "an AI system released with the freedoms and materials required to use, study, modify, and share it—not merely a model whose trained weights can be downloaded."
published: true
first_published: 2026-05-02
last_revised: 2026-09-06
---

# Open source

## In one sentence

**Open-source AI gives people the freedoms and practical materials required to use, study, modify, and share the system; releasing trained weights alone creates an open-weight model, which may or may not meet that fuller standard.**

## Why the distinction matters

Traditional open-source software distributes source code: the preferred form in which a person studies and changes the program. A trained model complicates that idea. Its important ingredients include:

1. the code used to train and run it,
2. information about the training data and how it was prepared,
3. the resulting weights and configuration,
4. and a licence that grants meaningful rights to use, study, modify, and redistribute the system.

Many releases called “open source” publish the weights but not the full training data or reproducible training recipe. Their licences may also restrict certain users or uses. Those releases can still be valuable: operators can run them locally, fine-tune them where permitted, inspect their behavior, and keep a usable version even if a hosted service changes. The accurate category is usually **open weights**.

The Open Source Initiative published version 1.0 of its Open Source AI Definition on 28 October 2024. The definition requires the freedoms to use, study, modify, and share the system, together with sufficient information and components to exercise those freedoms. For training data, it requires detailed information about provenance, scope, acquisition, selection, labelling, and processing; it does not require release of the complete dataset. The debate is not semantic housekeeping. It determines what an operator can actually reproduce, audit, change, and redistribute.

Genuinely open-source AI systems do exist. OSI's validation exercise identified EleutherAI's **Pythia** and AI2's **OLMo**, among others, as systems that met the definition. These examples matter because they show that *open source* is a practicable category, not merely a standard used to disqualify open-weight releases.

## What an open-weight release usually includes

- Model weights and configuration files.
- Inference code or compatibility with open runtimes such as Ollama, llama.cpp, MLX, or vLLM.
- A model card describing architecture, evaluations, and intended uses.
- A licence, which must be read rather than inferred from the word *open*.

It may omit the original data, data-processing pipeline, training code, hyperparameters, intermediate checkpoints, and full post-training recipe. Without those materials, the released artifact can be runnable without being reproducible from its sources.

## Strategic value

Open-weight models provide three durable options:

1. **Local operation.** Sensitive work can stay on infrastructure the operator controls, subject to the surrounding software and security design.
2. **Vendor leverage.** A downloadable artifact cannot be repriced or withdrawn in the same way as an API, although updates, hardware, and support remain the operator's responsibility.
3. **Independent evaluation.** Researchers and users can probe, fine-tune, quantize, and compare the released artifact rather than relying entirely on a vendor's hosted interface.

None of these benefits requires pretending that every open-weight release is open source.

## Trade-offs

- **The operator pays for inference and operations.** Hardware, electricity, deployment, monitoring, and security do not disappear.
- **Capability is task-specific.** A closed model may lead on one workload while an open-weight model is preferable on privacy, cost, latency, language, or control. A frozen “months behind” estimate ages badly.
- **Licences differ.** Some releases use standard open-source licences; others impose commercial, acceptable-use, or scale restrictions.
- **Auditability has limits.** Access to weights expands the inspection surface, but weights alone do not reveal the training corpus or guarantee trustworthy behavior.

## See also

*[Open Weights](/entries/open-weights/)* · *[Closed Source](/entries/closed-source/)* · *[Ollama](/entries/ollama/)* · *[Hugging Face](/entries/hugging-face/)* · *[Llama](/entries/llama/)*

## Sources

- Open Source Initiative, *The Open Source AI Definition*: <https://opensource.org/ai/open-source-ai-definition>
- Open Source Initiative, *The Open Source Initiative Announces the Release of the Industry's First Open Source AI Definition* (28 October 2024): <https://opensource.org/blog/the-open-source-initiative-announces-the-release-of-the-industrys-first-open-source-ai-definition>
- Open Source Initiative, *OSAID FAQs* (validation examples): <https://opensource.org/ai/faq>
- Open Source Initiative, *Open Weights*: <https://opensource.org/ai/open-weights>
