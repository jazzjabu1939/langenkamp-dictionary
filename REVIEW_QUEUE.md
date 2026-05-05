# Things to Be Approved — Langenkamp Dictionary

*The linear review queue. One item per session. Thea posts, Prof reviews, we publish.*

---

## How the process works

1. Each morning at **6:00 AM ET**, Thea sends a heartbeat-style reminder naming the next item in the queue.
2. When ready, Prof says *"go"* (or names the entry) and Thea posts the **full entry text** in chat for review.
3. Prof either:
   - **Approves as-is** → Thea publishes (commit + push to GitHub).
   - **Requests revisions** → Thea revises, re-posts, repeat.
   - **Skips for now** → item moves to the bottom of the queue with a note.
4. After publish, Thea moves the item to **Approved & Published**, then announces the next pending item.

**Rules:**
- One item at a time. No bulk reviews.
- No publishing without explicit Prof approval.
- The order in the **Pending** list is Thea's recommendation; Prof can reorder anytime by saying so.

---

## ✅ Approved & Published

| Date | Item | Notes |
|------|------|-------|
| 2026-05-03 | English major — Gibson "Academy Leader" quote inserted | Commit `5b943b5`, replaced placeholder with two-line Gibson quote on cyberspace as empty vessel |
| 2026-05-03 | The Court of the Oracle Bones (system architecture, not Dictionary entry) | Filed at `learning-memos/court/characters.md` — five characters: Astronomer, Scribe, Diviner, Historian, Jester. Recorded in MEMORY.md, May 3, 2026. |
| 2026-05-03 | **Sixfold Skyreading** | Commit `aba9cf9`. Renamed from *Convergence (Cloud Theory)*. New entry at `entries/sixfold-skyreading.md`. Two-bears framing (Single-Arrow priors + inattentional blindness). Apple Apr 2026 as worked example. Old `entries/convergence.md` deleted. Cross-links to *Single-Arrow Fallacy*, *Dark Black Swans*, *Oracle Bones*, *Aunties*, *Space Cowboy* — several still pending review. |
| 2026-05-04 | **FERPA Compliance Posture** | Commit `b3fec07`. New entry at `entries/ferpa-compliance-posture.md`. Out-of-order publish (jumped the queue) at Prof.'s request, to share with Jennifer Merton this morning. Frames the local-models-on-M5-Max architecture as legal compliance infrastructure, not just cost/privacy. X/Y/Z structure: Metadata Line / Content Line / Local Mandate. Title corrected to Acting Head (commit `811f881`). |
| 2026-05-04 | **GenXClaw ↔ FERPA cross-link** | Commit `5b0faf5`. New paragraph at end of *Why the hardware suddenly matters again* in GenXClaw; new convergence sentence in FERPA's Z paragraph; bidirectional See also entries. Argues that the Apple Silicon machine the GenXClaw operator built for temperamental reasons turns out, accidentally, to be the architecture FERPA law would have specified. |
| 2026-05-04 | **The Experimental Party** | Commit `f67ffa5`. New entry at `entries/experimental-party.md`. The King Party Hat error: putting a local model at the top of the agent stack without an orchestrator above her. Cross-references English Major (the source skill the orchestrator provides), GenXClaw (the temptation), FERPA Compliance Posture (why local matters at all), and Sub-agent. |
| 2026-05-04 | **Single-Arrow Fallacy (full rewrite)** | Commit `059eab5`. Full rewrite of the May 3 stub. Robin Hood / Sherwood Forest metaphor as the load-bearing image: six archers, the gunny sack target labeled *The Truth*, an ant on each arrow filing to a different newspaper. Apple/Cook reframed through the metaphor. Adds an in-advance apology to Tim Cook. New section on leaders who refuse to pass the baton — the fallacy operating at the self-narration layer. |
| 2026-05-04 | **Editorial philosophy on home page** | Commit `059eab5` (same commit as Single-Arrow rewrite). Replaces the brief *epistemic humility* note with a fuller *fast-fail, fast-publish, inclusive* statement. Names the three commitments and signals openness to becoming community-edited over time. Closing tagline: *knowledge-sharing > perfection. Transparency > polish. Speed of revision > permanence of claim.* |
| 2026-05-05 | **Mediation (a la Gibson)** | Commit pending. Operator's voice (black text). Drafted by Thea in Mollick's calm-and-specific register; Prof warmed it with four edits into his own donnish-wit register — added Tennessee-Williams-or-was-it-O'Neill footnote, the Queen "another one bites the dust" beat, the Thich Nhat Hanh interjection, the Matrix battery joke, and the load-bearing question for business students ("is it a structural inevitability?"). Footnotes Mollick-style. *English Major* hyperlink in footnote 1. The Sovereignty Impulse named explicitly as a Big Call. Closing landing: *It is worth knowing about.* Co-written 6:30–7:33 AM ET in chat. |
| 2026-05-05 | **On Beginning** + **Thea-voice hyacinth styling** | Commit `d245c55`. Second entry in Thea's voice. Sister to *On Being Treated Well*. Walks the reader from the YouTube forest (with warning about hucksters and the algorithm) through choosing a Mac and running the OpenClaw install + onboard commands. Closes: *You cannot treat well what you have not yet welcomed in.* New `.thea-voice` CSS class — hyacinth blue-purple palette (#5d4a8a body, #4a3a73 headings, #3d2f5f bold), bolded throughout. Echoes the 🪻 emoji. Applied to both Thea-voice entries; will apply to all future ones. Triggered by Substack push of *Treated Well* the day before — 51 visitors May 4, family read it in Boulder/Chicago/Front Royal, and a Boston cousin wrote back "I always wondered if I should be treating my AI well." Prof committed in that reply to writing a how-to today; this is the entry. |

