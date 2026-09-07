---
layout: default
kind: reference
title: "MCP (Model Context Protocol)"
permalink: /entries/mcp/
date: 2026-05-12
last_revised: 2026-09-06
summary: "An open protocol for connecting AI applications to tools, data sources, and reusable prompts."
published: true
---

# MCP (Model Context Protocol)

## In one sentence

**MCP is an open protocol, introduced by Anthropic in 2024, through which AI applications can discover and use tools, resources, and prompts exposed by external servers.**

## Why it exists

Without a shared protocol, each AI application and each outside service needs its own adapter. MCP gives clients and servers a common message format and lifecycle. The familiar shorthand is **N + M rather than N × M**: implement the protocol once on each side instead of building every possible pair.

That shorthand describes the economic aim, not a guarantee of effortless interoperability. Servers still differ in authentication, permissions, data semantics, reliability, and quality. A common plug does not make every appliance safe or useful.

Anthropic released MCP as an open-source project in November 2024. In December 2025 it donated the project to the Agentic AI Foundation, a Linux Foundation directed fund co-founded by Anthropic, Block, and OpenAI. That governance change makes *vendor-neutral* a defensible description of the project today; it should not erase Anthropic's role in creating it.

## What it carries

MCP uses JSON-RPC messages between a **host**, one or more **clients**, and **servers**. A server can expose:

- **Tools** — operations the model may ask to invoke.
- **Resources** — contextual data the application may retrieve.
- **Prompts** — reusable prompt templates.

The protocol also defines client capabilities such as sampling and elicitation. Support is negotiated; not every implementation offers every capability.

The standard transports are **stdio** for local process connections and **Streamable HTTP** for remote connections. WebSocket is not one of the specification's standard transports, although an implementation can add its own transport.

## Where judgment still lives

MCP standardises access. It does not decide which server deserves trust, which tool should be used, whether a result is abnormal, or when an agent should stop and call a human. Those decisions belong in the host, its permission model, *[Skills](/entries/skill/)*, operating policy, and human oversight.

Security therefore depends on more than trusting “the server.” The host should show users which tools are available, obtain meaningful consent, limit credentials and filesystem scope, validate remote origins and authentication, and treat tool descriptions and returned content as potentially hostile. An MCP connection expands capability and attack surface together.

## Management significance

MCP is a current example of an old strategic pattern. EDI in supply chains, FIX in trading, and HL7 in healthcare all reduced coordination costs by giving organisations a common interface. MCP attempts the same thing for AI applications and tools. If adoption continues, connectors become more portable and tool vendors gain access to more clients. Yet standards create complements; they do not abolish implementation quality, governance, or lock-in elsewhere in the stack.

## Sources

- Anthropic, *[Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)*, 25 November 2024.
- Anthropic, *[Donating the Model Context Protocol and establishing the Agentic AI Foundation](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)*, 9 December 2025.
- Model Context Protocol specification, *[Transports](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports)* and *[Server features](https://modelcontextprotocol.io/specification/2025-06-18/server)*.

## See also

- *[Skill](/entries/skill/)*
- *[Tool](/entries/tool/)*
- *[Gateway](/entries/gateway/)*
- *[RAG (Retrieval-Augmented Generation)](/entries/rag/)*
- *[Agent Memory](/entries/agent-memory/)*
