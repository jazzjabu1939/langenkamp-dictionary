---
layout: default
kind: reference
title: "Parameters"
permalink: /entries/parameters/
date: 2026-05-02
summary: "Learned numerical values inside a model; parameter count describes model scale and memory requirements, not quality by itself."
published: true
first_published: 2026-05-02
last_revised: 2026-09-06
---

# Parameters

## In one sentence

**A parameter is a learned numerical value inside a model; parameter count describes the scale of the model's learned machinery, not its quality by itself.**

## What the number means

A neural network contains matrices of learned values, usually called weights, along with other learned quantities such as biases. Training adjusts those values so that the network becomes better at its task. The resulting knowledge is distributed across a numerical system whose behaviour depends on many values acting together; it is not a database with one fact stored in each slot.

Parameter count is therefore a structural measure. It helps estimate the storage and memory required for the weights, and it gives some indication of the amount of learned capacity available. It does not tell you which data trained the model, how well it was trained, whether its architecture is efficient, how it was aligned, or how it performs on the work you care about.

## The useful memory arithmetic

For a dense model with seven billion parameters, storing every parameter at four bits gives a theoretical weight payload of about 3.5 gigabytes:

`7 billion × 4 bits ÷ 8 = 3.5 billion bytes`

That is a lower bound, not a complete deployment estimate. File formats add metadata and quantisation scales. A running model also needs memory for activations, runtime buffers, and the key-value cache used to hold context. Different quantisation methods may use different bit widths for different parts of the model. Parameter count is useful for the first fit calculation; the actual model file and runtime are the final answer.

## Dense and mixture-of-experts counts

A dense model uses its main learned layers for every token. A sparse *[Mixture of Experts](/entries/mixture-of-experts/)* model stores many expert networks but routes each token through only a subset. Its model card may therefore report both **total parameters** and **active parameters per token**.

The distinction matters. Total parameters help describe weight storage and the model's overall architecture. Active parameters help describe part of the per-token computation. Neither number, alone, is a performance score. Routing, attention, memory traffic, quantisation, software, hardware, batching, training, and the task all affect what the operator observes.

## Why the headline can mislead

Within one carefully controlled model family, scaling parameter count may improve capability. Across unrelated models, the comparison is much weaker. A smaller model can outperform a larger one because of better data, architecture, training, fine-tuning, or tool support. An MoE model with a very large total count can require substantial memory while using much less arithmetic per token than a dense model of the same headline size.

For a management classroom, this is the useful lesson: **a headline number is a starting point, not an answer.** Revenue without revenue quality, headcount without role mix, and patent count without patent value create the same analytical trap.

## Sources

- Google, *[Machine Learning Glossary: model parameters](https://developers.google.com/machine-learning/glossary#model-parameters)*.
- Google DeepMind, *[Gemma 4 model card](https://ai.google.dev/gemma/docs/core/model_card_4)* — a current example reporting total and active parameters separately.
- NVIDIA, *[Model Quantization: Concepts, Methods, and Why It Matters](https://developer.nvidia.com/blog/model-quantization-concepts-methods-and-why-it-matters/)*.

## See also

*[Quantization](/entries/quantization/)* · *[Mixture of Experts](/entries/mixture-of-experts/)* · *[Ollama](/entries/ollama/)* · *[Token Burn](/entries/token-burn/)* · *[Fine-tuning](/entries/fine-tuning/)*
