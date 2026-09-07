# Batch P — Plain-Prose Review

**State:** approved and published

**Baseline:** `592982c`

**Branch:** `editorial/alphabetical-plain-prose-audit-p`

**Published corpus:** 12 entries

**Excluded current drafts:** none

## Ledger

| Entry | Review status | Change class | Notes |
|---|---|---|---|
| Pangram Labs | reviewed | substantive revision | Replaced the product-specific bias verdict with a sourced institutional description; retained the documented Mamdani episode as a governance warning and made a detector score a lead rather than proof. |
| Parameters | reviewed | substantive revision | Rebuilt the entry around learned numerical values, weight-memory arithmetic, runtime overhead, and the distinction between total and active MoE parameters; removed the stale local-model ranking and claims that count predicts knowledge or quality. |
| Patch Gap | reviewed | light revision | Added explicit revision metadata, a NIST source, and canonical related-entry links. |
| Pax | reviewed | light revision | Preserved the *Serenity* interpretation and operator's mosh-pit line; added a film source, revision metadata, and canonical links. |
| Performance Artifact | reviewed | light revision | Marked the term as the Dictionary's pedagogical usage, retained its assessment argument, added revision metadata, and repaired links. |
| The Peripheral | reviewed | substantive revision | Corrected the mechanics of stubs and peripherals: information and telepresence cross the connection, not matter or consciousness; separated Gibson's novel from the Dictionary's Lowbeer and Aunties extensions. |
| Persona Scaffold | reviewed | light revision | Marked the term as a Dictionary coinage, repaired one sentence boundary, added revision metadata, and converted all related entries to canonical URLs. |
| Pre-buying the Physical Future | reviewed | substantive revision | Recast the phrase as a Dictionary term, replaced unsourced turbine-year specifics with GE Vernova's reported backlog and slot reservations, and distinguished reservations from completed assets or guaranteed demand. |
| Prompt | reviewed | substantive revision | Distinguished a user's prompt from the model's full context; made instruction roles product-specific and sourced OpenAI's current chain of command. |
| Proof of Learning | reviewed | light revision | Marked the pedagogical term as the Dictionary's usage, added revision metadata, and repaired canonical links. |
| Provenance | reviewed | substantive revision | Expanded origin into origin plus transformation; removed the categorical claim that AI systems cannot show evidentiary chains and added the essential boundary that provenance does not prove truth. |
| Pwned | reviewed | light revision | Qualified the keyboard-typo origin as uncertain, added a second source and revision metadata, and repaired canonical links. |

## Batch findings

- **12 entries reviewed:** six received light revisions and six received substantive revisions.
- *Parameters* contained the largest technical repair. Parameter count is now a structural and memory measure, with total and active MoE counts kept separate from observed capability.
- *The Peripheral* no longer turns Gibson's telepresence into consciousness transfer or presents the Dictionary's governance architecture as Gibson's own specification.
- *Pangram Labs* retains the documented public controversy without claiming that class-level detector research proves a defect in every Pangram version.
- *Prompt* now separates the user's message from the surrounding instruction and context layers.
- *Pre-buying the Physical Future* retains the physical-infrastructure argument while grounding it in a supplier's backlog and reservation disclosures.
- All 12 entries now have explicit publication and revision metadata. Every changed internal link points to a built canonical target.
- The negative-parallelism scanner reports 84 hits across 155,556 words (0.54 per thousand), unchanged in count from the O baseline despite the larger corpus text.

## Entries recommended for approval reading

1. **Parameters** — full technical rebuild and removal of the stale machine benchmark.
2. **Pangram Labs** — the evidentiary boundary around detector scores is materially narrower.
3. **The Peripheral** — telepresence mechanics and the line between Gibson and Dictionary extensions are corrected.
4. **Pre-buying the Physical Future** — the infrastructure thesis is now tied to disclosed reservations rather than unsourced delivery years.
5. **Prompt** — user prompt, context, and instruction hierarchy are now distinct.
6. **Provenance** — traceability is separated from truth.

## Representative before and after

### Parameters

**Before:** "The headline parameter count is the rough size of the model. It is *not* the rough quality of the model," followed by a dated local leaderboard.

**After:** "Total parameters help describe weight storage and the model's overall architecture. Active parameters help describe part of the per-token computation. Neither number, alone, is a performance score."

### The Peripheral

**Before:** peripherals "allow a consciousness from one branch to inhabit a body in another."

**After:** "Information travels between the later world and the earlier one" and "a peripheral is a telepresent body that a remote operator can control through a neural interface."

### Provenance

**Before:** provenance was "the difference between an answer that merely sounds right and an answer that can be audited."

**After:** the audit function remains, with the boundary added: "Provenance does **not** prove truth."

## Rendered previews

The rendered pages under `_site/entries/` were inspected for all 12 slugs, including distinctive revised text, accidental `.md` links, and canonical internal targets.

## Publication gate

Professor Langenkamp approved Batch P on 6 September 2026. The reviewed content was published in `ff29ddf`; both exact-SHA GitHub workflows succeeded, and all 12 live pages returned HTTP 200 with the revised text. Batch Q remains unreviewed.
