# Queue Audit — 2026-06-22

Working audit after the June 22 fast-entry batch.

## Current Published State

- Latest repo commit checked: `31978b1` — `Publish June dictionary entry batch`
- Local entry files: **214**
- Public local entries by frontmatter/site filter: **214**
- Live `https://langenkamp.io/entries/` entry links counted: **214**
- Unpublished/draft entry files: **0**

Conclusion: deployment is not the bottleneck. The bottleneck is editorial queue hygiene and deciding which public-but-light entries deserve full review or expansion.

## Uncommitted Files

These are uncommitted but are not pending Dictionary entry files:

- `VISION.md` — standalone public-facing vision/mission/values draft.
- `TRIAGE_OPERATOR_TONE.md` — May 8 operator-tone triage report; useful but stale after many entries changed.
- `using-in-a-course.md` — course-use page/draft.
- `substack/2026-05-05-we-are-not-batteries-yet.md`
- `substack/2026-05-11-decent-red-pills.md`
- `substack/2026-05-15-oracle-bones.md`

Recommendation: keep these outside the entry queue. Treat them as site/page/Substack backlog.

## Queue Source Quality

### `REVIEW_QUEUE.md`

Best source for historical queue intent, but currently stale.

Problems:

- It still says several now-published entries are "not yet drafted" or awaiting review.
- It mixes true queue items, historical notes, cluster concepts, stale process notes, and already-published batches.
- It still contains the pre-June-22 review rule "no publishing without explicit Prof approval," while the June 22 fast-entry push intentionally used a bulk-publish posture.

### `CANDIDATE_ENTRIES.md`

Useful as a historical triage artifact, but currently stale.

Problems:

- Auto-generated May 12.
- Many marked candidates were published June 22.
- Some candidates are extraction noise or better handled as subterms inside existing entries.

Recommendation: regenerate only after `REVIEW_QUEUE.md` is cleaned, otherwise it will recreate noise.

### `topics.md`

Useful public thematic index. It has a current planned-entry section, but it is intentionally short. It should not be treated as the full queue.

Current issue: 76 public entry files are not listed in `topics.md`. That is not a build error, because `/entries/` is the complete alphabetical index, but it means the thematic index is incomplete after the fast-entry batch.

## Published But Still Deserving Editorial Review

These are public on `langenkamp.io` but should be considered "published fast, still worth reviewing/warming" rather than finally settled.

### June 22 Fast Batch

Promoted or added in the fast-entry batch:

- Agentic Threshold
- Capability Overhang
- The CERN Alternative
- Cheng
- Cooperative Writing
- Country of Geniuses in a Data Center
- Ethan Mollick
- Implementation Layer War
- Incremental Construction
- KV Cache Poisoning
- Move 37
- Quantum Effects in the Brain
- Root Node Problems
- Sliding Window Attention
- Sparse Routing
- William Gibson
- Claude Code
- Coding Solved
- Demis Hassabis
- OpenClaw
- Manus
- King Party Hat
- Borrowed Brain
- Sovereignty Impulse
- Cloud Theory
- Reasoning Model

Recommendation: do not unpublish. Keep them live. Review selectively for voice and depth, especially the more essay-shaped items: Implementation Layer War, Country of Geniuses, The CERN Alternative, Agentic Threshold, Capability Overhang, Move 37, Root Node Problems, Cheng, Cooperative Writing, and William Gibson.

### Older Public Entries with Stale Queue Notes

These appear in `REVIEW_QUEUE.md` as pending or draft-ish but are now public:

- The Judge Layer
- Verification Gap
- AI Produced Artifact
- Institutional Lag
- Implementation Outrun
- Big Blob of Compute
- Open Model Trust
- Heinlein Protagonist
- Time for Tea with The Oracles
- Space Cowboy
- Aunties
- Mandi Step
- Durable Workflow
- Oracle Bones

Recommendation: mark these as published in the queue. If review remains desired, move them into a separate "published, polish later" section.

## Still To Draft / Review / Publish

This is the cleaned working list of genuinely pending Dictionary material.

### Highest-Value Next Entries

