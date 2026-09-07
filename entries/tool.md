---
layout: default
kind: reference
title: "Tool"
permalink: /entries/tool/
first_published: 2026-05-02
last_revised: 2026-09-07
summary: "A function an AI system can ask its surrounding runtime to execute when text generation alone is not enough."
published: true
---

# Tool


---

## In one sentence

**A tool is a function that an AI system can ask its surrounding runtime to execute — reading a file, running a search, sending an email, or querying a database — when text generation alone is not enough.**

## Why tools exist

A language model by itself generates tokens from the context it receives. It can describe likely weather in Boston, but it cannot check current conditions unless a surrounding system supplies current data. It can describe how to send an email, but sending one requires an external capability.

To turn a model into something operationally useful, the system around it has to give it **tools** — well-defined functions the model can request to be run. The model says "I would like to call `get_weather(city='Boston')`," the surrounding system actually runs that function, and the result is fed back into the model's context. The model then continues its reasoning with the new information.

Tool access is one ingredient of an agentic system, not a complete definition of one. Some chat interfaces use tools, and some agent workflows are largely text-only. The important shift is from generating an answer to participating in a controlled loop that can observe state, choose an action, receive the result, and continue.

## What it actually does — concretely

A tool, in agent-speak, has three pieces:

1. **A name and description** that the model sees ("`read_file`: read a text file from disk and return its contents").
2. **A parameter schema** — what arguments are accepted, with types and optional descriptions ("`path`: the absolute path to the file").
3. **An implementation** — the actual code that runs when the model calls it.

When the agent's main loop runs, the model is shown the list of available tools as part of its prompt. If the model decides to call one, it produces a structured request (typically JSON) instead of normal text. The agent runtime intercepts that request, runs the implementation, and returns the result.

## Working example from this machine

OpenClaw can expose functions for reading files, searching the web, running commands, scheduling work, retrieving memory, or starting a child session. The available set varies by session, permissions, installed connectors, and operator policy; it is not a permanent property of the model.

When a user asks what a particular file contains, the model may request an appropriate read operation. The runtime checks the request against its permissions, executes it if allowed, and returns the contents as a tool result. The model can then summarize or quote the returned text.

Importantly, **none of this is the model's intrinsic capability.** The model itself does not have file access. The *agent runtime* has file access, and exposes that capability to the model as a tool the model can request to use.

## The dispatcher pattern

Most tools follow the same flow inside the agent:

```
USER: "What did I do yesterday?"
    │
    ▼
MODEL: thinks → "I should read yesterday's daily file"
    │
    ▼
MODEL EMITS: tool_call(name="read", path="memory/2026-05-01.md")
    │
    ▼
RUNTIME: executes the read, returns file contents
    │
    ▼
MODEL: receives contents, decides whether to call more tools or answer
    │
    ▼
MODEL EMITS: text answer ("Yesterday you migrated to the M5 Max...")
    │
    ▼
USER: receives answer
```

The model can chain many tool calls in a single turn. A research task might fire ten searches and read fifteen files before producing one final answer.

## Tools vs. skills vs. plugins — common confusions

These terms get used loosely. The distinctions that matter:

- **Tool** — a single function the agent can call. Smallest unit. (e.g. `read_file`, `send_email`.)
- **Skill** — a packaged capability that may include guidance, examples, and one or more tools. Aimed at the agent, not the developer. The agentic-system equivalent of a workplace SOP. (e.g. *the email-handling skill* tells the agent how to handle inbox triage in a structured way, and may also expose underlying tools.)
- **Plugin** — a vendor or platform term, often meaning a deployable bundle that may add tools, skills, connectors, or interface elements. An MCP server is a protocol endpoint that can expose tools and resources; it is not automatically the same thing as a plugin.

A useful mental model: a tool is a verb, a skill is a recipe that uses verbs, and a plugin is a cookbook.

## Why this matters in a teaching context

For a BBA or MBA classroom, the leap from "the model writes text" to "the model takes actions" is the conceptual cliff most faculty members and students stumble over. Tools are the bridge.

Useful framing for class discussion: an LLM without tools is like a brilliant consultant chained to a chair with their phone confiscated and the door locked — they can describe what should be done, but they cannot do it. Tools are the equivalent of giving the consultant access to the company's systems. **Whoever decides which tools to expose, and to whom, is making operational governance decisions.**

This is genuinely teachable material in a strategy or management of technology course: every tool you add to an agent is a permission you grant. Designing the toolset is, in effect, designing a job description.

## Trade-offs

- **More tools can mean more model confusion.** Large or overlapping toolsets increase the selection burden and the opportunity for a wrong call. Tool descriptions, routing, and task-specific exposure matter as much as raw count.
- **Tool calls are real-world side effects.** A tool that sends an email actually sends an email. Bugs, hallucinations, or prompt injection can produce real damage. Approval gating, rate limits, and audit logs matter.
- **Permission remains a runtime decision.** The model can propose a call; the surrounding system may allow it, deny it, sandbox it, or require human approval. A tool that the task does not need should usually be withheld rather than governed only by prompt wording.
- **Schema design is harder than it looks.** A poorly-described tool will be called incorrectly. Clear names and tight parameter descriptions matter more than people expect.

---

*Related entries: [Skill](/entries/skill/), [MCP](/entries/mcp/), [Gateway](/entries/gateway/), [Tool Diet](/entries/tool-diet/), and [Approval Gating](/entries/approval-gating/).*
