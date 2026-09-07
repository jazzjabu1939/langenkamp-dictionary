---
layout: default
kind: glossary
title: "Pangram Labs"
permalink: /entries/pangram-labs/
date: 2026-05-12
last_revised: 2026-09-06
summary: "An AI-text-detection company whose products and public controversies illustrate both the demand for detection and the danger of treating a probabilistic score as a verdict."
draft: false
published: true
---

**Pangram Labs** is an AI-detection company that sells classifiers intended to distinguish human, AI-assisted, and AI-generated text. Pangram publishes its own benchmark results and false-positive estimates. Those are vendor evaluations, not independent guarantees for every genre, language, model, or future version of the product.

The company belongs in this Dictionary because it makes the detector's governance problem concrete. In May 2026, co-founder and CEO Max Spero publicly highlighted a sentence from New York City mayor Zohran Mamdani with the implication that it sounded AI-generated. The post drew more than four million views. The episode did not establish who drafted the sentence. It did show how quickly a stylistic suspicion can become a public accusation without provenance evidence.

That is the narrower connection to *[The Olang' Trap](/entries/olang-trap/)*. Research has found bias and reliability problems in AI-text detection as a class, especially across language backgrounds and under paraphrasing. It does not follow that every result from every Pangram version is biased or wrong. The operational rule is simpler: **a detector score is a lead for further inquiry, not proof of authorship or misconduct.** A consequential decision should add process evidence, source history, conversation with the writer, and an appeal path.

Pangram also works on identifying text altered by *humaniser* tools, which places it inside the recursive contest described by *[The Sinceerly Stack](/entries/sinceerly-stack/)*: generators produce a detectable style, humanisers try to remove it, and detectors train on the attempted removal.

## Sources

- Pangram, *[Introducing Pangram 4](https://www.pangram.com/blog/introducing-pangram-4)* — the company's own description and benchmark claims.
- Jason Koebler, *[Your AI Use Is Breaking My Brain](https://www.404media.co/your-ai-use-is-breaking-my-brain/)* — reporting on the Mamdani episode and detector-humaniser contest.
- Jason Koebler, *[Substackers Say New AI Detection Tool Is a “Witch Hunt”](https://www.404media.co/substackers-say-new-ai-detection-tool-is-a-witch-hunt/)* — reporting on Pangram's Substack integration and acknowledged error risk.

## See also

- *[The Olang' Trap](/entries/olang-trap/)* — the detector-governance argument
- *[The Sinceerly Stack](/entries/sinceerly-stack/)* — the recursive cat-and-mouse
- *[AI Writing](/entries/ai-writing/)*
- *[GPTZero](/entries/gptzero/)*, *[Originality.ai](/entries/originality-ai/)* — competitors
