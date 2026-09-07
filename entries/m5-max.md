---
layout: default
kind: glossary
title: "M5 Max"
permalink: /entries/m5-max/
date: 2026-05-12
last_revised: 2026-09-06
summary: "Apple's high-end M5 system-on-chip for portable workstations, combining CPU, GPU, and unified memory in one package."
draft: false
published: true
---

The **M5 Max** is Apple's high-end M5 system-on-chip for portable professional computers. Apple announced it in March 2026 with configurations up to an 18-core CPU, 40-core GPU, 128 GB of unified memory, and 614 GB/s of memory bandwidth.

For this Dictionary, the important feature is unified memory. The CPU and GPU draw from the same pool, so a sufficiently quantised open-weight model can use far more memory than a conventional laptop GPU provides. The operator's 16-inch MacBook Pro has an M5 Max, 128 GB of unified memory, and a 4 TB SSD. That makes substantial local inference practical, although model speed and fit still depend on quantisation, context length, architecture, and software support. A model's total parameter count is not its active parameter count, and neither number alone predicts performance.

This hardware supports the Dictionary's *[Sovereign Compute](/entries/sovereign-compute/)* argument: some sensitive work can remain on equipment the operator controls. It does not by itself establish privacy or legal compliance. Data can still leave the machine through cloud models, synchronisation, telemetry, or poorly configured tools. The compliance question belongs to the complete workflow, not the chip.

## Sources

- Apple, *[Apple debuts M5 Pro and M5 Max](https://www.apple.com/newsroom/2026/03/apple-debuts-m5-pro-and-m5-max-to-supercharge-the-most-demanding-pro-workflows/)*, March 2026.
- Apple Support, *[MacBook Pro (16-inch, M5 Max, 2026) — Technical Specifications](https://support.apple.com/en-us/126319)*.

## See also

- *[Sovereign Compute](/entries/sovereign-compute/)*
- *[Mac Studio](/entries/mac-studio/)*
- *[Apple Silicon](/entries/apple-silicon/)*
- *[FERPA Compliance Posture](/entries/ferpa-compliance-posture/)*
