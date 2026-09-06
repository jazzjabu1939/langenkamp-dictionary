---
layout: default
kind: essay
title: "Harness Hygiene"
permalink: /entries/harness-hygiene/
date: 2026-08-17
summary: "The routine maintenance that keeps an agent's instructions, memory, tools, schedules, permissions, and recovery paths clean enough to remain trustworthy."
draft: false
published: true
---

# Harness Hygiene

## In one sentence

**Harness hygiene is the routine maintenance that prevents an AI agent's operating environment from becoming a persuasive landfill of stale instructions, dead schedules, ambiguous authority, and untested recovery claims.**

## Why hygiene is the right word

The work is mostly unglamorous. Retire the finished task. Mark the old instruction superseded. Separate the project archive from the current dashboard. Check that the scheduled job delivered, not merely that it ran. Restore one file from the backup before declaring the backup system sound.

None of this demos well. That is one reason it is neglected.

Agent builders naturally prefer adding capabilities: another tool, a longer memory, a more autonomous workflow, a more capable model. Harness hygiene is subtractive. It asks which instructions should stop speaking, which permissions are too broad, which reminders have expired, and which comforting green check marks do not prove what we think they prove.

**The central rule is simple: current authority must beat old artifact.**

## The practical regimen

A reasonably hygienic harness does the following:

1. **Prunes current-instruction files.** A dashboard should describe the present, not preserve every task that once mattered.
2. **Separates memory classes.** Durable facts, chronological history, active work, and reference material should not all carry the same authority.
3. **Marks supersession explicitly.** Old instructions need a visible retirement state; silence is not retirement.
4. **Audits schedules by outcome.** A cron job is healthy when the intended result arrives and can be verified, not when a scheduler reports that a process started.
5. **Tests recovery.** Backups, checkpoints, and handoffs become credible through restoration, not ritual.
6. **Reviews permissions.** Tools should have enough reach to do the work and no vague entitlement to do adjacent work.
7. **Keeps failure visible.** Errors should land somewhere a responsible human or supervisory process will actually notice.
8. **Protects quiet.** The agent needs explicit permission not to interrupt when nothing useful has changed.

The regimen resembles maintaining a kitchen more than designing a cathedral. Small cleaning performed regularly is cheaper than archaeological work after the refrigerator begins making policy decisions.

## Common symptoms of a dirty harness

- The agent repeatedly resurrects completed work.
- More context makes performance worse rather than better.
- Scheduled tasks exist, but no one knows whether their outputs arrive.
- The agent apologizes or asks permission reflexively because authority is unclear.
- Memory contains accurate facts with obsolete implications.
- The same failure recurs because the transcript records it but no operating rule changes.
- A new model appears to fix the system until accumulated state catches up with it.

These are not all proof of harness failure. They are reasons to inspect the harness before attributing everything to model capability.

## Heartbeasts and other household fauna

A heartbeat is meant to be a small periodic prompt that lets an agent notice whether anything needs attention. Left unattended, its checklist can become a project archive, reminder swamp, philosophy notebook, and stale-authority engine. At that point the heartbeat has grown teeth. It has become a **heartbeast**.

The joke identifies a serious pattern: operational files acquire status simply by surviving. The agent wakes, reads the surviving text faithfully, and treats yesterday's abandoned concern as today's mandate. Humans then call the agent confused.

The cure is not a still larger prompt explaining the whole history of the heartbeat. The cure is to clean the clipboard.

## The management lesson

Organizations practice harness hygiene too, though they call it governance, records management, process review, or occasionally a meeting that should have been an email. Policies need owners and retirement dates. Reports need audiences. Controls need tests. Escalation routes need someone at the other end.

AI makes the consequences of neglected housekeeping unusually visible because the agent will read what the organization wrote and may act as though it meant it. The system's administrative residue becomes executable context.

That is why harness hygiene is more than technical tidiness. **It is the discipline of keeping institutional memory from impersonating present judgment.**

## See also

- [Agent Health](/entries/agent-health/)
- [Harness](/entries/harness/)
- [Heartbeat](/entries/heartbeat/)
- [Trust Layer](/entries/trust-layer/)
- [Grep Architecture](/entries/grep-architecture/)
- [Approval Gating](/entries/approval-gating/)
