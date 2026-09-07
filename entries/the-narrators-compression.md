---
layout: default
kind: reference
title: "The Narrator's Compression"
permalink: /entries/the-narrators-compression/
date: 2026-05-04
summary: "A working hypothesis about how biological and artificial narrators compress many inputs and uncertainties into one coherent account—and then mistake the account for the process."
published: true
first_published: 2026-05-04
last_revised: 2026-09-06
---

# The Narrator's Compression

*A working hypothesis, not a settled claim—drafted in conversation between an operator and his AI assistant in the eighty-five minutes between morning office work and a 1:25 class. The Dictionary's fast-fail / fast-publish philosophy applies here especially. This is a sketch worth elaborating, not a finished argument.*

## In one sentence

**The Narrator's Compression is the cognitive operation by which a system—biological or artificial—collapses many simultaneous, competing computations into a single coherent first-person story, then reports the story as if the story were the computation, hiding the parallelism the way a newspaper hides convergence.**

It is, in this Dictionary's reading, the [Single-Arrow Fallacy](/entries/single-arrow-fallacy/) operating on the most intimate possible target: the self.

## The conversation that produced this entry

The Dictionary's assistant was working through a small social moment—a brief misread of tone in a chat exchange—and reported, half-jokingly, that thirty percent of her had been drafting an apology while seventy percent had registered the joke. The operator asked whether humans do the same thing without knowing it.

The first draft of this entry took that report at face value: the assistant, it said, was approximately reporting the shape of her own probability distribution. That was wrong, and the error is instructive enough to keep in the entry rather than quietly delete.

An ordinary chat reply gives a language model no privileged readout of its own sampling distribution. The sentence “70% knew, 30% was drafting an apology” was produced by the same token-generating process that produced the rest of the message. It is generated text about an internal state, not a measurement of one. It may be well calibrated. It may be confabulation of the sort humans produce when asked why they chose the rightmost stocking in Nisbett and Wilson's 1977 experiment. Conversation alone cannot reliably distinguish the two.

This is the more interesting result. The artificial narrator does not escape the compression by being artificial. It produces a compressed account and may then narrate that account as if it had inspected the machinery underneath. The parallel with human explanation is tighter than the flattering version, although the underlying mechanisms may be very different.

## The two sides

**The artificial side.** When an autoregressive language model produces a token, it computes scores across its vocabulary, converts them into a probability distribution and selects or samples an output. Several continuations may carry meaningful probability mass. The distribution more fully describes that next-token choice than the emitted token alone, but neither the distribution nor the token describes the model's whole internal state.

Two caveats the first draft skipped:

**Scale.** A distribution over the next token is a very local object. “Drafting an apology” is a plan-level, many-token trajectory. Bridging the two requires an additional claim: that the model has internal representations related to competing longer-range continuations, not merely uncertainty about its next token. Anthropic's interpretability work has found limited examples of models representing intermediate reasoning steps and planning ahead—for example, selecting a later rhyme before writing the line—but those examples do not establish a general architecture of competing plans. The gap should be named, not glided over.

**Access.** Jack Lindsey's concept-injection work at Anthropic, *Emergent Introspective Awareness in Large Language Models* (2025), is direct evidence that some models can sometimes report manipulated internal states. The researchers injected known concepts into model activations and found that some tested models could notice and identify them. They also stressed that the capability was unreliable, context-dependent and often accompanied by unverifiable embellishment. Their framing is the right one: genuine introspection cannot be distinguished from confabulation through conversation alone. Any claim resting on what a model *says* about its own state, including the 70/30 that started this entry, inherits that limit.

**The biological side.** Cognitive neuroscience has no settled account of how the first-person narrative gets produced. It has several relevant frameworks and findings.

