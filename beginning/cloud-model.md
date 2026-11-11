---
layout: default
title: "Connect a cloud model"
permalink: /beginning/cloud-model/
description: "Connect OpenClaw to a cloud model from OpenAI or Anthropic during setup, and check which account is being billed."
---

*Part of [On Beginning](/entries/on-beginning/). Step 4 of 8.*

# Connect a cloud model

*For readers who chose a model run by a provider such as OpenAI or Anthropic. You do **not** need Ollama, Gemma, or the `127.0.0.1:11434` address.*

The provider supplies the model. Your workspace can stay on your computer, but your prompts, and any file contents or tool results included with them, are sent to that provider.

## During OpenClaw setup

1. In **Custom setup**, choose **OpenAI** or **Anthropic**, not Ollama. Choose the account connection you intend to use, not simply the first login OpenClaw detects.
2. **Check how you'll be billed before signing in.**
   - OpenAI offers API-key access billed through its Platform account. OpenClaw also documents ChatGPT/Codex subscription sign-in for eligible accounts.
   - Anthropic offers usage-based API access. OpenClaw also documents a Claude CLI route for people with an installed, signed-in Claude Code client. If you have not installed Claude Code, use the API route.
   - These routes have different requirements and limits. A paid chat subscription does not automatically pay for API calls.
3. Follow the supported browser sign-in or protected credential-entry flow. For API access, create the key in the provider's own account dashboard and enter it only in setup's designated secret field. **Do not paste keys, passwords or tokens into chat, workspace files, screenshots or shell commands.**
4. Select an available model from the picker. Check its current price or subscription limits. For API access, enable billing as required and set spending limits and alerts. Check whether a budget is a hard stop or only a notification.
5. Finish setup without adding email, messaging apps or other optional connections.

## Check your model

Run:

```bash
openclaw models status
openclaw models fallbacks list
```

(Intel Mac local-prefix users: use the full command path shown on the [Intel Mac page](/beginning/intel-mac/#using-the-commands-in-the-rest-of-this-guide).)

The default should be the provider and model you selected. Leave fallback models unconfigured for the first experiment, or include only ones whose costs and data handling you understand.

A model name alone does not tell you which account is being billed. Check the selected connection and the provider's usage page too.

## First cloud checkpoint

After you [start the assistant](/beginning/start/), ask: "Reply with exactly: Cloud model ready." Confirm that you get a response, type `/model status` to check the conversation's model, and look at the account's usage or quota display.

A successful reply proves the connection works, not that the assistant can use file tools. You'll test that with invented notes in [Give it a first job](/beginning/first-job/). Do not begin with sensitive documents.

If setup reports an authentication, billing or model-access error, see [Troubleshooting](/beginning/troubleshooting/#authentication-billing-or-model-access-error).

For exact screens, use the current [OpenClaw OpenAI setup guide](https://docs.openclaw.ai/providers/openai/setup) or [Anthropic setup guide](https://docs.openclaw.ai/providers/anthropic). OpenAI's [authentication documentation](https://developers.openai.com/codex/auth) explains subscription versus API-key access.

---

**Next:** [Start the assistant safely](/beginning/start/).

**Related:** [Model](/entries/model/) · [Troubleshooting](/beginning/troubleshooting/)
