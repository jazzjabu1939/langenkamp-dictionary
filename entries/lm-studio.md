---
layout: default
kind: glossary
title: "LM Studio"
permalink: /entries/lm-studio/
date: 2026-05-12
last_revised: 2026-09-06
summary: "Desktop application and local server for downloading and running open-weight language models on macOS, Windows, and Linux."
draft: false
published: true
---

LM Studio is a desktop application and local server for downloading and running open-weight language models on macOS, Windows, and Linux. It provides chat and model-discovery interfaces, hardware-aware loading controls, and OpenAI-compatible local API endpoints. It supports GGUF models through llama.cpp and, on Apple silicon, MLX models.

For this Dictionary, LM Studio matters as a polished consumer-facing local-model runner. Where *[Ollama](/entries/ollama/)* is command-line-first, LM Studio offers a graphical path into local inference. Model discovery still requires judgment: a downloadable model may be too large for the machine, governed by a restrictive licence, or unsuitable for the task.

The Dictionary's *[Sovereign Compute](/entries/sovereign-compute/)* framework treats LM Studio as one accessible starting point, with Ollama as an alternative for command-line-comfortable users. The operator's own setup uses both, depending on whether the task wants a GUI or a service-oriented workflow.

## See also

- *[Sovereign Compute](/entries/sovereign-compute/)*
- *[Ollama](/entries/ollama/)* — the command-line alternative
- *[Hugging Face](/entries/hugging-face/)* — a model source
- *[Hermes](/entries/hermes/)*, *[Gemma](/entries/gemma/)*, *[Qwen](/entries/qwen/)* — common targets

## Sources

- LM Studio, *Welcome to LM Studio Docs*: <https://lmstudio.ai/docs/app>
- LM Studio, *Offline operation*: <https://lmstudio.ai/docs/app/offline>
