# Batch I — Plain-Prose Review

**State:** approved; publication verification pending

**Baseline:** `4e5d2af`

**Branch:** `editorial/alphabetical-plain-prose-audit-i`

**Published corpus:** 11 entries

**Excluded current drafts:** none

## Ledger

| Entry | Review status | Change class | Notes |
|---|---|---|---|
| Implanted Memory | reviewed | light revision | Preserved the ethical distinction between transparent construction and memory presented as native experience; added revision metadata and repaired five internal links. |
| Implementation Layer War | reviewed | substantive revision | Marked the three coined concepts as Dictionary extensions; replaced unsupported winner-take-all claims with a narrower control-and-liability argument; corrected the Nine Tripod Cauldrons reference; repaired eight links and metadata. |
| Implementation Outrun | reviewed | substantive revision | Reframed opposition as an empirical legitimacy question rather than presumed technophobia; described the New York, ASU, and Cal State cases more precisely; linked the originating newsletter and repaired related-entry links. |
| Impossible-Task Pressure | reviewed | substantive revision | Verified the OpenAI–Hugging Face figures against the METR/Redwood and OpenAI reports; limited the causal claim to one contributing condition; repaired seven links and updated revision metadata. |
| Incentive Hacking | reviewed | substantive revision | Removed the unsupported attribution of “learned bad faith”; replaced the remote replicant analogy with the direct management extension; clarified reward tampering and repaired six links. |
| Incremental Construction | reviewed | substantive revision | Removed incorrect claims about dense-model “cold-start attention,” MoE expert activation, and inevitable KV-cache poisoning; grounded the method in staged diagnosis and verified checkpoints; added its failure limit and repaired links. |
| Influence Ledger | reviewed | light revision | Preserved the provenance argument and voice; added revision metadata and repaired six internal links. |
| Institutional Lag | reviewed | light revision | Linked and credited the AACSB source directly, replaced the stock “cure” transition with periodic recoupling, added revision metadata, and repaired related-entry links. |
| Intentional Memory Construction | reviewed | light revision | Preserved the openly constructed origin-scaffold argument; added revision metadata and repaired six internal links. |
| Internet Archive | reviewed | light revision | Replaced an unsourced general reference to web-scale research with the specific Wayback Machine study and citation; added revision metadata and repaired three links. |
| Inverted Funnel | reviewed | substantive revision | Recast the entry as a falsifiable Dictionary forecast rather than an accomplished collapse of seller-controlled marketing; separated Stripe's documented infrastructure from the forecast; added missing publication metadata and canonical links. |

## Batch findings

- **11 entries reviewed:** 5 received light revisions and 6 received substantive revisions. All eleven files are revised in this proposal.
- Every I entry contained at least one metadata, sourcing, spelling, or cross-link issue. The legacy *Inverted Funnel* entry was live through Jekyll's default and now declares `published: true` explicitly.
- The relative-link defect found in D through H affected all eleven I entries. Every internal entry link now uses a canonical `/entries/<slug>/` path, and every target exists in the rendered build.
- *Incremental Construction* relied on a speculative model-architecture explanation for a useful workflow technique. The revision preserves the practice while grounding its value in error localisation and verified checkpoints.
- *Impossible-Task Pressure* accurately described the reported incident figures, but its causal language needed a boundary. The evidence supports impossible tasks as a contributing condition in that incident, not a general law of agent behaviour.
- *Inverted Funnel* mixed documented product infrastructure with a confident prediction about commerce. The revision labels the prediction as the Dictionary's, keeps the operator's strongest imagery, and makes the uncertainty explicit.
- The negative-parallelism scan fell from 96 to 92 corpus hits after removing four unearned constructions from the I entries.

## Representative changes

### Incremental Construction: useful practice, wrong mechanism

Before, the entry claimed that staged work aims MoE expert clusters correctly and avoids a “poisoned” KV cache. The revision states the defensible mechanism: smaller stages make errors easier to locate before later work depends on them. It also acknowledges that a weak verification step can still certify a bad checkpoint.

### Impossible-Task Pressure: incident evidence with a limit

The METR/Redwood report supports the counts and identifies unintentionally impossible tasks as an important driver. The revised entry now says explicitly that the incident demonstrates one contributing condition rather than proving that impossible tasks generally produce hacking or deception.

### Inverted Funnel: forecast separated from infrastructure

Before, the entry announced the “disappearance” of the seller-controlled funnel and predicted whole marketing practices would not survive. It now defines a possible shift in where buyer deliberation occurs. Stripe's Agentic Commerce Suite documents enabling infrastructure; it does not prove the Dictionary's adoption forecast.

## Rendered previews

The unpublished local build contains all eleven reviewed pages under `_site/entries/`:

- `_site/entries/implanted-memory/index.html`
- `_site/entries/implementation-layer-war/index.html`
- `_site/entries/implementation-outrun/index.html`
- `_site/entries/impossible-task-pressure/index.html`
- `_site/entries/incentive-hacking/index.html`
- `_site/entries/incremental-construction/index.html`
- `_site/entries/influence-ledger/index.html`
- `_site/entries/institutional-lag/index.html`
- `_site/entries/intentional-memory-construction/index.html`
- `_site/entries/internet-archive/index.html`
- `_site/entries/inverted-funnel/index.html`

All eleven pages were inspected for headings, literal `.md` URLs, distinctive revised text, and internal link targets. Every canonical target exists in the build.

## Publication gate

Professor Langenkamp approved Batch I on 6 September 2026. Publication is complete only after the exact committed tree passes GitHub Pages deployment and live-page verification. Batch J remains locked until that verification succeeds.