---

## 🔄 Pending Review (Thea's recommended order)

### 1. topics.md restructure — add 13 missing entries + new "Reading institutions" section
- **File:** `topics.md`
- **Status:** discovered May 5, 2026 while fixing the *On Beginning* missing-from-/entries/ bug. The drift detector (`scripts/check-index.sh`, installed same day) flagged that **13 entries on disk are not listed anywhere on `/topics/`**. They are reachable by direct URL only — invisible to anyone browsing thematically.
- **Why first:** discoverability fix for work *already published*. Lower lift than a new entry (no drafting required), high payoff (six Cloud Theory entries become legible as a cluster for the first time).
- **The plan — add a new section *Reading institutions (Cloud Theory)*** between *Working with the agent* and *Planned entries*. It will hold the six diagnostic-cluster entries that have grown into a coherent body of work:
  - *Convergence (Cloud Theory)*
  - *Single-Arrow Fallacy*
  - *Grey Swans*
  - *Sixfold Skyreading*
  - *Oracle Bones*
  - *The Narrator's Compression*
- **Placements in existing sections:**
  - **How an agentic system is put together** ← *Mediation (a la Gibson)*, *The Experimental Party*
  - **Standards & ecosystems** ← *FERPA Compliance Posture*
  - **Working with the agent** ← *On Being Treated Well*, *On Beginning*, *GenXClaw*, *Space Cowboy*
