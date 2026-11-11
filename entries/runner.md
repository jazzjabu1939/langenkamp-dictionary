---
layout: default
kind: glossary
title: "Runner"
permalink: /entries/runner/
date: 2026-11-11
summary: "A program that loads a local AI model into memory, runs it on your hardware, and makes it available to other programs. Ollama and LM Studio are common examples."
published: true
first_published: 2026-11-11
last_revised: 2026-11-11
---

A **runner** is a program that loads a [local model](/entries/local-model/) into your computer's memory, runs it on your processor or graphics chip, and makes it available to other programs. [Ollama](/entries/ollama/) and [LM Studio](/entries/lm-studio/) are common examples. Technical writing also calls this layer an *inference engine*, *inference server*, or *model runtime*; the Dictionary uses *runner* as the plain name.

A runner usually does three jobs. It downloads and stores model files. It performs the computation that produces the model's responses. It also opens a local connection, often an address such as `127.0.0.1:11434`, so that a [harness](/entries/harness/) like [OpenClaw](/entries/openclaw/) can send requests to the model and receive answers.

A runner does not turn a model into an assistant. It has no instructions file, no tools, and no project folder. Those belong to the harness and the [workspace](/entries/workspace/). Cloud users do not install a runner, because the provider runs the model on its own servers.

## See also

[Model](/entries/model/) · [Local Model](/entries/local-model/) · [Ollama](/entries/ollama/) · [LM Studio](/entries/lm-studio/) · [Harness](/entries/harness/) · [On Beginning](/entries/on-beginning/)
