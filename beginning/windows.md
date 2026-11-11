---
layout: default
title: "Install OpenClaw on Windows"
permalink: /beginning/windows/
description: "Install OpenClaw on a Windows computer with the PowerShell installer, or with the Windows Hub desktop app."
---

*Part of [On Beginning](/entries/on-beginning/). Step 3 of 8.*

# Install OpenClaw on Windows

*For Windows computers. If your institution manages your computer and blocks installation, ask for its approved route rather than working around the restriction.*

**Local model users:** first finish [Part 1 of Connect a local model](/beginning/local-model/#part-1-get-one-local-model-answering).

## Install with PowerShell

1. Open **PowerShell** from the Windows Start menu.
2. Paste this line and press Enter:

   ```powershell
   iwr -useb https://openclaw.ai/install.ps1 | iex
   ```

3. Read the prompts. The installer checks software requirements and can install Node.js, a program OpenClaw needs.

Do not paste the Mac/Linux command into PowerShell. If installation fails, stop and keep the exact error message.

## Or use the Windows Hub app

OpenClaw also offers a desktop app for Windows, [Windows Hub](https://docs.openclaw.ai/platforms/windows), which OpenClaw's own docs now recommend for Windows desktop setup. Its local setup can put the Gateway inside **WSL**, a Linux environment within Windows. That is a different arrangement from running both programs directly in Windows. If you choose it, follow its setup and networking instructions; the Ollama address in this guide may not reach an Ollama app running in Windows from inside WSL.

This guide follows the PowerShell route, where OpenClaw and Ollama run directly in the same operating system.

## Start setup

Setup (called *[onboarding](/entries/onboarding/)*) starts automatically after installation. Choose **Custom setup**, not Quick start, then follow **one** of these:

- [Connect a local model (Ollama)](/beginning/local-model/#part-2-choose-ollama-during-openclaw-setup)
- [Connect a cloud model (OpenAI or Anthropic)](/beginning/cloud-model/)

---

**Next:** [connect a local model](/beginning/local-model/#part-2-choose-ollama-during-openclaw-setup) or [connect a cloud model](/beginning/cloud-model/).

**Related:** [OpenClaw Windows guide](https://docs.openclaw.ai/platforms/windows) · [Troubleshooting](/beginning/troubleshooting/)
