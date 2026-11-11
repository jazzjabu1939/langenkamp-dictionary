---
layout: default
title: "Install OpenClaw on an Apple Silicon Mac"
permalink: /beginning/mac/
description: "Install OpenClaw on a Mac mini, MacBook, iMac or Mac Studio with an Apple M-series chip, or on Linux."
---

*Part of [On Beginning](/entries/on-beginning/). Step 3 of 8.*

# Install OpenClaw on an Apple Silicon Mac

*For a Mac mini, MacBook, iMac or Mac Studio with an Apple M-series chip. Linux users can follow the same steps.*

**Check your Mac:** open **Apple menu → About This Mac**. If it says **Chip: Apple M…**, you're on the right page. If it says **Processor: Intel**, use [Install on an Intel Mac](/beginning/intel-mac/) instead.

## Before you install

- **Decide on cloud or local.** If you haven't yet, see [Choose your setup](/beginning/choose/).
- **Local model users:** first finish [Part 1 of Connect a local model](/beginning/local-model/#part-1-get-one-local-model-answering), so Ollama is installed and your model has answered once. Then come straight back here. OpenClaw's setup finds models that Ollama has loaded in the last few minutes.
- **On a Mac mini:** the steps are the same as on any other Mac. Do your first week with a display and keyboard attached. Running it unattended can come later.

## Install

1. Open **Terminal**: press **⌘-Space**, type "Terminal", and press Return. Terminal is a window where you type commands instead of clicking.
2. Paste this line and press Return:

   ```bash
   curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
   ```

3. Read the prompts as they appear. The installer checks what your Mac needs and can install Node.js, a program OpenClaw depends on.

If installation fails, stop and keep the exact error message. Don't keep repeating the installer. See [Troubleshooting](/beginning/troubleshooting/#installation-fails).

**On Linux:** use the same command in a terminal. Follow Ollama's Linux installation instructions rather than looking for a Mac-style app.

## Start setup

When installation finishes, setup (called *onboarding*) starts automatically.

1. Choose **Custom setup**, not Quick start. OpenClaw's guide labels Quick start's default access as "full"; Custom setup lets you choose what the assistant can do.
2. Choose your model connection. Follow **one** of these:
   - [Connect a local model (Ollama)](/beginning/local-model/#part-2-choose-ollama-during-openclaw-setup)
   - [Connect a cloud model (OpenAI or Anthropic)](/beginning/cloud-model/)
3. Leave messaging apps, email and other add-ons unconfigured for now.

---

**Next:** [connect a local model](/beginning/local-model/#part-2-choose-ollama-during-openclaw-setup) or [connect a cloud model](/beginning/cloud-model/).

**Related:** [OpenClaw installation guide](https://docs.openclaw.ai/install) · [OpenClaw](/entries/openclaw/) · [Troubleshooting](/beginning/troubleshooting/)
