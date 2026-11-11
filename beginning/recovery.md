---
layout: default
title: "Stop, back up and recover"
permalink: /beginning/recovery/
description: "Practise stopping and restarting OpenClaw, test a file backup, and plan what comes after the first week."
---

*Part of [On Beginning](/entries/on-beginning/). Step 8 of 8.*

# Stop, back up and recover

*For everyone. Learn how to turn things off before you need to.*

## Stop and restart

These commands stop the Gateway, start it again, and check on it:

```bash
openclaw gateway stop
openclaw gateway start
openclaw gateway status
```

For an everyday restart, `openclaw gateway restart` does both steps in one.

Stopping the Gateway doesn't necessarily stop Ollama, other programs, or tasks already sent to online services. Know which part you're turning off. After restarting, open the dashboard and repeat the practice-file check from [your first job](/beginning/first-job/).

## Test a backup

1. Copy the `practice` folder somewhere safe, such as an external drive.
2. Restore that copy into a **different** folder in your workspace, such as `projects/restore-check`.
3. Open the restored files and compare them with the originals.

Don't delete your working setup or overwrite the originals to test a backup.

This proves you can recover *those files*, not the whole assistant. A full recovery may also need OpenClaw's settings, scheduled tasks, and saved credentials, which live outside the workspace. OpenClaw has its own [backup guide](https://docs.openclaw.ai/install/backups). Keep a short list of what you'd need to reinstall or reconnect.

## Try switching models

When it's convenient, try the same practice task with a different model in a new conversation and compare the results. Keeping your own files is what makes switching possible. It doesn't guarantee that different models will behave the same way.

## The first week, and what comes next

A good first week leaves you with four things: a working conversation with your chosen local or cloud model, one file task you've checked, a workspace you understand, and a small backup test that passed. That's enough.

If local performance disappoints you, figure out *which task* failed before buying new hardware. A shorter prompt, a better-suited model, or a simpler workflow may fix it. Some jobs will still be worth sending to a cloud model. When you add one, do it on purpose, sign in through OpenClaw's supported setup, and decide what information it's allowed to see. Keep sensitive work on a local model with no cloud fallback, and check that setup separately.

Set a budget for any paid services. Running things locally also costs time: updates, backups, model downloads, and the occasional troubleshooting session. Ownership includes the mornings when software sulks.

Phone access can come later. Start with the browser dashboard. When you connect a messaging app, set it so only your own account can send requests. A convenient channel shouldn't quietly become an open door for everyone.

---

**Back to:** [On Beginning](/entries/on-beginning/).

**Related:** [Workspace](/entries/workspace/) · [Backup guide](https://docs.openclaw.ai/install/backups) · [Troubleshooting](/beginning/troubleshooting/)
