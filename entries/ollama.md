---
layout: default
kind: reference
title: "Ollama"
permalink: /entries/ollama/
date: 2026-05-02
summary: "a runtime for downloading, serving, and running language models locally, with optional cloud features and a deliberately simple API."
published: true
first_published: 2026-05-02
last_revised: 2026-09-06
---

# Ollama

## In one sentence

**Ollama is a model runtime and manager that makes it comparatively simple to download and run language models on a local machine, then expose them to other software through a local API.**

## What it actually does

Three jobs matter most:

1. **Model manager.** It downloads model artifacts, often quantized to reduce their memory requirements, and stores them locally.
2. **Inference server.** It serves its own API on `localhost:11434` and implements parts of the OpenAI API. Many applications can therefore switch between a cloud model and Ollama with a small configuration change, although compatibility is not complete.
3. **Hardware integration.** It manages inference across supported CPUs and GPUs. On Apple silicon, it can use unified memory and the integrated GPU without requiring the operator to assemble the lower-level stack.

Ollama also offers cloud-connected features. “Ollama” therefore does not automatically mean that every request stays on the machine. Locality depends on the model selected, the client configuration, and any surrounding tools.

## Why it matters in an agentic system

- **Sovereignty.** A locally served model can process material without sending prompts to a model provider. That is useful for sensitive drafts and documents, provided the surrounding application does not transmit them elsewhere.
- **Cost control.** Local inference substitutes hardware, electricity, and operator time for a per-token API charge.
- **Capacity under your control.** A local deployment has no vendor quota, but it still has limits imposed by memory, thermals, concurrency, and the machine's speed.
- **Offline operation.** Once the required software and weights are present, local inference can continue without an internet connection.

## The trade-off

Local and cloud systems have different strengths. Model size is not a reliable proxy for a named commercial generation, and a benchmark score does not settle whether a model is good for a particular workflow. The durable strategy is **routing**: measure candidate models on the work you actually do, keep private or routine tasks local where that is adequate, and use a hosted frontier model when its capability justifies the dependency.

## Basic commands

```bash
ollama pull <model>
ollama list
ollama run <model>
curl http://localhost:11434/api/generate ...
```

Model names and sizes change quickly, so the current Ollama library is a better source than a frozen list in this entry.

## Working example from this machine

On 2 May 2026, the operator measured 29.0 generated tokens per second for Gemma 3 27B and 25.7 for Qwen 2.5 32B on a MacBook Pro with an M5 Max and 128 GB of unified memory. Those are observations from one machine, prompt, model build, and software version. They show that large local models can be usable in an interactive workflow; they are not general performance rankings.

## Closely related tools

- **LM Studio** provides a graphical model browser and local server.
- **MLX / mlx-lm** is Apple's lower-level framework for running models on Apple silicon.
- **llama.cpp** is a widely used local-inference engine and file-format ecosystem.

## Teaching context

A locally deployed model can reduce the amount of student work sent to third-party model providers. It does not, by itself, establish FERPA compliance: the institution must still consider the client application, logs, access control, retention, backups, and the model's licence. The useful feature is architectural choice, not automatic compliance.

## See also

*[LM Studio](/entries/lm-studio/)* · *[Open Weights](/entries/open-weights/)* · *[Sovereign Compute](/entries/sovereign-compute/)* · *[Gateway](/entries/gateway/)*

## Sources

- Ollama, *OpenAI compatibility*: <https://docs.ollama.com/openai>
- Ollama, *Models*: <https://ollama.com/search>
