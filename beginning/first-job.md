---
layout: default
title: "Give it a first job"
permalink: /beginning/first-job/
description: "Find the assistant's workspace, write its instruction file, and test one small file task whose right answer you already know."
---

*Part of [On Beginning](/entries/on-beginning/). Step 6 of 8.*

# Give it a first job

*For everyone whose assistant has answered a first message.*

## Find the workspace

OpenClaw created a [workspace](/entries/workspace/) folder during setup. On Mac and Linux it is commonly `~/.openclaw/workspace` (`~` means your home folder). On Windows or with an app-managed setup, use the exact workspace path shown during setup. Check yours before creating files somewhere else.

## Tell the assistant who it is

Inside the workspace you'll find a file called `SOUL.md`. This is where you describe who the assistant is and how it should work. You can give it a name if you like; a name can make the work feel less anonymous. More important are clear instructions about the job and its limits.

Open `SOUL.md` in a text editor and adapt it. Keep anything already there that you like. Here's an example:

```markdown
You are Ada, a careful and practical assistant.
Help me organize notes and draft clear prose.
Be concise. Say when you are uncertain. Do not flatter.
For now, work only on the practice files I provide.
Ask before sending messages, publishing, buying, or deleting anything.
Show me what you changed and how you checked it.
```

Put a few preferences about yourself in `USER.md`. Keep project notes in a project folder. Don't paste your whole personal history into the first session.

**These files are instructions, not locks.** They guide behaviour, but they can't physically stop the assistant from doing something. The real limits come from tool permissions and access settings, including the shell setting on [Start the assistant safely](/beginning/start/). Leave email, purchases, Terminal commands, and posting online turned off unless you deliberately need them.

Never put passwords or API keys in these files. When you add services later, use OpenClaw's built-in way of entering credentials.

## Try one small job you can check

1. Inside your workspace, create a folder called `projects`, then a folder inside it called `practice`.
2. In `practice`, create a plain-text file named `meeting-notes.txt` containing these made-up notes:

   ```text
   We need a room for Tuesday's workshop.
   Alex will check availability by Friday.
   The budget is undecided.
   We have not chosen a start time.
   ```

3. Send the assistant this message:

   > Read projects/practice/meeting-notes.txt. Create projects/practice/action-list.md with the agreed task, its owner and deadline, and a separate list of unresolved questions. Do not invent missing decisions or use external services.

4. Open the new file yourself. It should say Alex is checking the room by Friday, and it should list the budget and start time as still undecided. If it made up a budget or a time, that's a mistake worth noticing.

## Check how it did the job

The [dashboard](/entries/dashboard/) shows tool activity. Did the assistant actually read and write the files, or did it just *say* it did? If it asks permission to use a file tool, read the request before approving.

If it prints something that looks like code (for example, `{"name": "write_file", ...}`) instead of creating the file, the task did not happen. See [Troubleshooting](/beginning/troubleshooting/#the-assistant-printed-code-instead-of-creating-the-file).

This is a better first test than asking the assistant to reorganize your real documents. You know what the right answer looks like, and you can inspect every change.

---

**Next:** [Memory and continuity](/beginning/memory/).

**Related:** [Workspace](/entries/workspace/) · [SOUL.md](/entries/soul-md/) · [Tool](/entries/tool/) · [Troubleshooting](/beginning/troubleshooting/)
