# Batch D — Plain-Prose Review

**State:** ready_for_professor

**Baseline:** `3fd5325`

**Branch:** `editorial/alphabetical-plain-prose-audit-d`

**Published corpus:** 11 entries

**Excluded current drafts:** `descartes-was-wrong.md` and `dusty-laptop.md`

## Ledger

| Entry | Review status | Change class | Notes |
|---|---|---|---|
| Dario Amodei | reviewed | substantive revision | Replaced character speculation and stacked aphorisms with the institutional question the entry is meant to pose. |
| Data Processing Agreement | reviewed | light revision | Defined the abbreviation, stated the vendor-safeguard consequence directly, limited the local-first claim to cases without an outside processor, and repaired cross-links. |
| Dead Internet | reviewed | light revision | The prose remains unchanged; repaired three cross-links that rendered as dead relative `.md` URLs. |
| DeepSeek | reviewed | substantive revision | Corrected malformed Markdown, removed unsupported location and state-relationship claims, distinguished weights from practical local deployment, and added primary model sources. |
| Demis Hassabis | reviewed | light revision | The prose remains unchanged; repaired five cross-links that rendered as dead relative `.md` URLs. |
| Digital Sovereignty | reviewed | light revision | Normalised British editorial spelling and repaired cross-links; the four-layer definition and coercion analysis remain intact. |
| Discovery-Patch Race | reviewed | light revision | The prose remains unchanged; repaired five cross-links that rendered as dead relative `.md` URLs. |
| Du Fu (杜甫) | reviewed | substantive revision | Removed an unsupported death toll and court-poetry contrast, added concrete works, corrected the Han Yu claim, and separated history from the Dictionary's interpretation. |
| Durable Workflow | reviewed | light revision | The prose remains unchanged; repaired three cross-links that rendered as dead relative `.md` URLs. |
| Dwarkesh Patel | reviewed | light revision | The prose remains unchanged; repaired four cross-links that rendered as dead relative `.md` URLs. |
| Dylan Patel | reviewed | light revision | Normalised house spelling and repaired cross-links; retained the physical-stack contrast because it performs explanatory work. |

## Batch findings

- **11 entries reviewed:** 8 received light revisions and 3 received substantive revisions. Five entries required no prose change but did require cross-link repair.
- Every D entry contained at least one relative `.md` cross-link. Under permalink pages these rendered as nested URLs such as `/entries/dario-amodei/anthropic.md` and returned 404. D now uses canonical `/entries/<slug>/` paths. The defect is corpus-wide and should be repaired outside the alphabetical prose batches rather than rediscovered letter by letter.
- *DeepSeek* contained the batch's clearest technical defects: malformed emphasis, an unsupported two-city headquarters claim, an unhelpful repository-root link for *zhengming*, and no boundary between downloadable weights and affordable local operation.
- *Du Fu* compressed a disputed death toll, an unsupported contrast with court poetry, posthumous reception, and Han Yu's role into one confident historical paragraph. The revision retains the Dictionary's sincerity argument while marking it as an interpretation.
- *Dario Amodei* now treats the safety-founder problem as an institutional question rather than a speculative judgment about personal goodness.
- The remaining entries were already short, legible, and properly bounded. The scanner flag in *Dylan Patel* was retained because the sentence distinguishes computational models from their physical substrate.

## Representative changes

### Institution rather than personality

*Dario Amodei* no longer asks whether its subject is personally good and then answers with successive aphorisms. It asks whether a safety-motivated lab can preserve its commitments after becoming a hyperscale commercial institution, and identifies governance, incentives, and conduct as the evidence.

### Weights are not deployment

*DeepSeek* now separates three facts: the company's relationship to High-Flyer, the architecture and training of V3 and R1, and the practical consequences of released weights. It explicitly notes that a 671-billion-parameter model remains difficult and expensive to run even when its weights can be downloaded.

### History before Dictionary extension

*Du Fu* now names particular works and records the An Lushan Rebellion's effect on his life before presenting *The Sincere Society*'s use of him as a model of writing against power. The Han Yu paragraph identifies him as a leading advocate of the Ancient Prose Movement rather than its sole founder.

### A bounded legal claim

*Data Processing Agreement* now says exactly when a local-first architecture reduces the vendor-contract problem: the institution must process the data on infrastructure it controls without an outside processor. Other privacy and security duties remain.

## Professor review gate

Batch E must not begin until Professor Langenkamp has reviewed this ledger and the proposed D revisions.
