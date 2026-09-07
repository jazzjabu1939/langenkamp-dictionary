# Batch Q — Plain-Prose Review

**State:** published

**Baseline:** `de2d4bf`

**Branch:** `editorial/alphabetical-plain-prose-audit-q`

**Published corpus:** 3 entries

**Excluded current drafts:** none

## Ledger

| Entry | Review status | Change class | Notes |
|---|---|---|---|
| Quantization | reviewed | light revision | Extended the definition from weight storage to weights or activations, added exact memory arithmetic and runtime overhead, qualified speed and quality claims, added sources and revision metadata, and repaired canonical links. |
| Quantum Effects in the Brain | reviewed | substantive revision | Rebuilt the entry around the actual Orch OR claim and its evidentiary limits; separated ordinary quantum chemistry from functionally important coherent effects, removed unsupported conclusions about AI capability, and made every implication conditional. |
| Qwen | reviewed | substantive revision | Replaced the conflated and obsolete “Qwen 3.6 30B A3B” account with the current Qwen 3.8 family, separated dense and MoE deployment propositions, and used ecosystem evidence without converting adoption into benchmark supremacy. |

## Batch findings

- **3 entries reviewed:** one received a light revision and two received substantive revisions.
- *Quantum Effects in the Brain* contained the largest conceptual repair. Orch OR is now described as a serious but unconfirmed theory, and evidence for quantum-scale effects in microtubules is separated from evidence for cognition, objective reduction, or consciousness.
- *Qwen* no longer conflates Qwen3-30B-A3B with later Qwen3.6 releases. It now uses Alibaba's August 2026 Qwen 3.8 disclosures and distinguishes local usefulness, ecosystem adoption, provenance, and model quality.
- *Quantization* retains its practical purpose while accounting for activations, metadata, runtime buffers, and KV-cache overhead rather than treating nominal weight size as total memory use.
- All three entries have explicit publication and revision metadata. Every changed internal link points to a built canonical target.
- The negative-parallelism scanner reports 83 hits across 155,919 words (0.53 per thousand), one fewer hit than the P baseline.

## Entries recommended for approval reading

1. **Quantum Effects in the Brain** — the AI-ceiling claim and the evidentiary status of Orch OR are materially narrower.
2. **Qwen** — the model-family description, current releases, and geopolitical interpretation are rebuilt.

## Representative before and after

### Quantum Effects in the Brain

**Before:** the hypothesis was “the strongest available argument that AI systems have a hard ceiling” and, if correct, implied that genuine understanding, creativity, and moral reasoning might all be impossible for AI.

**After:** “The hypothesis therefore does not settle whether AI can understand, create, or reason morally. It identifies one proposed physical boundary and makes clear how many premises must hold before that boundary becomes an AI ceiling.”

### Qwen

**Before:** “Qwen 3.6 30B A3B” was described as a roughly 30-billion-parameter MoE and the current local-compute leader, combining a Qwen3 architecture with a later generation name.

**After:** the entry distinguishes the dense Qwen3.8-27B local proposition from Qwen3.8-2.4T-A95B, whose 2.4 trillion total and 95 billion active parameters require infrastructure beyond an ordinary workstation.

## Rendered previews

The rendered pages under `_site/entries/` were inspected for all three slugs, including distinctive revised text, accidental `.md` links, and canonical internal targets.

## Publication gate

Professor Langenkamp approved Batch Q on September 6, 2026. Content commit `b9815f6` passed both GitHub workflows and all three live HTTPS checks. Batch R remains unreviewed.