1. **AI Librarian** — campus role for AI as information/evidence/citation/privacy/assessment support. Strong teaching relevance and current.
2. **Vibe Coding** + **Agentic Engineering** — Karpathy vocabulary correction; pairs with AI Writing and implementation trust.
3. **Open Weights, Closed Habits** — Meta/Llama trust contradiction; strong current AI ecosystem entry.
4. **Yann LeCun** — person entry and counter-pole to Dario/Blob scaling.
5. **World Model** — concept entry needed for LeCun and robotics/physical-world AI.
6. **Agent Health** / **Harness Hygiene** — operational quality of an agentic system; central to OpenClaw governance.
7. **Backup Performance Art** — backup ritual vs recoverability; useful, memorable, and connected to sovereignty.
8. **Hanging Thread** — conversational/workflow obligation left open without status; practical human-agent term.
9. **Favorite Child** — model-selection bias and emotional reality of multi-model operation.
10. **A Channel of One's Own** — may already exist as a public compact entry, but the queue material suggests it deserves expansion into a full essay.

### Role Substitution / Replicant Cluster

Draft cluster still pending:

- Role Substitution
- Machine Matthew L.
- Replicant Problem
- Anchored Persona
- Borrowed Memory
- Implanted Memory
- Intentional Memory Construction
- Relationally Real Memory
- Anti-Replication Strategy
- Tears in Rain Buddhism
- Snowflake on a Black Glove

Recommendation: publish as a few compact glossary entries plus one fuller essay, probably **Role Substitution** or **Replicant Problem** as the hub.

### Invented Worlds / Neuroscience-AI Cluster

Draft cluster still pending. Handle carefully and avoid clinical overclaiming:

- Invented Worlds
- Reality Contact
- Biological Hallucination / Machine Hallucination
- Reality Scaffolding
- Shared Reality Check
- Invented Certainty
- Human-Agent Reality Repair

Recommendation: defer until there is time to draft carefully. This is high-risk prose because it touches mental illness and cognitive decline.

### Sovereign Assistant / Agent Architecture Cluster

Still pending or underdeveloped:

- Sally / The Sovereignty Experiment
- Claudia / Multi-Agent Specialisation
- The Nine Tripod Cauldrons / 九鼎
- Buy the Ticket, Take the Ride
- Architectural Cost Translation
- My Agent Is Better Than Your Agent / The Corpus Moat
- Cache-Write Tax
- Prefill
- P2: Personality and Performance
- Constant Calibration Mechanism
- Agentic Philosophy
- HAL Test
- Shared Past Substrate / Artifice of Shared Memory
- Mandate of Heaven
- Alt Intelligence

Recommendation: do not try to publish all at once. Choose one hub entry first. Best hub candidates: **Agent Health**, **Sally**, **Buy the Ticket, Take the Ride**, or **Nine Tripod Cauldrons**.

### Teaching / Hyacinth 3 Terms

Still pending:

- Brain Rot
- Learning Mode

Recommendation: these are useful but should probably wait until the teaching-material architecture stabilizes.

### Agent Town / Emergence World

Still pending:

- Agent Town Experiment / Emergence World

Recommendation: high-value, but source-dependent. Draft from the Emergence AI post and treat it as a benchmark/ecology entry: "the harness is the town."

## Suggested Next 20 Queue

If the goal is to keep entering terms today, this is the recommended next queue:

1. AI Librarian
2. Vibe Coding
3. Agentic Engineering
4. Open Weights, Closed Habits
5. Yann LeCun
6. World Model
7. Agent Health
8. Harness Hygiene
9. Backup Performance Art
10. Hanging Thread
11. Favorite Child
12. A Channel of One's Own — full expansion
13. Role Substitution
14. Machine Matthew L.
15. Replicant Problem
16. Anchored Persona
17. Reality Contact
18. Agent Town Experiment
19. Sally / The Sovereignty Experiment
20. Buy the Ticket, Take the Ride

## Recommended Cleanup Actions

1. Replace the top of `REVIEW_QUEUE.md` with a current queue summary and move old historical notes below a "Historical Queue Notes" divider.
2. Add a `PUBLISHED_FAST_NEEDS_REVIEW` section for public-but-light entries.
3. Remove or mark superseded notes that say Move 37, Root Node Problems, Capability Overhang, The CERN Alternative, Heinlein Protagonist, The Judge Layer, and the AI Education Verification Cluster are not drafted.
4. Regenerate `CANDIDATE_ENTRIES.md` only after the queue cleanup.
5. Expand `topics.md` selectively, not exhaustively. The alphabetical `/entries/` page is the complete index; `topics.md` should remain editorial.

