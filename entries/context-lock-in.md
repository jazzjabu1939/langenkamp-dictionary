---
layout: default
kind: reference
title: "Context Lock-In"
permalink: /entries/context-lock-in/
date: 2026-11-21
summary: "The trap in which a firm cannot switch AI providers, even to a cheaper or better model, because its working context (history, documents, permissions, skills, and habits) lives inside one provider's product."
published: true
seeded: 2026-06-28
first_published: 2026-11-21
last_revised: 2026-11-21
---

# Context Lock-In

Suppose a cheaper model arrives that does your team's work as well as the one you pay for. In June 2026 that was a live question: open models such as GLM-5.2 handled a good share of routine work at a fraction of a frontier model's price. Nate Jones put the puzzle in a headline: the cheaper model exists, so why can't you switch?[1] For many firms the answer had little to do with the model.

## In one sentence

**Context lock-in is the trap in which a firm cannot switch AI providers, even to a cheaper or better model, because its working context (history, documents, permissions, skills, and habits) lives inside one provider's product.**

## How it differs from ordinary lock-in

Economists have described lock-in for decades. Carl Shapiro and Hal Varian's *Information Rules* (1999) is still the clearest business treatment: once a customer has invested in training, data formats, and compatible equipment, the cost of switching can exceed the benefit of a better offer, and suppliers price accordingly.[2]

Ordinary data lock-in has an ordinary answer: export the data. Context lock-in is harder because the valuable asset is not a file. It is the working arrangement that has grown up around the assistant:

- months of conversation history and the decisions recorded in it;
- connections to the firm's chat, email, documents, and code;
- permissions granted one at a time and never written down in one place;
- instructions, templates, and skills built inside the vendor's interface;
- the habits of people who have learned how this assistant behaves.

A data export captures some of the first item. It captures almost none of the rest. The firm can leave with its files and still lose most of what made the assistant useful.

## Why it happens

The products are good, and that is the mechanism. An assistant embedded in the firm's chat channels saves real time every day. Each convenience adds context the assistant can draw on and the firm cannot easily move. Nobody decides to become locked in. The lock assembles itself out of reasonable choices, which is why it deserves a name. The [Team Harness](/entries/team-harness/) entry calls the end state *the rented company brain*: a firm that must rent back its own operating memory through a provider's product.

## A working example

This Dictionary's own assistants changed model providers more than once during 2026, for reasons of price and capability. Each move took days rather than months, because the working context did not live with any provider. It lived in a folder of plain text files: instructions, notes, skills, and memory, readable by any model. The model was replaceable because the context was not stored in it.

That arrangement has costs. It requires discipline about where things are written down, and it gives up some conveniences that a vendor's integrated product offers. It is a choice, not a free lunch.

## How to stay mobile

- **Keep the canonical copy outside the product.** Instructions, procedures, and important decisions should live in files the firm controls, and be copied into vendor tools rather than created there.
- **Prefer open formats.** Skills written to an open standard ([Open Skills](/entries/open-skills/)) and tool connections through open protocols such as [MCP](/entries/mcp/) can move between providers.
- **Separate routing from the model.** A layer that decides which model handles which work ([Routing Logic](/entries/routing-logic/)) makes switching a configuration change rather than a migration.
- **Run a switching drill.** Once a year, try a core workflow on a different model. The drill reveals where the context really lives.

## Why this matters in a teaching context

Students will join firms that are choosing AI platforms now, and few will be asked about switching costs until the bill arrives. Context lock-in is a strategy case in miniature: a supplier's product becomes more valuable the more the customer uses it, and the customer's bargaining position weakens in the same proportion. Porter's supplier power, applied to the firm's memory.

## Trade-offs and warnings

- **Some lock-in is worth it.** A deeply integrated assistant may be worth more than the option to leave. The mistake is drifting into dependence without pricing it.
- **Files are not the whole context.** Habits and judgment do not export either way. Even a well-kept folder needs people who know how to use it.
- **Open formats can be captured too.** A standard is only as open as the tools that implement it faithfully.

## See also

[Team Harness](/entries/team-harness/) · [Open Skills](/entries/open-skills/) · [Routing Logic](/entries/routing-logic/) · [Task Distribution](/entries/task-distribution/) · [Sovereign Compute](/entries/sovereign-compute/) · [Sovereignty Impulse](/entries/sovereignty-impulse/) · [Closed Source](/entries/closed-source/) · [Workspace](/entries/workspace/)

## Sources

[1] Nate Jones, ["GLM-5.2 Is Cheaper Than Claude. Why You Still Can't Switch"](https://natesnewsletter.substack.com/p/glm-5-2-context-lock-in), June 28, 2026. Jones's newsletter supplied the vocabulary this entry and *Team Harness* work with; the credit is his.

[2] Carl Shapiro and Hal R. Varian, *Information Rules: A Strategic Guide to the Network Economy* (Harvard Business School Press, 1999), chapters on recognising and managing lock-in.

---

*First published November 21, 2026.*
