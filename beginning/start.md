---
layout: default
title: "Start the assistant safely"
permalink: /beginning/start/
description: "Limit what the assistant can run, start OpenClaw in the background, and have a first conversation in the browser dashboard."
---

*Part of [On Beginning](/entries/on-beginning/). Step 5 of 8.*

# Start the assistant safely

*For everyone who has installed OpenClaw and connected a model, local or cloud.*

## Limit what the assistant can run

Because you chose Custom setup, you were asked about access. For your first week, also block the assistant from running Terminal commands on its own:

```bash
openclaw config set tools.exec.mode deny
```

This blocks the assistant from running shell commands on your computer. It does not by itself restrict file tools, web tools, or every plugin; configure those separately so the assistant can read and write only the practice material you'll use. Do not treat the workspace folder as a security boundary without checking the file-access settings.

After starting the Gateway below, run `openclaw exec-policy show` to see the policy actually in effect. See [permission modes](https://docs.openclaw.ai/tools/permission-modes) for the other settings.

## Run OpenClaw in the background

OpenClaw's core is a background program called the **[Gateway](/entries/gateway/)**. If setup left it running inside your Terminal window, press **Control-C** to stop it. Then install it as a background service and open the chat page in your browser:

```bash
openclaw gateway install
openclaw gateway status
openclaw dashboard
```

The status check should say the Gateway is running and reachable. The last command opens the dashboard. Keep any login link private; it may contain a short-lived access token.

## Your first conversation

1. Send a short message and make sure you get a reply.
2. Type `/model status` in the chat to confirm this conversation is using the model you chose. Local users should see their local model; cloud users should see their chosen cloud model.
3. Cloud users: also complete the [first cloud checkpoint](/beginning/cloud-model/#first-cloud-checkpoint).

---

**Next:** [Give it a first job](/beginning/first-job/).

**Related:** [Gateway](/entries/gateway/) · [Harness](/entries/harness/) · [Gateway commands](https://docs.openclaw.ai/cli/gateway) · [Troubleshooting](/beginning/troubleshooting/)
