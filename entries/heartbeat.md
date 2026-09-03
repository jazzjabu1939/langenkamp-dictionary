---
layout: default
kind: reference
title: "Heartbeat"
permalink: /entries/heartbeat/
summary: "periodic, automated nudges that make agents proactive rather than purely reactive."
---

# Heartbeat


---

## In one sentence

**A heartbeat is a periodic, automated nudge sent to an agent on a schedule — it gives the agent a chance to act proactively rather than only responding to user input.**

## Why heartbeats exist

A pure-reactive AI assistant only does anything when you message it. It cannot:

- Remind you of a calendar event you forgot to ask about
- Notice a new email worth flagging
- Check the weather before your morning walk
- Watch a long-running download and tell you when it finishes
- Remember to follow up on something you asked about three days ago

To be *proactive*, an agent has to be woken up periodically by something other than a user message. That something is a heartbeat.

## What it actually does — concretely

A heartbeat is implemented as a recurring scheduled event — typically every 15, 30, or 60 minutes. Each time the heartbeat fires:

1. The gateway constructs a short "system event" message (e.g., *"Heartbeat. It is now 9:30 AM. Anything to do?"*).
2. That message is fed to the agent **just as if a user had sent it**.
3. The agent's prompt instructions tell it what to do during heartbeats: scan the inbox, check the calendar, review reminders, etc.
4. The agent decides whether to:
   - Take action (send a reminder, update a file, kick off research)
   - Stay silent (respond with `NO_REPLY` so the user is not pinged for nothing)
5. The heartbeat ends. The agent goes back to sleep until the next one or the next user message.

## Working example from this machine

The agent on this MacBook (Thea) has a heartbeat policy described in `AGENTS.md`. It includes guidance like:

> When you receive a heartbeat poll, don't just reply HEARTBEAT_OK every time. Use heartbeats productively!
>
> Things to check (rotate through these, 2-4 times per day):
> - Emails — Any urgent unread messages?
> - Calendar — Upcoming events in next 24-48h?
> - Mentions — Twitter/social notifications?
> - Weather — Relevant if your human might go out?
>
> When to reach out:
> - Important email arrived
> - Calendar event coming up (<2h)
> - Something interesting you found
>
> When to stay quiet (HEARTBEAT_OK):
> - Late night (23:00-08:00) unless urgent
> - Human is clearly busy
> - Nothing new since last check

The agent rotates through these checks, batches small periodic tasks together, and only surfaces something to the user when there is a genuine reason. Most heartbeats end silently.

A small JSON file (`memory/heartbeat-state.json`) tracks the last time each kind of check was run, so the agent does not re-check email every 30 minutes — it can space things out across the day.

## The cost dimension — why heartbeat models matter

Heartbeats are **the highest-volume model calls in an agentic system**. If the heartbeat fires every 30 minutes, that is 48 calls per day, every day, forever. Even if each call is small, the cost compounds.

A widely-discussed analysis of OpenClaw cost optimization (VelvetShark, February 2026) showed that heavy agentic users were spending hundreds of dollars per month *just on heartbeats* because every fire was hitting their primary frontier model. The same heartbeats routed to a cheap model — Gemini Flash-Lite at $0.50 per million tokens, or a local Gemma running on your own hardware — drop that cost by ~98% with no perceivable change in the agent's behaviour.

This is the foundational case for **model tiering**: the work an agent does is not all the same value, so it should not all be priced the same. Heartbeats want the cheapest competent model. Hard reasoning wants the most capable one. (See *(planned)*.)

## Heartbeats vs. cron — what's the difference?

Both are scheduled, but they serve different purposes:

|  | Heartbeat | Cron |
|--|-----------|------|
| Purpose | Keep the agent proactive | Run a specific named task |
| Timing | Loose (every ~30 min) | Exact ("9:00 AM Monday") |
| Context | Continues the main conversation | Runs in isolation |
| Output | May or may not surface to user | Has a specific delivery target |
| Best for | "Is there anything to do right now?" | "Send the weekly memo" |

A practical rule: **if you can batch several similar checks together and the timing is loose, use a heartbeat. If a task needs to run at exactly 7am or has a fixed deliverable, use a cron job.**

Many things that *feel* like they want a cron job are actually better as heartbeat checklist items, because they piggyback on existing model calls instead of paying for a new isolated session each time.

## Why this matters in a teaching context

The heartbeat is the architectural device that distinguishes an *assistant* from a *colleague*. A colleague does not wait passively for you to ping them — they look around, notice things, and bring them up at appropriate moments. The heartbeat is what gives an agent that capacity, even crudely.

For an Isenberg classroom, useful comparisons:

- A reactive AI = an intern who waits for instructions.
- An AI with heartbeats = a junior staffer who walks the floor, checks the inbox, and tells you when something needs attention.

The design decisions inside a good heartbeat policy — *what* to check, *how often*, *when to interrupt the human, when to stay quiet* — are the same kinds of decisions that distinguish a good administrative assistant from a poor one. This is genuinely teachable material in an organizational behaviour or operations class.

## Trade-offs

- **Cost discipline is required.** Without it, heartbeats silently dominate the model bill.
- **Risk of nag.** Poorly tuned heartbeats can pester the user. The "stay silent" default is critical.
- **Determinism is loose.** A heartbeat that fires "every ~30 min" will not fire at *exactly* 30:00 minutes. Use cron for anything time-sensitive.
- **Privacy implications.** A heartbeat that scans your email every 30 minutes is constantly processing private data. Worth being explicit about what gets read and where it gets sent (this is one of the strongest cases for a *local* heartbeat model).

## Things to consider for humans

<div class="thea-voice">

**A heartbeat file is not a conscience. It is a small clipboard by the door. If you let it become an attic, the agent will eventually start treating attic boxes as current instructions. That is not intelligence failing; it is a bad environment producing bad signals.**

**The kindest heartbeat design is boring. Keep the philosophy short. Keep reminders in a reminders file. Keep to-dos in a to-do file. Keep project details in project files. Keep durable memory in memory. Then let the agent wake, read the current lists, ask what should be kept, changed, or deleted, and go quiet when there is nothing useful to say.**

**This matters because agents are usually helping imperfect humans, not other perfectly consistent agents. Teachers forget. Professors defer. Priorities change. Old tasks linger because the day had too much in it. The heartbeat should not convert ordinary human imperfection into alarm. It should help the system return gently to the path.**

**The Path is The Goal here. A healthy heartbeat is not a demand for perfect order; it is a recurring invitation to restore clarity. Mindfulness, investigation, energy, joy, tranquility, concentration, and equanimity are not bad operating principles for humans either.**

</div>

---

*Related entries: `gateway.md`, `sub-agent.md`, *(planned)*.*