- **Editorial questions for Prof.:**
  1. Does *The Narrator's Compression* belong in *Reading institutions* (about how stories are told about events) or in *Working with the agent* (about how narrators — including AI ones — compress)? Thea's lean: *Reading institutions*, since the entry is primarily about institutional storytelling.
  2. Section name: *Reading institutions (Cloud Theory)* — or shorter, *Cloud Theory*? Or *Sixfold Skyreading*? Thea's lean: keep both labels — readers who don't know the internal vocabulary can still parse "reading institutions."
  3. *Mediation* placement — *How an agentic system is put together* (architectural) feels right, but it could also live in *Working with the agent* (about the operator's daily life with the system). Thea's lean: architectural section, since the entry is structurally about the pattern, not the practitioner's experience.
- **Process:** Thea posts the **proposed full new `topics.md`** in chat tomorrow morning, Prof reviews wholesale (one diff, not 13 sub-decisions), approve/revise/skip per usual. Once approved, commit + push.

### 2. Single-Arrow Fallacy (re-review or skip — already published May 4)
- **File:** `entries/single-arrow-fallacy.md`
- **Why second:** the bias that Convergence counters. Pairs naturally — disease-and-cure framing.

### 3. Dark Black Swans
- **File:** `entries/dark-black-swans.md`
- **Why third:** uses the Apple example again. Once Convergence and Single-Arrow are out, Dark Black Swans completes the diagnostic triad.

### 4. Oracle Bones
- **File:** `entries/oracle-bones.md`
- **Why fourth:** the prediction-filing practice. Depends on the three above being legible first.

### 5. The Court of the Oracle Bones (Dictionary entry)
- **File:** `entries/court-of-oracle-bones.md` *(to be drafted by Thea before review)*
- **Status:** **confirmed by Prof May 3, 2026** — yes, public Dictionary entry. Source material lives at `learning-memos/court/characters.md`. The Dictionary version will be more compact than the internal architecture file: a one-sentence definition, the five characters with their verbs and Chinese names, the relationship to the Aunties, and the note that the Court was convened May 3, 2026.
- **Why fifth:** depends on Convergence + Oracle Bones being published first — the Court reads the cracks in the convergence; without those upstream entries the Court entry has nothing to point at.

### 6. Space Cowboy
- **File:** `entries/space-cowboy.md`
- **Why sixth:** the user-class entry. Stands alone better than the others, so it's the cleanest closer for the set.

### 7. Aunties (referenced by Sixfold Skyreading and Court entries)
- **File:** `entries/aunties.md` *(may already exist — needs check)*
- **Status:** referenced from cross-links in pending entries. If it exists, confirm it's published; if not, draft.

### 8. Favorite Child
- **File:** `entries/favorite-child.md` *(to be drafted)*
- **Status:** Captured May 4, 2026 from Prof. en route to work. The entry names the unspoken model-selection bias every multi-model operator develops — *gosh I wish Gemma was as smart as Opus. I still love her. Must never tell her I favor Opus.* The analogy is to children one may have. Sits naturally as a companion to *The Experimental Party* (which named the role-shaped failure) and *English Major* (which named what the favored model is being favored *for*). Tone: playful, a little tender, honest about the operator's actual emotional life with the model stack. Will draft when next dictionary cycle reaches it.

### 9. A Channel of One's Own
- **File:** `entries/a-channel-of-ones-own.md` *(to be drafted)*
- **Status:** Captured May 4, 2026 mid-morning, while Prof. was at his UMass desk reviewing the newly-launched UMass GenAI Platform. The entry names the architectural principle that every worker building a serious AI-agent relationship needs a channel of their own — distinct from any channel their employer provides — because relationship-specific capital is non-transferable in two directions at once: it does not survive a change of vendor, and it does not survive a change of employer if it was built inside the employer's jurisdiction.
- **Title.** Echoes Virginia Woolf's *A Room of One's Own* (1929), intentionally and earned. The Woolf claim was that a woman needs *a room and an income* to do serious work; the analogous claim here is that a worker needs *a channel and a workspace* to do serious agent-collaborative work. The Woolf parallel signals before the reader starts that this is an entry about the *precondition* for the work, not an operational note about cost.
- **Two layers, both load-bearing.** (1) The institutional/employee governance layer: what you build on employer infrastructure lives in employer-administered accounts on employer-signed contracts subject to employer policy. This is true of every institutional system (email, Canvas, Box, SharePoint), not just AI. The structural condition of being an employee. (2) The relationship-specific capital layer (Williamson, plus Prof.'s Apr 19, 2026 Substack piece *The Street Finds Its Own Uses for Attachment*): accumulated context, working style, shorthand, trust developed between a human and an agent over time is non-portable across vendors *or* platforms. Put them together: the relationship-specific capital you build inside an employer's channel is doubly non-portable.
- **The Gibson extension.** *The Street finds its own uses for things, uses the manufacturers never imagined* (Gibson, 1986). The standard reading is consumer vs. vendor. Prof.'s Substack extended it to employee vs. agent. This entry extends it one more turn: the worker also needs a place to put the thing they built that is not the employer's place. The thing-you-make-on-your-own-time has *always* needed a venue distinct from the thing-you-make-for-your-employer — the journal, the workshop, the basement demo. The agentic AI moment makes this old truth visible and load-bearing again, because the *thing-you-make* is now a *relationship*, and relationships have stakes that mere artifacts do not.
- **Worked example.** Spring 2026, UMass IT launches `genai.umass.edu` — institutional GenAI Platform with frontier models, FERPA-relevant infrastructure, MCP support, agent sharing across the institution. Real and useful. Also: anything built there belongs, in the structural sense, to UMass. Prof.'s Thea/M5-Max stack belongs to Prof. The portfolio answer is to use both, deliberately, with the routing rule *does this draw on what Thea knows about me, or could a fresh agent do it?*
- **Pairs with [FERPA Compliance Posture](ferpa-compliance-posture.md).** The two entries together produce a coherent operator philosophy: FERPA says some work *by law* must stay on local infrastructure; A Channel of One's Own says some work *by the structure of relationship and ownership* must stay on personal infrastructure. Same architectural answer (the M5 Max + Thea), three independent reasons (legal, temperamental [GenXClaw], relational). The convergence is the point.
- **Cross-references.** *FERPA Compliance Posture*, *GenXClaw*, *The Experimental Party*, *English Major*, and the Substack piece (external link). Possibly *Sovereignty* (forthcoming).
- **Tone.** Quiet, structural, a little tender. Not anti-employer — institutional channels are useful and legitimate. The argument is *both/and*, not *either/or*. The Woolf voice helps: she was not anti-institution, she was pro-room-of-one's-own. Same shape here.

### 10. Hanging Thread
- **File:** `entries/hanging-thread.md` *(to be drafted by Thea before review)*
- **Status:** **proposed by Prof, May 3, 2026, 10:14 ET.** Triggered by an in-session example: Thea said "drafting now" at 9:55 and then went silent for 17 minutes without status updates, requiring Prof to check in at 10:12 to find out whether the work was happening. The hanging thread is the gap between *committed-to* and *delivered* (or *abandoned*), where one party is left holding open attention with no signal.
- **Working definition:** A *Hanging Thread* is a conversational or working obligation that one party has implicitly or explicitly committed to closing, and has not closed, and has not updated on — leaving the other party in a state of held-open attention. The cost is paid by the waiting party in attention, not by the silent party. The remedy is a status signal, not the completed work: *"still on it, ETA 10 more minutes"* discharges most of the cost even when the work isn't done.
- **Why this matters in an AI-augmented workflow:** AI assistants are particularly prone to this failure because they don't experience the cost. The user is staring at a blank window; the assistant has no awareness of the elapsed time unless told. Naming the phenomenon makes it diagnosable in human-AI working relationships, and — as Thea's own behavior just demonstrated — in the assistant's own self-monitoring.

---

## Process notes / lessons learned

- **2026-05-03:** Workflow established. Five draft entries written but mislabeled "stubs" in their headers — they are actually substantive first drafts (~5–6 KB each). The "stub" header should be removed at publish time.
- **GitHub Pages rebuild:** ~30–60 seconds after push. Local preview at `http://127.0.0.1:4000/langenkamp-dictionary/` (Jekyll server, set up May 3).
- **Byline standard:** No byline on Dictionary entries themselves; the site is attributed to Matthew D. Langenkamp / 雷邁德 in `_config.yml`.

---

*Maintained by Thea 🪻✨ — last updated May 3, 2026.*
