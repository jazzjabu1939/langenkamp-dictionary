# Contributing to The Langenkamp Dictionary

Contributions are welcome — corrections, new entries, sharper wording, friendly arguments. The goal is a glossary that is *useful* to someone trying to make sense of agentic AI, and that improves over time.

---

## Style guide

Every entry follows the same six-section structure:

1. **In one sentence** — the shortest accurate definition. No marketing copy.
2. **Why it exists** — the problem it solves.
3. **What it actually does — concretely** — the operational mechanics, with examples or diagrams when they help.
4. **A working example** — drawn, where possible, from a real running system. If you cannot give a working example, ask whether the term is over-defined or under-defined.
5. **Why this matters in a teaching context** — analogies, classroom discussion seeds, BBA- and MBA-relevant framing.
6. **Trade-offs** — what it costs, what breaks, where to be careful.

Entries also end with a short **Related entries** line so readers can traverse the dictionary easily.

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
3. Use the structure above.
4. Open a pull request.

For corrections to existing entries, open a pull request that explains the correction in the PR description. Small typo PRs are welcome and merged quickly.

## How to suggest an entry without writing it

Open a GitHub issue with the term and a sentence about why it should be in the dictionary. The maintainer will pick it up when capacity allows.

## On AI-assisted contributions

This dictionary was itself drafted with the help of an AI assistant (an instance of Claude running through OpenClaw). That is part of the joke and part of the point. Contributors are welcome to use AI assistance for their drafts. The standard, however, is the same as for human-only writing: every claim should be defensible, every example should be real, every judgement should be honest. AI-generated boilerplate that does not meet that bar will be rejected like any other low-quality submission.

If your contribution leans heavily on AI drafting, please say so in the PR description. Transparency is house style here.

---

*Maintained by Matthew D. Langenkamp / 雷邁德. Questions: open an issue.*
