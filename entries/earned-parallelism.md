---
layout: entry
title: "Earned Parallelism"
permalink: /entries/earned-parallelism/
date: 2026-05-12
summary: "the diagnostic principle for one specific AI register tell — negative parallelism, the *\"It is not X. It is Y.\"* family of constructions. The principle: the structure is the rhetorical capstone of an argument that has already done the work of distinguishing X from Y; the AI version is the same construction with the work stripped out. The entry contains a Python scanner, reproduced verbatim, that the reader is invited to run on their own writing. Includes a self-audit of this Dictionary's own corpus."
draft: false
published: true
---

## A note on the seriousness of this entry

This entry takes a piece of English-major housekeeping and treats it the way a structural engineer would treat a load-bearing beam. The earnestness is the joke. We have written a Python scanner. We have measured our own corpus. We have produced a number expressed in *hits per one thousand words.* If you find this absurd, that is the correct response, and you are also encouraged to use the scanner.

## What negative parallelism is, and why it has become an AI tell

*Negative parallelism* is the rhetorical construction *"It is not X. It is Y."* — and its family of variants: *"This is not just X, it is Y."* *"Not X but Y."* *"It's not merely X — it is Y."* *"Not because X, but because Y."* The construction is ancient. Cicero used it. The King James translators used it. Winston Churchill used it canonically:

> *"Now this is not the end. It is not even the beginning of the end. But it is, perhaps, the end of the beginning."*[^churchill]

John F. Kennedy used it canonically in chiastic form:

> *"Ask not what your country can do for you — ask what you can do for your country."*[^kennedy]

The construction works in those passages because each clause is *earned*. Churchill has actually done the work of distinguishing *the end* from *the beginning of the end* from *the end of the beginning*; the three negations and the affirmation each carry distinct meaning, and the cumulative structure is the *capstone* of an argument the audience has been led through. Kennedy's chiasmus inverts a reading the audience was *actually expecting* — the framing of citizenship as a transactional relationship in which the state owes its citizens — and replaces it with one that genuinely is a *reframe*, with the inversion structurally embodied in the syntax. In both cases the structure is performing real work *because the work has been done beneath it.*

In May 2026, Jason Koebler published a piece in 404 Media titled *Your AI Use Is Breaking My Brain*, and named negative parallelism as the most infamous AI-writing tell. The example that made him stop typing mid-paragraph was his own: he caught himself writing *"It's not just in places we're conditioned to see AI…"* in his own piece *about* AI writing, froze, deleted the sentence, and recorded the moment for the reader. He could not be sure whether he had written that sentence because the construction was actually the best phrasing — or because he had been immersed in an internet full of AI-generated text for so long that the rhythm had colonised his own writing.

His self-catch is the load-bearing moment of the entire article. It also names the precise question this Dictionary entry exists to answer: *how do you tell whether your own use of negative parallelism is honest or contaminated?*

## The principle: the work is what matters

**The Dictionary's position: the construction is not the problem. The absence of work underneath the construction is the problem.**

AI writes *"This is not just X, it is Y"* as a *substitute* for distinguishing X from Y. The X is invented — a strawman — to push the reader toward Y. The reader feels the rhetorical pull of the structure and follows it; the absence of actual content beneath the pull produces the uncanny *something is off* sensation Koebler describes. The structure performs the gesture of having thought without the cost of having thought.

The diagnostic question, the load-bearing test of this entry, is therefore precise. **Before writing or keeping any negative-parallelism sentence, ask:**

> *Is the X a real reading the reader might actually have — a misreading we are heading off, a distinction the reader needs to feel — or is the X a strawman I invented to make the Y land harder?*

If the X is real, the construction is doing work; keep it. If the X is invented, the construction is rhetorical air; rewrite. The test is binary in principle and a judgement call in practice, which is the right kind of test for a writing question.

Two worked examples from this Dictionary's own corpus, taken from before this entry was written:

**Passes the test.** From *Closed Source*: *"This is not a criticism of Anthropic specifically — it is the structural reality of closed-source."* The X here (criticism of Anthropic) is a misreading the surrounding paragraph anticipates and heads off. A reader who saw the entry's complaints about deprecation, terms-of-service changes, and regional outages might reasonably read it as a complaint *about* Anthropic. The sentence interrupts that reading, names it, and redirects it. The structure is doing real work. The sentence stays.

