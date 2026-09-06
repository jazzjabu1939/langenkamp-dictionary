---
layout: default
kind: glossary
title: "JSON"
permalink: /entries/json/
date: 2026-06-04
first_published: 2026-06-04
last_revised: 2026-09-06
summary: "A plain-text data format used by APIs, tools, agents, and configuration files to pass structured information around."
draft: false
published: true
---

**JSON** — JavaScript Object Notation — is a text-based, language-independent format for exchanging structured data. Its values may be objects, arrays, strings, numbers, `true`, `false`, or `null`; object member names are strings.

It matters in agentic AI because tools need a shared way to pass information around. When an agent calls a tool, reads a configuration file, sends an API request, stores heartbeat state, or receives a structured result, JSON is often the little envelope carrying the meaning. It is not glamorous, but it is everywhere.

The useful intuition is this: ordinary prose is for humans; JSON is for machinery that needs to know exactly which value belongs to which name. A misplaced comma can break the machine. A well-shaped JSON object can make a tool call precise, auditable, and repeatable.

## See also

- *[Tool](/entries/tool/)*
- *[MCP](/entries/mcp/)*
- *[System Prompt](/entries/system-prompt/)*

*Source: IETF [RFC 8259, “The JavaScript Object Notation (JSON) Data Interchange Format”](https://www.rfc-editor.org/rfc/rfc8259.html).*
