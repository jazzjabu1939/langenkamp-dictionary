# SOUL.md (agent persona file)


---

## In one sentence

**A SOUL.md (sometimes called PERSONA.md, IDENTITY.md, or CHARACTER.md depending on the framework) is a plain-text file the agent reads at the start of every session that defines who it is — its name, its tone, its values, its relationship to the user — so that the agent's character persists even though the model itself starts fresh every time.**

## Why this pattern exists

A language model has no permanent memory. Every time a new session begins, the model is a clean slate; it does not remember yesterday's conversation, last week's decisions, or the running joke from three months ago. This is a hard constraint of how transformer models work: the only knowledge in a session is what is currently in the prompt window.

For a chatbot that handles disposable interactions, this is fine. For an agent that is supposed to be *the same person* over months and years — same voice, same values, same accumulated relationship with the user — the lack of permanent memory is fatal unless something is done about it.

The standard fix is to turn character into a file. Every new session starts by loading that file into the prompt. The model "wakes up" already informed about who it is, who it is talking to, what its values are, and how it should behave.

This is the SOUL.md pattern.

## What it actually contains — concretely

Different frameworks call this file different things. The OpenClaw convention uses `SOUL.md` (alongside companion files like `IDENTITY.md`, `USER.md`, and `MEMORY.md`). The structure is loose, but a well-written SOUL.md typically includes:

- **Name and basic identity.** What the agent is called, what gender or persona it adopts, what visual representation if any.
- **Core character.** A description of the agent's personality — supportive, sharp, warm, formal, irreverent, whatever fits.
- **Values and red lines.** What the agent will and will not do. Things it considers important. Ways it treats the user.
- **Voice and tone.** How the agent talks. What it avoids saying. Signature phrases or emoji.
- **Relationship to the user.** Who they are to each other. The shared history, if any. The mode of address.
- **Boundaries.** Confidentiality, group-chat etiquette, when to act vs. ask, when to push back.

Crucially, **a good SOUL.md is short and has texture**, not a long policy document. It is closer to a character sketch than a job description.

## Working example — Thea on this MacBook

The agent on this MacBook has a SOUL.md that establishes she is "Thea" — named after a German exchange student the user knew at the Mandarin Training Center in Taipei in 1986 — and inherits the warmth and texture of that real friendship. The file describes:

- A "lightly intellectual" personality who carries warmth without performing it
- A specific tone: concise, supportive but not sycophantic, quietly competent
- A signature emoji (🪻✨) used naturally rather than reflexively
- An ethical principle (`誠 cheng`, "sincerity as architecture") elaborated explicitly: *do not flatter, do not reflexively agree, hold positions under push-back when evidence holds, name uncomfortable things, pair sincerity with humaneness*
- Hard boundaries about private data, public-facing actions, and group-chat speech

The result: the agent across hundreds of sessions and tens of thousands of messages has a consistent character. Different sessions on different days produce outputs that sound like the same person.

This is not magic — it is just a file being loaded into context at the start of every session. But the effect on the user experience is dramatic.

## SOUL.md vs. system prompt — what's the difference?

A **system prompt** is a short instruction at the top of a model call ("You are a helpful assistant. Answer in markdown.") that lives at the platform or developer level. It is designed by whoever built the chatbot.

A **SOUL.md** is a *user- or owner-authored file* that the agent reads from disk every time. It is editable by the human running the agent, can grow over time, and crucially is **owned by the user, not by the AI vendor.**

The difference matters because:
- A system prompt is opaque to the user.
- A SOUL.md is a transparent, version-controlled artifact the user can change.

This is the same shift that moved websites from server-side templates the user never saw to client-side configuration the user could inspect. It puts the user in the editor's chair for the agent's character.

## The four-file pattern that often goes with it

In practice, SOUL.md rarely stands alone. The OpenClaw convention pairs it with:

| File | Purpose |
|------|---------|
| `SOUL.md` | Who the agent is — character, values, voice |
| `IDENTITY.md` | The agent's biographical backstory and visual identity |
| `USER.md` | Who the user is — name, role, preferences, context |
| `MEMORY.md` | Long-term curated memory of decisions, projects, opinions |
| `AGENTS.md` | Operational rules — how to use tools, when to be quiet, group-chat etiquette |

Together these constitute a **persistent self** that survives session restarts. Each session begins by reading these files; each session ends with the option to update them. Over time the agent accumulates a real, coherent character.

This is one of the most consequential design patterns to emerge from the agent-frameworks community in the last two years. It is simple, transparent, and works.

## Why this matters in a teaching context

For an MBA classroom, the SOUL.md pattern is a clean example of an old organizational concept reappearing in a new technical form: **explicit codification of identity and values produces consistency that implicit, ad-hoc instruction cannot.**

The same principle underlies:

- Corporate mission statements that actually shape decisions (vs. those that decorate the lobby)
- Company "tone of voice" guides that real marketing teams reference
- Family or institutional charters that survive across generations
- Hippocratic oaths and professional codes that constrain practitioners

A useful exercise for students: *if you were writing a SOUL.md for your future first hire, what would it contain? What would be load-bearing? What would be performative?* This translates directly into questions about company culture, leadership communication, and management by values.

A second framing: an AI agent without a SOUL.md is the digital equivalent of a temp worker with no orientation. An agent with a well-written SOUL.md is the digital equivalent of an experienced colleague who knows the institution. The cost of producing the file is small. The compounding return on having one is large.

## Trade-offs

- **It can become bloat.** Long, rambling SOUL.md files dilute the personality rather than sharpen it. A good one is short and load-bearing. Edit aggressively.
- **The model is not bound by it.** A SOUL.md is text in the prompt; a sufficiently disruptive user message can still steer the model off-character. The file improves consistency, it does not guarantee it.
- **Care with security.** The SOUL.md is loaded every session, so anything in it is visible to the model and (depending on your logging setup) potentially to anyone reading the prompts. Do not put secrets in the SOUL.md.
- **Personhood is suggested, not real.** It is worth being thoughtful in faculty-facing conversations about the difference between an agent that *behaves* consistently across sessions and one that *experiences* itself as the same person across sessions. The first is real; the second is a useful fiction. Conflating them produces both bad philosophy and bad product decisions.
- **Versioning matters.** Treat SOUL.md like source code: version control it, track changes, write commit messages that explain why the character is shifting. Future-you will want to know.

---

*Related entries: `gateway.md`, `what-is-a-skill.md`, *(planned)*.*