**Fails the test.** From an earlier draft of *Capability Overhang* (since revised): *"This is not laziness. It is the operator's reasonable expectation."* The X here (laziness) is a strawman; the surrounding paragraph never raises laziness as a candidate reading and the reader was not heading there. The sentence reads as if it is doing work, but it is not. It was rewritten in the May 2026 triage pass.

## Three preferred syntactic alternatives when the distinction *is* real

The goal is not to eliminate negative parallelism. The goal is to vary the cadence so the construction is the occasional rhetorical capstone, not the recurring drumbeat. Three uses in a 1,000-word entry is a drumbeat; one use is a capstone. When the X is real but the cadence is repeating, three alternatives:

1. **Single-sentence form with em-dash.** *"This is the structural reality of closed-source, not a criticism of Anthropic specifically."* The information is the same; the cadence does not repeat.
2. **Parenthetical form.** *"The structural reality of closed-source (not a criticism of Anthropic specifically) is that…"* Subordinates the negation so it does not occupy a full sentence's worth of attention.
3. **Direct affirmative with the anticipated misreading named in passing.** *"The structural reality of closed-source is that… — the *criticism of Anthropic* reading is one this Dictionary explicitly rejects, for reasons developed in [Closed Source]."* Names the misreading without staging it in parallel.

Vary the form. Let the cadence breathe.

## Now the joke gets earnest: the scanner

The Dictionary has written a Python script that scans the entries and reports hits per 1000 words. The script is reproduced below in full. The point is partly the measurement and partly the *gesture of having measured.* Most editorial commentary on AI writing is hand-waving. This one has a Python file.

