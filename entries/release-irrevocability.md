---
layout: default
kind: glossary
title: "Release Irrevocability / No-Recall Problem"
permalink: /entries/release-irrevocability/
date: 2026-08-21
summary: "The rule that downloadable model weights, once published and copied, cannot reliably be withdrawn or made safe by a later decision from the original lab."
draft: false
published: true
---

# Release Irrevocability / No-Recall Problem

**Release irrevocability is the rule that downloadable model weights, once published and copied, cannot reliably be withdrawn. The No-Recall Problem is the operational consequence.**

A defective physical product can sometimes be recalled. A hosted model can be patched or taken offline. Published weights behave differently. Copies can cross borders, move into private storage, be mirrored under new names, and run indefinitely without contacting the original developer.

Nor does a safety layer necessarily travel intact with the weights. Refusal behaviour may be altered through fine-tuning, model editing, or a different system harness. The publisher may announce a new policy, but the earlier artifact remains in circulation.

This does not make open weights inherently irresponsible. Local operation supports privacy, research, competition, resilience, and *[Sovereign Compute](sovereign-compute.md)*. It does make the release decision unusually permanent. The safety question must therefore be asked before publication, because after publication the lab can issue guidance and better versions, but it cannot retrieve every working copy.

## See also

*[Control Surface Asymmetry](control-surface-asymmetry.md)* · *[Open Weights](open-weights.md)* · *[Capability Diffusion](capability-diffusion.md)*
