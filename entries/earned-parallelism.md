---
layout: entry
kind: essay
title: "Earned Parallelism"
permalink: /entries/earned-parallelism/
date: 2026-05-12
summary: "the diagnostic principle for one specific AI register tell — negative parallelism, the *\"It is not X. It is Y.\"* family of constructions. The principle: the structure is the rhetorical capstone of an argument that has already done the work of distinguishing X from Y; the AI version is the same construction with the work stripped out. Includes a linked scanner and a self-audit of this Dictionary's own corpus."
draft: false
published: true
---

## In one sentence

**Earned Parallelism is the editorial test for negative-parallelism sentences — the *"It is not X. It is Y."* family — where the X must be a real possible reading rather than a strawman invented to make the Y sound wiser.**

You have probably noticed the cadence by now. It has the slightly priestly rhythm of contemporary AI prose: *this is not merely a tool; it is a transformation.* *This is not just automation; it is a new substrate.* *This is not a sentence; it is a small fog machine wearing a blazer.*

The construction itself is innocent. English has been using it for centuries. The problem is the unearned version, where the sentence performs the gesture of thought without doing the work underneath it.

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

The Dictionary has a small Python scanner that searches entries for negative-parallelism patterns and reports hits per thousand words. The point is partly the measurement and partly the editorial discipline of having measured. Most commentary on AI writing is hand-waving. This one has a file.

The scanner lives at `scripts/scan-negative-parallelism.py` in the [Dictionary's source repository](https://github.com/jazzjabu1939/langenkamp-dictionary). Run it with:

```bash
python3 scripts/scan-negative-parallelism.py --top 10 --verbose
```

The scanner is deliberately modest. It is a triage tool, not a judge. It can find the pattern; it cannot tell whether the pattern is earned. That remains the writer's job.

## What the scanner found, May 12, 2026

The May 12 audit found **54 hits across 89,057 words**, or **0.61 hits per thousand words**. That is low. For comparison, the kind of AI-assisted LinkedIn or marketing prose that triggered this whole discussion often runs many times higher.

The distribution, however, was uneven. The highest-density entries were *Capability Overhang*, *Agentic Threshold*, *Earned Parallelism* itself, *GenXClaw*, and *Token Angst*. That list was useful because it turned a vague worry — *are we writing in the AI register?* — into an editorial triage queue.

The dominant construction family was *"It is not X. It is Y."* The next most common was *"not because X, but because Y."* Those two families accounted for most of the Dictionary's fingerprint.

The triage pass did not try to eliminate the construction. It asked the diagnostic question for each hit: **is the X real, or invented?** Most occurrences passed. A few did not, and were rewritten. The corpus density barely moved; the cadence improved.

## A confession, in the spirit of the entry

The scanner has, of course, been run on this entry. It found **7 hits**, which puts the entry on diagnosing the symptom near the top of the symptom list. This is funny, but not embarrassing. Several hits are quotations or worked examples; the remaining ones are doing the work the entry says they must do.

That is the point. The doctrine is not zero parallelism. The doctrine is earned parallelism. The scanner produces a signal; judgement makes the diagnosis.

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
