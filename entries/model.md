---
layout: default
kind: glossary
title: "Model"
permalink: /entries/model/
date: 2026-11-11
summary: "The trained AI system itself: a large set of learned parameters that takes text or other input and produces a response. It can run on your own computer or on a provider's servers."
published: true
first_published: 2026-11-11
last_revised: 2026-11-11
---

A **model** is the trained AI system itself: a very large set of learned numbers, called [parameters](/entries/parameters/), that takes input such as a question, a document, or an image and produces a response. In everyday use the word usually means a *large language model*, which writes text by predicting what should come next. Claude, GPT, Gemini, Gemma, Llama, and Qwen are model families; each family has numbered versions and sizes.

A model writes answers and can propose actions, such as "read this file" or "search for that". It cannot carry out those actions by itself. A surrounding program, the [harness](/entries/harness/), decides which proposed actions are allowed, runs them, and returns the results. A model also has no memory between conversations unless the harness supplies earlier material again.

A model runs in one of two places. A **cloud model** runs on a company's computers; your requests travel to the provider over the internet, and the provider sets the price and the rules. A [local model](/entries/local-model/) runs on your own computer, usually through a [runner](/entries/runner/) such as [Ollama](/entries/ollama/), and depends on your hardware.

The same model can perform well in one setup and badly in another, because the tools, instructions, and context around it differ. That is why the Dictionary treats the model as one component of an assistant rather than the whole of it.

## See also

[Harness](/entries/harness/) · [Local Model](/entries/local-model/) · [Runner](/entries/runner/) · [Parameters](/entries/parameters/) · [Open Weights](/entries/open-weights/) · [Reasoning Model](/entries/reasoning-model/) · [Model Tiering](/entries/model-tiering/) · [Model–Harness Fit](/entries/model-harness-fit/) · [On Beginning](/entries/on-beginning/)
