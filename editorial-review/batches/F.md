# Batch F — Plain-Prose Review

**State:** approved and published

**Baseline:** `191eecb`

**Branch:** `editorial/alphabetical-plain-prose-audit-f`

**Published corpus:** 8 entries

**Excluded current drafts:** none

## Ledger

| Entry | Review status | Change class | Notes |
|---|---|---|---|
| The Familiar Ogre | reviewed | light revision | The prose remains unchanged; repaired four cross-links that rendered as dead relative `.md` URLs. |
| Fan Jin (范進) | reviewed | substantive revision | Corrected the duration and level of Fan Jin's examination history, removed unsupported embellishment, named Zhang Jingzhai's actual gifts, marked the sycophancy argument as the Dictionary's reading, added sources, and repaired three cross-links. |
| FERPA Compliance Posture | reviewed | substantive revision | Replaced a categorical local/cloud rule with a source-backed disclosure framework; corrected the treatment of student names, DPAs, vendor approval, de-identification, and local processing; made the entry's institutional status explicit; added metadata, sources, and cross-links. |
| Fine-tuning | reviewed | substantive revision | Corrected claims about weight updates, prompting, RAG, SFT, RLHF, DPO, LoRA, structured output, dataset size, vendor availability, current knowledge, and privacy; replaced invented cost thresholds with an evaluation-first teaching example; added metadata and sources. |
| Firefly / Serenity | reviewed | light revision | Replaced the “matters less as fandom” construction with a direct statement of editorial purpose, softened the claim that the film completed the story, normalised house spelling, and repaired six cross-links. |
| FLOP (Floating-Point Operation) | reviewed | light revision | Clarified counting conventions, repaired exponent rendering and petaflop styling, added a source for the training-compute approximation, updated revision metadata, and repaired four cross-links. |
| Frontier Dependence | reviewed | light revision | Recast the definition as a workflow condition rather than a universal model ranking, dated the operator's capability judgement, made its task dependence explicit, and repaired six cross-links. |
| Fully Autonomous Agent Myth | reviewed | light revision | Dated the term's capability boundary, made the compounding-error arithmetic and assumptions explicit, changed “verifier models” to “verifier systems”, added explicit draft metadata, reduced stock contrast, and repaired six cross-links. |

## Batch findings

- **8 entries reviewed:** 5 received light revisions and 3 received substantive revisions. Every F entry required at least one repair.
- The corpus-wide relative-link defect found in D and E affected all eight F entries. Canonical `/entries/<slug>/` paths now replace every relative `.md` cross-link.
- *FERPA Compliance Posture* contained the batch's most consequential errors. FERPA does not make a document labelled DPA the universal switch for vendor use; names are personally identifiable information rather than harmless metadata; and local processing reduces disclosure risk without automatically certifying legal compliance.
- *Fine-tuning* repeatedly turned tendencies into guarantees. Fine-tuning changes parameters but does not necessarily store retrievable “knowledge”; LoRA is not equivalent to full fine-tuning on every task; structured output does not require fine-tuning; and both fine-tuning and RAG have architecture-dependent privacy risks.
- *Fan Jin* overstated the chronology as more than thirty years of failure and added gifts not supported by the chapter. The revision follows chapter 3 and identifies the status argument as the Dictionary's interpretation.
- *Frontier Dependence* and *Fully Autonomous Agent Myth* now state their 2026 evidence boundary rather than presenting a moving capability comparison as timeless fact.
- The negative-parallelism scanner reports 102 hits across 160,310 words (0.64 per thousand). *FERPA Compliance Posture* retains three deliberate constructions: the opening posture joke and two distinctions needed to prevent legal overstatement.

## Representative changes

### FERPA: approval and control rather than a magic contract label

Before, the entry said cloud LLMs could freely receive educational metadata, including student names, while any student-authored content required local processing unless a DPA existed. The revision follows FERPA's actual structure: disclosure of personally identifiable information generally requires consent or an exception; an outsourced school official must meet specified conditions; and a contract is a common control mechanism rather than a magic phrase. Local processing remains the Dictionary's conservative option, with its security and institutional-policy limits stated.

### Fine-tuning: adaptation rather than bottled documents

Before, fine-tuning permanently placed behaviour and domain knowledge inside a model's weights, reliably guaranteed JSON, became worthwhile at tens of thousands of examples, and put private documents “in the weights”. The revision defines parameter adaptation precisely, separates SFT from preference methods, treats LoRA as one parameter-efficient method, and explains that memorisation is a risk to test rather than a theory that weights are a document store.

### Fan Jin: the chapter rather than the embellishment

Before, Fan Jin had failed for more than thirty years and local gentry arrived with houses, land, and daughters. The revision records the chapter's narrower facts: at fifty-four he had failed more than twenty times; after becoming a *juren*, neighbours brought help and Zhang Jingzhai offered silver and a house. The social-status reading remains, now explicitly attributed to the Dictionary.

### Capability claims with dates and scopes

*Frontier Dependence* now defines reliance within a workflow and dates the operator's task-specific comparison to 2026. *Fully Autonomous Agent Myth* gives the simple assumptions behind its 36-percent illustration and says plainly that the term is not a permanent ceiling on agents.

## Rendered previews

The unpublished local build contains all eight reviewed pages under `_site/entries/`. The principal previews are:

- `_site/entries/fan-jin/index.html`
- `_site/entries/ferpa-compliance-posture/index.html`
- `_site/entries/fine-tuning/index.html`
- `_site/entries/flop/index.html`
- `_site/entries/fully-autonomous-agent-myth/index.html`

All eight rendered pages were inspected for headings, literal `.md` URLs, and internal link targets. Every canonical entry target exists in the build.

## Publication record

Professor Langenkamp approved batch F on 6 September 2026. The reviewed content was integrated into `main` as `8ecc6fd`. Batch G was authorised to begin after publication verification.
