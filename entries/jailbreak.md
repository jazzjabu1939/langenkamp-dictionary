---
layout: default
kind: glossary
title: "Jailbreak"
permalink: /entries/jailbreak/
date: 2026-05-16
first_published: 2026-05-16
last_revised: 2026-09-06
summary: "An attempt to elicit behaviour that a model or application is designed to refuse, usually through adversarial prompting."
draft: false
published: true
---

A **jailbreak** is an attempt to elicit behaviour that a model or application is designed to refuse, usually through adversarial prompting. The familiar direct form asks the model to ignore, reinterpret, or route around its safeguards.

Jailbreaking and **prompt injection** overlap, but they are not synonyms. Prompt injection is the broader manipulation of a model through instructions placed in its input or context. It may be direct, from the user, or indirect, hidden in a webpage, document, tool result, or retrieved record. An indirect injection may produce a jailbreak-like bypass, steal data, or redirect an agent without asking for conventionally prohibited content.

The term comes from older computing culture: escaping a locked-down device or environment. In AI, the prison metaphor is imperfect. A model's boundaries come from training and system instructions; an application's boundaries also include tool policy, permissions, sandboxes, and external controls.

Good systems do not rely only on the model's willingness to refuse. They limit privileges, isolate untrusted content, require approval for consequential actions, and validate tool calls. These controls matter most in agentic systems, where a successful bypass may act outside the chat window.

## See also

- *[System Prompt](/entries/system-prompt/)*
- *[Approval Gating](/entries/approval-gating/)*
- *[Provenance](/entries/provenance/)*
- *[The Judge Layer](/entries/judge-layer/)*

*Sources: [OWASP, “LLM01:2025 Prompt Injection”](https://genai.owasp.org/llmrisk/llm01-prompt-injection/); OpenAI, [“Understanding prompt injections”](https://openai.com/safety/prompt-injections/).*
