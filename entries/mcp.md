---
layout: default
title: "MCP (Model Context Protocol)"
permalink: /entries/mcp/
summary: "the open standard for connecting agents to tools and data sources."
---

# MCP (Model Context Protocol)


---

## In one sentence

**MCP (Model Context Protocol) is an open standard, introduced by Anthropic in late 2024, that defines how AI agents connect to outside tools, data sources, and services — analogous to USB-C for AI agents: one standard plug instead of a tangle of custom wires.**

## Why MCP exists

Before MCP, every time someone wanted their AI agent to access a new resource — a Google Drive folder, a Postgres database, a GitHub repo, a calendar — they had to write a custom integration. Every agent platform reinvented this wheel separately. ChatGPT's plugins were one shape; Anthropic's tools another; LangChain another; in-house systems each had their own.

This created a familiar problem: **N agents × M services = N × M integrations to build and maintain.** Vendors that wanted broad reach had to write a bespoke connector for every agent platform. Agent builders had to write bespoke connectors for every service.

Anthropic proposed MCP as a public, vendor-neutral protocol so that any MCP-compliant agent can talk to any MCP-compliant service. **N + M** instead of **N × M.**

The model is the same one that gave us USB, HTTP, SMTP, and PDF: a boring open standard that everyone can implement, so individual products do not have to negotiate point-to-point.

## What it actually does — concretely

MCP defines a small protocol — running over standard transports like stdio or HTTP/WebSocket — with a few core concepts:

- **Tools** — functions the agent can call (e.g., `search_drive`, `query_database`, `send_email`).
- **Resources** — read-only data the agent can fetch (e.g., document contents, file listings, recent commits).
- **Prompts** — reusable instruction templates that a server can offer to clients.
- **Sampling** — a way for the server to ask the agent to think about something on its behalf (used carefully).

A **MCP server** advertises these capabilities. An **MCP client** (your agent) discovers them at connection time and can then call them as needed. The protocol itself is simple JSON-RPC under the hood; the value is in the standardization.

## Where MCP fits in the broader stack

```
┌──────────────────────────────────────┐
│ Agent (e.g., OpenClaw, Claude Desktop)
├──────────────────────────────────────┤
│           MCP client                 │
└─────────────────┬────────────────────┘
                  │   (MCP protocol — JSON-RPC over stdio/HTTP)
       ┌──────────┼──────────┬──────────────┐
       ▼          ▼          ▼              ▼
   ┌──────┐  ┌──────┐  ┌────────┐      ┌──────────┐
   │ MCP  │  │ MCP  │  │  MCP   │      │   MCP    │
   │server│  │server│  │ server │      │  server  │
   │      │  │      │  │        │      │          │
   │Drive │  │Postgres│ │GitHub │      │1Password │
   └──────┘  └──────┘  └────────┘      └──────────┘
```

Each service exposes its own MCP server. The agent connects to whichever ones it needs.

MCP provides access, not operating judgment. It can let an agent read an error dashboard, but it does not tell the agent which dashboard to inspect first, what counts as abnormal, or when to stop and call a human. Those parts usually belong in a *[Skill](/entries/skill/)*, retrieved documentation, or *[Agent Memory](/entries/agent-memory/)*.

## Working example — what would MCP look like on this machine?

The setup on this MacBook today does most of what MCP enables, but using **internal tools** rather than the external MCP standard. The agent can already read files, run shell commands, query Canvas, send emails, and so on — through OpenClaw's built-in tool system.

If the same setup were rebuilt on MCP, the file-reading capability, the Canvas integration, the 1Password integration, and the calendar integration would each be small standalone MCP servers. Other AI clients — Claude Desktop, Cursor, an in-house custom agent — could then use those exact same servers without reconfiguration. The integrations become **portable assets**, not platform-locked.

The case for moving in that direction grows as the ecosystem matures: a service-by-service migration so that each integration is reusable beyond OpenClaw. The case against is operational — every running MCP server is one more process to start, monitor, and secure.

## Why this matters in a teaching context

MCP is an example of an old business-school idea showing up in a new domain: **a market that was crippled by N×M integration work has been reorganized by a public standard.** The same logic that gave us EDI in supply chain, FIX in trading, and HL7 in healthcare is now being applied to AI tooling.

For BBA and MBA students, the analogies are direct:

- USB-C in consumer electronics: one standard plug ended a generation of cable confusion.
- ISO containers in shipping: a 40-foot box made global logistics tractable.
- HTTP in software: anyone could publish, anyone could consume, no central permission required.

MCP is in the early-but-fast-growing phase. As of mid-2026 it is supported by Anthropic Claude (native), OpenAI's API (recent), Cursor, Continue, and a long list of community-built tools. The trend line is the usual one for successful open protocols — slow first year, exponential adoption after.

A management student learning to evaluate emerging-tech investments should be able to recognize the **N×M-to-N+M pattern** and know that protocols which solve it tend to compound in value.

## Trade-offs

- **It is a young standard.** Some details are still in flux. Implementations vary in maturity.
- **It introduces another moving part.** An MCP server is one more process that can fail.
- **Security thinking is required.** Every MCP server you connect to is something your agent now trusts. Scope-limiting, sandboxing, and audit logs all matter.
- **Vendor lock-in is reduced, not eliminated.** The model layer (the LLM itself) is still proprietary in most cases — MCP just makes the *tool* layer portable.

## Related and competing standards

- **OpenAI's "function calling"** — predates MCP and works inside the OpenAI ecosystem only. Many MCP servers also expose function-calling-compatible interfaces for backward compatibility.
- **LangChain tools** — a Python-library-level pattern for wiring tools into an agent. Pre-MCP. Now often co-exists with MCP rather than replacing it.
- **OpenAPI / REST** — older, broader standard for any HTTP service. MCP servers often wrap an OpenAPI service. The two are complementary, not in competition.

---

## See also

- *[Skill](/entries/skill/)*
- *[Tool](/entries/tool/)*
- *[Gateway](/entries/gateway/)*
- *[RAG (Retrieval-Augmented Generation)](/entries/rag/)*
- *[Agent Memory](/entries/agent-memory/)*
