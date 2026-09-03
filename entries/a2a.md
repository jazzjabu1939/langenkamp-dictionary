---
layout: default
kind: reference
title: "A2A (Agent-to-Agent Protocol)"
permalink: /entries/a2a/
date: 2026-08-11
summary: "Google's open protocol for discovery, delegation, and collaboration between independent AI agents. MCP connects an agent to tools; A2A connects one agent to another."
draft: false
published: true
---

# A2A (Agent-to-Agent Protocol)

**A2A is an open protocol for communication and collaboration between independent AI agents: discovery, delegation, progress tracking, and the exchange of results across different vendors and frameworks.**

The shortest useful distinction comes from IBM:

- **[MCP](mcp.md)** is how an agent talks to tools and data.
- **A2A** is how an agent talks to another agent.

That sounds like a small difference. It is the difference between giving an employee access to a database and giving one department a reliable way to commission work from another.

## Why A2A exists

An agent may be perfectly capable within its own environment but unable to collaborate with agents built by another vendor or organization. A procurement agent might need a finance agent to approve spending. A travel agent might need a specialist visa agent. A buyer's agent might need to ask a seller's agent for availability, delivery commitments, and return terms.

Without a shared protocol, every pair needs a custom integration:

**Agent A × Agent B × Agent C × every new platform = a rapidly expanding tangle of bespoke connections.**

A2A supplies a common communication layer. An agent built with one framework can discover and delegate work to an agent built with another without learning its internal code, private memory, tool configuration, or proprietary reasoning process.

This last point is important. A2A treats the remote agent as **opaque**. The client does not need to inspect the other agent's mind. It needs to know what the agent can do, how to ask, how to authenticate, how to track the work, and what result came back.

That is how organizations already cooperate. A company does not ordinarily inspect the internal deliberations of every supplier. It evaluates the supplier's identity, capabilities, terms, credentials, status reports, and deliverables.

## Agent Card

The central discovery object in A2A is the **Agent Card**: a JSON document functioning as a machine-readable business card and service description.

An Agent Card can describe:

- the agent's identity;
- its service endpoint;
- the skills or capabilities it offers;
- supported protocol features;
- authentication requirements;
- the information a client needs to decide whether and how to use it.

The card makes delegation possible before the agents have spoken. A client agent reads it, decides whether the remote agent is suitable, learns how to structure the request, and establishes the required security context.

This is more consequential than the stationery metaphor suggests. The Agent Card is an early unit of **machine-readable professional identity**. It says: *this is who I am, this is what I can do, this is where I can be reached, and these are the conditions under which I will accept work.*

For the Dictionary, Agent Card belongs inside A2A rather than as a separate entry. It is the protocol's discovery and capability-declaration mechanism.

## What passes between agents

A2A defines several basic objects:

- A **Task** is a stateful unit of delegated work with an identifier and lifecycle.
- A **Message** is one turn in the interaction: an instruction, question, answer, context, or status update.
- A **Part** is a content container that can carry text, structured data, a file reference, or binary material.
- An **Artifact** is a concrete deliverable produced during the task: a document, image, dataset, report, or other retrievable result.

The protocol supports immediate request-and-response work, polling for longer tasks, streamed progress, and push notifications for work that continues after the original connection has closed.

In other words, A2A is not merely a chat format. It is a small operating language for commissioning and supervising work.

## MCP and A2A are complementary

MCP and A2A are sometimes presented as rival standards. They solve different layers of the problem.

Imagine a finance agent asked to review a proposed vendor contract:

1. The procurement agent uses **A2A** to delegate the financial review to the finance agent.
2. The finance agent uses **MCP** to retrieve budget data, query the accounting system, and inspect the contract repository.
3. The finance agent returns its analysis and approval status through **A2A**.

MCP equips the specialist. A2A engages the specialist.

This layering is one reason both protocols matter to **[Commercial Legibility](commercial-legibility.md)**. A business must expose more than callable tools. In an agent-mediated market it may also need a legible agentic representative that can declare capabilities, receive delegated work, negotiate within authority, and return structured commitments.

## A2A is not a sub-agent protocol

A2A should also be distinguished from the **[Sub-agent](sub-agent.md)** pattern.

A sub-agent is usually an internal child session created and controlled by a parent agent inside one harness. The parent decides what context to provide, what tools the child may use, and how the result returns.

A2A is for communication between **independent agentic applications**. They may belong to different vendors, organizations, security domains, or technical frameworks. The client generally does not control the remote agent's internal architecture.

The distinction resembles employees and suppliers. A manager delegates to an employee through the firm's internal hierarchy. The company engages a supplier through an external interface, contract, and trust boundary. Both involve delegation. They are not the same governance problem.

## Governance and trust

Open communication does not mean automatic trust. An Agent Card is a claim about identity and capability, not proof that the agent is competent, honest, solvent, secure, or authorized to make the promises it makes.

A mature A2A ecosystem therefore requires layers the base communication protocol cannot supply by itself:

- identity and credential verification;
- authorization and scoped delegation;
- audit trails and task histories;
- contractual limits;
- reputation and certification;
- dispute and recourse mechanisms;
- controls preventing one agent from laundering an unauthorized action through another.

This is where an open technical standard becomes a market institution. HTTP made websites reachable; it did not make every website trustworthy. A2A can make agents interoperable; it cannot make every agent worthy of delegation.

## Why it belongs in the Dictionary

A2A names the moment when agents stop being isolated products and begin becoming an economy.

The first wave of agentic AI concentrated on what one agent could do: reason, call tools, use memory, and complete a workflow. The next layer concerns specialization and exchange. One agent cannot carry every context, permission, jurisdiction, professional credential, and organizational relationship. It will need to find other agents, commission work, receive artifacts, and decide whether to trust the result.

That is not only a technical architecture. It is an organizational one. A2A turns delegation, specialization, coordination, and transaction costs into protocol design.

Google originally developed A2A and later donated it to the Linux Foundation. The protocol is now maintained through a technical steering structure representing several large technology and enterprise-software companies. That governance move matters: a protocol intended to connect agents across organizational boundaries cannot remain credible if it is merely one vendor's private dialect.

## See also

[MCP](mcp.md) · [Commercial Legibility](commercial-legibility.md) · [Agent](agent.md) · [Sub-agent](sub-agent.md) · [Harness](harness.md) · [Tool](tool.md) · [AGENTS.md](agents-md.md) · [Agentic-Native Design](agentic-native-design.md)

## Sources

- A2A Protocol, official documentation and specification: <https://a2a-protocol.org/latest/>
- A2A Protocol, "Core Concepts and Components in A2A": <https://a2a-protocol.org/latest/topics/key-concepts/>
- IBM Technology, "5 AI Agent Terms You Need to Know," June 23, 2026: <https://www.youtube.com/watch?v=k5jYwyhDMxA>
