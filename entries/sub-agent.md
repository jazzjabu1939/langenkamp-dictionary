---
layout: default
kind: reference
title: "Sub-agent"
permalink: /entries/sub-agent/
date: 2026-05-02
first_published: 2026-05-02
last_revised: 2026-09-07
summary: "A child agent session created by another agent to perform a bounded piece of work and report a result."
published: true
---

# Sub-agent

**A sub-agent is a child agent session created by another agent to perform a bounded piece of work and report a result.** It has its own model turn and context, and it may have its own tool policy, workspace, timeout, and model selection depending on the system that spawned it.

Sub-agents are useful when a task can be decomposed cleanly: inspect one component, research one question, run one long build, or compare several independent options. The parent supplies the task and relevant context, continues other work or waits, and then evaluates the child's report.

Isolation is not absolute. Some systems start the child with a clean context; others fork part or all of the parent conversation. A child may share the parent's filesystem even while its conversational context is separate. Its tools may be narrower, identical, or separately configured. The earlier version of this entry treated a fresh context, a separate sandbox, and summary-only return as universal properties. They are implementation choices and must be checked in the actual runtime.

## Sub-agents and tools

A tool performs a defined operation and returns its result. A sub-agent can interpret an open-ended task, choose among tools, and perform several steps before reporting. That extra judgment also adds token cost, latency, and another place for errors to enter.

Delegation is therefore appropriate when the task boundary is clearer than the path through the task. Reading one known file or running one command is usually a tool call. Comparing competing explanations across many sources may justify a sub-agent.

## Management analogy

The useful analogy is a manager assigning a bounded job to a temporary colleague. Good delegation requires a clear deliverable, enough context, stated constraints, and review of the returned work. Poor decomposition creates coordination overhead or two agents changing the same thing at once.

In OpenClaw, sub-agent runs are spawned as background child sessions and announce results back to the requester. Codex also supports native child agents for bounded internal work. Their exact context, visibility, persistence, filesystem, and return behaviour differ, so the product documentation and current tool contract are authoritative.

## Trade-offs

- **Coordination overhead.** Spawning and reviewing can cost more than doing a small task directly.
- **Context loss.** A child given too little context may solve the wrong problem; a full fork can reproduce the context load delegation was meant to avoid.
- **Cost and latency.** Each child consumes model time and tokens.
- **Conflicting writes.** Shared files require explicit ownership or isolated worktrees.
- **Verification.** A polished child report is still a claim the parent must assess.

## Source

- OpenClaw, *[Sub-agents](https://docs.openclaw.ai/tools/subagents)*, current documentation.

## See also

*[Tool](/entries/tool/)* · *[Agent](/entries/agent/)* · *[Durable Workflow](/entries/durable-workflow/)* · *[Context Window](/entries/context-window/)*
