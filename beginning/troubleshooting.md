---
layout: default
title: "Troubleshooting"
permalink: /beginning/troubleshooting/
description: "Fixes for common problems when setting up OpenClaw with a local or cloud model, listed by what you see."
---

*Part of [On Beginning](/entries/on-beginning/).*

# Troubleshooting

*Find the heading that matches what you see. When something fails, keep the exact error message (with any passwords or keys removed) before trying a fix.*

## Installation fails

Stop and keep the exact error message. Don't keep repeating the installer, and don't assume you need a new computer. Check the [official installation guide](https://docs.openclaw.ai/install). If your institution blocks installation, ask for its approved route rather than working around the restriction.

## "Homebrew on macOS is only supported on Apple Silicon processors!"

You're on an Intel Mac, and the standard installer tried to install Homebrew. Use the local-prefix installer on [Install on an Intel Mac](/beginning/intel-mac/). This is a problem with an installation dependency, not evidence that OpenClaw cannot run on your Mac.

## "command not found: openclaw"

If you used the Intel-Mac local-prefix installer, the command lives in `~/.openclaw/bin`. Type `"$HOME/.openclaw/bin/openclaw"` wherever this guide says `openclaw`. For example: `"$HOME/.openclaw/bin/openclaw" gateway status`.

## Ollama doesn't answer

Check that the Ollama app is open. The [Ollama quickstart](https://docs.ollama.com/quickstart) explains how to start it. Don't start a second copy if one is already running.

## My computer slowed down or ran out of memory

Press **Control-C** to stop the model, then choose a smaller one. On a 16 GB computer, start with `gemma4:e2b` and close other large applications. See [Will my computer run a local model?](/beginning/choose/#will-my-computer-run-a-local-model)

## My local model isn't listed during setup

Run the `ollama run` command from [Part 1](/beginning/local-model/#part-1-get-one-local-model-answering) again so the model is loaded, then rerun setup with `openclaw onboard`. In the OpenClaw desktop app, you can also choose **Choose connection → Local only** on the Ollama card to select any installed model. If your screens look different, follow the [current Ollama setup page](https://docs.openclaw.ai/providers/ollama/setup).

## OpenClaw can't reach Ollama

The address `http://127.0.0.1:11434` works only when Ollama and the OpenClaw Gateway run directly in the same operating system, with Ollama on its default port. `127.0.0.1` means "this same computer or environment"; `11434` is Ollama's default port. It is not a personal address; it works for each reader's same-system setup.

- Don't add `/v1` to the end. This setup uses OpenClaw's own Ollama connection, not an OpenAI-compatible one.
- If Ollama is on another computer, in a separate container or WSL environment, or uses a changed port, follow the [Ollama configuration recipes](https://docs.openclaw.ai/providers/ollama/recipes) instead.
- Do not expose Ollama to the internet to make the address work.

## I see a model name ending in "cloud"

Names such as `gemma4:31b-cloud` run on Ollama's servers, not your computer. For a local setup, use a model you've downloaded, and check the default and fallback models with the commands on [Connect a local model](/beginning/local-model/#check-where-your-requests-are-going).

## Authentication, billing or model-access error

Keep the error text with any credentials removed. Check which account you selected and the current provider guide ([OpenAI](https://docs.openclaw.ai/providers/openai/setup), [Anthropic](https://docs.openclaw.ai/providers/anthropic)) before switching routes. A paid chat subscription does not automatically pay for API calls. Paying for a different service is not the first troubleshooting step.

## The shell setting didn't take effect

If you changed `tools.exec.mode` on an OpenClaw installation that was already running, follow the documented restart instructions, then check with `openclaw exec-policy show`. The `ask` mode permits commands already on an allowlist and asks about others; it does not prompt for every command. See [permission modes](https://docs.openclaw.ai/tools/permission-modes).

## The assistant printed code instead of creating the file

If it shows something like `{"name": "write_file", ...}` and no file appears, the task did not happen. That usually means the model struggles with tools. Try another model, or see the [Ollama troubleshooting guide](https://docs.openclaw.ai/providers/ollama/troubleshooting).

## The assistant says it did something, but nothing changed

Check the tool activity in the dashboard and open the file yourself. A confident report is not evidence that the assistant read or wrote anything. Check the file path, the workspace location, and file permissions.

## A new conversation doesn't know what we did

Check the file path, the workspace, file permissions, and which instruction files the session actually loads. Tell the assistant exactly which file to read. Don't assume that a larger model will fix a missing file or a configuration problem. See [Memory and continuity](/beginning/memory/).

## My screens look different from this guide

Software changes. Trust the current official documentation: [OpenClaw installation](https://docs.openclaw.ai/install), [onboarding](https://docs.openclaw.ai/start/wizard), and [Ollama setup](https://docs.openclaw.ai/providers/ollama/setup).

---

**Back to:** [On Beginning](/entries/on-beginning/).
