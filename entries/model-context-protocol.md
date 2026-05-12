---
layout: default
kind: glossary
title: "Model Context Protocol"
permalink: /entries/model-context-protocol/
date: 2026-05-12
summary: "Open specification, originated by Anthropic and increasingly cross-vendor, for connecting AI applications to external data sources, tools, and services. Named in *Commercial Legibility* as an early protocol of agent-platform infrastructure."
draft: false
published: true
---

The Model Context Protocol (MCP) is an open specification, originated by *[Anthropic](anthropic.md)* in late 2024 and increasingly adopted across the AI tooling ecosystem, for connecting AI applications (chatbots, agents, IDEs) to external data sources, tools, and services. The protocol defines a JSON-RPC-based interface for *MCP servers* (which expose resources and tools) and *MCP clients* (the AI applications that consume them), allowing the same agent to plug into a filesystem, a database, a SaaS API, or any other capability without needing custom per-vendor integration code.

For this Dictionary, MCP matters as one of the **early protocols of legibility** named in *[Commercial Legibility](commercial-legibility.md)*. The argument there: the AI market is now beginning to develop standardised protocols for agent-to-tool communication, in the same way that earlier internet eras developed HTTP, SMTP, and IMAP. MCP is to AI agents what HTTP was to early-web browsers — not the only protocol, not necessarily the winning one, but a structurally important attempt to make the layer above the model itself addressable and interoperable. The competing/complementary specification *A2A* (Agent-to-Agent), also named in *[Commercial Legibility](commercial-legibility.md)*, sits adjacent in this layer.

The Dictionary's editorial position on MCP: it is unfinished and may not be the protocol that wins, but the *category* of protocol is now structurally necessary and will exist in some form across the next decade.

## See also

- *[Commercial Legibility](commercial-legibility.md)*
- *[Anthropic](anthropic.md)*
- **Claude Code* *, *[Claude Desktop](claude-desktop.md)* — early adopters
