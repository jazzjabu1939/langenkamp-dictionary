---
layout: default
title: "Connect a local model with Ollama"
permalink: /beginning/local-model/
description: "Download a model with Ollama, check that it answers, and connect it to OpenClaw during setup."
---

*Part of [On Beginning](/entries/on-beginning/). Steps 2 and 4 of 8.*

# Connect a local model with Ollama

*For readers who want the model to run on their own computer. Do Part 1 **before** installing OpenClaw, and Part 2 **during** OpenClaw's setup. Cloud users can skip this page.*

## Part 1: get one local model answering

1. Download Ollama from [its official site](https://ollama.com/download), install it, and open the app. On Linux, follow Ollama's Linux installation instructions.
2. Open **Terminal** on a Mac (press **⌘-Space** and type "Terminal"), **PowerShell** from the Windows Start menu, or a terminal on Linux.
3. Type each line below and press Return:

   ```bash
   ollama pull gemma4:e2b
   ollama list
   ollama run gemma4:e2b "Reply with exactly: Local model ready."
   ```

   - The first line downloads the model. This needs internet and can take a while.
   - The second lists your installed models. Your model's exact name should appear.
   - The third asks the model a question. The first answer may be slow while the model loads.

These commands use `gemma4:e2b`, a small starting model. If you chose another model on [Choose your setup](/beginning/choose/#will-my-computer-run-a-local-model), replace the name in all three lines and in OpenClaw's settings later.

Avoid any model name that includes **`cloud`** (such as `gemma4:31b-cloud`). Those run on Ollama's servers, not your computer.

**Checkpoint:** a model on your computer answered you. You haven't yet tested whether it can use tools. That comes later.

**Now go straight on and install OpenClaw** for your [Apple Silicon Mac](/beginning/mac/), [Intel Mac](/beginning/intel-mac/), or [Windows](/beginning/windows/) computer. Ollama keeps a model in memory for a few minutes after you use it, and OpenClaw's setup looks for models that are already loaded.

If nothing happens or your computer slows down, see [Troubleshooting](/beginning/troubleshooting/#ollama-doesnt-answer).

## Part 2: choose Ollama during OpenClaw setup

When OpenClaw's setup asks, choose:

1. **Custom setup**, not Quick start.
2. **Ollama** as the provider, then **Local only**.
3. For the Ollama address (the *base URL*), enter:

   ```text
   http://127.0.0.1:11434
   ```

   This works when Ollama and OpenClaw run directly on the same computer, with Ollama on its default port. Don't add `/v1` to the end. If your setup is different, see [Troubleshooting](/beginning/troubleshooting/#openclaw-cant-reach-ollama).

4. Select the exact model you downloaded.

OpenClaw then tests the model with a real request before saving it. Passing that test means the model can answer. It doesn't yet prove the model handles tools well.

If your model isn't listed, see [Troubleshooting](/beginning/troubleshooting/#my-local-model-isnt-listed-during-setup). Leave messaging apps and other add-ons unconfigured for now.

## Check where your requests are going

Run:

```bash
openclaw models list --provider ollama
openclaw models status
openclaw models fallbacks list
```

`models status` shows your default model. A *fallback* is a backup model OpenClaw switches to if the main one fails. For a local-only setup, the default should be your local model, and the fallback list should be empty or contain only local models you chose deliberately.

If you need to set the default yourself:

```bash
openclaw models set ollama/gemma4:e2b
```

To remove every fallback (including any local ones), run this, then check the list again:

```bash
openclaw models fallbacks clear
```

If you later set up more than one agent, each can have its own model, so check each one.

Installing Ollama does not by itself make your setup local. Check both the selected model and the server it connects to.

---

**Next:** [Start the assistant safely](/beginning/start/).

**Related:** [Ollama](/entries/ollama/) · [Runner](/entries/runner/) · [Local Model](/entries/local-model/) · [Ollama setup in OpenClaw](https://docs.openclaw.ai/providers/ollama/setup) · [Troubleshooting](/beginning/troubleshooting/)
