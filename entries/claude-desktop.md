---
layout: default
kind: glossary
title: "Claude Desktop"
permalink: /entries/claude-desktop/
date: 2026-05-12
summary: "*Anthropic*'s native macOS and Windows application for interacting with the *Claude* model family. The primary surface for the *Model Context Protocol* on the desktop."
draft: false
published: true
---

Claude Desktop is Anthropic's native macOS and Windows application for interacting with the *[Claude](claude.md)* model family. The application launched in October 2024 and has been progressively expanded with file uploads, screenshot sharing, voice input, and — most consequentially — *[MCP (Model Context Protocol)](mcp.md)* (MCP) support, which lets the desktop client connect to local MCP servers exposing filesystem access, databases, custom tools, and other resources.

For this Dictionary, Claude Desktop matters as **the early surface for MCP on the desktop**. The integration pattern Claude Desktop establishes — a desktop AI client that consumes local capability via a standardised protocol — is the structural shape *[Commercial Legibility](commercial-legibility.md)* names as the early protocol-of-agent-infrastructure layer. The application is also one of the primary ways non-developer users get access to Anthropic's models without writing API code.

The operator of this Dictionary uses Claude Desktop occasionally, but defaults to API access via *[OpenClaw](https://github.com/openclaw/openclaw)* and the broader agentic toolchain for daily work. Claude Desktop is mentioned here because it is the **named surface** other Dictionary entries refer to.

## See also

- *[Anthropic](anthropic.md)*
- *[Claude](claude.md)*
- *[MCP (Model Context Protocol)](mcp.md)*
- *[Commercial Legibility](commercial-legibility.md)*
