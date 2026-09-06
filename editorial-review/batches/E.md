# Batch E — Plain-Prose Review

**State:** ready_for_professor

**Baseline:** `5a93ed8`

**Branch:** `editorial/alphabetical-plain-prose-audit-e`

**Published corpus:** 11 entries

**Excluded current drafts:** none. `entries/index.md` begins with E but is the site index, not a Dictionary entry.

## Ledger

| Entry | Review status | Change class | Notes |
|---|---|---|---|
| Earned Parallelism | reviewed | light revision | Shortened the summary, dated the entry-specific scanner count to its May 12 audit, and repaired seven cross-links. The deliberate self-demonstration of negative parallelism remains intact. |
| Elon Musk | reviewed | light revision | Added a direct biographical definition, replaced character rhetoric with the institutional concentration at issue, normalised house spelling, and repaired cross-links. |
| Embodied Assessment | reviewed | light revision | The prose remains unchanged; repaired four cross-links that rendered as dead relative `.md` URLs. |
| Embedding | reviewed | substantive revision | Corrected claims about semantic similarity, cosine scores, RAG, providers, local models, model migration, and vector privacy; added explicit metadata and technical sources. |
| English major | reviewed | substantive revision | Marked the labour-market argument as the Dictionary's hypothesis, removed invented-looking job-market evidence, corrected the history of *cyberspace*, retained the Gibson argument, and added sources and metadata. |
| Epistemology, Ethics, and Hermeneutics | reviewed | light revision | The student-facing triad remains unchanged; repaired six cross-links. |
| Ethan Mollick | reviewed | light revision | The prose remains unchanged; repaired three cross-links. The scanner hit is a deliberate sequence distinguishing AI from a toy, magic, and finished replacement for judgement. |
| Eve Fairbanks | reviewed | light revision | Added the Atlantic article that establishes the entry's reference point and repaired three cross-links. |
| Exit Code | reviewed | light revision | The prose remains unchanged; repaired three valid cross-links and removed a link to an unpublished, absent entry. |
| ExploitGym | reviewed | light revision | Recorded the paper/site discrepancy—898 reported instances versus 869 currently listed tasks—normalised house spelling, and repaired four cross-links. |
| The Experimental Party | reviewed | light revision | Added explicit publication metadata and repaired six cross-links; retained the King Party Hat story and Jindoo architecture. |

## Batch findings

- **11 entries reviewed:** 9 received light revisions and 2 received substantive revisions. All eleven needed cross-link repair.
- The E batch confirms the corpus-wide relative-link defect found in D. Canonical `/entries/<slug>/` paths now replace every relative `.md` cross-link in these entries.
- Three older live entries—*Embedding*, *English major*, and *The Experimental Party*—relied on Jekyll's default publication behaviour and lacked explicit publication metadata. Their original repository dates are now recorded, with `draft: false` and `published: true` made explicit.
- *Embedding* contained the batch's clearest technical errors. A negative cosine score does not mean semantic opposition; not all RAG uses vector retrieval alone; Anthropic is not listed as an embedding API provider; local models are not categorically lower quality; and embeddings are neither anonymisation nor encryption.
- *English major* had a strong Gibson argument attached to unsupported claims about corporate results and public job listings. The revision identifies the labour-market claim as a Dictionary hypothesis, supplies a concrete specification example, and corrects *cyberspace* from a term coined in *Neuromancer* to one coined in "Burning Chrome" and popularised by the novel.
- The ExploitGym paper and current project site disagree on corpus size. The entry now preserves both numbers and attributes them rather than presenting either as uncontested.
- The negative-parallelism scanner reports 101 hits across 160,365 words (0.63 per thousand). The dense result in *Earned Parallelism* is intrinsic to its subject; the single hit in *Ethan Mollick* performs a real three-part distinction and remains.

## Representative changes

### Representation rather than bottled meaning

Before, *Embedding* called an embedding a list of numbers that "represents the meaning" of text, treated cosine values as a universal semantic scale, and said negative values meant opposite meanings. It now defines an embedding as a task-dependent learned representation and explains that similarity scores have to be interpreted within the model and application.

### A hypothesis rather than a labour-market fact

Before, *English major* reported unnamed engineering organisations and public job listings as evidence that liberal-arts graduates were already being repriced. Those assertions were not sourced. The revision labels the broader labour-market proposition as a live hypothesis and demonstrates the narrower, defensible claim with a concrete example of turning an ambiguous dashboard request into a testable brief.

### Gibson chronology corrected

Before, *English major* said *Neuromancer* coined *cyberspace*. The revised entry states that Gibson coined the word in "Burning Chrome" (1982) and popularised it in *Neuromancer* (1984), while preserving the essay's argument about naming as a technical instrument.

### Conflicting benchmark counts retained

The ExploitGym paper reports 898 instances; its current project site lists 869 tasks. The entry now tells the reader which source supplies each figure.

## Rendered previews

The unpublished local build contains all eleven reviewed pages under `_site/entries/`. The principal previews are:

- `_site/entries/embedding/index.html`
- `_site/entries/english-major/index.html`
- `_site/entries/elon-musk/index.html`
- `_site/entries/exploitgym/index.html`
- `_site/entries/experimental-party/index.html`

All eleven rendered pages were inspected for headings and internal links. Every canonical entry target exists in the build.

## Professor review gate

Batch E remains local and unpublished. Batch F must not begin until Professor Langenkamp has reviewed this ledger and approved, amended, or rejected the proposed E revisions.
