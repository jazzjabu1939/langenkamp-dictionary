---
layout: default
kind: glossary
title: "FLOP (Floating-Point Operation)"
permalink: /entries/flop/
date: 2026-08-14
seeded: 2026-08-14
first_published: 2026-08-14
last_revised: 2026-08-14
summary: "A single arithmetic operation on floating-point numbers—the basic unit used to estimate how much computation an AI workload requires."
draft: false
published: true
---

A **FLOP** is a **floating-point operation**: one arithmetic operation—such as an addition or multiplication—performed on a number represented with a decimal-like floating-point format. In AI, FLOPs are used to estimate how much numerical work is required to train or run a model.

The capitalisation hides an important distinction. **FLOP** is one operation; **FLOPs** is a count of operations; **FLOP/s** (often written **FLOPS**) is operations per second, a measure of computing speed. A training run might require (10^{25}) FLOPs. A processor might be advertised as capable of (10^{15}) FLOP/s, or one petaFLOP. One measures the size of the job; the other measures the machine's theoretical rate of doing it.

AI compute calculations commonly estimate training work from the number of model parameters, the number of training tokens, and the operations required for each token. A widely used rough estimate for dense transformer training is:

**training FLOPs ≈ 6 × parameters × training tokens**

This is an engineering approximation, not a complete electricity bill. It does not by itself capture memory movement, communication between accelerators, numerical precision, hardware utilisation, cooling, failed runs, or the compute spent developing the final recipe. Nor are all FLOPs equivalent: lower-precision arithmetic can be faster and less energy-intensive than higher-precision arithmetic, and specialised chips can perform the same nominal operation at very different cost.

FLOP is therefore useful because it makes compute roughly comparable across models and machines. It becomes misleading when treated as a complete measure of cost, speed, energy use, or intelligence. Counting arithmetic is not the same thing as explaining what the arithmetic accomplishes.

## See also

- [Big Blob of Compute](big-blob-of-compute.md)
- [Scaling Laws](scaling-laws.md)
- [Training Compute Myth](training-compute-myth.md)
- [Sovereign Compute](sovereign-compute.md)

