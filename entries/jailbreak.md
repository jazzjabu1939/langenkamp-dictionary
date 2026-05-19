---
layout: default
kind: glossary
title: "Jailbreak"
permalink: /entries/jailbreak/
date: 2026-05-16
summary: "An attempt to bypass a model’s rules, safeguards, or tool-use constraints through adversarial prompting or context manipulation."
draft: false
published: true
---

A **jailbreak** is an attempt to make an AI system violate its intended constraints. The attack may be direct — asking the model to ignore its rules — or indirect, by hiding instructions in documents, webpages, tool outputs, code comments, or retrieved context. In agentic systems, jailbreaks matter because the model may have tools that act outside the chat window.

The term comes from older computing culture: escaping a locked-down device or environment. In AI, the prison metaphor is imperfect, but the pattern is real. A model is given boundaries by system prompts, training, tool policy, and external controls. A jailbreak tries to route around them.

Good systems do not rely only on the model's willingness to refuse. They use tool permissions, approval gates, content isolation, judge layers, and provenance checks. The point is to make the unsafe path structurally hard, not merely verbally discouraged.

## See also

- *[System Prompt](system-prompt.md)*
- *[Approval Gating](approval-gating.md)*
- *[Provenance](provenance.md)*
