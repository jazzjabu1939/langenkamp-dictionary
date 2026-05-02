# Ollama


---

## In one sentence

**Ollama is a local LLM runtime** — software that lets you download large language models (Llama, Gemma, Qwen, etc.) and run them on your own machine, without sending anything to a cloud API.

## What it actually does

Three jobs:

1. **Model manager.** Downloads quantized model weights (compressed versions that fit in RAM) and stores them on disk. Like a package manager for AI models.
2. **Inference server.** Runs a local web server on `http://localhost:11434` that speaks an OpenAI-compatible API. Apps that "talk to OpenAI" can be pointed at Ollama instead and they don't know the difference.
3. **GPU/CPU optimizer.** Handles the math efficiently on whatever hardware you have. On Apple Silicon it uses the unified memory and the M-series GPU automatically.

## Why it matters in an agentic system

- **Sovereignty.** When you ask a local Gemma model a question, no data leaves the MacBook. Anthropic, Google, OpenAI never see it. For student grades, research drafts, sensitive documents — that is the whole point of running a local model.
- **Cost.** Once a model is downloaded, every token is essentially free (you pay electricity, not API fees). The 29 tokens-per-second I measured on Gemma 3 27B equates to roughly $0.00 per query, indefinitely.
- **No rate limits.** Anthropic's API can throttle you. Ollama can't — it is just your hardware.
- **Offline-capable.** Plane, hotel WiFi, internet outage — local models keep working.

## The trade-off

Local models are smaller and less capable than frontier cloud models. Gemma 4 26B is roughly equivalent to GPT-3.5-class reasoning, not GPT-5-class. So the strategy is not "replace the cloud" — it is **route the easy stuff locally, save the cloud spend for tasks that genuinely need frontier capability**.

This is the basis of *model tiering*, where heartbeats and routine sub-agent work go local (free, private), while complex reasoning still goes to a cloud frontier model. See *(planned)* for that pattern.

## How to use it (basic commands)

```bash
ollama pull gemma4:26b      # download the model (one-time, ~17 GB)
ollama list                 # see what is installed
ollama run gemma4:26b       # interactive chat at the terminal
curl http://localhost:11434/api/generate ...   # programmatic access
```

## Working example from this machine (May 2, 2026)

After migrating from a Mac Studio M1 Max (32 GB) to a MacBook Pro M5 Max (128 GB), I pulled three local models and benchmarked them on a fixed prompt:

| Model | Size on disk | Tokens per second |
|-------|-------------:|------------------:|
| Gemma 3 27B | 17 GB | 29.0 |
| Qwen 2.5 32B | 19 GB | 25.7 |
| Gemma 4 26B | 17 GB | *pending — pulling now* |

For reference, ~29 tokens per second is faster than human reading speed. That means a 26B-parameter model is genuinely usable for real-time conversation **on a laptop, with no internet required**, costing nothing per query.

The 128 GB unified memory is what makes this possible. The previous 32 GB machine could not hold a model larger than about 20 GB without swapping. The 128 GB machine can hold a 70 GB model comfortably and still leave room for the OS, apps, and browser tabs.

## Where Ollama fits in the broader stack

```
┌────────────────────────────────────────────────────────┐
│ Telegram / Signal / browser / IDE                      │  (interfaces)
├────────────────────────────────────────────────────────┤
│ OpenClaw gateway  ←  decides which model to call       │  (the agentic layer)
├──────────────────────┬─────────────────────────────────┤
│ Anthropic / OpenAI   │  Ollama (localhost:11434)       │  (model providers)
│ (cloud, per-token $) │  (local, free per-token)        │
├──────────────────────┴─────────────────────────────────┤
│ Apple M5 Max, 128 GB unified memory                    │  (hardware)
└────────────────────────────────────────────────────────┘
```

## Closely related tools

- **LM Studio** — a graphical front end. Easier to browse and test models. Same role as Ollama, friendlier UI, less scriptable.
- **MLX / mlx-lm** — Apple's native framework for running models on Apple Silicon. Faster than Ollama in some cases, but lower-level. Aimed at developers, not casual use.
- **llama.cpp** — the underlying C++ inference engine that Ollama itself wraps. The grandfather of local-LLM tooling.

## What this enables in a teaching context

If a Management Department wants to teach about generative AI without sending student work to a third-party provider, a single Mac Studio or MacBook Pro running Ollama can serve a small classroom. The model never leaves the building. FERPA and student-privacy concerns shrink considerably.

For larger deployments (a full course, a research center), the same software runs on a Linux server with the same API surface. The skill of working with Ollama scales from the teacher's laptop to the institution's data centre with no rewrite.

---

*Next entries to write in this glossary: What is a gateway? What is a sub-agent? What is RAG? What is MCP? What is a heartbeat?*
