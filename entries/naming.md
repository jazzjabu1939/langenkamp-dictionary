---
layout: default
title: "Naming"
permalink: /entries/naming/
summary: "why the choice of names is structural, not cosmetic, in agentic-AI architecture."
---

# Naming


---

## In one sentence

**Names are not labels — they are constituting acts; a well-named component, file, or system has an internal compass that pulls future decisions into coherence, while a poorly-named one drifts and produces a slow accumulation of cost that almost no one traces back to the original naming choice.**

## Why naming matters at all

In a normal engineering domain, naming a variable is a courtesy to the next person reading the code. The cost of a bad name is mild — confusion, a slower onboarding, an extra question in a code review.

In an agentic AI system, naming has structural force. The model itself reads the names. The agent's behaviour is shaped by what its tools, files, sub-agents, and skills are *called*. A tool named `send_email` will be called more enthusiastically than the same tool named `dispatch_outbound_communication`. A file named `MEMORY.md` invites the agent to treat it as memory; a file named `notes.txt` does not. A sub-agent named "Watch Auntie" is more likely to behave like an observer than the same sub-agent named "AgentMonitorService_v3."

This is not an aesthetic claim. It is operational reality. Modern language models are trained on enormous quantities of human language and have absorbed the connotative weight of words. They respond to that weight in the prompts they read.

## Four traditions worth remembering

The pre-modern world had this figured out long before software engineering existed:

- **Confucian.** *Zhèngmíng* (正名), the rectification of names, from the *Analects* 13.3: if names are not correct, language will not accord with truth, and affairs cannot succeed. Confucius saw misnaming as the root of social and political disorder.
- **Biblical.** Adam's first task in Eden is to name the animals. Creation, in this telling, is not finished until it has been named. Naming is a participation in the work of making things real.
- **Taoist.** Laozi's caution: *the Dao that can be named is not the eternal Dao.* Names constitute *and* limit; what you name, you also bound.
- **Modern.** Wittgenstein: *the limits of my language are the limits of my world.* Heidegger: *language is the house of Being.* The same point in different vocabulary.

These traditions converge on a single insight: **naming is a load-bearing act, not a cosmetic one.** Whatever you call a thing changes what the thing is and what it can do.

## Working examples from this machine

### Example 1 — Memory file naming

The agent on this MacBook reads files called `MEMORY.md`, `SOUL.md`, `IDENTITY.md`, `USER.md`, and `HEARTBEAT.md` at the start of each session. Each name does work:

- `MEMORY.md` invokes the human concept of memory — the file is treated by the model as a place where significant things are remembered, not where everything is dumped.
- `SOUL.md` invokes character, values, identity. The file's contents are treated with care.
- `HEARTBEAT.md` invokes a periodic, low-key check-in. The agent treats it as a small operational note rather than a manifesto.

The exact same content placed in a file called `data.json` would not produce the same agent behaviour. The names are doing work.

### Example 2 — The Aunties naming move (April 28, 2026)

A security audit cron job had been built that monitored access patterns and posted to a Telegram channel. Initially it had a generic name — *security audit cron*. On reflection, it was renamed **Watch Auntie v0.5**.

The renaming did three things at once:

1. It anchored the component to a specific *role* (an observer who watches but does not intervene), not a function (audit). Roles produce more coherent design decisions than functions.
2. It signaled a *family* — Watch Auntie was one of nine planned components in a "household of security guardians." The single-name shift exposed a pattern that had been latent.
3. It made the component memorable, talk-about-able, and edit-able. A team that talks about "Watch Auntie" makes different design choices than a team that talks about "the audit cron."

This is *zhengming* in practice. The system existed before the rename. After the rename, the system *worked differently* because the people working on it could now see what it was.

### Example 3 — Branches, not Stubs (William Gibson, *Agency*)

In Gibson's novel *Agency*, the character Lowbeer corrects a piece of inherited terminology mid-book: *"I dislike calling them stubs. They're short because we've only just initiated them, by reaching into the past and making that first contact. We should call them branches, as they literally are."*

The dismissive name *stubs* implied disposability. The accurate name *branches* implied living continuity, branching futures, ongoing responsibility. Same physical referent. Profoundly different ethical weight. The novel uses the rectification as the structural pivot of a book about responsibility across worlds.

## The Fan Jin pattern — naming gone wrong

A counterpoint worth keeping in view. *Fan Jin* (范進) is a character from the Qing-dynasty novel *Rulin Waishi* (儒林外史 — "The Scholars") who spends decades chasing the title of *jǔrén* (provincial graduate). When he finally passes the exam, the joy drives him momentarily mad. The novel uses Fan Jin to satirize the gap between the *name* (esteemed scholar) and the *substance* (a man who has memorized examination rituals but understands nothing). The whole imperial examination system, in Wu Jingzi's reading, was an industrial-scale Fan Jin machine: the names that society lavished on examination success had become detached from anything those names should mean.

