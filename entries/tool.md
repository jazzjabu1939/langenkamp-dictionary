# Tool


---

## In one sentence

**A tool is a function that an AI agent can call to do something in the real world — read a file, run a search, send an email, query a database — that the model itself cannot do on its own.**

## Why tools exist

A language model on its own is just a very fast text completer. It can imagine what the weather is like in Boston, but it cannot actually *check* the weather. It can describe how to send an email, but it cannot send one.

To turn a model into something operationally useful, the system around it has to give it **tools** — well-defined functions the model can request to be run. The model says "I would like to call `get_weather(city='Boston')`," the surrounding system actually runs that function, and the result is fed back into the model's context. The model then continues its reasoning with the new information.

This is the architectural shift that distinguishes a chatbot from an agent. A chatbot generates text. An agent generates text *and decides when to call tools*.

## What it actually does — concretely

A tool, in agent-speak, has three pieces:

1. **A name and description** that the model sees ("`read_file`: read a text file from disk and return its contents").
2. **A parameter schema** — what arguments are accepted, with types and optional descriptions ("`path`: the absolute path to the file").
3. **An implementation** — the actual code that runs when the model calls it.

When the agent's main loop runs, the model is shown the list of available tools as part of its prompt. If the model decides to call one, it produces a structured request (typically JSON) instead of normal text. The agent runtime intercepts that request, runs the implementation, and returns the result.

## Working example from this machine

In the OpenClaw setup on this MacBook, the agent has a built-in toolbox that includes:

| Tool | What it does |
|------|--------------|
| `read` | Read the contents of a file |
| `write` | Create or overwrite a file |
| `edit` | Make precise edits to a file |
| `exec` | Run a shell command |
| `web_search` | Search the web (Brave API) |
| `web_fetch` | Fetch and extract a web page |
| `cron` | Schedule a job |
| `memory_search` | Semantic search across the agent's memory |
| `image` | Analyze an image |
| `sessions_spawn` | Spawn a sub-agent |

When a user asks "what's in my MEMORY.md file?" the model decides to call `read(path='/Users/Jazz/.openclaw/workspace/MEMORY.md')`, the runtime executes that, the file contents come back as a tool result, and the model can then summarize, search, or quote from it.

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
- **Plugin** — a vendor or platform term. Often a bundle of tools delivered as a deployable unit. ChatGPT plugins were one early example. MCP servers are the modern, open-standard version.

A useful mental model: a tool is a verb, a skill is a recipe that uses verbs, and a plugin is a cookbook.

## Why this matters in a teaching context

For an MBA classroom, the leap from "the model writes text" to "the model takes actions" is the conceptual cliff most faculty members and students stumble over. Tools are the bridge.

Useful framing for class discussion: an LLM without tools is like a brilliant consultant chained to a chair with their phone confiscated and the door locked — they can describe what should be done, but they cannot do it. Tools are the equivalent of giving the consultant access to the company's systems. **Whoever decides which tools to expose, and to whom, is making operational governance decisions.**

This is genuinely teachable material in a strategy or management of technology course: every tool you add to an agent is a permission you grant. Designing the toolset is, in effect, designing a job description.

## Trade-offs

- **More tools = more model confusion.** A model with 50 tools available may struggle to pick the right one, or call the wrong one. Most production agents keep their toolboxes lean and curated.
- **Tool calls are real-world side effects.** A tool that sends an email actually sends an email. Bugs, hallucinations, or prompt injection can produce real damage. Approval gating, rate limits, and audit logs matter.
- **Permissions are now in the agent's hands.** The agent decides when to call which tool. If the agent has tools it should not have, no amount of careful prompting can fully prevent misuse. The right answer is *do not give the agent the tool* if you are not prepared to live with the worst case of it being called.
- **Schema design is harder than it looks.** A poorly-described tool will be called incorrectly. Clear names and tight parameter descriptions matter more than people expect.

---

*Related entries: `what-is-a-skill.md`, `mcp.md`, `gateway.md`.*
