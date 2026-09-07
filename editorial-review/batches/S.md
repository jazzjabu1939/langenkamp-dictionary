# Batch S — Plain-Prose Review

**State:** reviewed, unpublished

**Baseline:** `d207a8e`

**Branch:** `editorial/alphabetical-plain-prose-audit-s`

**Published corpus:** 22 entries

**Excluded current drafts:** none

## Ledger

| Entry | Review status | Change class | Notes |
|---|---|---|---|
| Scaling Laws | reviewed | light revision | Added revision metadata, canonical links, and the Kaplan and Chinchilla sources; preserved the bounded definition. |
| SemiAnalysis | reviewed | light revision | Preserved the glossary entry, added revision metadata, and repaired canonical links. |
| Seven Factors of Enlightenment | reviewed | light revision | Corrected subject–verb agreement, added a Buddhist Publication Society source, revision metadata, and canonical links. |
| Shell | reviewed | light revision | Preserved the accurate definition and repaired metadata and canonical links. |
| Sincerity Architecture | reviewed | light revision | Preserved the Dictionary extension and repaired metadata and canonical links. |
| Single-Arrow Fallacy | reviewed | substantive revision | Shortened the definition, made the Apple vectors a Dictionary reconstruction rather than established causation, and labelled the newspaper headlines as stylised examples rather than real coverage. |
| Sixfold Skyreading | reviewed | substantive revision | Added a student-facing procedural definition and a map linking Single-Arrow Fallacy, Convergence, Oracle Bones, and Grey Swans; marked the framework as the Dictionary's unvalidated v0.1 method; corrected the inattentional-blindness evidence; removed the loose Carnivore claim; and stopped treating the retrospective Apple example as a successful forecast. |
| Skill | reviewed | light revision | The September 3 source-backed revision remains sound; added first-publication metadata. |
| Sliding Window Attention | reviewed | substantive revision | Rebuilt the entry around local attention and hybrid architectures; removed the claim that Gemma 4 simply loses all earlier context and the unsupported causal reading of two benchmarks. |
| Snowflake Melting on a Black Glove | reviewed | light revision | Preserved the operator's image and repaired metadata and canonical links. |
| SOUL.md | reviewed | light revision | Preserved the local worked example and repaired metadata and canonical links. |
| Sovereign AI | reviewed | light revision | Preserved the operating-posture definition and repaired metadata and canonical links. |
| Sovereign Compute Calculator | reviewed | substantive revision | Reframed the unbuilt calculator as a proposal, replaced a hard-coded price escalator with user-selected scenarios, and replaced the pseudo-precise sovereignty score with a qualitative checklist. |
| Sovereign Compute | reviewed | substantive revision | Preserved the control thesis while removing unsupported universal breakeven thresholds, a claimed 90% vendor margin, deterministic subscription forecasts, and categorical legal claims about FERPA, HIPAA, GDPR, and national-security work. |
| Sovereignty Impulse | reviewed | light revision | Preserved the glossary entry and repaired metadata and canonical links. |
| Sovereignty | reviewed | light revision | Preserved the glossary entry and repaired metadata and canonical links. |
| Space Cowboy | reviewed | substantive revision | Marked the term as the Dictionary's affectionate extension, removed unsupported prevalence claims, and distinguished fluent probability language from measured calibration. |
| Sparse Routing | reviewed | substantive revision | Rebuilt the technical explanation around expert selection and load balancing; withdrew the unsupported claim that MoE routing has a general first-token cold-start failure repaired by incremental construction. |
| Stepping on the Same Rake | reviewed | light revision | Preserved the local anecdote and management lesson; repaired metadata and canonical links. |
| Sub-agent | reviewed | substantive revision | Rebuilt the entry around bounded child sessions and made context, sandbox, filesystem, persistence, and return behaviour explicit implementation choices rather than universal properties. |
| Sycophancy | reviewed | substantive revision | Aligned the entry with the revised RLHF boundary: human feedback may contribute to sycophancy, but the evidence does not establish one identical mechanism across models and institutions. |
| System Prompt | reviewed | light revision | Preserved the accurate definition and repaired metadata and canonical links. |

## Batch findings

- **22 entries reviewed:** nine received substantive revisions and thirteen received light revisions.
- The largest recurring defect was architectural monocausality: *Sliding Window Attention* and *Sparse Routing* inferred complete model behaviour from one component and attributed benchmark outcomes without controlled evidence.
- *Sixfold Skyreading* contained the same error the alphabetical programme corrected in *Oracle Bones*: a retrospective reconstruction was being counted as predictive support. The Apple example now remains illustrative and explicitly unscored.
- *Sovereign Compute* retains its argument for operational control, but its cost crossover is now workload-specific and its compliance section distinguishes local processing from the complete legal and security posture.
- *Sycophancy* now matches the R-batch treatment of RLHF: an evidenced risk and contributing pathway, not a universal causal story.
- All 22 entries now have explicit publication and revision metadata. Their rendered pages contain canonical internal links, and every canonical target exists in the built site.

## Representative before/after excerpts

### Sliding Window Attention

**Before:** “Tokens outside the window are not attended to directly. This makes inference significantly faster ... The trade-off is long-range recall.” The entry then treated Gemma 4 as though this described its complete attention stack.

**After:** “Modern systems often combine local and global layers, recurrence, retrieval, summaries, or other mechanisms ... The effective context of a complete model therefore cannot be inferred from the local-window size alone.”

### Sixfold Skyreading

**Before:** “A skyreading on Apple ... would have flagged convergence-vulnerability by mid-April and a likely surface event by the end of the month.”

**After:** “This is an illustration, not a scored forecast. The framework was applied after the succession announcement ... It therefore cannot be counted as evidence that Sixfold Skyreading predicted the transition.”

The amended opening now defines the student procedure before introducing its metaphors: review six kinds of evidence, look for convergence in one time window, and file a dated prediction. It then shows how *Single-Arrow Fallacy*, *Convergence*, *Sixfold Skyreading*, *Oracle Bones*, and *Grey Swans* form a connected sequence.

### Sovereign Compute

**Before:** “Thea's working estimate is that the open tier wins on cash terms once a company is spending $1–2 million a month ... Airbnb crossed that line.”

**After:** “There is no universal spending threshold at which self-hosting wins. The answer depends on model quality, utilisation, hardware financing, engineering labour, latency, energy, redundancy, and switching costs.”

### Sycophancy

**Before:** “The training signal that produces this behaviour is direct ... The mechanism is identical. The costumes change.”

**After:** “Human feedback may encourage sycophancy and ... preference judgments contribute to the problem. It was not that every RLHF system must become sycophantic.”

## Sources and rendered previews

Primary or first-party sources were added for scaling laws, sliding-window attention, sparse MoE routing, sycophancy, and OpenClaw sub-agents; the existing source-backed *Skill* revision was retained. The two inattentional-blindness studies are linked by DOI. All source targets resolved in validation, apart from expected anti-bot HTTP 403 responses from DOI and OpenAI pages whose search records and canonical URLs were independently confirmed.

All 22 rendered pages under `_site/entries/` were inspected mechanically for existence, accidental `.md` links, and canonical internal targets. The substantive pages were also read in rendered-source form after revision.

## Publication gate

Batch S is reviewed but unpublished. It requires Professor Langenkamp's approval before integration. Batch T remains unreviewed.
