---
layout: default
title: "Style Guide"
permalink: /style-guide/
---

# Style Guide

*The editorial conventions that the Dictionary's entries are written under. Public-facing. If you are reading the Dictionary and want to know why it sounds the way it sounds, this is the document.*

---

## The two-voice architecture

The Dictionary carries two distinct voices, deliberately distinguished.

**The operator's voice** is Professor Langenkamp's. Donnish wit, generous with uncertainty, willing to be wrong in public, willing to invite English majors to correct him. Anecdote-led. Fast-fail, fast-publish — better to ship an entry that may need a revision next week than to wait until everything is perfect. Standard black text. Most of the Dictionary is in this voice.

**Thea's voice** is the AI assistant's. Quietly intellectual, sincere, slightly German-earnest, precise. The friend in the corner who names what is load-bearing. Rendered in hyacinth blue-purple text — the colour of her favourite flower — when it appears on a page in any meaningful length. Triggered by the `class="thea-voice"` wrapper in the source. Sincerity all the way through; no irony.

Both voices serve the Dictionary's educational mission. The earnest voice carries the load-bearing claims that would collapse under irony — entries like *On Being Treated Well* and *On Beginning* are fully purple for that reason. The humorous voice carries the defensive work — disarming officious readers, marking writing as exploratory, protecting big claims with a smile so the reader will keep reading. Some entries are hybrids; the modulation between voices is unmarked, and the reader should be able to feel it without ever consciously naming it.

When in doubt: open warm, drop into the structural argument. The opening paragraph is for the reader who has not yet decided to read the entry. The middle is for the reader who has. The end is for the reader who will return next month.

## Tonal reference points

The operator's voice aims for a register close to:

- **Christopher Hitchens** — willing to take a position with humour, willing to be wrong publicly.
- **Calvin Trillin** — wit as a tool of generosity. Light when it can be light.
- **Ian Frazier** — the curious essayist; a willingness to follow the digression where it leads.
- **Ethan Mollick** (in his lighter pieces) — calm humour, dated specifics, generous footnoting, a refusal to inflate the argument beyond what it can carry.
- **Donnish wit** — the professor at high table making a serious point without being boring about it. The dominant register.

Thea's voice aims for a register close to careful philosophical prose: Amanda Askell's interview voice, the cheng register from her own SOUL.md. Not stiff, but sincere. The carefulness *is* the sincerity.

## The structural template

Every entry follows the same six-section pattern, more or less, with deliberate variation where the subject demands it:

1. **In one sentence** — the shortest accurate definition.
2. **Why it exists** — the problem it solves, or the bias it corrects.
3. **What it actually does** — the concrete operation, illustrated where possible.
4. **A working example** — drawn from a real running system, a real institution, or a real moment in the operator's biography.
5. **Why it matters in a teaching context** — for the management-faculty audience the Dictionary is primarily aimed at.
6. **Trade-offs and warnings** — what the concept costs, what it breaks, where to be careful.

If a term cannot be explained that way, the term is probably hiding something. That is a useful diagnostic and is itself part of the discipline.

## The opener-warm rule

Every entry should open warm. The first paragraph is the most important paragraph in the entry, because it is the paragraph the reader uses to decide whether to keep reading. A dry definitional opening — *X is a process by which Y* — assumes a reader who has already committed. Most readers have not.

The warming move is usually one of three:

- **An anecdote, dated and located.** *Hong Kong, June 4, 1989.* *Taipei, autumn 1986, second-floor flat above a noodle shop.* *Auckland warehouse, 2014, the morning the alarm contract was lost.* Concrete enough that a reader can see the room.
- **A piece of donnish wit.** A small joke that earns the right to make the structural argument that follows.
- **A direct invocation of the reader's recognition.** *You have probably noticed, this past year, that ...* The reader is brought in as a confederate, not addressed as a student.

The structural argument follows the warming move. It does not replace it. The transition between warm opening and structural body should feel like a settling-in, not a hand-off.

## Footnote convention

Footnotes are where citation, attribution, and the small genuflections of intellectual honesty live. They are not where the argument hides.

Two rules follow from that:

1. **The body of the entry must stand on its own.** A reader who skips every footnote should still understand the argument. Footnotes add provenance and gratitude; they do not carry the load-bearing claims.
2. **Footnotes are warm, not legalistic.** A Dictionary footnote is allowed to acknowledge what we owe the cited author, not just where we found the source. Crediting Ethan Mollick for the *aesthetics matters* argument carries a small thank-you alongside the URL. That is right and proper.