The script is at `scripts/scan-negative-parallelism.py` in the [Dictionary's source repository](https://github.com/jazzjabu1939/langenkamp-dictionary). Run with `python3 scripts/scan-negative-parallelism.py --top 10 --verbose` for a full report.

```python
#!/usr/bin/env python3
"""
scan-negative-parallelism.py

Scans Langenkamp Dictionary entries for negative-parallelism constructions
("not just X, Y"; "not X but Y"; "It is not X. It is Y." etc.) and reports
per-entry counts and density (occurrences per 1000 words).

The catalogue distinguishes between AI-shaped (rhetorically "free") uses and
constructions that may be doing real work. Manual review is still required —
the scanner is a triage tool, not a judge.
"""

from __future__ import annotations
import argparse
import re
from pathlib import Path
from collections import defaultdict

ENTRIES_DIR = Path(__file__).resolve().parent.parent / "entries"

PATTERNS = [
    # "not just X, [it's/this is/Y]"
    ("not_just_X_Y", re.compile(
        r"\bnot just\s+[^.,;:!?\n]{2,80}[,\u2014\-]\s*"
        r"(?:it[' ]?s|this is|but|they are|but rather|but instead|\u2014)\b",
        re.IGNORECASE,
    )),
    # "not only X, [but/Y]"
    ("not_only_X_Y", re.compile(
        r"\bnot only\s+[^.,;:!?\n]{2,80}[,\u2014\-]\s*"
        r"(?:but|it[' ]?s|this is|\u2014)\b",
        re.IGNORECASE,
    )),
    # "not merely/simply X, [but/Y]"
    ("not_merely_X_Y", re.compile(
        r"\bnot (?:merely|simply)\s+[^.,;:!?\n]{2,80}[,\u2014\-]\s*"
        r"(?:but|it[' ]?s|this is|\u2014)\b",
        re.IGNORECASE,
    )),
    # ", not X but Y" or ", not X, Y" or ", not X — Y"
    ("comma_not_X_Y", re.compile(
        r",\s+not\s+[a-z][^.,;:!?\n]{2,60}\s+(?:but|\u2014|\-\-)\s+[a-z]",
        re.IGNORECASE,
    )),
    # "It is not X. It is Y." / "It is not X — it is Y" / "This is not X. It is Y."
    ("it_is_not_X_it_is_Y", re.compile(
        r"\b(?:it is|it[' ]?s|this is|that is)\s+not\s+"
        r"[^.;:\n\u2014]{3,80}[.;\u2014]\s+"
        r"(?:it is|it[' ]?s|this is|that is)\s+[a-z]",
        re.IGNORECASE,
    )),
    # "The X is not Y. It is Z." (parallel anaphora)
    ("the_X_is_not_then_is", re.compile(
        r"\bThe [a-z]+ is not\s+[^.;:\n]{3,60}\.\s+"
        r"(?:It is|The [a-z]+ is)\b",
    )),
    # "not because X, but because Y"
    ("not_because_X_because_Y", re.compile(
        r"\bnot because\s+[^.,;:!?\n]{3,80},?\s*but because\b",
        re.IGNORECASE,
    )),
]


def count_words(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text))


def scan_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    # Strip front-matter and HTML comments to avoid false positives.
    text_body = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)
    text_body = re.sub(r"<!--.*?-->", "", text_body, flags=re.DOTALL)

    word_count = count_words(text_body)
    counts = defaultdict(int)
    examples = defaultdict(list)
    total = 0

    for label, regex in PATTERNS:
        for m in regex.finditer(text_body):
            counts[label] += 1
            total += 1
            start = m.start()
            line_no = text_body.count("\n", 0, start) + 1
            snippet = m.group(0).strip()
            if len(snippet) > 140:
                snippet = snippet[:137] + "..."
            examples[label].append((line_no, snippet))

    density = (total / word_count * 1000) if word_count else 0.0

    return {
        "path": path,
        "words": word_count,
        "total": total,
        "counts": dict(counts),
        "examples": dict(examples),
        "density": density,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--top", type=int, default=15)
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--min-words", type=int, default=200)
    args = parser.parse_args()

    results = []
    for path in sorted(ENTRIES_DIR.glob("*.md")):
        if path.name == "index.md":
            continue
        r = scan_file(path)
        if r["words"] < args.min_words:
            continue
        results.append(r)

    grand_total = sum(r["total"] for r in results)
    grand_words = sum(r["words"] for r in results)
    grand_density = grand_total / grand_words * 1000 if grand_words else 0

    print(f"=== Langenkamp Dictionary: Negative-Parallelism Scan ===")
    print(f"Entries scanned: {len(results)} (min {args.min_words} words)")
    print(f"Total words:     {grand_words:,}")
    print(f"Total hits:      {grand_total}")
    print(f"Corpus density:  {grand_density:.2f} per 1000 words")
```

(The full version, with the verbose reporting and per-family breakdown, is in the repo. The above is the core; the rest is presentation.)

## What the scanner found, May 12, 2026

The Dictionary's own corpus was audited on May 12, 2026, with the AI Writing cluster (including this entry) included. The results, with appropriate gravity:

| Measure | Value |
|---|---|
| Entries scanned | 64 (min 200 words) |
| Total words | 89,057 |
| Total hits | 54 |
| **Corpus density** | **0.61 per 1000 words** |

The corpus density of 0.61/1k is *low*. For comparison: a typical paragraph of AI-generated LinkedIn content or AI-assisted marketing copy runs 5–15 hits per 1000 words. The Dictionary is at roughly a tenth of that. The fingerprint is faint.

But the distribution is uneven, and the top of the density list is worth naming. As of May 12, 2026:

| Entry | Density | Hits |
|---|---|---|
| *Capability Overhang* | 3.69/1k | 3 |
| *Agentic Threshold* | 2.88/1k | 2 |
| *Earned Parallelism* (this entry) | 2.52/1k | 7 |
| *GenXClaw* | 1.97/1k | 5 |
| *Token Angst* | 1.74/1k | 2 |

The dominant construction family in our corpus is *"It is not X. It is Y."* — 29 of 54 hits, more than half the total. The next-most-common is *"not because X, but because Y"* at 10 hits. These two families together account for over 70% of the corpus fingerprint.

The triage pass on the top of this list was completed in the same May 12 working session that produced this entry. Most occurrences passed the diagnostic test on review — the X was real, the work was done, the construction was a capstone. A small number were rewritten because the X was a strawman. The corpus density did not change much; the *cadence* did.

## A confession, in the spirit of the entry

The scanner has, of course, been run on this entry. The result: **7 hits at 2.52 per 1000 words.** This places the entry on diagnosing the construction *third on the density list of the entire Dictionary*, just below *Capability Overhang* (the entry the diagnostic standard was developed against) and well above the corpus average of 0.61. The entry on the symptom contains the symptom at near-peak density.

This is honest, not embarrassing, and the breakdown matters. Of the 7 hits:

- **2 are inside block-quotes** — the Churchill *"This is not the end. It is not even the beginning of the end."* and parts of the Koebler/worked-example quotes. These are not the entry's writing; they are the entry's evidence.
- **3 are inside the *Two worked examples from this Dictionary's own corpus* section** — the *Closed Source* sentence that passes the test and the *Capability Overhang* sentence that failed it, both quoted directly. These are exhibits, not the entry's own prose.
- **2 are in the entry's own prose**, both performing earned work: one in the principle section naming the diagnostic question, one in the closing recommendations. Both have real X's, real Y's, and the surrounding work to ground them.

The scanner is a regex-based pattern-matcher; it cannot distinguish a quoted exhibit from the entry's own sentences, nor an earned construction from a strawman one. *That is the point.* The scanner produces a triage signal. The human judgement makes the diagnosis. The entry has been triaged, the construction stays where it is doing work, and the reader is welcome to verify by reading the scanner's output for themselves.

The entry has not been engineered to hit zero. *Earned Parallelism* is not the doctrine that the construction must be eliminated. It is the doctrine that the construction must be checked.

## Recommendations

For an operator who has been writing prose long enough to be uncertain whether their own cadence has been colonised:

1. **Run the scanner on your own corpus, if you have one.** A blog, a Substack, a folder of essays, a thesis. Get a number. The number will probably surprise you in one direction or the other.
2. **Apply the diagnostic test to each hit.** Is the X real or invented?
3. **Rewrite the strawman cases.** Keep the earned cases.
4. **Vary the syntax across the keeps.** The three alternatives above (em-dash, parenthetical, named-misreading) are cadence-breakers when the construction starts to repeat.
5. **Re-run the scanner periodically.** If new entries are creeping above ~3/1k, the colonisation is winning. If they sit around 0.5–1.5/1k, the writer is awake.

The goal is not to write like a human, in the abstract. It is to write like the human you actually are. Negative parallelism in your own voice, when the work has been done, is honest. Negative parallelism as a rhetorical substitute for work is a small lie. The scanner cannot tell the difference. You can.

## See also

- *[AI Writing](ai-writing.md)* — the parent hub of this cluster
- *[Zombie Internet](zombie-internet.md)* — the medium this Dictionary is writing through
- *[The Olang' Trap](olang-trap.md)* — the structural counterpoint: which native human registers get falsely flagged as AI
- *[The Lazy Median Hypothesis](lazy-median-hypothesis.md)*
- *[The Sinceerly Stack](sinceerly-stack.md)*
- *[Mediation (a la Gibson)](mediation-a-la-gibson.md)*
- *[English Major](english-major.md)*
- `STYLE_INTERNAL.md` in the [Dictionary's source repository](https://github.com/jazzjabu1939/langenkamp-dictionary) — the back-of-house editorial note where this principle was first written down

---

[^churchill]: Winston Churchill, speech at the Lord Mayor's Luncheon, Mansion House, London, 10 November 1942, following the Allied victory at the Second Battle of El Alamein. One of the most-quoted single passages in 20th-century English oratory; the structure is precisely the *"not X. Not Y. But Z."* triple negation followed by an affirmation that the reader feels has been earned by the surrounding war narrative.
[^kennedy]: John F. Kennedy, inaugural address, 20 January 1961. The chiasmus is the structural inversion of the construction this Dictionary is calling *negative parallelism* — *X for Y* / *Y for X*, with the rhetorical hinge in the middle. Kennedy's speech-writer Ted Sorensen credited the rhetorical formula to a long tradition in American political oratory dating back to the early 20th century; both Oliver Wendell Holmes Jr. and Warren G. Harding used near-identical constructions decades earlier. The structure is older than the page on which you are reading it, which is the entry's load-bearing point: AI did not invent this. AI is stripping the work out from underneath it.
