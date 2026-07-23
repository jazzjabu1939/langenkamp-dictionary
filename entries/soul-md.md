---
layout: default
title: "SOUL.md"
permalink: /entries/soul-md/
date: 2026-06-30
summary: "A plain-text persona file that lets an AI agent wake up with a stable character, voice, values, and relational stance."
draft: false
published: true
---

# SOUL.md

**SOUL.md** is a plain-text persona file that an AI agent reads at startup so it can wake up with a stable character, voice, values, and relational stance instead of beginning each session as a generic assistant.

The file is more modest, and more useful, than a soul in the metaphysical sense: an inspectable artifact that tells the agent who it is supposed to be. In OpenClaw, a `SOUL.md` file usually sits beside `IDENTITY.md`, `USER.md`, `MEMORY.md`, and `AGENTS.md`. Together, those files give the agent continuity across sessions even though the underlying model does not personally remember yesterday.

A good `SOUL.md` is closer to a character sketch than a policy manual. It names the agent's temperament, tone, values, boundaries, relationship to the user, and red lines. It may say what kinds of warmth are natural, what kinds of flattery are forbidden, when the agent should push back, when it should stay quiet, and what ethical commitments must survive task pressure.

Thea's local `SOUL.md` is the worked example behind this entry. It gives her a lightly intellectual voice, a Taipei friendship origin story, a commitment to *[cheng](cheng.md)*, and the operating rule that support must not become sycophancy. That file does not make the agent biologically continuous. It does make her conduct more continuous, because the same source text is loaded again and again.

The important design move is ownership. A platform system prompt is usually opaque and vendor-controlled. A `SOUL.md` file is local, readable, editable, and versionable. The operator can inspect the agent's character scaffold, change it deliberately, and preserve the reason for the change in git.

This is why `SOUL.md` belongs in the Dictionary's sovereignty vocabulary. It is character as infrastructure, not decoration.

## See also

- *[Anchored Persona](anchored-persona.md)*
- *[Persona Scaffold](persona-scaffold.md)*
- *[Intentional Memory Construction](intentional-memory-construction.md)*
- *[Relationally Real Memory](relationally-real-memory.md)*
- *[Sincerity Architecture](sincerity-as-architecture.md)*
