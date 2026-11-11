---
layout: default
kind: glossary
title: "Fallback"
permalink: /entries/fallback/
date: 2026-11-11
summary: "A backup model an assistant switches to when its main model fails or is unavailable. Useful for reliability, but it can change cost, quality, and where your data goes."
published: true
first_published: 2026-11-11
last_revised: 2026-11-11
---

A **fallback** is a backup [model](/entries/model/) that an AI assistant switches to when its main model fails, for example because the provider is down, a usage limit is reached, or an account has run out of credit. In OpenClaw, the main model and an ordered list of fallbacks are part of the configuration. The commands `openclaw models status` and `openclaw models fallbacks list` show them.

Fallbacks keep work moving when one model is unavailable. They also change what happens without your noticing. A setup meant to be local can quietly send a request to a [cloud model](/entries/cloud-model/) if a cloud model is on the fallback list. A fallback may also cost more, or answer less well, than the model you chose.

For a first setup, or for sensitive work, keep the fallback list empty or limit it to models whose cost and data handling you understand. In OpenClaw, the fallback list applies to the configured default model. If you choose a model yourself for a conversation, for example with `/model`, and it fails, OpenClaw reports the failure rather than answering from a different model.

## See also

[Model](/entries/model/) · [Cloud Model](/entries/cloud-model/) · [Local Model](/entries/local-model/) · [Model Tiering](/entries/model-tiering/) · [Frontier Dependence](/entries/frontier-dependence/) · [On Beginning: Connect a local model](/beginning/local-model/#check-where-your-requests-are-going)

## Source

- OpenClaw documentation, [Model failover](https://docs.openclaw.ai/concepts/model-failover), accessed 11 November 2026.
