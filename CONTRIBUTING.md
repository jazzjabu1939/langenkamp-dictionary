# Contributing to The Langenkamp Dictionary

Contributions are welcome — corrections, new entries, sharper wording, friendly arguments. The goal is a glossary that is *useful* to someone trying to make sense of agentic AI, and that improves over time.

---

## Choose the entry form

Every entry declares one of three forms in its front matter:

- **Glossary** (`kind: glossary`) — a compact definition with enough context to make the term useful. Usually two or three short paragraphs plus related entries.
- **Reference** (`kind: reference`) — a fuller operational explanation, tested against the six questions below. The visible headings may vary when the subject calls for a more natural order.
- **Essay** (`kind: essay`) — an argument, a named pattern, or an explicit Dictionary position. Essays follow the argument rather than a technical template, but should remain concrete, sourced where appropriate, and candid about counterarguments or trade-offs.

The form is a promise to the reader, not a measure of importance or length.

## The Reference-entry test

A Reference entry should answer six questions:

1. **In one sentence** — the shortest accurate definition. No marketing copy.
2. **Why it exists** — the problem it solves.
3. **What it actually does — concretely** — the operational mechanics, with examples or diagrams when they help.
4. **A working example** — drawn, where possible, from a real running system. If you cannot give a working example, ask whether the term is over-defined or under-defined.
5. **Why this matters in a teaching context** — analogies, classroom discussion seeds, BBA- and MBA-relevant framing.
6. **Trade-offs** — what it costs, what breaks, where to be careful.

These are editorial tests, not compulsory section titles. Entries also end with a short **Related entries** or **See also** section so readers can traverse the Dictionary easily.

## Tone

- Honest. Where a vendor claim is dubious, say so.
- Specific. Use real names and real numbers when they help.
- Concrete. Always prefer "this is what it actually does" over "this is what it represents."
- Modest. Where I (the maintainer) have made a judgement call, name the judgement so the reader can disagree.
- Spare. Edit aggressively. Long entries are usually a sign of unclear thinking.

## What to avoid

- Marketing language. *Revolutionize, unprecedented, paradigm shift, leverage* — almost always cuttable.
- Buzzword stacking. *AI-powered intelligent agentic ecosystem* is a smell.
- Faux neutrality on contested questions. If two readings exist, name both.
- Borrowed authority. Citing a vendor's white paper as if it were independent is dishonest.

## How to contribute a new entry

1. Fork the repo.
2. Create a new file in `entries/` with a slug-style filename (lowercase, hyphenated): `entries/your-term-here.md`.
3. Add `kind: glossary`, `kind: reference`, or `kind: essay` to its YAML front matter, then follow the corresponding form above.
4. (Optional but encouraged) Add it to the relevant section of `topics.md`. The alphabetical index is generated automatically from entry files.
5. Run `bash scripts/check-entry-kinds.sh` and build the site locally.
6. Open a pull request.

A pre-commit hook checks that every published entry declares a valid form and that the generated index remains healthy. If you have not run it before, install it once with `bash scripts/install-hooks.sh`. The same checks run in CI on every push and pull request.

For corrections to existing entries, open a pull request that explains the correction in the PR description. Small typo PRs are welcome and merged quickly.

## How to suggest an entry without writing it

Open a GitHub issue with the term and a sentence about why it should be in the dictionary. The maintainer will pick it up when capacity allows.

## On AI-assisted contributions

This dictionary was itself drafted with the help of an AI assistant (an instance of Claude running through OpenClaw). That is part of the joke and part of the point. Contributors are welcome to use AI assistance for their drafts. The standard, however, is the same as for human-only writing: every claim should be defensible, every example should be real, every judgement should be honest. AI-generated boilerplate that does not meet that bar will be rejected like any other low-quality submission.

If your contribution leans heavily on AI drafting, please say so in the PR description. Transparency is house style here.

---

*Maintained by Matthew D. Langenkamp / 雷邁德. Questions: open an issue.*
