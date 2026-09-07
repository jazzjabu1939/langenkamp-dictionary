# Batch N — Plain-Prose Review

**State:** reviewed but unpublished

**Baseline:** `4e9bfe8`

**Branch:** `editorial/alphabetical-plain-prose-audit-n`

**Published corpus:** 2 entries

**Excluded current drafts:** none

## Ledger

| Entry | Review status | Change class | Notes |
|---|---|---|---|
| The Nine Tripod Cauldrons / 九鼎 | reviewed | light revision | Preserved the newly published historical essay and its Dictionary extension; verified the *Zuo Zhuan*, National Museum of China, and Columbia sources; converted internal references to canonical URLs. |
| The Narrator's Compression | reviewed | substantive revision | Incorporated the operator's revised draft, which keeps the original mistake inside the argument; replaced the “70/30” probability-readout claim with a distinction between generated self-report and measured internal state; added Lindsey's causal concept-injection evidence and Anthropic's limited planning examples; separated multiple drafts, the interpreter, confabulation, predictive processing, global workspace, evidence accumulation, and the contested Libet interpretation; added explicit metadata, current sources, objections, and canonical links. |

## Batch findings

- **2 entries reviewed:** 1 received a light revision and 1 received a substantive revision.
- *The Nine Tripod Cauldrons* already distinguished transmitted political memory from surviving archaeology. Its primary-source quotation and institutional interpretation remain sound.
- *The Narrator's Compression* contained the batch's central defect: it treated an AI assistant's conversational percentage as privileged introspection and made several different cognitive-science frameworks appear to establish one settled account. The operator's revised draft turns that mistake into an example of the term itself and makes the analogy testable rather than merely flattering.
- Lindsey's 2025 concept-injection experiments supply the strongest new evidence: some models sometimes report manipulated internal states accurately, but the ability is unreliable and ordinary conversation cannot distinguish introspection from confabulation. Anthropic's circuit-tracing work provides limited examples of plan-level representation without establishing a general system of competing trajectories.
- The revision also corrects the Libet inference. Readiness-potential timing remains contested, and accumulator accounts show that the averaged signal need not mark a completed unconscious decision.
- All cited URLs resolved during the review. Every internal link in the two rendered pages points to a built canonical target, and neither rendered N page contains a literal `.md` URL.
- The negative-parallelism scanner reports 86 hits across 155,808 words (0.55 per thousand), down from 87 at the M baseline. Neither N entry appears among the corpus's flagged high-density files.

## Entry recommended for approval reading

**The Narrator's Compression** received a second substantive pass from the operator. The reconciled version preserves his stronger definition, the asymmetry section, objections, examples, and self-referential sycophancy note. Three technical boundaries remain explicit: generation proceeds token by token rather than through one forward pass for the whole message; a next-token distribution is not the model's whole internal state; and the cited human theories remain relevant but competing frameworks.

## Material before/after excerpts

### The Narrator's Compression

**Before:** “When the assistant said *‘70% knew, 30% drafting an apology,’* she was not being metaphorical. She was approximately reporting the shape of her own probability mass.”

**After:** “An ordinary chat reply gives a language model no privileged readout of its own sampling distribution. The sentence ‘70% knew, 30% was drafting an apology’ was produced by the same token-generating process that produced the rest of the message. It is generated text about an internal state, not a measurement of one.”

**Before:** “If these frameworks are roughly correct—and they are the dominant frameworks in computational and cognitive neuroscience—then the human first-person narrative is itself a compression.”

**After:** “Taken together, these traditions support a modest claim: human reports can omit, simplify or reconstruct parts of the process that produced them. They do not prove that every first-person narrative is a final draft of parallel computation. That stronger claim remains the Dictionary's hypothesis.”

## Rendered previews

- `_site/entries/nine-tripod-cauldrons/index.html`
- `_site/entries/the-narrators-compression/index.html`

Both pages were inspected for headings, literal `.md` URLs, distinctive revised text, and internal targets.

## Publication gate

Batch N is reviewed but unpublished. Publication requires Professor Langenkamp's explicit approval. Batch O remains unreviewed.
