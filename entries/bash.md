---
layout: default
kind: glossary
title: "Bash"
permalink: /entries/bash/
date: 2026-09-01
summary: "A widely used Unix shell that reads commands, launches programs, connects them together, and reports whether they succeeded."
draft: false
published: true
---

# Bash

**Bash is a widely used Unix shell: a program that reads commands, launches other programs, connects them together, and reports whether they succeeded.**

The name stands for **Bourne Again Shell**, a successor to Stephen Bourne's earlier Unix shell. Bash is both interactive—you can type commands into it—and programmable—you can save a sequence of commands as a shell script.

When OpenClaw reports **“Bash failed,”** it usually means a command run through the shell returned a non-zero *[exit code](exit-code.md)*. It does not necessarily mean Bash itself broke. The shell may have worked perfectly while reporting that a file was missing, a search found no match, a program rejected an option, or permission was denied.

That distinction mattered in the September 1, 2026 Dictionary work. A search included an `essays/` directory that did not exist. The search command reported failure; Bash faithfully passed that result upward; the article was then found elsewhere and published normally. **The messenger reported a failed command. The messenger was not the failure.**

Modern macOS uses *zsh* as its default interactive shell, while many automation systems still describe shell-command execution generically as “Bash.” In ordinary conversation, people often blur *Bash*, *shell*, and *terminal*. They are related but not identical.

## Sources

- GNU Project, *Bash Reference Manual*: <https://www.gnu.org/software/bash/manual/bash.html>

## See also

*[Shell](shell.md)* · *[Terminal](terminal.md)* · *[Command-Line Interface](command-line-interface.md)* · *[Exit Code](exit-code.md)*
