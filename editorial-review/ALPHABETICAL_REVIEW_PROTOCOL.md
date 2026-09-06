# Alphabetical Plain-Prose Review

## Purpose

Review every published Dictionary entry for plain definition, factual clarity, reader legibility, and the rhetorical habits that can make collaborative prose sound artificially clever. The programme follows the `dictionary-entry-editor` skill and moves one initial letter at a time.

## Governing sequence

1. Freeze a letter batch from the published `main` branch.
2. Record unpublished and uncommitted files separately; do not sweep them into the batch.
3. Read every entry in the batch. An entry may be marked **reviewed—no change**; completion does not require cosmetic rewriting.
4. For each entry, check:
   - the first substantive sentence defines the headword;
   - facts, traditions, disputes, and Dictionary extensions are distinguishable;
   - unfamiliar names and allusions are explained before use;
   - each paragraph has one definitional or explanatory job;
   - concrete examples replace abstract summary where useful;
   - mirrored antitheses, stacked aphorisms, crescendos, decorative tricolons, and overextended metaphors do not supply momentum in place of thought;
   - wit clarifies or preserves the operator's real voice;
   - the term still merits its own entry;
   - links, metadata, spelling, and dates remain sound.
5. Record the result in the batch ledger as **no change**, **light revision**, **substantive revision**, **source check needed**, or **structural question**.
6. Run the mechanical scanner, repository integrity checks, and the unpublished Jekyll build.
7. Inspect the rendered entries changed in the batch.
8. Prepare a review packet containing:
   - the complete ledger;
   - a short account of recurring problems;
   - before/after excerpts for material changes;
   - the branch and commit containing the proposed revisions;
   - rendered previews.
9. Stop. Professor Langenkamp reviews the batch and may approve, amend, or reject individual edits.
10. Only after explicit approval, merge and publish the batch. Begin the next letter only after that publication decision.

## Editorial restraint

This is a review programme, not a homogenisation programme. Do not revise a sentence merely because another sentence could be shorter. Preserve sourced anecdotes, real jokes, useful digressions, and the two-voice architecture. Make the smallest change that removes an actual defect.

## Publication gate

No alphabetical batch is published automatically. Review completion and publication approval are separate states.

## Batch states

- `inventory`
- `reviewing`
- `ready_for_professor`
- `approved`
- `published`
- `held`

Only one letter may be `reviewing` at a time. The following letter remains `held` until the current letter is approved or otherwise closed by Professor Langenkamp.