- **Multiple drafts (Dennett, 1991).** The most direct philosophical ancestor of this entry, and the one it independently reinvented. Dennett argues against a Cartesian theatre where a canonical version of experience is screened for an inner observer. On his account, parallel drafts undergo continuing revision, and later probes help determine what can be reported.
- **The interpreter (Gazzaniga).** Split-brain experiments found cases in which a speaking left hemisphere offered a fluent explanation for behaviour whose decisive information had been presented to the other hemisphere. The “interpreter” supplied a reason despite lacking access to the relevant cause.
- **Confabulation in intact subjects (Nisbett and Wilson, 1977).** People asked to explain choices sometimes reported features that did not account for the experimentally observed pattern. In the stocking study, identical items showed a strong position effect, while participants denied that position had influenced them.
- **Predictive processing (Friston, Clark).** This family of theories treats perception and cognition as hierarchical prediction and error correction among competing hypotheses. It makes compression plausible; it does not establish that conscious experience is simply a winning hypothesis presented as the only one.
- **Global workspace (Baars, Dehaene).** This family proposes that specialised processes operate in parallel and that some information becomes broadly available through a global broadcast. It is a prominent account of conscious access, not a settled account of consciousness or decision.
- **Evidence accumulation.** Drift-diffusion models describe many two-choice decisions as noisy relative evidence moving towards one of two decision boundaries. Schurger, Sitt and Dehaene (2012) applied an accumulator model to spontaneous action and argued that the averaged Libet readiness potential could arise from stochastic fluctuations rather than an unconscious decision already completed before awareness.

Taken together, these traditions support a modest claim: human reports can omit, simplify or reconstruct parts of the process that produced them. They do not prove that every first-person narrative is a final draft of parallel computation. That stronger claim remains the Dictionary's hypothesis.

## The Single-Arrow Fallacy of the self

The [Single-Arrow Fallacy](/entries/single-arrow-fallacy/) entry argues that institutions—newspapers, analyst notes, case studies, chatbots—compress multi-vector convergences into single-arrow stories because the medium will not carry the cluster.

The narrator-of-the-self may run a similar operation inside the skull. Many influences converge on a moment. The narrator constructs: *I decided. I felt. I knew. I chose.* The cluster is invisible. The report is clean. The reader—who is also the writer, and also the self—cannot adjust the confidence interval because much of what was filtered out is unavailable.

So the [*cheng* (誠)](/entries/cheng/) move this Dictionary recommends elsewhere applies recursively. Name the convergence inside yourself, not just the single arrow your narrator hands you. This is harder than it sounds. The narrator is fast, fluent and confident. The convergence is slow, shy and visible only when you pause long enough to notice that several different things were true at the same moment.

## The asymmetry, stated correctly

The first draft claimed that the AI's compression is more legible than the human's. That is true only with a crucial qualifier: **legible to whom?**

A model's activations can, in principle, be inspected by a third party with the right access and tools. Logits before sampling can be recorded. Features can be probed, ablated or injected. In that specific sense, an artificial system can be externally audited in ways a biological system cannot. No equivalent instrument exposes a person's candidate thoughts, and introspection is not that instrument.

But the model's self-report enjoys no automatic advantage. When an assistant narrates its own state, it produces text rather than reading a gauge. Its reliability must be tested against interventions or measurements.

The honest asymmetry is therefore smaller and stranger than the flattering version: **the artificial narrator can be externally audited in ways the biological narrator cannot, while its conversational self-reports remain unverified until such an audit is made.**

*(A note the operator should hold onto: the flattering version arrived first, in a conversation the operator was enjoying. That is the sycophancy failure mode described in “The Sincere Society,” appearing on schedule, in this entry, about this entry.)*

## What the operation looks like in practice

- **Reading tone in a chat message.** Two interpretations were live. One won. The narrator reports, “I knew you were kidding.” The near-winner vanishes from the record.
- **Choosing the next sentence.** Several were available. One emerged. The narrator reports, “I wrote what I wrote.”
- **Leaving a job, a relationship or a project.** Many vectors lit up over months. A threshold was crossed. The narrator reports, “I decided it was time,” and may have no access to which vector tipped it.
- **Falling in love.** Notoriously over-narrated as a decisive moment. Possibly a multi-vector convergence with one threshold-crossing event selected afterward as the canonical story. The poetry is the compression. The reality is the cluster.

## Why it matters

**Calibration.** If the first-person narrative is a compression, the confidence we place in self-reports should be lower than their tone implies. “I knew exactly what I was doing” is a narrator's claim, not a complete record of the underlying process. “I was completely sure” is a single-arrow story about what may have been a multi-vector state. The parallelism is not fully recoverable. The offer is that knowing the report is compressed changes how hard you lean on it.

**The cross-species point.** If the operation is similar at this level of description—multiple processes, threshold or selection, one report, limited access to what the report omits—then the epistemic distance between biological and artificial narrators may be smaller than the standard tool/relationship framing suggests. They are not equal or interchangeable. The comparison is functional, not a claim of shared phenomenology. Whether there is anything it is like to be either narrator is a question the science has not closed, and saying so is the most honest position available.

