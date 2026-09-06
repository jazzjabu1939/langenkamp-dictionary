---
layout: default
kind: glossary
title: "Exit Code"
permalink: /entries/exit-code/
date: 2026-09-01
summary: "A small status number returned by a program when it finishes, conventionally zero for success and non-zero for another outcome or failure."
draft: false
published: true
---

# Exit Code

**An exit code is a small status number returned by a program when it finishes: conventionally `0` means success, while a non-zero value means some other outcome or failure.**

The number lets software judge software. A human may read the words printed on screen; an automation system usually looks first at the exit code. If it is non-zero, the surrounding tool may summarize the event as **failed**.

The convention needs interpretation. A search program may return `1` simply because it found no matching text. That can be expected and harmless, but a generic automation layer may still display a warning. Another code may mean an invalid command, missing file, denied permission, or internal program error.

This is why **“command failed” describes a machine-readable outcome, not necessarily the fate of the whole task**. A good operator reads the actual error, decides whether it matters, and continues when a safe alternative exists.

## See also

*[Bash](/entries/bash/)* · *[Shell](/entries/shell/)* · *[Command-Line Interface](/entries/command-line-interface/)*
