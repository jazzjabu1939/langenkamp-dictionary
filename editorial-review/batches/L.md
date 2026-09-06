# Batch L — Plain-Prose Review

**State:** approved and published

**Baseline:** `ec37267`

**Branch:** `editorial/alphabetical-plain-prose-audit-l`

**Published corpus:** 8 entries

**Excluded current drafts:** none

## Ledger

| Entry | Review status | Change class | Notes |
|---|---|---|---|
| Lab Character | reviewed | substantive revision | Replaced a permanent moral ranking of laboratories with a dated, evidence-limited institutional test; removed unsupported personal judgments and brittle forecasts; added sources, revision metadata, and canonical links. |
| The Lazy Median Hypothesis | reviewed | substantive revision | Preserved the Dictionary's prediction while distinguishing it from an established empirical distribution; added falsification conditions; removed repetitive and overconfident historical claims; repaired metadata and canonical links. |
| Lee Sedol | reviewed | light revision | Preserved the entry's argument while qualifying the interpretation of Move 78, documenting the 4–1 match, adding primary and specialist sources, and repairing metadata and canonical links. |
| Llama | reviewed | substantive revision | Recast Llama accurately as an open-weight rather than conventionally open-source family; replaced ecosystem superlatives with Meta's dated download count; documented the Llama 4 licence restrictions and repaired canonical links. |
| LM Studio | reviewed | light revision | Updated the product definition to include its local server, llama.cpp, and MLX paths; removed a categorical recommendation; added official sources, revision metadata, and canonical links. |
| Local-first / Sovereignty | reviewed | light revision | Preserved the redirect into Sovereign Compute while clarifying that local execution does not itself establish legal compliance; repaired metadata and canonical links, and left the unpublished *Dusty Laptop* companion as plain text. |
| Logic, Memory, Power | reviewed | light revision | Tightened the physical triad, added the SemiAnalysis source, and repaired revision metadata and canonical links. |
| The Lowbeer Question | reviewed | substantive revision | Separated Gibson's characters from the Dictionary's proposed governance architecture; removed unsupported claims about the novels and characters; replaced a universal separation rule with bounded, reversible emergency powers; added sources, metadata, and canonical links. |

## Batch findings

- **8 entries reviewed:** 4 received light revisions and 4 received substantive revisions. All eight files are revised in this proposal.
- *Lab Character* had become a rapidly aging moral scorecard mixing institutional evidence, personality judgments, forecasts, and unsourced commercial detail. The revision keeps the useful question—what an institution does when commitments become costly—while making every reading dated, revisable, and limited by the evidence.
- *The Lazy Median Hypothesis* remains a Dictionary hypothesis. It now identifies what evidence would weaken it instead of presenting a bimodal distribution as already established.
- *Llama* now distinguishes access to model weights from an open-source software licence. The Llama 4 licence includes attribution, acceptable-use, naming, and very-large-service conditions that matter to the definition.
- *The Lowbeer Question* contained the batch's main literary-attribution defect. Gibson supplies Lowbeer, Netherton, Eunice, and the aunties; Principal-of-Principals, Recovery Auntie, Gate, Watch, and the proposed division of authority are Dictionary extensions.
- Fifteen cited pages were directly retrievable during the review. Reuters and Meta's AI blog blocked the text extractor, but their current URLs and the claims they support were independently checked. All internal links use canonical `/entries/<slug>/` paths, and every published target exists in the rendered build.
- The negative-parallelism scanner reports 89 corpus hits across 157,201 words (0.57 per thousand). None of the changed L entries appears among the corpus's flagged high-density files.

## Representative changes

### Lab Character: from league table to institutional test

The former entry ranked laboratories and inferred personal motives from public events. The revision asks observable questions about governance, research authority, release choices, costly commitments, and correction. Its five laboratory sketches are dated readings, not permanent rankings or claims about private virtue.

### Llama: open weights are not the whole licence

The former entry called Llama open source and treated it as the foundation of most of the open ecosystem. The revision uses the narrower term *open-weight*, records Meta's one-billion-download announcement as a vendor count, and describes the conditions in the Llama 4 Community License.

### The Lowbeer Question: Gibson analogy, Dictionary architecture

The former entry attributed a detailed multi-agent hierarchy and termination rule to Gibson's novels. The revision marks that architecture as the Dictionary's extension, preserves the characters as memory aids, and turns the entry into an operational governance checklist centred on authority, reversibility, absence, and recovery.

## Rendered previews

The local build contains all eight reviewed pages:

- `_site/entries/lab-character/index.html`
- `_site/entries/lazy-median-hypothesis/index.html`
- `_site/entries/lee-sedol/index.html`
- `_site/entries/llama/index.html`
- `_site/entries/lm-studio/index.html`
- `_site/entries/local-first-sovereignty/index.html`
- `_site/entries/logic-memory-power/index.html`
- `_site/entries/lowbeer-question/index.html`

All eight pages were inspected for headings, literal `.md` URLs, distinctive revised text, and internal targets. Every published target exists in the build.

## Publication gate

Professor Langenkamp approved Batch L on 6 September 2026. The exact committed tree passed both GitHub workflows and live-page verification for all eight entries. Batch M remains locked.