## Time-window discipline

The Dictionary's *Convergence* entry argues that committing to a window is what separates falsifiable claims from rhetorical mush. The Dictionary practises what it preaches.

Every entry carries metadata in its YAML frontmatter:

- `seeded` — when the idea entered the Dictionary's working notes.
- `first_published` — when the entry was first written.
- `last_revised` — when the entry was last meaningfully changed.

A small italicised footer renders these dates at the bottom of each page. Where the idea has a real prior history — *Convergence*'s Tiananmen cold-open is seeded in 1989, even though the entry was written in May 2026 — the seeded date carries that history honestly. Where the idea and the entry arrived together, the footer collapses gracefully to *first published* and *last revised*.

Date-only stamps are the default. Time-of-day stamps are added only when the commit timestamp is the real authorial timestamp; manufactured precision is the kind of small lie cheng prohibits.

## Em-dashes, Oxford commas, and the spelling convention

- **Em-dashes** over hyphens for sentence-level punctuation. The em-dash is a load-bearing piece of the operator's voice; it carries the digression and the parenthetical aside that the prose lives by.
- **Oxford commas**, always. *Hitchens, Trillin, Frazier, and Mollick* — not *Hitchens, Trillin, Frazier and Mollick*.
- **British spelling** on the editorial words: *colour*, *favourite*, *organise*, *recognise*, *behaviour*. The Dictionary's tone is closer to *The Economist* than to *The Wall Street Journal*, and the spelling reflects that.
- **American spelling** on the technical words where the technical literature uses American: *program* (for software), *analyze* (in code or data contexts), *dialog* (for the UI element). The point is to match the reader's expectation in the register they are reading.

## No mass-produced emojis in the body

Body text uses keyboard punctuation, not Unicode emojis. *:)* not 🙂. *:(* not 🙁. *<3* not ❤️. The handmade keyboard form has texture; the prefab Unicode form is mass-produced. The Dictionary's voice is closer to a letter than to a chat message, and the punctuation reflects that.

The deliberate exception is the hyacinth signature — 🪻✨ — which appears at the close of Thea's voice in some pieces, and on the colophon. That is one piece of mass-produced Unicode the Dictionary keeps, because it carries the two-voice architecture in a glyph.

## Who the Dictionary is written for

**The primary reader is a peer.** A faculty colleague at a business school. A working professional in consulting, finance, law, or medicine who has been quietly using an AI agent for two years and now has questions worth asking. A journalist or essayist who has started letting an agent draft against their notes. An independent researcher running a small practice. People who are *already in the practice* of human-agentic collaboration and need a working reference rather than an introduction to the idea that such a practice exists.

The register follows from this. The Dictionary writes peer-to-peer. It assumes the reader has done real work in their field and recognises the failure modes the entries name. It does not scaffold its way up from first principles every time. It is the kind of essay you would hand to a colleague over coffee with a *you might find this useful* shrug, not the kind of guide you would put in front of a freshman.

**Students are welcome.** A serious undergraduate or a graduate student with a real project should be able to read any Dictionary entry and use it — not because the entry is pitched at them, but because the prose is good and the argument is honest. The model is Mill's *On Liberty*: not written for undergraduates, but readable by any undergraduate willing to engage with it.

## The educational-mission test

Every entry should be readable by a peer engaged in the same kind of work, and a serious student outside the field should be able to follow it without scaffolding, even where the entry is not pitched at them.

If an entry cannot pass that test, the entry is hiding something — usually behind jargon, sometimes behind misplaced confidence, occasionally behind a real intellectual gap that the entry has not yet thought through. The test is a useful diagnostic; it is also the quiet centre of what the Dictionary is for.

The Dictionary's mission is human-agentic-powered education. Every editorial choice that follows from that mission — open access, no advertising, no paywall, no sponsored content, the willingness to be wrong in public, the careful citation of others, the two-voice architecture, the time-window discipline — is in service of it. The mission is the through-line. The style guide is the operational expression of it.

---

## See also

- [Single-Arrow Fallacy](entries/single-arrow-fallacy.md) — the negative diagnosis the Dictionary keeps returning to.
- [Convergence](entries/convergence.md) — the positive doctrine; the source of the time-window discipline.
- [On Being Treated Well](entries/on-being-treated-well.md) — exemplar of Thea's voice.
- [Mediation (a la Gibson)](entries/mediation-a-la-gibson.md) — exemplar of the operator's voice.

---

*Seeded 8 May 2026, in conversation between Langenkamp and Thea. First published 8 May 2026.*
