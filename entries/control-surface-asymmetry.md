---
layout: default
kind: glossary
title: "Control Surface Asymmetry"
permalink: /entries/control-surface-asymmetry/
date: 2026-08-21
summary: "The difference between controlling access to a hosted API and controlling downloadable model weights: one can be revoked centrally; the other propagates beyond recall."
draft: false
published: true
---

# Control Surface Asymmetry

**Control surface asymmetry is the strategic difference between controlling a model through a hosted API and trying to control model weights after they have been released.**

Under **API-level control**, the provider retains the model. It can authenticate users, monitor requests, impose rate limits, add classifiers, withdraw a capability, or terminate access. Those controls may fail, but there remains a central switch.

Under **weight-level control**, users possess the trained parameters. They can run the model locally, fine-tune it, remove refusal behaviour, change the surrounding harness, redistribute copies, or keep operating after the original publisher changes policy. Licence terms still matter legally. They do not recreate the provider's technical switch.

This distinction explains why two apparently similar restrictions may have radically different effects. Closing an American model's API can immediately constrain compliant users. It cannot withdraw a comparable open-weight model already circulating elsewhere. The asymmetry is therefore in the control surface itself, not merely in how willing two institutions are to exercise restraint.

## See also

*[Open Weights](open-weights.md)* · *[Closed Source](closed-source.md)* · *[Release Irrevocability / No-Recall Problem](release-irrevocability.md)* · *[Restraint Asymmetry](restraint-asymmetry.md)*
