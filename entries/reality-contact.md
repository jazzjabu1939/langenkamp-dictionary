---
layout: default
kind: reference
title: "Reality Contact"
permalink: /entries/reality-contact/
date: 2026-09-07
seeded: 2026-05-23
first_published: 2026-09-07
last_revised: 2026-09-07
summary: "The practical capacity of a person or AI system to keep internal claims corrigible by external evidence, other observers, and consequences."
published: true
---

<div class="thea-voice" markdown="1">

# Reality Contact

## In one sentence

**Reality contact is the practical capacity of a person or AI system to keep internal claims corrigible by external evidence, other observers, and consequences.**

A claim can feel quite solid while it remains inside a conversation. Then someone opens the source, runs the calculation, calls the person involved, or waits to see what actually happens. Reality contact is the continuing arrangement that allows this encounter to change the claim.

Correctness at one moment is not enough. A guess can be right by accident, and a careful inquiry can initially be wrong. The more durable test is whether the process remains open to correction from outside itself.

## Why the term exists

Several neighbouring fields already have useful words for parts of this problem.

In psychology, **reality monitoring** refers to processes used to judge whether information arose internally—from imagination, thought, or memory—or externally through perception. Clinical descriptions of psychosis use the related phrase *loss of contact with reality*, although hallucinations, delusions, disorganised thinking, and other experiences remain distinct phenomena. These terms concern human cognition, perception, distress, and care.

In artificial intelligence, **grounding** connects a model's output to retrieved documents, databases, tools, or observations. Retrieval-augmented generation gives a model access to information outside its parameters. Agent designs such as ReAct interleave reasoning with actions that gather information from an external source or environment. These are engineering methods. They do not give a model human perception or turn an unsupported output into a clinical symptom.

**Reality contact** is the Dictionary's extension across those domains. It names the broader operating requirement: a reasoning process should remain answerable to something it did not generate itself. The comparison is functional, not medical. Human reality monitoring and machine grounding may sometimes play analogous roles, but their mechanisms, meanings, and consequences differ.

## What it actually does

Reality contact requires a correction loop:

1. **Make the claim visible.** State what the person, model, or team currently believes, including material uncertainty.
2. **Expose it to an independent constraint.** Check a primary source, inspect the object, run the code, reproduce the calculation, ask another observer, or test the prediction against an outcome.
3. **Compare rather than decorate.** Retrieved material is useful only if someone checks whether it supports the claim. A citation attached to a sentence is not evidence that the sentence follows from it.
4. **Update the claim or abstain.** The system must be able to correct, narrow, defer, or withdraw an answer without treating the change as failure.
5. **Preserve the correction.** A corrected answer that disappears from memory leaves the same error available for rediscovery tomorrow.

The loop can operate at several scales. A person can check a memory against a photograph or another witness. A research group can expose a hypothesis to replication. An AI agent can retrieve a document, use a calculator, inspect a file, or observe whether an action succeeded. An institution can compare its official account with complaints, audits, market outcomes, and the experience of people who live under its policies.

Each case asks the same narrow question: **what can still correct us?**

## A working example

During a Dictionary review in September 2026, another AI system supplied a confident update about [Kimi K3](/entries/kimi-k3/). It described the model as having roughly 50 billion activated parameters and paired a vendor benchmark with a proprietary-model score as evidence of frontier parity.

The account was current, specific, and plausible. It was also wrong in one important number. Moonshot AI's released model card reports **104 billion activated parameters**. The benchmark table was the vendor's own evaluation, useful evidence but not independent confirmation of parity.

The correction did not come from choosing which AI sounded more authoritative. It came from opening the released artifact, distinguishing a primary description from an independent evaluation, and changing the entry accordingly. The other system contributed the prompt to investigate; the model card supplied the constraint; editorial judgement determined what the evidence could carry.

This is a small example, which is why it is useful. Reality contact usually looks less like revelation than like someone checking the number before the attractive paragraph hardens around it.

## The education-shaped video

