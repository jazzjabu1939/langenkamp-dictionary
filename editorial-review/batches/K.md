# Batch K — Plain-Prose Review

**State:** approved; publication verification pending

**Baseline:** `820ab55`

**Branch:** `editorial/alphabetical-plain-prose-audit-k`

**Published corpus:** 4 entries

**Excluded current drafts:** none

## Ledger

| Entry | Review status | Change class | Notes |
|---|---|---|---|
| Kimi K3 | reviewed | substantive revision | Replaced the stale promise of a future weight release with the completed July 2026 release; added the official model card, weights, license, and technical report; distinguished vendor evaluations from independent validation; repaired canonical links and added revision metadata. |
| King Party Hat | reviewed | light revision | Preserved the operator's term and joke while replacing the categorical demand for a harness “above” every local model with risk-proportionate governance; added revision metadata and canonical links. |
| KV Cache Explosion | reviewed | substantive revision | Replaced the broad long-context claim with a precise account of inference-time KV-cache growth and the architecture, precision, batch, and concurrency variables that determine memory use; added mitigation boundaries, official sources, metadata, and canonical links. |
| KV Cache Poisoning | reviewed | substantive revision | Removed unsupported claims about cold-start MoE routing, wrong expert clusters, cache corruption, and router reset; retained the term only as an explicit Dictionary metaphor for error compounding through a misleading transcript; added an operational recovery account, naming boundary, source, metadata, and canonical links. |

## Batch findings

- **4 entries reviewed:** 1 received a light revision and 3 received substantive revisions. All four files are revised in this proposal.
- *Kimi K3* was written before Moonshot's announced 27 July release date. The weights, model-specific license, model card, and technical report are now public. The revision records that completed release while treating Moonshot's benchmark table as vendor evidence whose results depend on harness and protocol.
- *KV Cache Explosion* names a real infrastructure pressure, but its former explanation made context length do too much work. Cache memory grows with stored token positions for a fixed architecture; the actual serving bill also depends on layers, KV heads, head dimension, numerical precision, batch size, concurrency, and cache-management choices.
- *KV Cache Poisoning* contained the batch's principal technical defect. A KV cache stores tensors derived from processed context; it is not “poisoned” when the text is wrong. Flawed output can still anchor later work because it remains in the transcript. The revision keeps that practical observation and explicitly withdraws the unverified MoE-routing mechanism.
- *King Party Hat* remains a Dictionary term. Its governance claim is now proportional to the consequence of the action rather than a universal architecture rule.
- All six external source URLs returned HTTP 200. All internal links use canonical `/entries/<slug>/` paths, and every target exists in the rendered build.
- The negative-parallelism scanner reports 91 corpus hits across 160,666 words (0.57 per thousand). The changed K entries contain no flagged unearned construction.

## Representative changes

### Kimi K3: promised release to completed artifact

The former entry, dated 19 July, said Moonshot would release the weights and technical report by 27 July. The revision records the completed publication and links directly to the official weights, license, model card, and report. It also separates vendor benchmark evidence from independent reproduction.

### KV Cache Explosion: define the physical bill

The former entry said only that longer context expands the cache. The revision explains the reuse of attention keys and values, the approximately linear sequence-length term for a basic dynamic cache, and the other variables that determine total memory pressure. It also notes that quantization, sliding windows, paging, offloading, and related techniques manage rather than abolish the trade-off.

### KV Cache Poisoning: preserve the observation, remove the mechanism

The former entry claimed that cold-start MoE routing selected the wrong expert clusters, contaminated the cache, made self-correction unreliable, and could be reset by opening a fresh session. No reviewed source establishes that sequence. The revision describes the observable problem as context contamination: later work may inherit an earlier mistake because the mistaken draft remains in the transcript. A fresh session changes the context; it does not repair a corrupted cache or demonstrably reset a task-level router.

## Rendered previews

The local build contains all four reviewed pages:

- `_site/entries/kimi-k3/index.html`
- `_site/entries/king-party-hat/index.html`
- `_site/entries/kv-cache-explosion/index.html`
- `_site/entries/kv-cache-poisoning/index.html`

All four pages were inspected for headings, literal `.md` URLs, distinctive revised text, and internal targets. Every target exists in the build.

## Publication gate

Professor Langenkamp approved Batch K on 6 September 2026. The exact approved tree must pass the repository checks, GitHub workflows, Pages deployment, and live-page verification before Batch L begins.
