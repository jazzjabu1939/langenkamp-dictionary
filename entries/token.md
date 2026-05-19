---
layout: default
kind: glossary
title: "Token"
permalink: /entries/token/
date: 2026-05-19
summary: "The unit of language-model text processing that becomes, in practice, a unit of cost, throughput, memory, and capacity."
draft: false
published: true
---

A **token** is a chunk of text used by a language model. It may be a whole word, part of a word, punctuation, whitespace, or another small unit depending on the tokenizer. Models do not literally read text as humans do; they process token sequences.

In practice, tokens become the accounting unit of AI systems. They determine how much text fits in the context window, how much a model call costs, how quickly a system can respond, and how much output can be generated. This is why operators talk about *token burn*, *token angst*, and context limits. The token is tiny, but the economics are not.

For most users, the important lesson is simple: more context and more output are not free. They consume capacity, money, time, and attention.

## See also

- *[Token Burn](token-burn.md)*
- *[Token Angst](token-angst.md)*
- *[Context Window](context-window.md)*
