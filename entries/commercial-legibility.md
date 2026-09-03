---
layout: default
kind: reference
title: "Commercial Legibility"
permalink: /entries/commercial-legibility/
summary: "the property of a business being readable to an AI agent acting on a buyer's behalf; the post-funnel competitive moat. Distinct from SEO (findable by search engine) and from brand (remembered by a person). Cousin to MCP and A2A."
---

# Commercial Legibility

*Sister entry to [Inverted Funnel](inverted-funnel.md). Where that one names what is ending, this one names what is beginning.*

---

## In one sentence

**Commercial Legibility is the property of a business being readable to an AI agent acting on a buyer's behalf — and it is the moat that replaces the seller-controlled funnel as the principal axis of competitive advantage in digital commerce.**

## What it is — and what it is not

Commercial Legibility is not SEO. SEO is the property of being *findable* by a search engine, where the consumer is a human reading ten blue links. Commercial Legibility is the property of being *callable* by an agent, where the consumer is a piece of software that needs structured prices, structured terms, structured fulfilment commitments, structured identity, structured recourse paths.

Commercial Legibility is not brand. Brand is the property of being *remembered* by a person. Commercial Legibility is the property of being *parseable* by code that has no episodic memory, no aesthetic preference, and no susceptibility to a clever advertisement. The agent does not feel the brand. It reads the data.

A vendor with strong SEO and strong brand can still be commercially illegible — and increasingly will be punished for it.

## The technical surface

The early protocols of legibility are already named, even if the practice is not yet mature: **MCP** (the [Model Context Protocol](mcp.md), Anthropic's open standard for connecting AI agents to external tools and data sources), **A2A** (Google's *Agent-to-Agent* protocol), structured product feeds, machine-readable terms of service, callable APIs for prices and inventory, scoped payment tokens, signed-and-published return policies. The tooling is rough. The direction is clear.

A commercially legible vendor in 2030 will publish:

- a structured catalogue with prices, availability, and fulfilment SLAs,
- machine-readable terms of service with explicit return, refund, and dispute clauses,
- an identity assertion (who is the legal entity, where is it incorporated, how is it regulated),
- an agent-callable API for transacting,
- a known fraud-and-abuse posture so the buyer's agent can decide whether to trust the vendor with a payment token.

A commercially illegible vendor will publish a beautiful website that no agent can read. The website will get fewer and fewer visits, regardless of how good the human marketing is, because increasingly the visitors that matter are not human.

## Why the two-tier market matters here

The AI market has split into a *closed tier* (rented API access, frontier capability, premium price) and an *open tier* (downloadable weights, run on your own hardware, dramatically lower marginal cost). This is not a temporary state of affairs; it is a structural bifurcation locked in by the differing business models of the major labs.[^1]

This split matters for legibility because the question *legible to whom?* has two very different answers depending on which tier the buyer's agent is running on:

- **Legible to one platform.** A vendor can integrate with the proprietary recommendation surface of a single major closed-API agent (the way merchants once integrated with Amazon). This is *platform dependence in disguise* — it looks like reach, but the platform owns the relationship and can change the terms whenever it wants.
- **Legible via open standards.** A vendor can publish to MCP, A2A, structured-data conventions, and machine-readable policies that *any* agent can read — closed or open, US or European or Chinese, hosted or self-run. This is *real* legibility, in the same sense that a website on the open web is real reach in a way that a Facebook page is not.

The vendors that will compound advantage over the next decade are the ones that publish openly enough to be readable by both tiers — and that especially includes the open-tier agents, because those are the agents the largest, most sophisticated buyers will increasingly run on their own hardware.

## A note on geography

Legibility will be politically scoped. The protocols (MCP, A2A) are technically open, but the *trust roots* and *identity layers* underneath them are already partitioning along geopolitical lines. The PRC's blocking of Meta's acquisition of Manus in early May 2026 was a clear signal: agent-platform infrastructure is now treated as strategic-tech, like 5G or semiconductors. There will be a Western agent ecosystem and a Chinese agent ecosystem, and they will not be fully interoperable. A vendor with global reach will need to be legible in both — which means publishing to standards both sides accept, with identity attestations both sides recognise.

This is going to be slow, expensive, and unavoidable.

## What this means for ordinary businesses

Most small and mid-sized businesses will not need to think about MCP or A2A directly, just as most did not need to think about HTTP. Tools will arrive that wrap legibility into something resembling a Shopify-for-agents — publish your catalogue once, and the legibility is generated for you. **The risk is being the last shop on the street that still has not done it.**

The internet economy of the next decade will quietly divide into businesses that are commercially legible to agents and businesses that are not. The latter will get less traffic, fewer transactions, and softer margins, regardless of how good their human marketing is. The shift will be gradual until it is not.

## See also

- [Inverted Funnel](inverted-funnel.md) — what the new moat replaces
- [MCP](mcp.md) — the early protocol of legibility
- [Sovereign Compute](sovereign-compute.md) — where the buyer's agent runs, and why it matters for legibility
- [Mediation (a la Gibson)](mediation-a-la-gibson.md) — the buyer-side argument

---

[^1]: The bifurcation thesis is articulated cleanly by Ali Salam in a May 2026 YouTube essay on Google's release of Gemma 4 under Apache 2.0. The short version: only labs whose AI revenue is a *complement* to a larger business (Google's cloud + Android, Meta's ads, Chinese labs' national-strategic positioning) can sustainably give frontier models away. OpenAI and Anthropic cannot, because for them the model *is* the business. The two tiers will permanently coexist because they serve different customer economics. See [Sovereign Compute](sovereign-compute.md) for the longer treatment.
