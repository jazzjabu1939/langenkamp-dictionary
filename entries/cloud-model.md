---
layout: default
kind: glossary
title: "Cloud Model"
permalink: /entries/cloud-model/
date: 2026-11-11
summary: "An AI model that runs on a provider's servers and is reached over the internet. It offers stronger capability without local hardware, in exchange for sending your requests to that provider."
published: true
first_published: 2026-11-11
last_revised: 2026-11-11
---

A **cloud model** is an AI [model](/entries/model/) that runs on a company's servers and is reached over the internet. You send a request; the provider runs the model and sends back the answer. Claude from Anthropic and GPT from OpenAI are common examples. Access usually comes through a subscription or an API account billed by use.

The main advantage is capability. The strongest models need far more memory and computing power than an ordinary computer has, so for hard tasks a cloud model will usually do better than a [local model](/entries/local-model/). It also needs no download and no special hardware. The costs are dependence and exposure: you need an internet connection, you accept the provider's prices and rules, and your prompts, along with any file contents or tool results included with them, go to the provider.

Keeping your files on your own computer does not keep them from a cloud model. If the [harness](/entries/harness/) sends part of a file with a request, that part leaves the machine. Check which model each request uses, including any [fallback](/entries/fallback/) models, before giving the assistant sensitive material.

## See also

[Model](/entries/model/) · [Local Model](/entries/local-model/) · [Fallback](/entries/fallback/) · [Closed source](/entries/closed-source/) · [The Biggest Brains Live in the Cloud](/entries/biggest-brains-live-in-the-cloud/) · [Frontier Dependence](/entries/frontier-dependence/) · [On Beginning](/entries/on-beginning/)
