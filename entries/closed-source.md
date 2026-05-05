---
layout: default
title: "Closed source"
permalink: /entries/closed-source/
summary: "AI models delivered only through vendor-hosted APIs; the strategic counterpart to open source."
---

# Closed source

*The other large strategic camp in the contemporary AI model ecosystem.*

---

## In one sentence

**A *closed-source* AI model is one whose weights are kept proprietary; users access the model only through an API hosted by the vendor, who charges per token, controls the training and update cycle, and sees every prompt that flows through.**

## Why this term exists

By default, building a frontier AI model is enormously expensive — hundreds of millions of dollars in compute alone, plus the equivalent in research talent and data acquisition. A lab that has spent that much wants to recoup the investment, and the most direct way is to keep the model proprietary, expose it as an API, and charge per use.

The closed-source camp in mid-2026 includes the most capable models commercially available: **OpenAI's GPT-5**, **Anthropic's Claude (Opus, Sonnet, Haiku)**, **Google's Gemini Ultra and Pro**, and most of the next tier of well-funded contenders. The frontier-capability ceiling, in 2026, is held by closed models. The open-weights ecosystem is closing the gap, but is not yet at parity.

## What it actually does — concretely

A closed-source model is delivered as a *service*, not a *file*. You:

1. Sign up for an account with the vendor.
2. Get an API key.
3. Send HTTP requests with your prompts.
4. Receive responses.
5. Pay for what you used at the end of the month.

You do not have access to the model weights, the training data, the exact architecture (sometimes a rough description is published in a paper, sometimes not), or any guarantee that the model you call today will behave identically to the model you called last month.

## Working example

The OpenClaw setup on this MacBook calls Anthropic's Claude Opus 4.7 as its primary model. The interaction looks like:

```
Your laptop  →  HTTPS POST  →  Anthropic's data center  →  GPU cluster
                                                            running Opus 4.7
                                                                  ↓
                                                              response
                                                                  ↓
Your laptop  ←  HTTPS reply  ←  Anthropic's data center  ←  GPU cluster
```

The model itself is on Anthropic's hardware. Your prompt and response transit Anthropic's network. The billing meter ticks for every token in either direction. **The capability is real and excellent; the dependence is also real and total.**

When Anthropic raises prices, deprecates a model, changes terms of service, or has a regional outage, every workflow you have built on Opus is affected. This is not a criticism of Anthropic specifically — it is the structural reality of closed-source.

## Why this matters in a teaching context

For a BBA or MBA classroom, the open-vs-closed AI conversation is a clean case of *commoditize-your-complement* strategy taught through current events.

Worth working through with students:

- **Closed-source labs** want to keep model weights scarce and valuable. Their pricing power depends on it. Their safety story partly depends on it.
- **Open-weights labs** (Meta, Mistral, Alibaba) want to commoditize the model layer so that *their other businesses* (advertising, cloud, hardware sales) capture the value.
- **Hardware vendors** (NVIDIA, Apple, AMD) want both, because both buy chips.
- **Cloud providers** (AWS, Azure, GCP) want open-weights to win the inference business while their own first-party closed models (Bedrock-hosted, Azure OpenAI, Vertex) capture the high-margin frontier work.

The strategic positions of these players, mapped against the open-vs-closed axis, are some of the cleanest competitive-strategy material currently available for an Isenberg classroom — especially when paired with the equipment-auctions research thread, which has the same shape: *who profits when the underlying asset commoditizes?*

## Trade-offs

- **Best frontier capability available.** As of mid-2026, the top of the capability ceiling is closed. If you need the most capable model that exists, it is closed.
- **Operational simplicity.** No GPU bill, no model-update cycle, no inference engineering. The vendor handles it.
- **Vendor risk is total.** Pricing changes, deprecations, outages, terms-of-service shifts, model behaviour drift, geopolitical access restrictions — all of these are decisions made by the vendor, applied to your workflow.
- **Privacy is a contract, not a guarantee.** The vendor *says* they don't train on your prompts (most major labs now have explicit no-training-on-API-data policies). You believe them or you don't. There is no technical mechanism preventing it.
- **Cost can be surprising.** See [Token burn](token-burn.md) for the practitioner's reality of closed-source costs at scale.

## Related and adjacent terms

- *Open source* — the strategic counterpart.
- *API* — the delivery mechanism. Closed-source models live behind APIs by definition.
- *Sovereignty* — what you trade away when you commit to closed-source.
- *Commoditize-your-complement* — the strategic frame for understanding why some labs are open and others are closed.

---

*Related entries: [Open source](open-source.md), [Token burn](token-burn.md), [Token angst](token-angst.md), [Ollama](ollama.md).*
