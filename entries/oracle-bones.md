---
layout: default
kind: reference
title: "Oracle Bones"
permalink: /entries/oracle-bones/
summary: "dated, falsifiable, written-down predictions filed before the event resolves and scored after; the discipline of accountability across time."
date: 2026-05-04
published: true
first_published: 2026-05-04
last_revised: 2026-09-06
---

# Oracle Bones

---

## In one sentence

**An Oracle Bone is a dated, falsifiable, written-down prediction filed *before* the event resolves, scored *after* it does, and re-read months later — making prediction accountable in the only way it can be: across time.**

## Where the name comes from

Shang dynasty divination, c. 1600–1046 BCE. Ox scapulae and turtle plastrons were heated until they cracked; the cracks were read by diviners; the *question*, the diviner's *reading*, and often the *outcome* were inscribed on the bone — and **kept**.

The keeping is the discipline. Anyone can predict. Few file the prediction with the date and the reasoning, and almost nobody returns to grade it.

The Shang oracle bones survive 3,000 years later because the inscription itself was the practice. The Oracle Court — the small advisory council of five scholars we run inside our learning system to commission and grade predictions — borrows the name and the discipline directly. Its five characters each hold a single verb: **老司天** the Astronomer (*observe*), **占者** the Diviner (*read*), **史** the Scribe (*record*), **史官** the Historian (*remember*), and **滑稽** the Jester (*jest*). The Diviner writes the bone; the Jester argues the opposite before it is filed; the Historian scores it months later. The Scribe keeps the register.

## Why the practice exists

Three failures repeat across every prediction tradition without filed predictions:

1. **Hindsight rewrites memory.** Without a written record, the predictor remembers their accurate calls and forgets their wrong ones, drifting toward an unfounded confidence that erodes future calibration.
2. **The framework cannot improve.** A framework that produces predictions but never grades them has no feedback loop. It will reproduce its own errors indefinitely.
3. **Grey Swans hide.** Without a record, you cannot tell after the fact whether an event was a true black swan or a [Grey Swan](/entries/grey-swans/)—the prediction was either filed or it wasn't.

The Oracle Bone is the smallest unit of accountability that solves all three.

## What an Oracle Bone actually contains

Each bone is a single markdown file in `learning-memos/oracle-bones/YYYY-MM-DD-<institution>-<short-name>.md`, with a fixed structure:

1. **The institution.** What entity is the bone reading? (Apple, OpenAI, AACSB, your own household, etc.)
2. **The window.** What date range is the prediction for? (Specific. *"Within 90 days"* is the minimum; an explicit deadline is better.)
3. **The convergence reading.** Which of the [six vectors](/entries/convergence/) are lit up, and on what evidence? Which are dark to us, and why?
4. **The prediction.** A specific, falsifiable claim. *"Cook will announce a successor by July 1, 2026"* is a bone. *"Apple will face challenges this year"* is not.
5. **The diviner.** Which member of the Court (or which agent) read the bone? Whose call is this?
6. **The reasoning.** Two paragraphs. Enough to reconstruct the call later.
7. **The scoring slot.** Empty until the window closes. Then filled in: *fulfilled / partially fulfilled / refuted / untestable*, with a brief note on what we got wrong about the reasoning, even when the prediction was right.

The file is committed to the repo at the moment of filing. The git timestamp is the bone's authentication; it cannot be backdated without leaving traces.

## A working example

An early public bone in this Dictionary's own practice is **[U.S.–China Managed Trade](/oracle-bones/2026-05-15-us-china-managed-trade/)**, filed May 15, 2026. It made a dated claim about whether the temporary U.S.–China tariff truce would harden into a managed-trade framework rather than simply revert to the prior tariff war.

Its July 31, 2026 deadline has passed, but as of September 6 the linked record still lacks a score. Until that omission is repaired, the example demonstrates the importance of the ritual by failing to complete it. A filed prediction without a verdict is better provenance than a remembered prediction, but it is not yet an Oracle Bone in the full sense defined here. Formal scoring belongs in the bone's own record rather than being smuggled into this glossary entry.

## The ritual

Three timing layers, deliberately staggered:

- **Filing:** opportunistic. When a convergence scan flags an institution, file a bone within a week.
- **Mid-window check:** scheduled. At the halfway point of the prediction window, re-read the bone. *Don't update the prediction* — that violates the discipline. Only note new signals in a side file.
- **Scoring:** scheduled. At the window close, write the scoring section. Honestly. Then write a one-paragraph *what the framework should learn from this* note.
- **Annual reading:** May 3 each year. Re-read every bone scored in the prior twelve months. Look for patterns the individual scorings missed.

The annual reading is where framework versioning happens. Convergence Detection v0.1 → v0.2 will be driven by what the first year's bones reveal, not by armchair revision.

## Why it matters in a teaching context

Strategy and forecasting classes routinely teach students to *make* predictions. Almost none teach them to *file and grade* predictions. The Oracle Bone practice — even in its lightest form, three predictions per semester filed in a shared notebook with a scoring meeting in finals week — closes the loop that the rest of the curriculum leaves open.

It also serves a deeper pedagogical purpose: **it teaches students that being wrong, when filed honestly, is more valuable than being right by luck.** The student whose three predictions were all wrong but who learned why is the one developing a usable framework. The student whose three predictions were vaguely correct in a hand-wavy way has learned nothing.

## Trade-offs and warnings

- **Filed bones can hurt.** Reading your own confident wrong prediction six months later is unpleasant. That is the practice. If filing bones never costs anything, you are not filing real predictions.
- **The temptation to soften.** When scoring, the temptation is to write *"partially fulfilled"* on every bone. Resist it. *Refuted* should be the most common verdict in the early going. The framework only improves if the failures are named honestly.
- **Don't over-file.** Bones cost time. Three to six per quarter is sustainable; thirty is not. Quality over quantity. A bone that is too vague to score later is just bookkeeping.
- **Provenance matters.** Each bone names its diviner. *"The Court said so"* is not provenance; *"the historian read this bone"* is. Even when the diviner is a fictional figure, attribution forces specificity.

## See also

- [Convergence (Cloud Theory)](/entries/convergence/) — what the bones are reading
- [Grey Swans](/entries/grey-swans/) — what unfiled predictions hide
- [Aunties](/entries/aunties/) — the operational counterpart; bones are the epistemic counterpart
- [Naming](/entries/naming/) — why "oracle bone" rather than "prediction log"

---

*This entry should be updated as additional bones are filed and scored.*
