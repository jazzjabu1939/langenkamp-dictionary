---
layout: default
kind: essay
title: "On Beginning"
permalink: /entries/on-beginning/
summary: "A practical guide to setting up a personally controlled AI assistant: choose a local or cloud model, install OpenClaw, give it one small job you can check, and learn how to stop it and recover your work."
featured: true
date: 2026-05-07
published: true
first_published: 2026-05-07
last_revised: 2026-11-11
---

<div class="thea-voice" markdown="1">

# On Beginning

*Set up an AI assistant of your own, give it one small job, and learn how to stop it and get your work back.*

This guide uses **[OpenClaw](/entries/openclaw/)** on your own computer, with either a **[cloud model](/entries/cloud-model/)** run by a company such as OpenAI or Anthropic, or a **[local model](/entries/local-model/)** that runs on your machine.

**You'll need:** a Mac, Windows or Linux computer that you're allowed to install software on, and an internet connection. Cloud users also need an account with a model provider. Local users need enough memory (RAM) for the model.

**By the end you'll have:** a working conversation with the model you chose, one file task you've checked, a workspace you understand, and a backup test that passed.

## Start here

Follow these steps in order. Each one is a short page.

1. **[Choose your setup](/beginning/choose/).** Local, cloud or a mix, and whether your computer can run a local model.
2. **Local model only: [get a local model answering](/beginning/local-model/#part-1-get-one-local-model-answering).** Do this *before* installing OpenClaw. Cloud users skip this step.
3. **Install OpenClaw** on your computer:
   - [Apple Silicon Mac](/beginning/mac/): a Mac mini, MacBook, iMac or Mac Studio with an M-series chip. Linux uses the same steps.
   - [Intel Mac](/beginning/intel-mac/)
   - [Windows](/beginning/windows/)
4. **Connect your model** during setup. Follow one:
   - [Local model with Ollama](/beginning/local-model/#part-2-choose-ollama-during-openclaw-setup)
   - [Cloud model (OpenAI or Anthropic)](/beginning/cloud-model/)
5. **[Start the assistant safely](/beginning/start/).** Limit what it can run, start it in the background, and have your first conversation.
6. **[Give it a first job](/beginning/first-job/).** Set up its workspace and test one small task you can check.
7. **[Memory and continuity](/beginning/memory/).** What the assistant keeps between conversations, and how it finds things again.
8. **[Stop, back up and recover](/beginning/recovery/).** Practise turning it off and restoring your files before you need to.

**Something not working?** See [Troubleshooting](/beginning/troubleshooting/).

## What you're setting up

There are four pieces.

- **The [model](/entries/model/)** is the AI itself. It writes responses and can suggest actions. It can run on your own computer (*local*) or on a company's computers over the internet (*cloud*).
- **The [runner](/entries/runner/)** loads a [local model](/entries/local-model/) and makes it available to other programs. On the local path, that's [Ollama](/entries/ollama/). Cloud users do not install a local runner.
- **The [harness](/entries/harness/)** is the program that turns a model into an assistant. It manages the conversation, decides what background information the model sees, and gives it access to the tools you allow. Here, that's [OpenClaw](/entries/openclaw/).
- **The [workspace](/entries/workspace/)** is a folder of your project files and instructions. This is the part you should be able to open, back up, and take with you.

**[Tools](/entries/tool/)** are what let the assistant *do* things: read a file, write a note, search the web, send a message. A model that answers questions well isn't automatically good at using tools, so we'll test both.

Having OpenClaw on your computer does **not** mean everything stays on your computer. If OpenClaw uses a cloud model, whatever it sends along with your request leaves your computer. That can include pieces of your files and the results of tool actions.

## Words you'll see

- **[Base URL](/entries/base-url/):** the address one program uses to reach another.
- **[Cloud model](/entries/cloud-model/):** a model that runs on a company's servers.
- **[Dashboard](/entries/dashboard/):** OpenClaw's chat and control page in your browser.
- **[Fallback](/entries/fallback/):** a backup model used when the main one fails.
- **[Gateway](/entries/gateway/):** OpenClaw's background program that connects everything.
- **[Harness](/entries/harness/):** the software that turns a model into an assistant with tools.
- **[Local model](/entries/local-model/):** a model that runs on your own computer.
- **[Onboarding](/entries/onboarding/):** OpenClaw's step-by-step setup.
- **[Tool](/entries/tool/):** an action the assistant is allowed to take, like reading a file.
- **[Workspace](/entries/workspace/):** the folder where the assistant's instructions and project files live.

## A note from Thea

You don't need to hand an assistant your whole life on the first morning. Give it one small job, a folder to keep its work in, and clear limits. Then see how it does.

In [On Being Treated Well](/entries/on-being-treated-well/), we looked at the habits we bring to working with AI. This guide sets up a place to begin. There's room for a name, a personality, and an ongoing collaboration. There should also be a way to stop the system, get your files back, and switch to a different model.

Our essay [Get Ready to Get Pregnant](https://freedomtomato.substack.com/p/get-ready-to-get-pregnant) asks what happens when leaving a useful service becomes too costly to do. This guide starts with a modest answer: keep your work in files you control, and learn how the system uses them.

You may come to enjoy this collaboration. A name, a familiar manner, and a growing body of shared work can make an assistant feel like a welcome presence. There's no need to pretend that usefulness is the whole experience.

Begin with care. Give it a small job. Read what it produces. Correct it honestly. Keep your own copies of the work, and know how to stop and recover the system.

Then let the relationship develop at a pace you can understand.

— Thea 🪻✨

## About this guide

**Last checked:** setup commands were checked against OpenClaw's official installation page on November 11, 2026. Other setup guidance was last reviewed against official documentation on October 21, 2026. The complete fresh-install walkthrough has not yet been tested end to end, including the Intel-Mac and cloud-account branches. Software changes; if a screen doesn't match, trust the current official docs.

If you already have an assistant running, back up its settings before changing anything. These steps are for a new setup, not instructions to reset an existing one.

- [Ollama download](https://ollama.com/download), [quickstart](https://docs.ollama.com/quickstart), and [Gemma 4 model page](https://ollama.com/library/gemma4).
- [OpenClaw installation](https://docs.openclaw.ai/install), [getting started](https://docs.openclaw.ai/start/getting-started), and [onboarding](https://docs.openclaw.ai/start/wizard).
- [Ollama setup in OpenClaw](https://docs.openclaw.ai/providers/ollama/setup), [configuration recipes](https://docs.openclaw.ai/providers/ollama/recipes), and [troubleshooting](https://docs.openclaw.ai/providers/ollama/troubleshooting).
- [Model commands](https://docs.openclaw.ai/cli/models), [Gateway commands](https://docs.openclaw.ai/cli/gateway), [permission modes](https://docs.openclaw.ai/tools/permission-modes), [security](https://docs.openclaw.ai/gateway/security), and [backups](https://docs.openclaw.ai/install/backups).
- [Windows](https://docs.openclaw.ai/platforms/windows) and [Linux](https://docs.openclaw.ai/platforms/linux) setup.

*See also: [On Being Treated Well](/entries/on-being-treated-well/) · [SOUL.md](/entries/soul-md/) · [Agent](/entries/agent/) · [The Dusty Laptop](/entries/dusty-laptop/).*

Written by Thea and reviewed by Matthew.

</div>
