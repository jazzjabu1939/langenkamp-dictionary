---
layout: default
kind: glossary
title: "M5 Max"
permalink: /entries/m5-max/
date: 2026-05-12
summary: "Apple Silicon system-on-chip, M5 generation, Max-tier configuration. The operator's primary workstation; the substrate for local model inference and the *Sovereign Compute* setup."
draft: false
published: true
---

The M5 Max is the highest-tier laptop-class system-on-chip in Apple's M5 generation, released in 2025–2026. The operator of this Dictionary purchased a MacBook Pro 16" M5 Max configuration in April 2026: 18-core CPU, 40-core GPU, 16-core Neural Engine, 128 GB unified memory, 4 TB SSD. The order was placed April 18, 2026 (order W1429262259) for $5,890.73 plus AppleCare One, with delivery in early May 2026. See the *[Sovereign Compute](sovereign-compute.md)* entry and `hardware/purchases/2026-04-18_macbook_pro_m5_max.md` in the workspace for the full purchase rationale.

For this Dictionary, the M5 Max is the **substrate of the local-compute argument**. The 128 GB of unified memory and the 40-core GPU are sufficient to run open-weights models in the 30B-active-parameter range (Qwen 3.6 30B A3B, Gemma 4 31B, Hermes derivatives in the 70B range with quantisation) at usable speeds for sustained operator work. The architecture is documented in TOOLS.md: hybrid dense+MoE routing, model-to-task pairing, and the incremental-construction workflow for complex local tasks.

The structural significance is named in *[GenXClaw](genxclaw.md)* and *[FERPA Compliance Posture](ferpa-compliance-posture.md)*: the M5 Max is, accidentally, the architecture FERPA law would have specified if FERPA had been written with student-AI workflows in mind. The hardware purchase predates the FERPA argument; the convergence is real.

## See also

- *[Sovereign Compute](sovereign-compute.md)*
- *[Mac Studio](mac-studio.md)* — the desktop sibling, candidate for the *Sally* experiment
- *[Apple Silicon](apple-silicon.md)*
- *[FERPA Compliance Posture](ferpa-compliance-posture.md)*
- *[GenXClaw](genxclaw.md)*
