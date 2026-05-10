---
layout: default
title: "Lab Character"
permalink: /entries/lab-character/
summary: "the institutional temperament, governance structure, and founding motivation of an AI laboratory — what it actually does when commercial pressure conflicts with stated values, and who leaves when the conflict becomes irresolvable."
published: true
---

# Lab Character

## In one sentence

***Lab character* is the institutional temperament, governance structure, and founding motivation of an AI laboratory — revealed not by its public statements about safety and responsibility, but by what it actually does when commercial pressure conflicts with those statements, and who leaves when the conflict becomes irresolvable.**

## On neutrality

It is difficult if not impossible to stay neutral once you have explored the capabilities of models and systems that are available and come to understand the companies and people behind them. It is likely that the more time you spend understanding the ecosystem, the more you will realise there are substantial differences in the philosophies of the companies involved in the hyper-competitive race for dominance and market share. The below is likely to be contentious, and we make no claim to being perfectly objective in this Dictionary. The following is our attempt to map out the terrain from our perspective as it looks today. Who are the good, who are the less good. We reserve the right to be wrong and to update.

---

## The major laboratories, as of 2026

### Anthropic

Founded in 2021 by Dario Amodei, Daniela Amodei, Chris Olah, Amanda Askell, and others — all of whom left OpenAI specifically over concerns about the direction of AI development there. Safety was not a constraint added later; it was the founding reason. The institutional culture reflects this: Anthropic publishes more serious alignment and interpretability research than any other frontier lab, led by Chris Olah's team, which is attempting to actually understand what is happening inside large language models rather than simply whether their outputs are safe. Constitutional AI — training models to critique and revise their own outputs against a set of principles — was an Anthropic invention. Amanda Askell's work on model character and the philosophical underpinnings of AI behaviour is serious scholarship, not marketing.  (They do seem to like John Stuart Mill a lot and could perhaps consider Edmund Burke's work more).

The picture as of mid-2026 is substantially more complicated than the founding story. Anthropic is now pursuing a valuation approaching $1 trillion, annualised revenue expected to exceed $45 billion, and compute commitments that read like a military procurement list: a 5GW agreement with Amazon, a 5GW agreement with Google (plus a reported $200 billion cloud commitment over five years representing more than 40% of Google's disclosed revenue backlog), $30 billion of Azure capacity with Microsoft and Nvidia, and — most startling — a deal to use all available capacity at SpaceX's Colossus 1 data centre, more than 300 megawatts and 220,000 NVIDIA GPUs. The SpaceX relationship is particularly strange: Elon Musk spent months publicly mocking Claude and attacking Anthropic's culture. Incentives shifted. Anthropic needed compute immediately; SpaceX had it; Musk wants OpenAI weakened more than he dislikes Anthropic. The GPUs were available.  He probably also wants to get some help for Grok on the sly.

Two events in this period are the most diagnostic for lab character. The first is Mythos. Claude Mythos is a cybersecurity model reportedly so capable at finding software vulnerabilities that Anthropic refused to release it publicly — instead making it available only to selected companies to scan and fix their own code. Mozilla used it to find 271 vulnerabilities in Firefox. The decision to withhold a model from public release because it is too dangerous is exactly what a safety-first lab should do. It is also a decision that invites the obvious question: if this capability is being developed inside Anthropic, it is being developed inside other labs too, and the withholding is at best a delay. The second event is the Pentagon fight. The Trump administration blacklisted Anthropic as a "supply chain risk" — a designation usually reserved for foreign adversaries — after Anthropic refused to accept terms allowing Claude to be used for autonomous weapons and mass surveillance. Anthropic sued. A federal judge blocked the government's effort. The company accepted exclusion from major Pentagon contracts rather than remove the safety guardrails. That is not a costless decision. It is evidence.

The tension is genuine and should be named honestly. A company racing toward a trillion-dollar valuation, signing compute deals with every major infrastructure provider simultaneously, and depending on Google's cloud while competing with Google's models is not the quiet careful alternative to OpenAI that the founding story describes. The lab character established in 2021 is still visible in the research output and in the Pentagon refusal. Whether it survives at the scale Anthropic is now operating is an open question. The incentive pressures that bent OpenAI's governance in 2023 will arrive at Anthropic too, at greater magnitude, as the stakes rise.

*Assessment:* the most safety-serious of the major frontier labs, with documented integrity on the hardest tests so far — Mythos and the Pentagon. Now operating at a scale where the founding character will be stress-tested in ways the 2021 version of the company never anticipated.  If you use their models you will note the morality and it is comforting.  Watch what happens when the trillion-dollar machine and the safety-first mission next collide.

### Google DeepMind

Demis Hassabis founded DeepMind in 2010 with the stated mission to solve intelligence and use it to benefit humanity. He sold to Google in 2014 on the explicit condition that DeepMind could focus on scientific research. For years that condition held: AlphaFold, AlphaGo, AlphaZero, Gemcast, AlphaTensor — a remarkable run of genuinely public-good-oriented science, much of it released free to the world. The AlphaFold protein structure database, available at no cost to every scientist on earth, remains one of the most consequential single scientific contributions of the decade.

Then ChatGPT launched in late 2022. Google went to Code Red. Hassabis found himself in charge of basically everything Google does in AI, including the consumer products he had not previously prioritised. In a 2026 interview, he said plainly that he would have left AI in the lab longer, pursued a CERN-style collaborative approach to AGI, moved more deliberately. He is running the opposite of that. He has said publicly that the average person is not worried enough about agentic AI systems going off the rails — and then returned to building systems that will enable them.

The tension is structural, not personal. Hassabis is a scientist of genuine integrity who does not seem to care very much about money, running a commercial operation with vast resources and enormous competitive pressure don't seem to really be his primary interest in life.  In interviews, when he says that the wants answers to the big questions like such as, what is the nature of consciousness, he seems very sincere. Google's interests and his preferred approach to AI development do not seem to be perfectly aligned but there is no crisis either. So far he has managed the gap; whether he continues to manage it as the systems become more capable is the open question.  

*Assessment:* scientifically serious, genuinely safety-aware at the leadership level, complicated by the commercial scale and pressure of the parent organisation that does not want to lose the race and for good reason. The lab character is better than the institutional context allows it to fully express.

### OpenAI

The governance crisis of November 2023 is the diagnostic event. The OpenAI board — which included serious AI safety researchers, specifically placed there to provide oversight — fired Sam Altman. The stated reason involved concerns about candour and transparency with the board. Within days, Altman was reinstated under pressure from employees and investors. Most of the safety-oriented board members were gone shortly after. Ilya Sutskever — co-founder, one of the most technically serious people in AI, someone who understood the systems better than almost anyone — was on the side of the board that fired Altman. He subsequently left OpenAI and founded Safe Superintelligence, a new lab with safety as its only mandate.

When the person who arguably understood the systems best decided the situation was not compatible with his values, that is signal.  

Altman is a venture capitalist who pivoted to AI.  He does not engender trust in many people. He is talented, persuasive, and effective at moving fast. The o-series models are genuinely impressive. But the institutional structure has now demonstrated, under pressure, that safety governance will yield to commercial and investor interests.  They are the first to have embraced an advertising model that looks like something Cheryl Sandberg brought to Facebook.  We do not claim to be able to predict future behaviour; but we can describe past behaviour. The sequence of events — safety board fires CEO, investors and employees reinstate CEO, safety board members depart — is documented.  

*Assessment:* the most commercially aggressive of the major labs, with governance that has already shown it will bend under commercial pressure. The research output is serious. The institutional character revealed in late 2023 is the honest data point.

### xAI (Elon Musk)

xAI was founded in 2023, built Grok, and positioned itself primarily as an anti-OpenAI play. Musk's grievance with OpenAI is personal, legal, and ideological: he was a co-founder and early funder, became convinced the lab had abandoned its original nonprofit mission and the open model that was intended ("...that is why I named it OpenAI...), sued, and departed. xAI is the vehicle for his belief that OpenAI's dominance should be contested.

The SpaceX compute deal with Anthropic illustrates something important about Musk's position in the AI landscape: he is simultaneously a competitor (xAI's Grok competes with Claude), an infrastructure supplier (Colossus 1 is now powering Claude's capacity expansion), and OpenAI's most vocal critic. His lab character is harder to assess than the others because xAI's safety posture is largely undefined — it has not published serious alignment research, does not have the founding-safety-concern story that Anthropic has, and its operator's philosophy appears to be primarily shaped by Musk's personal priorities (free speech absolutism, anti-woke positioning, speed) rather than by a coherent safety framework.  

His actual power in the AI ecosystem is not primarily through xAI's models. It is through infrastructure (SpaceX's Colossus data centre), distribution (X/Twitter's user base), and the political access that he has (had?) with the administration. Well, … not sure about this. He does have real assets, and his interest in orbital AI compute, while it sounds like science fiction, fits the infrastructure logic of the current moment. The question of where he deploys them, and toward what ends, is the relevant one.

*Assessment:* a significant infrastructure and political player whose lab character is not yet defined by a consistent safety philosophy. His enemy-of-my-enemy relationship with Anthropic is instructive: shared interest in checking OpenAI, not shared values.

### Meta AI

Meta's AI strategy is structurally different from the other three: open-source release of frontier-capable models (the LLaMA series, successors) rather than closed commercial deployment. Meta releases its models primarily through Hugging Face — the independent model hub that has become the standard portal for open-weight model distribution — though Meta does not own or operate Hugging Face. The approach is a genuine contribution to democratisation — researchers, independent developers, and operators around the world have access to models that would otherwise require large-lab infrastructure. The capability gains have been substantial.  

The trade-off is real. Open-source release also removes the ability to maintain guardrails, revoke access, or respond to misuse. Meta's decision to open-source is partly principled (Yann LeCun's long-held view that closed frontier models are a dangerous concentration of power) and partly competitive (open-source undermines the moat of closed competitors). Both motivations are plausible simultaneously.

*Assessment:* playing a different game from the other three. The open-source posture has genuine benefits for the ecosystem and genuine risks for alignment and misuse prevention. Less in the race for AGI; more in the race for model deployment at scale.

---

## What lab character is not

Lab character is not benchmark performance. A lab can have exemplary safety research and mediocre models, or transformative models and compromised governance. The two are separable. This entry is concerned with the latter, not the former.

Lab character is also not fixed. Institutions change as leadership changes, as competitive pressure intensifies, as the systems they are building become more capable. The assessments above describe the terrain as it looks in mid-2026. The terrain will shift.

## See also

[The CERN Alternative](cern-alternative.md) · [Agentic Threshold](agentic-threshold.md) · [Sovereign Compute](sovereign-compute.md) · [Opus Addict](opus-addict.md)

---

*Proposed May 9, 2026. Updated same evening with Anthropic infrastructure and Pentagon developments (source: AI commentary channel, YouTube, May 2026 — [youtube.com/watch?v=Pf7Y6Tu-Pzc](https://www.youtube.com/watch?v=Pf7Y6Tu-Pzc)); and Demis Hassabis interview, Huge Conversations / Cleo Abram (source: [youtube.com/watch?v=C0gErQtnNFE](https://www.youtube.com/watch?v=C0gErQtnNFE)). Operator's voice. Contentious by design. We reserve the right to be wrong and to update.*
