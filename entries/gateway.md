---
layout: default
kind: reference
title: "Gateway"
permalink: /entries/gateway/
summary: "the always-on coordinator process at the heart of an agentic system."
date: 2026-05-02
draft: false
published: true
---

# Gateway


---

## In one sentence

**A gateway is the long-running coordinator process at the heart of an agentic system** — it accepts incoming messages, routes them to the right model and tools, manages identity and authentication, schedules background jobs, and holds state between conversations.

## Why a gateway exists at all

A naive "AI assistant" is just a script that takes one prompt, calls a model API, prints the answer, and exits. That works for a calculator. It does not work for anything that needs memory, scheduled actions, multiple input channels, or coordination between agents.

Once you want any of these, you need a process that **stays running**:

- Receives messages from Telegram, Signal, Discord, browser, etc.
- Holds conversation history per user, per channel
- Triggers tasks at specific times (a 7am security audit, a Friday memo)
- Authenticates the devices that are allowed to send commands
- Mediates calls between language models and external tools (search, email, calendar)

That always-on coordinator is the gateway. Everything else hangs off it.

## What it actually does — concretely

In OpenClaw, the gateway is a single long-running process that:

1. **Listens** on a local WebSocket port (here, `127.0.0.1:<port>` — the specific port is set in config).
2. **Authenticates** every client connection (your laptop's CLI, the dashboard browser tab, your phone) using device tokens with scoped permissions.
3. **Receives messages** routed in from messaging providers (Telegram, Signal, etc.) via plugin connectors.
4. **Decides which model to call** based on the configuration (cloud frontier model, local Ollama model, etc.) — this is where model tiering happens.
5. **Executes tools** — file reads, shell commands, web searches, calendar lookups — when the model asks for them.
6. **Runs the cron daemon** — schedules and fires recurring jobs without ever needing the CLI.
7. **Persists state** — conversation history, memory files, cron job records, device pairings.

When the gateway is down, connected channels and gateway-mediated operations stop, though local files and independent services remain. When it is up, clients can come and go without becoming the source of truth.

## Working example

After starting the gateway on a typical Mac setup:

```
$ openclaw gateway status
Service: LaunchAgent (loaded)
Runtime: running (pid <n>, state active)
Listening: 127.0.0.1:<port>
```

That single process is doing all of the following simultaneously:

- Accepting messages from connected channels (Telegram, Signal, etc.)
- Holding the conversation history for active sessions
- Running scheduled cron jobs waiting for their next fire times
- Authenticating paired client devices (dashboard, CLI, mobile)
- Executing shell commands and file operations when tools are called
- Calling cloud model APIs (Anthropic, OpenAI, etc.) for responses
- Optionally calling a local Ollama instance at `localhost:11434` for cheaper local inference

Stop that process and the system's connected agent services go silent. Restart it and persisted sessions, pairings, and schedules become available again.

## The bind / scope / device model

A subtle but important detail: OpenClaw binds the gateway to **loopback by default**. A user can instead configure LAN or tailnet access, so the security claim depends on the actual `gateway.bind` setting rather than on the word *gateway* itself.

Devices that want to issue commands must be **paired** and given **scopes**:

- `operator.read` — can observe state
- `operator.write` — can run tools and write data
- `operator.admin` — can change configuration
- `operator.pairing` — can approve other devices

This is the agentic-system equivalent of role-based access control. Different clients get different powers. The dashboard can do everything; a phone client might be read-only; a public webhook might have an even smaller scope.

## Why a gateway differs from a chatbot

| | Chatbot | Gateway |
|--|---------|---------|
| Lifespan | One conversation | Always running |
| State | Usually conversation-scoped | Persistent sessions, pairing, and schedules |
| Inputs | One channel (web form) | Many channels (Telegram, Signal, etc.) |
| Tools | Product-dependent | Configurable tools and connectors |
| Scheduling | None | Cron, heartbeats, deferred jobs |
| Multiple clients | No | Yes (phone + laptop + dashboard) |
| Identity & permissions | None | Devices, scopes, tokens |

The chatbot is a vending machine. The gateway is a household.

## Why this matters in a teaching context

When colleagues ask "how is your AI assistant different from ChatGPT?" — the answer largely lives at the gateway layer.

A gateway-based agentic system is a *building*: a fixed address, a calendar, a set of staff (sub-agents), a set of tools (skills), and a set of doors (channels) that visitors can come through. A hosted assistant can now have tools, memory, and scheduled work too; the decisive distinction is operational control over the coordinator, its state, and its permissions.

For an Isenberg classroom: a gateway is the part of an agentic system that makes "operations" possible at all. Without it, you have a parlor trick. With it, you have an institution.

## Trade-offs

- **Operational overhead.** A gateway is a service that has to be started, monitored, restarted after crashes, updated, and secured. ChatGPT-as-a-service has none of that.
- **Single point of failure.** If the gateway misbehaves, everything stops. Worth investing in good logs, restart automation, and backups.
- **Security surface.** Every paired device, every scope, and every plugin connector is a potential attack path. Loopback binding where practical, scoped tokens, and regular audits reduce that surface.
- **You own it.** The flip side of all the above: nobody else can change the rules, raise prices, deprecate features, or change terms of service. The gateway is on your hardware, running your code, doing what you configured.

---

## Source

- OpenClaw, [“Discovery and transports”](https://docs.openclaw.ai/gateway/discovery), current documentation.

## See also

- *[Sub-agent](/entries/sub-agent/)*
- *[Heartbeat](/entries/heartbeat/)*
