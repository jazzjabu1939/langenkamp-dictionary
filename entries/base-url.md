---
layout: default
kind: glossary
title: "Base URL"
permalink: /entries/base-url/
date: 2026-11-11
summary: "The fixed starting address one program uses to reach another program's service. Specific requests are added to the end of it."
published: true
first_published: 2026-11-11
last_revised: 2026-11-11
---

A **base URL** is the fixed starting address one program uses to reach another program's service. The program adds the path for each specific request to the end of it. When you set up an AI assistant, the base URL tells the [harness](/entries/harness/) where to find the [model](/entries/model/).

For a [local model](/entries/local-model/) run by [Ollama](/entries/ollama/), the base URL is usually `http://127.0.0.1:11434`. The number `127.0.0.1` means "this same computer", and `11434` is the *port*, the numbered door on which Ollama listens. For a [cloud model](/entries/cloud-model/), the base URL is an internet address belonging to the provider.

Most connection problems in a new setup come down to a wrong base URL: the wrong port, a missing or extra ending such as `/v1`, or `127.0.0.1` used when the two programs are on different computers or in separate environments. The base URL also shows where requests go. An address on your own machine stays local; an address on the internet does not.

## See also

[Ollama](/entries/ollama/) · [Runner](/entries/runner/) · [Gateway](/entries/gateway/) · [JSON](/entries/json/) · [On Beginning: Troubleshooting](/beginning/troubleshooting/#openclaw-cant-reach-ollama)
