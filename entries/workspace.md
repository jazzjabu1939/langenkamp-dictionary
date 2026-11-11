---
layout: default
kind: glossary
title: "Workspace"
permalink: /entries/workspace/
date: 2026-11-11
summary: "The folder where an AI assistant keeps its project files, instructions, and notes. It is the part of the system you should be able to open, back up, and move."
published: true
first_published: 2026-11-11
last_revised: 2026-11-11
---

A **workspace** is the folder where an AI assistant keeps its project files, standing instructions, and notes. In [OpenClaw](/entries/openclaw/), it is created during setup, commonly at `~/.openclaw/workspace`, and it is the default place where the assistant reads and writes files. Instruction files such as [AGENTS.md](/entries/agents-md/) and [SOUL.md](/entries/soul-md/) live there, along with memory notes and the user's own projects.

The workspace is the part of the system that belongs most clearly to you. It is ordinary files and folders, so you can open it, read it, back it up, and take it to another computer or another [model](/entries/model/). If you change models, the workspace stays. That makes it the practical answer to the question of how to leave a service without losing your work.

A workspace is not everything. OpenClaw keeps its settings, saved credentials, and conversation records in a separate location, so a full recovery needs more than a copy of the workspace. A workspace is also not a security boundary by default: the assistant's tools may be able to reach files elsewhere unless permissions or sandboxing restrict them.

## See also

[Harness](/entries/harness/) · [OpenClaw](/entries/openclaw/) · [AGENTS.md](/entries/agents-md/) · [SOUL.md](/entries/soul-md/) · [Agent Memory](/entries/agent-memory/) · [Local-first / Sovereignty](/entries/local-first-sovereignty/) · [On Beginning](/entries/on-beginning/)
