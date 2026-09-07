---
layout: default
kind: glossary
title: "Prompt"
permalink: /entries/prompt/
date: 2026-05-19
last_revised: 2026-09-06
summary: "Instructions or context supplied to a model at inference time; in ordinary use, especially the request a user types into a chatbot."
draft: false
published: true
---

A **prompt** is an instruction or piece of context supplied to a model at inference time. In ordinary use, it means the request a person types into a chatbot. In technical and agentic systems, people also speak of system prompts, developer prompts, retrieved context, examples, files, and tool results. Those inputs may all shape the model's response, but the user's prompt is not the whole context.

Prompting matters because model behaviour is context-sensitive. The same request can produce different results when the task, audience, examples, constraints, available tools, and success condition change. Good prompting is therefore less like discovering magic words and more like writing a usable specification.

A *[System Prompt](/entries/system-prompt/)* is one higher-authority source of instructions, but message roles and precedence are properties of a particular product or API. OpenAI's public Model Spec, for example, describes a chain of command among higher-level platform instructions, developer instructions, and user requests. Other systems may organise the hierarchy differently. A prompt cannot safely override instructions above it merely by declaring itself more important.

## Source

- OpenAI, *[Model Spec: Chain of command](https://model-spec.openai.com/2026-08-18.html#chain_of_command)*.

## See also

- *[System Prompt](/entries/system-prompt/)*
- *[Context Window](/entries/context-window/)*
- *[English Major](/entries/english-major/)*
