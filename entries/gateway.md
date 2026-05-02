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

In an OpenClaw setup like this one, the gateway is a single Node.js process that:

1. **Listens** on a local WebSocket port (here, `127.0.0.1:18789`).
2. **Authenticates** every client connection (your laptop's CLI, the dashboard browser tab, your phone) using device tokens with scoped permissions.
3. **Receives messages** routed in from messaging providers (Telegram, Signal, etc.) via plugin connectors.
4. **Decides which model to call** based on the configuration (cloud frontier model, local Ollama model, etc.) — this is where model tiering happens.
5. **Executes tools** — file reads, shell commands, web searches, calendar lookups — when the model asks for them.
6. **Runs the cron daemon** — schedules and fires recurring jobs without ever needing the CLI.
7. **Persists state** — conversation history, memory files, cron job records, device pairings.

When the gateway is down, nothing works. When it is up, everything else is ephemeral and can come and go.

## Working example from this machine (May 2, 2026)

After the morning restart of the M5 MacBook:

```
$ openclaw gateway status
Service: LaunchAgent (loaded)
Runtime: running (pid 1022, state active)
Capability: read-only
Listening: 127.0.0.1:18789
```

That single PID 1022 process is doing all of the following simultaneously:

- Accepting Telegram messages routed to me from Matthew's phone
- Holding the conversation history for *this very exchange*
- Running 28 cron jobs (2 active, 26 disabled) waiting for their next fire times
- Authenticating two paired client devices (the dashboard and the CLI)
- Executing every shell command and file operation I run
- Calling Anthropic's API for my main responses
- Soon, calling Ollama at `localhost:11434` for cheaper local responses

Kill that process and the system goes silent. Restart it and everything resumes.

## The bind / scope / device model

A subtle but important detail: the gateway is **bound to loopback only** — it listens on `127.0.0.1`, meaning only software on this same MacBook can connect. No traffic from the network reaches it directly.

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
| State | None | Persistent (memory, history, cron) |
| Inputs | One channel (web form) | Many channels (Telegram, Signal, etc.) |
| Tools | None | Many (file, shell, calendar, web, …) |
| Scheduling | None | Cron, heartbeats, deferred jobs |
| Multiple clients | No | Yes (phone + laptop + dashboard) |
| Identity & permissions | None | Devices, scopes, tokens |

The chatbot is a vending machine. The gateway is a household.

## Why this matters in a teaching context

When colleagues ask "how is your AI assistant different from ChatGPT?" — the answer largely lives at the gateway layer.

ChatGPT is a vendor-hosted chatbot. A gateway-based agentic system is a *building*: a fixed address, a calendar, a set of staff (sub-agents), a set of tools (skills), and a set of doors (channels) that visitors can come through. Teaching this distinction clearly is one of the harder pedagogical jobs in a BBA- or MBA-level AI course, because the language used in marketing materials collapses both into "AI assistant."

For an Isenberg classroom: a gateway is the part of an agentic system that makes "operations" possible at all. Without it, you have a parlor trick. With it, you have an institution.

## Trade-offs

- **Operational overhead.** A gateway is a service that has to be started, monitored, restarted after crashes, updated, and secured. ChatGPT-as-a-service has none of that.
- **Single point of failure.** If the gateway misbehaves, everything stops. Worth investing in good logs, restart automation, and backups.
- **Security surface.** Every paired device, every scope, every plugin connector is a potential attack path. Worth doing things like loopback-only binding, scoped tokens, and regular audits (we run two security audits per day on this machine).
- **You own it.** The flip side of all the above: nobody else can change the rules, raise prices, deprecate features, or change terms of service. The gateway is on your hardware, running your code, doing what you configured.

---

*Related entries: `sub-agent.md`, `heartbeat.md`, and *(planned)*.*
