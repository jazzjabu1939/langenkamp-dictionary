---
layout: default
kind: glossary
title: "Dashboard"
permalink: /entries/dashboard/
date: 2026-11-11
summary: "OpenClaw's chat and control page, opened in a web browser and served by the Gateway on your own computer."
published: true
first_published: 2026-11-11
last_revised: 2026-11-11
---

In OpenClaw, the **dashboard** is the chat and control page you open in a web browser. OpenClaw's documentation also calls it the *Control UI*. It is served by the [Gateway](/entries/gateway/) running on your own computer, usually at an address such as `http://127.0.0.1:18789/`. The command `openclaw dashboard` opens it.

The dashboard is where most new users talk to the assistant. It also shows what the assistant is doing: which [tools](/entries/tool/) it called, which files it read or wrote, and which requests are waiting for your approval. That makes it the first place to check whether the assistant actually did a job or only said it did.

A dashboard login link may contain a short-lived access token, so keep it private. If the Gateway is stopped, the dashboard cannot connect.

In general business use, a *dashboard* is any screen that gathers key measures and controls in one place. OpenClaw's dashboard is one instance of that broader meaning.

## See also

[Gateway](/entries/gateway/) · [OpenClaw](/entries/openclaw/) · [Tool](/entries/tool/) · [Approval Gating](/entries/approval-gating/) · [On Beginning: Start the assistant safely](/beginning/start/)
