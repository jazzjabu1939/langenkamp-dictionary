---
layout: default
kind: glossary
title: "Apple Silicon"
permalink: /entries/apple-silicon/
date: 2026-05-12
summary: "Apple's family of ARM-based system-on-chip processors, introduced 2020. The technical substrate of the Dictionary's *Sovereign Compute* / *FERPA Compliance Posture* architecture."
draft: false
published: true
---

Apple Silicon is the umbrella name for Apple's family of ARM-based system-on-chip processors, introduced in November 2020 with the M1 and expanded over five subsequent generations through the M5 (2025–2026). The architecture's defining features are *unified memory* (CPU, GPU, and Neural Engine share a single high-bandwidth memory pool, rather than passing data across PCIe), and *integrated Neural Engine cores* (dedicated matrix-multiplication hardware for ML inference). Both features turn out, somewhat accidentally, to be ideal for running large language models locally.

For this Dictionary, Apple Silicon is the **technical substrate of the local-compute argument**. The *[Sovereign Compute](sovereign-compute.md)* calculator's Level-3 and Level-4 tiers are written assuming Apple Silicon hardware; the *[M5 Max](m5-max.md)* and *[Mac Studio](mac-studio.md)* entries document the specific configurations the operator runs and considers. The *[GenXClaw](genxclaw.md)* and *[FERPA Compliance Posture](ferpa-compliance-posture.md)* entries name Apple Silicon as the substrate that makes local-only student-data processing viable for a working faculty member without enterprise-grade infrastructure budget.

The strategic-tech significance of Apple Silicon — that Apple has, deliberately or otherwise, built the architecture most suited to consumer-grade local LLM inference — is a Dictionary-relevant data point about sovereignty infrastructure that the *[Sovereignty Impulse](sovereign-compute.md)* thread treats as load-bearing.

## See also

- *[Sovereign Compute](sovereign-compute.md)*
- *[M5 Max](m5-max.md)*, *[Mac Studio](mac-studio.md)* — specific configurations
- *[GenXClaw](genxclaw.md)*
- *[FERPA Compliance Posture](ferpa-compliance-posture.md)*
