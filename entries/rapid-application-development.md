---
layout: default
kind: glossary
title: "Rapid Application Development / RAD"
permalink: /entries/rapid-application-development/
date: 2026-08-17
seeded: 2026-08-17
first_published: 2026-08-17
last_revised: 2026-08-17
summary: "An iterative software-development method built around fast prototypes, user feedback, short construction cycles, and verified release—a useful ancestor of AI-assisted development."
draft: false
published: true
---

**Rapid Application Development**, or **RAD**, is a software-development method that favours early working prototypes, user feedback, and short construction cycles over exhaustive planning before anyone sees the system. James Martin formalised the method in 1991, building on an argument he had made in his wonderfully premature 1982 book, *Application Development Without Programmers*.

RAD matters again because an AI coding agent can now turn a plain-language description into a clickable application in minutes. The prototype lets users discover that the approval screen is confusing, the workflow is wrong, or the purple background has the unmistakable complexion of AI slop. This is useful knowledge, acquired while changes are still cheap.

But a prototype reveals what users can see. It does not reliably reveal a missing rule. An employee testing an expense application may never notice that nothing prevents self-approval. The discoveries and invariants therefore need to be written into a specification, turned into acceptance and security tests, and verified before release. In AI-assisted development, the prompt opens the inquiry; it is not yet the requirements document.

RAD's durable lesson is consequently less “build without programmers” than **build early enough to learn, then specify and verify what was learned**. When code becomes cheaper to produce, judgment migrates upstream into requirements and downstream into testing. The programmers have not vanished. They have moved toward the places where the system says what it means and proves that it did it.

## See also

- *[Martin Keen](/entries/martin-keen/)*
- *[Durable Workflow](/entries/durable-workflow/)*
- *[Human Judgment Layer](/entries/human-judgment-layer/)*
- *[Verification Gap](/entries/verification-gap/)*

## Sources

- James Martin, *Application Development Without Programmers* (Prentice-Hall, 1982).
- James Martin, *Rapid Application Development* (Macmillan, 1991).
- IBM Technology, Martin Keen, *[What Is RAD? Why It Matters in the Age of AI Coding](https://www.youtube.com/watch?v=J0zbWsutyA8)*, 17 August 2026.
