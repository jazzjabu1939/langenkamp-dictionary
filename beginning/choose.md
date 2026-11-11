---
layout: default
title: "Choose your setup"
permalink: /beginning/choose/
description: "Decide whether your assistant's model runs on your own computer or a provider's, and check whether your computer can run a local model."
---

*Part of [On Beginning](/entries/on-beginning/). Step 1 of 8.*

# Choose your setup

*For anyone deciding between a local model, a cloud model, or a mix of the two.*

## Where should the model run?

**Local:** the model runs on your own machine. You need enough memory (RAM) and storage, but no account with an AI company and no per-use charges. It isn't entirely free: you pay in hardware, electricity, and your own time.

**Cloud:** a company runs the model for you. You may get stronger results on hard tasks without buying a bigger computer. In exchange, you depend on an internet connection, the company's rules, and its prices, and your messages go to that company.

**Hybrid:** keep your workspace on your machine and send selected tasks to a cloud model. This can be practical, but keeping files locally doesn't stop their contents from being sent with a cloud request. Decide ahead of time what material is allowed to leave.

## Which path should I follow?

- **Cloud model:** go straight to installing OpenClaw for your computer ([Apple Silicon Mac](/beginning/mac/), [Intel Mac](/beginning/intel-mac/), or [Windows](/beginning/windows/)), then follow [Connect a cloud model](/beginning/cloud-model/). OpenAI and Anthropic are examples. Your computer runs OpenClaw and keeps the workspace, while the provider runs the model.
- **Local model:** first [get a local model answering](/beginning/local-model/#part-1-get-one-local-model-answering), then install OpenClaw, then connect the model during setup. This needs enough memory and a supported Ollama installation.

A cloud model can be a practical first choice for an older Intel Mac or a modest Windows or Linux computer. You do not need enough RAM to load that cloud model locally, though your computer must still support OpenClaw.

Web search, messaging apps, cloud syncing, and online memory services are each separate connections. Leave all of them off for your first experiment. "I'm using a local model" and "my whole system is offline" are two different claims.

## Will my computer run a local model?

**If you chose a cloud model, you can skip this section.** You do not need to download Gemma or install Ollama.

OpenClaw itself needs little memory. The model is what's demanding. Before downloading anything, check your computer's RAM and free storage:

- **Mac:** **Apple menu → About This Mac**, and **System Settings → General → Storage**.
- **Windows:** **Settings → System → About**, and **Settings → System → Storage**.
- **Linux:** your distribution's system-information and disk-usage tools.

Gemma 4, the family used in this guide, includes local models named `gemma4:e2b`, `gemma4:e4b`, `gemma4:12b`, `gemma4:26b`, and `gemma4:31b`. Start with a smaller model if memory is limited.

**For a 16 GB computer, start with the small `gemma4:e2b`.** It is a starting experiment, not a promise of good tool use. Keep other large applications closed and test one short request first. Do not start with `gemma4:31b` on a 16 GB machine.

Download size is not a RAM requirement. Our installed `gemma4:31b` download occupies about 19 GB on disk, and running it needs additional memory for the conversation and other work. Check the current [Ollama model page](https://ollama.com/library/gemma4), choose a model with tool support, and begin with a short task. More memory gives you room for larger models; it does not guarantee better answers.

You don't need a 128 GB computer to begin. Don't buy one until you've found out whether a smaller setup can handle your work.

### Older Intel Macs

In **About This Mac**, look for **Processor: Intel** rather than **Chip: Apple M…**. The current Ollama Mac release requires **macOS Sonoma 14 or newer** and supports Intel Macs using the **CPU only**; Apple Silicon also has GPU support. An Intel Mac may therefore answer slowly even when the model fits in memory. Check the [current Ollama Mac requirements](https://docs.ollama.com/macos) before installing.

Our companion article, [The Dusty Laptop](/entries/dusty-laptop/), looks at how an older machine can become a useful starting point. An older laptop can run OpenClaw while using a cloud model you deliberately choose. That's a perfectly good setup; it just isn't a local-only one.

### Chromebooks, tablets and managed computers

If you have a Chromebook, a tablet, or a managed computer that blocks installation, pause here. If you are following this guide for a class, ask your instructor which alternative is available: a lab computer, an approved remote environment, or a permitted cloud service. Do not assume you must buy hardware or a subscription. A remote environment is not local to your laptop; check where your work will be stored and processed.

---

**Next:** local model users, [get a local model answering](/beginning/local-model/#part-1-get-one-local-model-answering). Cloud users, install OpenClaw on your [Apple Silicon Mac](/beginning/mac/), [Intel Mac](/beginning/intel-mac/), or [Windows](/beginning/windows/) computer.

**Related:** [Local Model](/entries/local-model/) · [Model](/entries/model/) · [The Dusty Laptop](/entries/dusty-laptop/) · [Troubleshooting](/beginning/troubleshooting/)
