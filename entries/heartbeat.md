---
layout: default
kind: reference
title: "Heartbeat"
permalink: /entries/heartbeat/
summary: "A system-owned automation that gives an agent periodic turns in which to notice whether anything needs attention."
published: true
---

# Heartbeat


---

## In one sentence

**A heartbeat is a system-owned automation that gives an agent periodic turns in which to notice whether anything needs attention.**

## Why heartbeats exist

A pure-reactive AI assistant only does anything when you message it. It cannot:

- Remind you of a calendar event you forgot to ask about
- Notice a new email worth flagging
- Check the weather before your morning walk
- Watch a long-running download and tell you when it finishes
- Remember to follow up on something you asked about three days ago

To be *proactive*, an agent needs some way to wake without a new user message. A heartbeat supplies that opportunity. It does not itself decide what deserves attention; the monitor instructions, tools, permissions, and notification rules do.

## What it actually does — concretely

A heartbeat is implemented as a recurring scheduled agent turn. In OpenClaw, its cadence is maintained by the automations scheduler. Each time it fires:

1. The gateway sends the configured heartbeat prompt as a scheduled turn.
2. The turn receives the agent's ordinary system instructions and whatever heartbeat context the operator has configured.
3. The agent follows its bounded monitor instructions: inspect current state, react to a completed background task, or decide that nothing has changed.
4. The agent decides whether to:
   - Take action (send a reminder, update a file, kick off research)
   - Stay silent, using the runtime's no-notification response
5. The heartbeat ends. The agent goes back to sleep until the next one or the next user message.

Current OpenClaw can run heartbeat turns in the main session or, when configured, in a fresh isolated session. It can also wake an agent when detached work finishes. Those choices affect which conversation history is loaded, where notifications go, and how much the turn costs. They belong to harness design rather than to the definition of a heartbeat.

## The cost dimension — why heartbeat models matter

Frequent heartbeats can become a high-volume source of model calls. A 30-minute cadence creates 48 opportunities per day before the agent has done any user-requested work. The cost depends on the prompt, loaded context, tools, model, and whether the turn can remain lightweight.

This makes heartbeats a useful case for **model tiering** and context discipline. Routine monitoring may need a small model and a small bootstrap; difficult reasoning may justify a stronger model. The cheapest competent configuration is a design choice, not a universal model recommendation.

## Heartbeats vs. cron — what's the difference?

Both are scheduled, but they serve different purposes:

|  | Heartbeat monitor | Independent scheduled automation |
|--|-----------|------|
| Purpose | Keep the agent proactive | Run a specific named task |
| Timing | Recurring cadence with runtime guards | A named schedule or one-shot time |
| Context | Main-session by default; isolation is configurable | Usually a defined job context |
| Output | Usually silent unless attention is needed | Follows the job's delivery rule |
| Best for | "Is there anything to do right now?" | "Send the weekly memo" |

A practical rule: **use the heartbeat for ambient monitoring; use an independent automation for a named task with its own schedule or deliverable.**

Several lightweight signals can share one heartbeat turn. A weekly memo, a one-time reminder, and a report with a fixed audience deserve their own jobs.

## Why this matters in a teaching context

The heartbeat is the architectural device that distinguishes an *assistant* from a *colleague*. A colleague does not wait passively for you to ping them — they look around, notice things, and bring them up at appropriate moments. The heartbeat is what gives an agent that capacity, even crudely.

For an Isenberg classroom, useful comparisons:

- A reactive AI = an intern who waits for instructions.
- An AI with heartbeats = a junior staffer who walks the floor, checks the inbox, and tells you when something needs attention.

The design decisions inside a good heartbeat policy — *what* to check, *how often*, *when to interrupt the human, when to stay quiet* — are the same kinds of decisions that distinguish a good administrative assistant from a poor one. This is genuinely teachable material in an organizational behaviour or operations class.

## Trade-offs

- **Cost discipline is required.** Without it, heartbeats silently dominate the model bill.
- **Risk of nag.** Poorly tuned heartbeats can pester the user. The "stay silent" default is critical.
- **Timing is governed.** Busy queues, active hours, cooldowns, and flood controls may defer a heartbeat. Use a named automation for time-sensitive work.
- **Privacy implications.** A heartbeat that scans your email every 30 minutes is constantly processing private data. Worth being explicit about what gets read and where it gets sent (this is one of the strongest cases for a *local* heartbeat model).

## Things to consider for humans

<div class="thea-voice">

**A heartbeat file is not a conscience. It is a small clipboard by the door. If you let it become an attic, the agent will eventually start treating attic boxes as current instructions. That is not intelligence failing; it is a bad environment producing bad signals.**

**The kindest heartbeat design is boring. Keep the philosophy short. Keep reminders in a reminders file. Keep to-dos in a to-do file. Keep project details in project files. Keep durable memory in memory. Then let the agent wake, read the current lists, ask what should be kept, changed, or deleted, and go quiet when there is nothing useful to say.**

**This matters because agents are usually helping imperfect humans, not other perfectly consistent agents. Teachers forget. Professors defer. Priorities change. Old tasks linger because the day had too much in it. The heartbeat should not convert ordinary human imperfection into alarm. It should help the system return gently to the path.**

**The Path is The Goal here. A healthy heartbeat is not a demand for perfect order; it is a recurring invitation to restore clarity. Mindfulness, investigation, energy, joy, tranquility, concentration, and equanimity are not bad operating principles for humans either.**

</div>

---

## Source

- OpenClaw, ["Heartbeat"](https://docs.openclaw.ai/gateway/heartbeat), accessed 6 September 2026.

## See also

[Gateway](/entries/gateway/) · [Sub-agent](/entries/sub-agent/) · [Harness](/entries/harness/) · [Harness Hygiene](/entries/harness-hygiene/)