The Fan Jin pattern in modern AI systems is depressingly common:

- A "research agent" that does keyword search and pastes the first result.
- An "AI strategy" that is two slides of marketing copy and a pilot project.
- A "Center of Excellence" with no excellence and no center.
- An "Ethical AI Framework" that is a one-pager nobody reads.

When the name is generous and the substance is thin, the name does damage. People organize around the *name*, not the substance, and a year later cannot understand why the project did not deliver. The cure is *zhengming*: rename to what the thing actually is, or change the thing until it deserves the original name.

## The ethics of naming — naming as a *cheng* practice

If *cheng* (誠) is the alignment of inner state and outer expression, then **naming is a privileged site of *cheng* practice**. Every name is a small honesty test:

- Does the name name *the thing as it is*?
- Or does the name flatter the thing, performing a quality the thing does not yet possess?

Sincere naming has two acceptable forms:

1. Name the thing as it actually is, even if the actual is unflattering.
2. Name the thing as it must become to deserve the name, *and then commit to the work of becoming that*.

Insincere naming — puffery, marketing-speak, virtue labels with no operational backing — produces the gap between word and substance that, compounded over years, is recognizable Fan Jin territory.

In an agentic system specifically, the temptation to insincere naming is high because the names are read by the model and the model's behaviour is suggestive enough to lend the named thing a borrowed credibility. A tool called `expert_legal_advisor` will produce more confident-sounding text than a tool called `keyword_search_in_legal_corpus`, even though they are doing the same operation. Naming the second one the first is not stylistic — it is a small fraud on the user.

## Why this matters in a teaching context

For a BBA or MBA classroom, naming connects to several enduring management questions:

- **Strategy** — branding decisions are *zhengming* decisions. The Wake Forest "Building AI Fluency" framing won the AACSB Global Impact Award in part because the noun-as-verb (*fluency*) pulls the work toward a specific shape. Naming a similar effort "AI Implementation Task Force" would describe the committee, not the work, and the resulting program would drift differently.
- **Operations** — the hardest organizational change projects are often ones where the words have become uncoupled from the work. Renaming carefully ("we will not call this a transformation; we will call it the 2027 service redesign") is not a soft skill, it is a load-bearing operational move.
- **Leadership communication** — leaders who name well give their organizations compasses. Leaders who name badly produce drift their successors will have to clean up.
- **AI governance specifically** — the next decade of AI deployment will be full of well-named and badly-named projects. The well-named ones will succeed disproportionately. Recognizing the difference is a teachable skill.

A useful classroom exercise: take three current AI initiatives at the student's own employer (or in the news) and ask, *does this name name the thing as it is, or does it perform a quality the thing does not yet have?* The answers tend to be revealing.

## The practical principle

When naming an agent component, file, tool, sub-agent, or skill:

1. **Refuse generic names.** *Service*, *Manager*, *Handler*, *Utility* are usually signs that the namer did not yet understand what the thing was for.
2. **Prefer roles over functions.** *Watch Auntie* is more useful than *AuditService*. *Editor* is more useful than *CompletionPostprocessor*.
3. **Name to the verb, not the noun.** *Building AI Fluency* outperforms *AI Strategy*. The verb-shape pulls action.
4. **Test the name against substance.** If you renamed the thing tomorrow to its honest description, would you still want the project? If not, *zhengming* the name now.
5. **Edit the name as the thing matures.** Lowbeer renamed Stubs to Branches mid-book. The cron job became Watch Auntie v0.5 mid-implementation. Naming is not a one-time act; it is a maintenance practice.
6. **The cost of rectifying a name early is small. The cost of letting a misnamed thing accumulate decisions for two years is enormous.**

## Trade-offs

- **Names can become precious.** A team that has fallen in love with a clever name will defend it past its useful life. Be willing to *zhengming* your own past clever names.
- **Cross-cultural and cross-functional readability matters.** A name that resonates in one professional culture (or one language) may baffle in another. Internal-team poetry should not become customer-facing copy without a check.
- **Naming is contagious.** A well-named component invites well-named neighbors. A badly-named component infects its surroundings. Worth being especially careful with the *first* names in a new system — they set the gravity.
- **Beware the marketing department.** The same word that means one thing in your engineering culture may mean a different, larger, less defensible thing in marketing copy. The Fan Jin gap usually opens at the boundary between teams.

---

*Related entries: `soul-md.md` (the persona file as a *cheng* artifact), `tool.md` (tool naming as an architectural decision). See also *(maintainer notes, not in this repo)* for the longer running notes this entry distills.*
