---
layout: default
kind: glossary
title: "Kimi K3"
permalink: /entries/kimi-k3/
date: 2026-07-19
last_revised: 2026-09-06
summary: "Moonshot AI's 2.8T-parameter open-weight multimodal model, released in July 2026 with a 1-million-token context window and 104B activated parameters."
draft: false
published: true
---

Kimi K3 is a July 2026 open-weight model from Moonshot AI, a Chinese AI lab. Moonshot describes K3 as a **2.8-trillion-parameter** native multimodal model with **104 billion activated parameters**, a **1-million-token context window**, Kimi Delta Attention, Attention Residuals, and a sparse *[Mixture of Experts](/entries/mixture-of-experts/)* architecture that activates 16 of 896 routed experts per token.

For this Dictionary, Kimi K3 matters less as a leaderboard claim than as a strategic signal. It is another data point in the *[Open-Weights Inversion](/entries/open-weights-inversion/)*: a U.S. operator seeking practical model sovereignty may find some of the most aggressive open-weight releases coming from Chinese labs rather than from the leading U.S. frontier labs.

Moonshot reports strong results in coding, software engineering, visual work, and long-horizon agentic knowledge work. These are vendor evaluations, sometimes run with Kimi's own harness, so comparisons are sensitive to the harness, reasoning budget, tool access, and benchmark protocol. Moonshot's technical report says K3 still trails the strongest proprietary models overall. K3 is therefore not proof that open models have cleanly overtaken the closed frontier. It is evidence that the gap is narrowing in commercially important kinds of work.

The release is no longer merely promised. Moonshot published the full model weights, a model card, a license, deployment guidance, and a technical report in late July 2026. That makes K3 an open-weight artifact in the operational sense: others can inspect and run the released weights under the Kimi K3 License. It does not make the model open source in every possible sense, nor does publication independently validate the vendor's capability claims.

## Why it matters

Kimi K3 sharpens three Dictionary themes at once.

First, **open weights are becoming a geopolitical instrument**. A capable Chinese open-weight model is not merely a cheaper substitute for a U.S. API. It is an industrial-policy object: a model that can travel, be hosted by others, be optimized by inference providers, and create dependency patterns outside the closed U.S. lab stack.

Second, **frontier-adjacent capability is moving into the workflow layer**. The reported strengths are not only abstract reasoning benchmarks. They are engineering tasks, repo navigation, terminal-tool orchestration, visual feedback loops, dashboards, video editing, and other work surfaces where models become part of production.

Third, **"open source" remains an imprecise label**. The more useful operational questions are concrete: which weights, license, architecture details, evaluation harnesses, and reproducible artifacts are available? For K3, the weights and a model-specific license are public; that fact is clearer than the umbrella label.

## See also

- *[Open Weights](/entries/open-weights/)*
- *[Open-Weights Inversion](/entries/open-weights-inversion/)*
- *[Qwen](/entries/qwen/)*
- *[DeepSeek](/entries/deepseek/)*
- *[Mixture of Experts](/entries/mixture-of-experts/)*
- *[Sovereign Compute](/entries/sovereign-compute/)*

## Sources

- Moonshot AI, *Kimi K3* model card and released weights: <https://huggingface.co/moonshotai/Kimi-K3>
- Kimi Team, *Kimi K3: Open Frontier Intelligence*, technical report, July 2026: <https://arxiv.org/abs/2607.24653>
- Moonshot/Kimi, *Kimi K3: Open Frontier Intelligence*, launch post, July 2026: <https://www.kimi.com/blog/kimi-k3>
- Kimi API Platform, *Kimi K3* documentation: <https://platform.kimi.ai/docs/guide/kimi-k3-quickstart>