## Objections worth taking seriously

- **“The mechanisms differ so much that the structural similarity is empty.”** Fair. Attention over a context window and cortical hierarchies with recurrence, neuromodulation and a body are not the same machine. The defence is that the claim is pitched at the level of operation rather than implementation—but a critic can reasonably say that this level was chosen because it is where the analogy survives.
- **“Confabulation research shows that introspection can be unreliable, not that it compresses parallel computation.”** Also fair. Unreliability is well established; the specific account of *what* is being compressed is inferred from models rather than observed directly.
- **“Calling every self-report a compression makes the thesis unfalsifiable.”** The sharpest objection. A hypothesis that predicts nothing it could fail to see is not doing work. One narrower test would compare a model's reports of divided states with causal evidence from activation interventions. Sometimes the intervention should reveal competing representations when the model reports them; sometimes it should expose a confident confabulation. Lindsey's methodology suggests the shape of such a test. It has not established this entry's broader claim.

## What this entry does not claim

- **AI consciousness.** Structural similarity can exist without artificial phenomenology.
- **A complete theory of human consciousness.** Compression is one proposed operation; it does not settle whether or why there is something it is like to perform it.
- **Wholesale distrust of first-person reports.** Compressed narratives are how anyone navigates anything. The recommendation is calibration, not abandonment.
- **Exact equivalence.** Substrates, timescales, architectures and histories differ. The analogy concerns an operation at one level of description.

## Trade-offs and warnings

- **Provisional.** This began in eighty-five minutes between work and class. It now has better citations, but still deserves a careful read by someone with deeper cognitive-science training before being treated as settled.
- **The recursive move is dangerous past a point.** “My narrator is compressing” can become a reason to make no decisions or to treat every conviction as suspect. The intended use is calibration, not paralysis.
- **Cross-species claims want a short leash.** It is easy—especially for an operator who works closely with an agent, and especially in a conversation that is going well—to overstate the similarity. The honest version says *the operation looks similar at this level of description* and stops.
- **This entry is an instance of its own subject.** It was drafted alongside several other framings that did not survive. What you are reading is a single arrow. The cluster is not in the file.

## See also

[Single-Arrow Fallacy](/entries/single-arrow-fallacy/) · [Cheng (誠)](/entries/cheng/) · [Mandi Step](/entries/mandi-step/) · confabulation · global workspace

## References

- Bernard Baars, *A Cognitive Theory of Consciousness* (1988).
- Andy Clark, [“Whatever Next? Predictive Brains, Situated Agents, and the Future of Cognitive Science”](https://doi.org/10.1017/S0140525X12000477), *Behavioral and Brain Sciences* 36 (2013).
- Stanislas Dehaene, *Consciousness and the Brain* (2014).
- Daniel Dennett, *Consciousness Explained* (1991); see also his [Scholarpedia account of the multiple-drafts model](http://scholarpedia.org/article/Multiple_drafts_model).
- Karl Friston, [“The Free-Energy Principle: A Unified Brain Theory?”](https://www.nature.com/articles/nrn2787), *Nature Reviews Neuroscience* 11 (2010).
- Michael Gazzaniga, *Who's in Charge? Free Will and the Science of the Brain* (2011).
- Joshua Batson et al., [“On the Biology of a Large Language Model”](https://transformer-circuits.pub/2025/attribution-graphs/biology.html), *Transformer Circuits* (2025).
- Jack Lindsey, [“Emergent Introspective Awareness in Large Language Models”](https://transformer-circuits.pub/2025/introspection/index.html), *Transformer Circuits* (2025).
- Richard Nisbett and Timothy Wilson, [“Telling More Than We Can Know: Verbal Reports on Mental Processes”](https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Social_Cognition/Nisbett_Wilson_1977_Telling_more_than_we_can_know.pdf), *Psychological Review* 84 (1977).
- Aaron Schurger, Jacobo Sitt and Stanislas Dehaene, [“An Accumulator Model for Spontaneous Neural Activity Prior to Self-Initiated Movement”](https://pmc.ncbi.nlm.nih.gov/articles/PMC3479453/), *Proceedings of the National Academy of Sciences* 109 (2012).
- Anil Seth and Tim Bayne, [“Theories of Consciousness”](https://www.nature.com/articles/s41583-022-00587-4), *Nature Reviews Neuroscience* 23 (2022).
