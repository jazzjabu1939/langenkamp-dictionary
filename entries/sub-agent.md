---
layout: default
kind: reference
title: "Sub-agent"
permalink: /entries/sub-agent/
summary: "delegated AI sessions for parallel or focused work."
---

# Sub-agent


---

## In one sentence

**A sub-agent is a fresh, isolated AI session spawned by a parent agent to do a specific delegated task** — it has its own context, its own scratchpad, runs in parallel, returns a result, and then disappears.

## Why sub-agents exist

A single AI conversation has a fixed context window — the model can only "see" so many tokens at once. If you keep piling work into one conversation, two things go wrong:

1. **The context gets polluted.** Old messages crowd out the room needed for new reasoning.
2. **Costs scale badly.** Every turn re-processes the whole conversation. By turn 50, every new question is paying for a recap of all 49 previous ones.

The standard fix in software engineering — *delegation* — applies here too. Instead of doing five things in one giant conversation, the parent agent spawns five focused sub-agents, each with a clean slate, each given just enough context to do its job, each returning a finished result.

Anthropic, OpenAI, and most modern agent frameworks now support this pattern. The terminology varies (sub-agents, child sessions, workers, tools-of-tools), but the shape is the same.

## What it actually does — concretely

When the parent agent decides to delegate:

1. **Spawns** a new session with its own ID and its own clean context.
2. **Hands** it a task description and (optionally) some context to fork from.
3. **Continues** with its own work, or yields and waits.
4. **Receives** a completion event when the sub-agent finishes.
5. **Folds** the result into the parent conversation as a new message.

Crucially, only the **final result** comes back into the parent context — not the entire reasoning chain. So a sub-agent that needed 20 internal turns to figure something out returns only its summary, keeping the parent's context lean.

## Working example from this machine (May 2, 2026, 06:54 EDT)

This morning, after restoring write scope to the gateway, I tested the sub-agent path with a dead-simple ping:

```
sessions_spawn(
  task: "Run uname -m && date && echo 'M5 Max sub-agent spawn test successful'",
  mode: "run"
)
```

The gateway accepted the request and gave back a child session key. I yielded my turn (told the parent session "I'm done for now, wake me when the sub-agent finishes"). Sixteen seconds later, a completion event arrived in the parent session:

```
arm64
Sat May  2 06:54:47 EDT 2026
M5 Max sub-agent spawn test successful

Stats: runtime 16s • tokens 139 (in 7 / out 132)
```

Three things to notice:

- **Total token cost: 139.** Trivial.
- **Runtime: 16 seconds.** Fast enough for real workflows.
- **The parent session's context never had to load the sub-agent's working memory.** Only the eight-line result.

## Where sub-agents are actually useful

In daily work on this machine, sub-agents are routinely used for:

- **Reading large files** so the parent doesn't have to ingest 5,000 lines just to extract a summary.
- **Running multi-step research** ("read this article, summarize, cross-reference our notes, propose action items") — the messy intermediate work stays in the child.
- **Parallel exploration** — spawning three sub-agents to investigate three angles at once.
- **Long-running tasks** that would otherwise hold up the parent conversation.
- **Isolation for risky work** — a sub-agent doing a destructive operation runs in its own sandbox.

The general rule: *if a task has a clear input and a clear output, and the messy middle does not need to live in the parent's memory, delegate it.*

## Sub-agents vs. tools — a common confusion

Both extend an agent's reach, but they differ structurally:

|  | Tool | Sub-agent |
|--|------|-----------|
| What it is | A function call (e.g., "search the web", "read this file") | A whole new AI session |
| Returns | Raw data | A finished, reasoned result |
| Reasoning capacity | None — it just executes | Full LLM reasoning |
| Cost per call | Usually free or cheap | Real model tokens |
| Best for | Mechanical operations | Tasks that need judgment |

A sub-agent can *use tools internally*. So a parent might say "spawn a sub-agent to summarize this directory" and the sub-agent then uses the file-read tool, the grep tool, etc. as part of *its* reasoning before reporting back.

## Why this matters in a teaching context

The sub-agent pattern is how agentic systems scale beyond a single brain. It is the AI-system equivalent of a manager who can hire temporary contractors for specific projects.

For a BBA or MBA classroom, a productive comparison is to organizational design:

- **Sole proprietor** = a chatbot. One person, no help, every task in the same head.
- **Founder with junior staff** = an agent with sub-agents. Delegation, focused effort, less context-thrash.
- **Department with cross-functional teams** = an agent with parallel sub-agents on coordinated tasks. Faster, more expensive, more coordination overhead.

The skills required to design *good* sub-agent workflows — clean task decomposition, well-bounded delegation, useful summaries from delegates — are exactly the skills good managers already practice on their human teams.

## Trade-offs

- **Coordination overhead.** Spawning, waiting, parsing the result — every delegation has friction. Trivial tasks should not be delegated.
- **Loss of nuance.** The parent only sees the summary, so any subtlety in the sub-agent's internal reasoning is lost unless explicitly surfaced. (This is the same problem human managers have with their reports.)
- **Cost stacking.** Each sub-agent uses model tokens. Spawn ten and you have ten model bills. Worth using cheaper models for the routine sub-agents — see *(planned)*.
- **Debugging is harder.** When a parent agent gets a wrong answer, you sometimes need to inspect the sub-agent's internal session to figure out where the reasoning broke.

---

*Related entries: `gateway.md` (the process that spawns sub-agents), `tool.md`, *(planned)*.*
