---
layout: default
kind: glossary
title: "Local Model"
permalink: /entries/local-model/
date: 2026-11-11
summary: "An AI model whose files are stored and run on your own computer, so requests to it need not leave the machine. It trades provider fees and dependence for hardware limits."
published: true
first_published: 2026-11-11
last_revised: 2026-11-11
---

A **local model** is an AI [model](/entries/model/) whose files are stored and run on your own computer rather than on a provider's servers. You download it once, usually as an [open-weights](/entries/open-weights/) release such as [Gemma](/entries/gemma/), [Llama](/entries/llama/), or [Qwen](/entries/qwen/), and a [runner](/entries/runner/) such as [Ollama](/entries/ollama/) loads it when needed.

The main advantages are control and cost. Requests to the model do not have to leave the machine, there is no per-use charge, and the model keeps working without an internet connection. The costs are hardware, electricity, and setup time. A model must fit in the computer's memory, so a laptop can run only smaller models, and a smaller model is usually weaker than the strongest cloud models on hard tasks.

A local model does not by itself make the whole system private. If the [harness](/entries/harness/) also calls a cloud model, searches the web, or sends messages, material can still leave the computer. Some runners also list cloud-hosted models next to downloaded ones. Check where each request actually goes.

## See also

[Model](/entries/model/) · [Runner](/entries/runner/) · [Ollama](/entries/ollama/) · [Open Weights](/entries/open-weights/) · [Parameters](/entries/parameters/) · [Local-first / Sovereignty](/entries/local-first-sovereignty/) · [Sovereign Compute](/entries/sovereign-compute/) · [On Beginning](/entries/on-beginning/)
