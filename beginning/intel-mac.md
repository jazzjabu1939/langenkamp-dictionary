---
layout: default
title: "Install OpenClaw on an Intel Mac"
permalink: /beginning/intel-mac/
description: "Install OpenClaw on an older Intel Mac with the local-prefix installer, which avoids Homebrew."
---

*Part of [On Beginning](/entries/on-beginning/). Step 3 of 8.*

# Install OpenClaw on an Intel Mac

*For older Macs whose **About This Mac** window says **Processor: Intel**. If yours says **Chip: Apple M…**, use [Install on an Apple Silicon Mac](/beginning/mac/).*

An Intel Mac is often a good candidate for a [cloud model](/beginning/cloud-model/). A local model will run on the processor only and may be slow. See [Choose your setup](/beginning/choose/#older-intel-macs).

## Why a different installer?

The standard installer may try to install Homebrew to obtain Node.js, then stop with a message such as "Homebrew on macOS is only supported on Apple Silicon processors!" That is a problem with an installation dependency, not evidence that OpenClaw itself cannot run on your Mac.

OpenClaw documents an alternative that installs its own copy of Node.js under your home folder, without Homebrew.

## Install

1. **Local model users only:** first finish [Part 1 of Connect a local model](/beginning/local-model/#part-1-get-one-local-model-answering).
2. Open **Terminal** (press **⌘-Space**, type "Terminal", press Return) and paste:

   ```bash
   curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash
   ```

3. Wait for a successful finish. Then run these two lines, one at a time:

   ```bash
   "$HOME/.openclaw/bin/openclaw" --version
   "$HOME/.openclaw/bin/openclaw" onboard
   ```

   The first should print a version number. The second starts setup.

If installation fails, stop and keep the exact error message. Do not keep repeating the installer or assume you need a new computer.

## Using the commands in the rest of this guide

This installation puts the `openclaw` command in `~/.openclaw/bin`. Whenever this guide says `openclaw`, type `"$HOME/.openclaw/bin/openclaw"` instead. For example:

```bash
"$HOME/.openclaw/bin/openclaw" gateway status
```

That full path avoids a "command not found" error without editing your shell settings. The alternative is described in the [official installation guide](https://docs.openclaw.ai/install#local-prefix-installer-install-clish). We have checked the installer's Intel-Mac route, but have not yet verified this whole walkthrough end to end on an Intel Mac.

## Start setup

In setup, choose **Custom setup**, not Quick start, then follow **one** of these:

- [Connect a local model (Ollama)](/beginning/local-model/#part-2-choose-ollama-during-openclaw-setup)
- [Connect a cloud model (OpenAI or Anthropic)](/beginning/cloud-model/)

---

**Next:** [connect a local model](/beginning/local-model/#part-2-choose-ollama-during-openclaw-setup) or [connect a cloud model](/beginning/cloud-model/).

**Related:** [The Dusty Laptop](/entries/dusty-laptop/) · [Troubleshooting](/beginning/troubleshooting/)
