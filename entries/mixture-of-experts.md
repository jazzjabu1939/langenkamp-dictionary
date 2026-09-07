---
layout: default
kind: glossary
title: "Mixture of Experts (MoE)"
permalink: /entries/mixture-of-experts/
date: 2026-05-12
last_revised: 2026-09-06
summary: "A neural-network design that routes each token through only a subset of several specialised sub-networks."
draft: false
published: true
---

**Mixture of Experts (MoE)** is a neural-network design in which some layers contain several parallel sub-networks, called *experts*. A learned router sends each token to only a small number of them. Because most experts remain inactive for that token, the model can have many more total parameters than it uses in each forward pass.

Qwen3-30B-A3B is a useful example: its model card reports about 30.5 billion total parameters and 3.3 billion activated per token. That does **not** mean it behaves like a dense 3.3-billion-parameter model. Attention layers, routing, memory traffic, expert capacity, batching, and implementation overhead all affect speed and quality. Nor does a larger total count prove that the model “stores more knowledge.” Total and active parameters describe architecture, not a benchmark result.

MoE offers an attractive trade: increase model capacity without paying dense-model compute for every parameter on every token. The costs include routing and load-balancing problems, communication among devices during training and serving, and memory requirements for weights that may be inactive on a particular token but must still be available.

For a local operator, this distinction matters. Sparse activation can reduce arithmetic per token, yet the full quantised weights generally still need to fit in memory or be moved through it. An MoE model can therefore be computationally economical while remaining memory-hungry. Prompting advice should be justified by measured behaviour of a particular model; there is no established rule that MoE models require a special “warming” ritual.

## Sources

- Qwen Team, *[Qwen3-30B-A3B model card](https://huggingface.co/Qwen/Qwen3-30B-A3B)*.
- Mistral AI, *[Mixtral of Experts](https://mistral.ai/news/mixtral-of-experts/)*.
- DeepSeek-AI, *[DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)*.

## See also

- *[Sovereign Compute](/entries/sovereign-compute/)*
- *[Qwen](/entries/qwen/)*
- *[DeepSeek](/entries/deepseek/)*
- *[Mistral](/entries/mistral/)*
- *[M5 Max](/entries/m5-max/)*
