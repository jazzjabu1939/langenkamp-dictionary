---
layout: default
title: "Memory and continuity"
permalink: /beginning/memory/
description: "What an AI assistant keeps between conversations, how it finds saved material again, and a simple test to check it."
---

*Part of [On Beginning](/entries/on-beginning/). Step 7 of 8.*

# Memory and continuity

*For anyone wondering what the assistant will remember tomorrow.*

You can return to a conversation tomorrow and still see yesterday's messages. That does not necessarily mean the model receives all those messages when it answers. Nor does telling an assistant something once guarantee that it will know it in a new conversation.

It helps to distinguish four things.

## Conversation history: what was said

This is the saved exchange between you and the assistant. The application may let you reopen it, but the model usually receives a selected portion of it. A long conversation may be shortened or summarized. A new conversation may begin without the details of the previous one.

Think of the saved history as a transcript. Keeping the transcript and putting it in front of the model are separate actions.

## Workspace files: what was written down

These are ordinary files on your computer: meeting notes, action lists, drafts, and project records. You can open them yourself, copy them, and back them up. The `projects/practice/action-list.md` file from [your first job](/beginning/first-job/) is one.

A file can remain after you close the conversation, but its existence does not mean the assistant has read it. The assistant needs permission and a way to find and open it. Giving it the exact path is a useful start.

For example, "What did we decide yesterday?" leaves the assistant to find the relevant record. "Read projects/practice/action-list.md and tell me what remains undecided" tells it where to look.

## Instruction files: how you want it to work

Files such as `SOUL.md` and `USER.md` hold guidance about the assistant's role and your preferences. Depending on the harness and its settings, designated instruction files are supplied when a conversation starts. An arbitrary file does not become an instruction file merely because you give it an important-sounding name.

A preference might be: "When preparing an action list, put unresolved questions under their own heading." Put that in the instruction file your setup uses, rather than repeating it in every conversation. Then check whether a new conversation follows it. Instructions guide behaviour; they do not guarantee compliance.

## Searchable memory: a way to find relevant records

Some systems can search earlier notes or conversations and bring relevant passages into the current exchange. This can save you from remembering every filename. What gets searched depends on the configuration: it may cover selected workspace files, conversation records, or both.

Some search systems create an **index**, a catalog used to locate material. They may also create **[embeddings](/entries/embedding/)**, numerical representations of text that help find passages with related meanings even when the wording differs. Neither is a promise that the assistant will find every relevant fact.

Before enabling this feature, find out which files it indexes and where that processing happens. A remote embedding service may receive the text it processes. Running the chat model locally does not make that separate service local. You can begin without searchable memory and ask the assistant to open specific files instead.

## Try a simple continuity check

Use the invented practice notes, not personal information.

1. **Open the action-list file yourself.** Confirm that it exists and records Alex's room check, Friday's deadline, and the unresolved budget and start time.
2. **Start a new conversation.** Ask: "Read projects/practice/action-list.md. Who is checking the room, when is the deadline, and what have we not decided?"
3. **Check the answer and the file activity.** The assistant should read the file and report its contents accurately. A plausible answer alone does not establish that it opened the file.
4. **Test one instruction.** If you added the unresolved-questions preference to your instruction file, ask the new conversation to prepare an action list from the practice notes without repeating that preference. See whether it follows it.

The first test checks whether a new conversation can use a saved file when told where to look. It does not prove that the assistant will find that file on its own. The second checks one instruction in one task, not perfect memory.

If a test fails, see [Troubleshooting](/beginning/troubleshooting/#a-new-conversation-doesnt-know-what-we-did).

## During the first week

Notice what you repeatedly have to explain. Save useful preferences in the appropriate instruction file and project decisions in a clearly named project note. Ask the assistant to update those records when needed, then open them to check its work. Keep your own backups.

You are building a small, understandable record of your work together. The aim is to know where important information lives and how to bring it back into the conversation.

---

**Next:** [Stop, back up and recover](/beginning/recovery/).

**Related:** [Agent Memory](/entries/agent-memory/) · [Context Window](/entries/context-window/) · [Workspace](/entries/workspace/) · [SOUL.md](/entries/soul-md/)