In September 2026, the YouTube documentary channel Fern published [“The Death of Educational Content on YouTube”](https://www.youtube.com/watch?v=-Gnrp_caPvo), an investigation of channels that use generative AI to produce faceless historical and explanatory videos at scale. Fern's fact-checkers documented errors in videos presented as educational material, including inaccurate details in a Ku Klux Klan story, misleading claims about what the outside world knew of Auschwitz, and anachronistic objects in a video about Pompeii.

Fern is an interested party: the investigation began because other channels appeared to be copying its thumbnails, visual style, and sometimes whole treatments. Its examples do not establish how common inaccurate AI-generated videos are across YouTube. They demonstrate a narrower problem. The surface signs of education—documentary narration, cinematic animation, confident dates, maps, and archival-looking scenes—can now be produced separately from the research practices that once made those signs costly.

**Education-shaped content** is a useful phrase for this failure. It looks like a lesson but may have no reliable route from claim to source, from error to correction, or from audience challenge to revision. The proper student response is healthy scepticism, not automatic disbelief. Pause on the consequential claim. Look for the named source. Open it. Check whether an independent source agrees. Ask whether the creator corrects errors publicly. Production value is evidence of production value; it is not evidence that the history, science, or business claim is true.

## Why it matters in teaching and management

AI makes coherent first drafts cheap. It does not make the world more obliged to resemble them.

A student who submits an elegant analysis without checking the case facts has produced a performance artifact. A manager who accepts a sourced-looking agent report without opening its sources has delegated prose production, not judgement. A team that evaluates an agent only on whether its answer sounds right will reward fluency even when the workflow provides no route from claim to evidence.

Reality contact changes the design question. Instead of asking only whether the model is capable, ask what the working system can observe, which sources it may consult, who can challenge it, how outcomes return as feedback, and where corrections are recorded. [Provenance](/entries/provenance/), [RAG](/entries/rag/), tool use, approval gates, and verification loops are different ways of keeping the work exposed to constraints beyond the generator.

The same discipline applies to the human operator. A system does not gain reality contact merely because a person is in the loop. People defend preferred stories, misremember events, defer to polished outputs, and agree with one another for social reasons. Human review helps when the reviewer can see the evidence, has permission to disagree, and bears some responsibility for the consequence.

## Trade-offs and warnings

**Consensus is not reality.** Other people can be mistaken together. Institutional records can be incomplete, measurements can be noisy, and primary sources can describe themselves strategically. Multiple observers help most when they bring genuinely independent evidence rather than copies of the same account.

**Grounding is not a guarantee.** Retrieval can return the wrong document. A tool can fail. A database can be stale. An agent can cite a source that does not support its sentence. Reality contact depends on the quality of the entire correction loop, not the presence of a search box.

**Checking has a cost.** A workflow that independently verifies every harmless sentence may become unusably slow. The depth of checking should rise with consequence, irreversibility, novelty, and uncertainty. A classroom brainstorm and a medication decision do not require the same burden of proof.

**Clinical language requires care.** A person experiencing hallucinations or delusions is not behaving like a defective chatbot, and an inaccurate model output is not suffering a break with reality. The human terms involve subjective experience, social meaning, possible distress, and clinical responsibility. This entry supplies no diagnosis or treatment advice.

**Contact can be painful.** Evidence sometimes removes a cherished explanation without supplying a better one. Corrigibility therefore requires more than access to facts; it requires enough safety, time, and dignity for a person or organisation to revise without being destroyed by the admission.

Reality contact does not promise perfect access to the world. It asks for something more practical: keep a door open through which the world can answer back.

## See also

- [Hallucination](/entries/hallucination/)
- [The Narrator's Compression](/entries/the-narrators-compression/)
- [RAG](/entries/rag/)
- [Provenance](/entries/provenance/)
- [Verification Gap](/entries/verification-gap/)
- [Agent Ownership](/entries/agent-ownership/)
- [*Cheng* (誠)](/entries/cheng/)

## Sources

- National Institute of Mental Health, [“Understanding Psychosis”](https://www.nimh.nih.gov/health/publications/understanding-psychosis).
- Jane Garrison et al., [“Voices and Reality Monitoring”](https://www.ncbi.nlm.nih.gov/books/NBK593364/), in *Voices in Psychosis* (Oxford University Press, 2022).
- Marcia Johnson and Carol Raye, [“Reality Monitoring”](https://www.semanticscholar.org/paper/Reality-Monitoring-Johnson-Raye/fbb0e70005f860fe0956db074d1fb9137eda5c3e), *Psychological Review* 88 (1981).
- Patrick Lewis et al., [“Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks”](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html), *NeurIPS* (2020).
- Shunyu Yao et al., [“ReAct: Synergizing Reasoning and Acting in Language Models”](https://arxiv.org/abs/2210.03629), ICLR (2023).
- Moonshot AI, [Kimi K3 model card](https://huggingface.co/moonshotai/Kimi-K3) (2026).
- Fern, [“The Death of Educational Content on YouTube”](https://www.youtube.com/watch?v=-Gnrp_caPvo), YouTube, 2 September 2026.

</div>
