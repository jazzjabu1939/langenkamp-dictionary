---
layout: default
title: "Agentic Native Design"
permalink: /entries/agentic-native-design/
summary: "Designing a website, document, workflow, or institution so humans can use it naturally and AI agents can understand, search, cite, and act on it without scraping guesswork."
published: true
---

# Agentic Native Design

---

## In one sentence

**Agentic native design is the practice of building a website, document, workflow, or institution so that human readers can use it naturally and AI agents can understand, search, cite, and act on it without scraping guesswork.**

## Why the term matters

Most websites were built for three audiences: humans, search engines, and advertising systems. The human saw the page. Google saw the crawlable text and links. The advertising system saw the attention trail. That architecture made sense for the web we had.

Agentic systems add a fourth reader: the acting machine. Not a search crawler, not a browser, not a passive accessibility tool, but an agent that may be asked to answer questions, cite sources, compare claims, summarize a corpus, fill a form, schedule a meeting, check policy, or recommend a next action.

A site that is merely attractive to humans may be difficult for such an agent to use. The text may be buried inside scripts. The page hierarchy may be decorative rather than semantic. The canonical source may be unclear. The date may be hidden. The author may be ambiguous. The same term may appear in five places with no stable anchor. The site may look polished and still be agentically opaque.

An agentic native site is built against that failure.

## What changes

Agentic native design does not mean designing for agents instead of people. It means treating machine legibility as part of public legibility.

The practical moves are modest but cumulative:

- stable URLs
- clean semantic HTML
- readable Markdown or text equivalents
- one-sentence machine-readable definitions
- canonical citation blocks
- clear authorship and revision dates
- JSON-LD or similar structured metadata
- RSS or Atom feeds where appropriate
- `llms.txt` or `agents.txt` guidance at the site root
- stable anchor IDs for definitions, sections, and claims
- plain-language summaries that do not require the agent to infer the whole page from prose alone

None of these replaces good writing. They make good writing findable, citable, and usable by the agents now entering the loop.

## The Dictionary case

The Langenkamp Dictionary is a natural candidate for agentic native design because its subject is vocabulary. A dictionary entry is already a unit of machine-friendly knowledge: term, definition, explanation, related entries, source, revision history.

The agentic native move is to make that structure explicit enough that an agent can answer:

- What is the canonical definition?
- Who wrote this?
- When was it last revised?
- Is this entry stable, draft, or speculative?
- What should I cite?
- What other entries should I read before answering?
- Which claims are definitional, and which are interpretive?

Humans benefit from the same clarity. The machine-readable definition is also the student-readable definition. The canonical citation block helps an agent, but it also helps a colleague, journalist, student, or future reader who wants to quote the entry honestly.

## The human limit

There is an obvious danger here. A site designed for agents can become dead prose: over-structured, under-written, more schema than thought. That is not the goal. The Dictionary should remain written by a person and an assistant with a voice, an angle, and a willingness to be wrong in public.

Agentic native does not mean agent-authored, agent-owned, or agent-sovereign. It means the work is hospitable to agents without surrendering editorial judgment to them.

The phrase that belongs near this entry is: **by agents, for agents, with people in mind**. The order is slightly mischievous, but the authority is not. Agents help build and navigate the thing. People remain the reason it exists.

## Related entries

*Human in the Loop*, *Human Judgment Layer*, *Commercial Legibility*, *JSON*, *MCP*, *Provenance*, *AI Produced Artifact*, *Cheng*, *Sincerity as Architecture*.
