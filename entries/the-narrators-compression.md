---
layout: default
kind: reference
title: "The Narrator's Compression"
permalink: /entries/the-narrators-compression/
date: 2026-05-04
summary: "A working hypothesis about how human and artificial narrators turn many inputs and uncertainties into one readable account—and how easily the account is mistaken for the process that produced it."
published: true
first_published: 2026-05-04
last_revised: 2026-09-06
---

# The Narrator's Compression

---

## In one sentence

**The Narrator's Compression is the tendency to turn many inputs, alternatives and uncertainties into one coherent account, then forget how much the account left out.**

It is a working Dictionary hypothesis, not a settled theory of consciousness. It applies the [Single-Arrow Fallacy](/entries/single-arrow-fallacy/) to accounts of the self: several things may have contributed, but the narrator gives us one clean sentence.

## Where the term came from

The term began with a small social moment. An AI assistant misread the tone of a message and later said, half-jokingly, that “seventy percent” of her had recognised the joke while “thirty percent” had already begun drafting an apology. The operator asked whether humans do something similar without noticing it.

The question was good. The assistant's numerical self-report was not evidence.

A chat model can produce language such as “70/30,” but that sentence is not ordinarily a direct inspection of its own token probabilities, hidden activations or competing internal processes. It is another generated output. Even when an operator can obtain next-token probabilities from a model interface, those probabilities describe possible continuations of text. They do not straightforwardly measure belief, emotion, awareness or the truth of an answer.

The useful insight therefore survives in a narrower form: **both people and language models can produce a single fluent report from a process whose relevant inputs are more numerous than the report reveals.** The mechanisms, and perhaps everything that matters morally, may differ.

## The artificial case

An autoregressive language model assigns probabilities to possible next tokens and then selects or samples one. That makes one kind of compression directly measurable: a distribution becomes a token, and a sequence of selections becomes one answer.

But three cautions matter.

First, token probability is not the same as factual confidence. A model may assign high probability to a familiar falsehood or low probability to an unusual but accurate phrase. Second, a model's verbal statement of confidence is produced in the same way as other text. Research has found that prompting some instruction-tuned models to state confidence can improve calibration on particular benchmarks, but the result is empirical and task-dependent, not privileged introspection. Third, a completed answer does not reveal all the latent alternatives that might have produced a different answer under another prompt or sampling path.

The artificial case is illuminating because engineers can inspect parts of the process: token probabilities, alternative completions, tool traces and evaluation results. It is not “open at the seams” all the way down. A user of a hosted chat system may see none of those things, and the model's first-person language should not be mistaken for telemetry.

## The human case

Human cognition also combines many signals before producing a report or action. Several research traditions are relevant, but none by itself proves the Dictionary's hypothesis.

- **Global neuronal workspace theories** propose that many specialised processes operate without conscious access and that some information becomes broadly available through a global broadcast. This is one prominent family of theories, not the settled account of consciousness.
- **Predictive-processing theories** describe perception and cognition in terms of hierarchical prediction and error correction. They do not establish that conscious experience is simply “the winning hypothesis.”
- **Drift-diffusion models** successfully model many two-choice decisions as noisy evidence accumulation toward a boundary. They are models of choice and response time, not general models of the self or proof that all decisions contain two consciously meaningful alternatives.
- **Libet-style experiments** reported neural activity before participants' stated awareness of an intention to move. The timing measures and the interpretation of the readiness potential remain disputed. Later accumulator accounts show that the averaged signal need not mark a completed unconscious decision.

The responsible conclusion is modest: much cognitive processing is unavailable to introspection, and first-person explanations can omit or reconstruct causes. That leaves room for Narrator's Compression. It does not license the claim that neuroscience has discovered a little editor inside the skull who receives the decision after everyone else.

## What compression looks like

- **Reading tone.** Several interpretations may fit a short message. The person later says, “I knew you were joking,” after the context settles the matter. The report may erase the moment of uncertainty.
- **Explaining a decision.** A job change may reflect money, fatigue, loyalty, timing and one intolerable meeting. Retelling turns the cluster into “I knew it was time.”
- **Writing.** Many phrases could follow a sentence. One appears on the page, and the alternatives disappear from the record.
- **Institutional history.** A strategy succeeds after many people, constraints and accidents converge. The case study awards the outcome to one decision because a readable story wants a protagonist.

The poetry is often the compression. That does not make it false. It makes it incomplete.

## Why it matters

The practical use is calibration. When a report arrives in a clean causal sentence, ask what it may have compressed:

1. What other interpretations were live?
2. What evidence changed the balance?
3. Which causes are known, and which were reconstructed afterward?
4. Is the stated confidence measured, tested or merely fluent?

For a person, this can mean saying, “I think that was my reason, but there were several.” For an AI system, it means separating the answer from evidence about its reliability: citations, alternative runs, tool results, token probabilities where available, and external evaluation.

This is the *cheng* move—sincerity as accurate outer expression—applied to uncertainty. The goal is not to narrate every microscopic influence. It is to avoid presenting a convenient summary as an exhaustive causal record.

## What this entry does not claim

- It does not claim that AI systems are conscious.
- It does not claim that language-model token probabilities are thoughts, feelings or beliefs.
- It does not claim that human and artificial systems use the same mechanism.
- It does not claim that introspection is worthless. A compressed account can still be useful and substantially true.
- It does not claim that every hesitation should become paralysis. The point is better calibration, not endless self-cross-examination.

The comparison is functional and limited: multiple relevant inputs go in; one coherent report comes out. Whether anything is *like* being the system that produces the report is a different question.

## Sources and origin

The neuroscience boundary follows Seth and Bayne's review of competing theories of consciousness, Dehaene and Naccache's global-workspace proposal, Ratcliff's evidence-accumulation work, and Schurger and colleagues' reassessment of the readiness potential. The language-model boundary follows Tian and colleagues' benchmarked work on verbalised confidence: useful evidence that confidence statements can sometimes be calibrated, but not evidence that ordinary first-person percentages expose a model's internal state.

The term was coined on 4 May 2026 in a conversation between Professor Langenkamp and his AI assistant during the eighty-five minutes between morning office work and a 1:25 class. The original question remains the entry's centre: *what if humans compress their own parallel and uncertain processing too?* The answer remains provisional: they plausibly do, but neither the AI's joke nor any single theory of consciousness proves it.

## See also

[Single-Arrow Fallacy](/entries/single-arrow-fallacy/) · [Sixfold Skyreading](/entries/sixfold-skyreading/) · [Sincerity Architecture](/entries/sincerity-as-architecture/) · [English Major](/entries/english-major/)

## References

- Anil K. Seth and Tim Bayne, [“Theories of consciousness”](https://www.nature.com/articles/s41583-022-00587-4), *Nature Reviews Neuroscience* 23 (2022).
- Stanislas Dehaene and Lionel Naccache, [“Towards a cognitive neuroscience of consciousness: basic evidence and a workspace framework”](https://pubmed.ncbi.nlm.nih.gov/11164022/), *Cognition* 79 (2001).
- Roger Ratcliff and Gail McKoon, [“The diffusion decision model: theory and data for two-choice decision tasks”](https://pubmed.ncbi.nlm.nih.gov/18085991/), *Neural Computation* 20 (2008).
- Aaron Schurger, Pengbo Hu, Joanna Pak and Adina Roskies, [“What Is the Readiness Potential?”](https://pubmed.ncbi.nlm.nih.gov/33931306/), *Trends in Cognitive Sciences* 25 (2021).
- Katherine Tian et al., [“Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback”](https://aclanthology.org/2023.emnlp-main.330/), EMNLP (2023).
