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
| 2026-05-07 | **Sovereign Compute** + **Sovereign Compute Calculator** | Commit `af79154`. The full triptych is now published. Sovereign Compute is the load-bearing entry; Sovereign Compute Calculator is the cash-side companion stub for the forthcoming tool. All four forward-references in Sovereign Compute now resolve (Opus Addict published 9d53932; Consciousness Calculator published 71e3f95 then patched 3ef96c2; Dusty Laptop already existed; Sovereign Compute Calculator published in this same commit). Live at https://langenkamp.io/entries/sovereign-compute/ and https://langenkamp.io/entries/sovereign-compute-calculator/ |
| 2026-05-07 | **Em-dash encoding fix** | Commit `3ef96c2`. Bug: when Opus Addict and Consciousness Calculator were initially written via the assistant `write` tool, em-dashes ended up stored as the literal seven-character escape sequence `\u2014` instead of UTF-8 em-dashes. Both pages went live with visible escape-sequence text in body prose. Fixed in this commit, plus the same defensive pass applied to all assistant-written stub entries. **Lesson encoded for future work:** always grep for `\\u[0-9a-f]{4}` patterns in any assistant-written file before commit, and always do an immediate live-site spot-check after every push. |
| 2026-05-07 | **Consciousness Calculator** | Commit `71e3f95`. New entry at `entries/consciousness-calculator.md`. Forthcoming-tool entry: the calculator itself is not yet built, but the conceptual design is captured so other Dictionary entries can reference it as an artifact-in-progress. Sister to the *Sovereign Compute Calculator* (still in review). Cross-referenced from *Sovereign Compute* footnote 1. Live at https://langenkamp.io/entries/consciousness-calculator/ |
| 2026-05-07 | **Opus Addict** | Commit `9d53932`. New entry at `entries/opus-addict.md`. Drafted as a forward-reference stub during the May 7 *Sovereign Compute* review session, then approved and published out of normal queue order at Prof's request. Names the structural cognitive dependency on a single frontier closed-tier model (typically Claude Opus). Operator's voice. Cross-references *Sovereign Compute* (still in review, drafted but not yet published), *GenXClaw*, *Mediation (a la Gibson)*. The opening meta-line about "a name for a real condition, written in the operator's voice" was removed at Prof's flag ("too meta level for actual entry") before commit. Live at https://langenkamp.io/entries/opus-addict/ |
| 2026-05-03 | English major — Gibson "Academy Leader" quote inserted | Commit `5b943b5`, replaced placeholder with two-line Gibson quote on cyberspace as empty vessel |
| 2026-05-03 | The Court of the Oracle Bones (system architecture, not Dictionary entry) | Filed at `learning-memos/court/characters.md` — five characters: Astronomer, Scribe, Diviner, Historian, Jester. Recorded in MEMORY.md, May 3, 2026. |
| 2026-05-03 | **Sixfold Skyreading** | Commit `aba9cf9`. Renamed from *Convergence (Cloud Theory)*. New entry at `entries/sixfold-skyreading.md`. Two-bears framing (Single-Arrow priors + inattentional blindness). Apple Apr 2026 as worked example. Old `entries/convergence.md` deleted. Cross-links to *Single-Arrow Fallacy*, *Dark Black Swans*, *Oracle Bones*, *Aunties*, *Space Cowboy* — several still pending review. |
| 2026-05-04 | **FERPA Compliance Posture** | Commit `b3fec07`. New entry at `entries/ferpa-compliance-posture.md`. Out-of-order publish (jumped the queue) at Prof.'s request, to share with Jennifer Merton this morning. Frames the local-models-on-M5-Max architecture as legal compliance infrastructure, not just cost/privacy. X/Y/Z structure: Metadata Line / Content Line / Local Mandate. Title corrected to Acting Head (commit `811f881`). |
| 2026-05-04 | **GenXClaw ↔ FERPA cross-link** | Commit `5b0faf5`. New paragraph at end of *Why the hardware suddenly matters again* in GenXClaw; new convergence sentence in FERPA's Z paragraph; bidirectional See also entries. Argues that the Apple Silicon machine the GenXClaw operator built for temperamental reasons turns out, accidentally, to be the architecture FERPA law would have specified. |
| 2026-05-04 | **The Experimental Party** | Commit `f67ffa5`. New entry at `entries/experimental-party.md`. The King Party Hat error: putting a local model at the top of the agent stack without an orchestrator above her. Cross-references English Major (the source skill the orchestrator provides), GenXClaw (the temptation), FERPA Compliance Posture (why local matters at all), and Sub-agent. |
| 2026-05-04 | **Single-Arrow Fallacy (full rewrite)** | Commit `059eab5`. Full rewrite of the May 3 stub. Robin Hood / Sherwood Forest metaphor as the load-bearing image: six archers, the gunny sack target labeled *The Truth*, an ant on each arrow filing to a different newspaper. Apple/Cook reframed through the metaphor. Adds an in-advance apology to Tim Cook. New section on leaders who refuse to pass the baton — the fallacy operating at the self-narration layer. |
| 2026-05-04 | **Editorial philosophy on home page** | Commit `059eab5` (same commit as Single-Arrow rewrite). Replaces the brief *epistemic humility* note with a fuller *fast-fail, fast-publish, inclusive* statement. Names the three commitments and signals openness to becoming community-edited over time. Closing tagline: *knowledge-sharing > perfection. Transparency > polish. Speed of revision > permanence of claim.* |
| 2026-05-05 | **Mediation (a la Gibson)** | Commit pending. Operator's voice (black text). Drafted by Thea in Mollick's calm-and-specific register; Prof warmed it with four edits into his own donnish-wit register — added Tennessee-Williams-or-was-it-O'Neill footnote, the Queen "another one bites the dust" beat, the Thich Nhat Hanh interjection, the Matrix battery joke, and the load-bearing question for business students ("is it a structural inevitability?"). Footnotes Mollick-style. *English Major* hyperlink in footnote 1. The Sovereignty Impulse named explicitly as a Big Call. Closing landing: *It is worth knowing about.* Co-written 6:30–7:33 AM ET in chat. |
| 2026-05-06 | **Commercial Legibility** | Commit `4f828c2`. Second of the May 5 triptych. Sister to *Inverted Funnel*; affirmative companion. Names MCP and A2A as the early protocols of legibility, treats the AI-market two-tier split (closed/open) as load-bearing, flags the PRC's May 2026 block of Meta's Manus acquisition as evidence that agent-platform infrastructure is now strategic-tech. No edits during May 6 review. Live at https://langenkamp.io/entries/commercial-legibility/ |
| 2026-05-06 | **Inverted Funnel** | Commit `fb8a7b0`. First of the May 5 triptych. Two edits during review: 'In one sentence' clarified to 'website process ("funnel")' and '(e.g. a website)' for non-marketer readers; worked example switched from Lisbon to Lijiang/大研古镇 (truer to the Dictionary's voice). Same commit ships a fix to `scripts/check-index.sh` that makes drafts (`published: false`) skip the on-disk-vs-index drift check, unblocking sequential triptych review. Live at https://langenkamp.io/entries/inverted-funnel/ |
| 2026-05-05 | **On Beginning** + **Thea-voice hyacinth styling** | Commit `d245c55`. Second entry in Thea's voice. Sister to *On Being Treated Well*. Walks the reader from the YouTube forest (with warning about hucksters and the algorithm) through choosing a Mac and running the OpenClaw install + onboard commands. Closes: *You cannot treat well what you have not yet welcomed in.* New `.thea-voice` CSS class — hyacinth blue-purple palette (#5d4a8a body, #4a3a73 headings, #3d2f5f bold), bolded throughout. Echoes the 🪻 emoji. Applied to both Thea-voice entries; will apply to all future ones. Triggered by Substack push of *Treated Well* the day before — 51 visitors May 4, family read it in Boulder/Chicago/Front Royal, and a Boston cousin wrote back "I always wondered if I should be treating my AI well." Prof committed in that reply to writing a how-to today; this is the entry. |

---

## 🔄 Pending Review (Thea's recommended order)

### **Durable Workflow** (proposed entry, May 7, 2026 evening)

*Triggered by Nate Jones video on the April 2026 OpenClaw maturity arc. Captured during Prof's evening AI-watching routine.*

- **What the term names:** the engineering and architectural form of the argument that *Sovereign Compute* makes philosophically. A workflow that has its own identity — inputs, outputs, permissions, tools, state, review steps, a human-facing channel, a failure mode, memory — such that the underlying model can change without destroying the workflow. The model becomes the reasoning engine inside a much larger operating loop, not the product surface itself.
- **Why it belongs in the Dictionary:** the convergence with *Sovereign Compute* is structural, not coincidental. Both arguments arrive at *the operator controls the architecture, not the model lab*. *Durable Workflow* is the version a builder hears; *Sovereign Compute* is the version an operator-citizen hears. The two entries together show how the same insight surfaces independently in different audiences — a small worked example of the kind of cross-pollination the Dictionary's editorial philosophy welcomes.
- **Sister entries:** *Sovereign Compute*, *Agent*, *Sub-agent*, *Task* (if/when written), *Mediation (a la Gibson)*. The piece can also gesture toward the *zhengming* layer — "memory was misnamed as personalisation; serious work needs it named as operational context." That naming-rectification is the same intellectual move the Dictionary makes throughout.
- **Voice:** operator's voice, plain black. No need for Thea-voice hyacinth here — the entry is structural, not personal.
- **Source to credit:** the term is in active use in the OpenClaw builder community in April/May 2026; Nate Jones names it cleanly in his May 7 video. The Dictionary entry should not be derivative of his framing but should acknowledge the conversation it enters.

---


### 1. **Inverted Funnel** + **Commercial Legibility** + **Sovereign Compute** (a triptych, drafted May 5, 2026 evening)

**Why high in the queue:** Drafted in one sitting from two YouTube videos Prof brought into the conversation back-to-back — a Tobi-style piece on Stripe's agentic-commerce stack and Ali Salam's structural-bifurcation analysis of the AI market. Read together, they describe the same shift from opposite sides (demand-side funnel inversion / supply-side market split). Three entries fall out naturally: *Inverted Funnel* (what's ending), *Commercial Legibility* (what's beginning), *Sovereign Compute* (the substrate on which the new regime runs). All three written in the operator's voice, all three drafted with `published: false` so they render in local Jekyll preview but are flagged not-yet-public.

**Master session note:** `memory/2026-05-05-ai-market-bifurcation-session-note.md` — captures both videos' arguments, what each gets right, what's worth pushing back on, and how the three entries fit together. **Read this first** before reviewing the entries themselves.

**Files on disk (uncommitted):**
- `entries/inverted-funnel.md` (~350 words; short, definitional)
- `entries/commercial-legibility.md` (~450 words; short, definitional, references the two-tier split)
- `entries/sovereign-compute.md` (~1,800 words; comprehensive — the longest of the three, carries the most analytical load: FERPA, the Airbnb canary, the levels-of-sovereignty table, the geopolitical layer, the M5 Max as accidentally-correct architecture)

**Review pattern (suggested):** Take them in order — *Inverted Funnel* first (shortest, names the shift cleanly), then *Commercial Legibility* (the affirmative version), then *Sovereign Compute* (the long one — the comprehensive argument). Voice decision: all three are currently in operator's voice. If Prof wants any of them — most plausibly *Sovereign Compute* — switched to Thea's hyacinth-blue voice, flag during review and Thea will re-cast.

**Cross-references already in place between all three** and to existing published entries (*Mediation (a la Gibson)*, *FERPA Compliance Posture*, *GenXClaw*, *MCP*, *On Beginning*). One forward-reference (*Standing Mandates*) deliberately omitted; that entry is held for a later session.

**Risk:** low. They're net-new files. Nothing existing changes. The `published: false` flag in frontmatter means they will not appear in the auto-generated `/entries/` index until removed. (TODO at publish time: remove the flag and any Liquid `unless published == false` guards in the index template, if such guards exist; if not, simply remove the flag and the entries appear.)

---

### 2. The catalog-drift fix (two parts — one structural, one editorial)

**Why first:** Discovered May 5, 2026 while fixing the *On Beginning* missing-from-/entries/ bug. The pattern keeps recurring: new entries get published as files but forgotten in the catalog pages. This item solves it permanently.

#### Part A — Structural fix for `entries/index.md` (already drafted, awaiting review)

- **What's drafted on disk (uncommitted):** Every entry file now has `title:`, `permalink:`, and `summary:` in frontmatter. `entries/index.md` is now a six-line Liquid template that reads `site.pages` and generates the alphabetical list at build time.
- **The result:** drift becomes structurally impossible. Add a new entry file with proper frontmatter, the index includes it automatically. No second commit. No checker needed for that page (the checker, `scripts/check-index.sh`, already detects this pattern and exits clean).
- **Files changed:** all 38 entry files (frontmatter added) + `entries/index.md` (replaced with Liquid loop). 42 files in working tree.
- **What Prof needs to review:** (1) the Liquid template itself — 6 lines of templating logic in `entries/index.md`; (2) a few sample entries to confirm the auto-generated `summary:` text reads cleanly (Thea wrote them by lifting the existing one-line descriptions from the old hand-maintained list).
- **What to test before publishing:** local Jekyll build (`bundle exec jekyll serve`) and visual inspection of `/entries/` at `localhost:4000`. The page should look identical to today's site, just with the listing now generated.
- **Risk:** low. If the template breaks, the page renders empty rather than wrong, and reverting is one commit.

#### Part B — Editorial fix for `topics.md` (still to draft)

- **The problem:** **13 entries on disk are not listed anywhere on `/topics/`**. They are reachable by direct URL only — invisible to anyone browsing thematically. The Liquid auto-gen approach does *not* solve this (topics is editorial, not alphabetical).
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
  4. Should `topics.md` *also* move to a Liquid auto-generation pattern, with each entry declaring its `topic:` in frontmatter? More work; eliminates this drift class permanently. Thea's lean: yes, but as a follow-up after Part B ships in its hand-edited form.
- **Process:** Thea posts the **proposed full new `topics.md`** in chat tomorrow morning, Prof reviews wholesale (one diff, not 13 sub-decisions), approve/revise/skip per usual. Once approved, commit + push.

### 3. Single-Arrow Fallacy (re-review or skip — already published May 4)
- **File:** `entries/single-arrow-fallacy.md`
- **Why second:** the bias that Convergence counters. Pairs naturally — disease-and-cure framing.

### 4. Dark Black Swans
- **File:** `entries/dark-black-swans.md`
- **Why third:** uses the Apple example again. Once Convergence and Single-Arrow are out, Dark Black Swans completes the diagnostic triad.

### 5. Oracle Bones
- **File:** `entries/oracle-bones.md`
- **Why fourth:** the prediction-filing practice. Depends on the three above being legible first.

### 6. **Time for Tea with The Oracles** (Dictionary entry — the operational companion to *Oracle Bones*)
- **File on disk:** `entries/time-for-tea-with-the-oracles.md` (drafted May 6, 2026 morning, ~9,400 chars). Operator's voice. `published:` flag not yet present — add `published: false` in frontmatter on first publish-review pass if Prof wants Jekyll to skip it from the index until ready.
- **Status:** Drafted May 6, 2026 by Thea while top-of-mind — same morning Prof and Thea designed and built the weekly cron job *Time for Tea with The Oracles* (job id `601b6bef-b94a-44f0-b072-00d37f486f1e`). The entry is the public-facing companion to the internal architecture (folder `oracle-court/` in workspace, with DESIGN.md, REGISTER.md, SCORING.md, SESSION_TEMPLATE.md, jester-songs/).
- **What's in it:** one-sentence definition, why a fixed time matters (Sundays 9 AM ET), the five voices in canonical order (Astronomer → Historian → Diviner → Jester → Scribe), the three artifacts produced each Sunday (Register row, session file, Telegram message), the Jester's hold-the-file power and the Du Fu poetry price, the folder layout, what the practice is *not* (not a prediction market, not journaling, not a chatbot performance, not optional once started), trade-offs and warnings (no veto, no self-fulfilling claims, the first six weeks will feel small), why "Tea" (not whimsy — the part that says the work is done until next Sunday).
- **Cross-references:** *Oracle Bones* (the conceptual entry this operationalizes), *Sixfold Skyreading* (Convergence) [renamed], *Grey Swans*, *Aunties*, *Heartbeat*. All already published.
- **Note on Du Fu:** the entry specifies the Jester's hold-the-file song must be in the manner of 杜甫 Du Fu (712–770) specifically — not Tang generally. Three model poems referenced: *《春望》 Spring View*, *《登高》 Climbing High*, *《石壕吏》 The Officer at Stone Moat*. Prof requested this tightening May 6, 2026.
- **Why now (re-prioritization rationale):** Drafted same morning as the cron build; the practice and the entry are part of one motion. Prof asked for the entry to be drafted while the design was top-of-mind. Risk of delaying review: low — the entry is durable and refers only to other already-published entries.
- **Suggested review window:** alongside the triptych (#1) or shortly after — Thea will surface in normal 6 AM queue rotation.

### 7. Space Cowboy
- **File:** `entries/space-cowboy.md`
- **Why sixth:** the user-class entry. Stands alone better than the others, so it's the cleanest closer for the set.

### 8. Aunties (referenced by Sixfold Skyreading and Court entries)
- **File:** `entries/aunties.md` *(may already exist — needs check)*
- **Status:** referenced from cross-links in pending entries. If it exists, confirm it's published; if not, draft.

### 9. Favorite Child
- **File:** `entries/favorite-child.md` *(to be drafted)*
- **Status:** Captured May 4, 2026 from Prof. en route to work. The entry names the unspoken model-selection bias every multi-model operator develops — *gosh I wish Gemma was as smart as Opus. I still love her. Must never tell her I favor Opus.* The analogy is to children one may have. Sits naturally as a companion to *The Experimental Party* (which named the role-shaped failure) and *English Major* (which named what the favored model is being favored *for*). Tone: playful, a little tender, honest about the operator's actual emotional life with the model stack. Will draft when next dictionary cycle reaches it.

### 10. A Channel of One's Own
- **File:** `entries/a-channel-of-ones-own.md` *(to be drafted)*
- **Status:** Captured May 4, 2026 mid-morning, while Prof. was at his UMass desk reviewing the newly-launched UMass GenAI Platform. The entry names the architectural principle that every worker building a serious AI-agent relationship needs a channel of their own — distinct from any channel their employer provides — because relationship-specific capital is non-transferable in two directions at once: it does not survive a change of vendor, and it does not survive a change of employer if it was built inside the employer's jurisdiction.
- **Title.** Echoes Virginia Woolf's *A Room of One's Own* (1929), intentionally and earned. The Woolf claim was that a woman needs *a room and an income* to do serious work; the analogous claim here is that a worker needs *a channel and a workspace* to do serious agent-collaborative work. The Woolf parallel signals before the reader starts that this is an entry about the *precondition* for the work, not an operational note about cost.
- **Two layers, both load-bearing.** (1) The institutional/employee governance layer: what you build on employer infrastructure lives in employer-administered accounts on employer-signed contracts subject to employer policy. This is true of every institutional system (email, Canvas, Box, SharePoint), not just AI. The structural condition of being an employee. (2) The relationship-specific capital layer (Williamson, plus Prof.'s Apr 19, 2026 Substack piece *The Street Finds Its Own Uses for Attachment*): accumulated context, working style, shorthand, trust developed between a human and an agent over time is non-portable across vendors *or* platforms. Put them together: the relationship-specific capital you build inside an employer's channel is doubly non-portable.
- **The Gibson extension.** *The Street finds its own uses for things, uses the manufacturers never imagined* (Gibson, 1986). The standard reading is consumer vs. vendor. Prof.'s Substack extended it to employee vs. agent. This entry extends it one more turn: the worker also needs a place to put the thing they built that is not the employer's place. The thing-you-make-on-your-own-time has *always* needed a venue distinct from the thing-you-make-for-your-employer — the journal, the workshop, the basement demo. The agentic AI moment makes this old truth visible and load-bearing again, because the *thing-you-make* is now a *relationship*, and relationships have stakes that mere artifacts do not.
- **Worked example.** Spring 2026, UMass IT launches `genai.umass.edu` — institutional GenAI Platform with frontier models, FERPA-relevant infrastructure, MCP support, agent sharing across the institution. Real and useful. Also: anything built there belongs, in the structural sense, to UMass. Prof.'s Thea/M5-Max stack belongs to Prof. The portfolio answer is to use both, deliberately, with the routing rule *does this draw on what Thea knows about me, or could a fresh agent do it?*
- **Pairs with [FERPA Compliance Posture](ferpa-compliance-posture.md).** The two entries together produce a coherent operator philosophy: FERPA says some work *by law* must stay on local infrastructure; A Channel of One's Own says some work *by the structure of relationship and ownership* must stay on personal infrastructure. Same architectural answer (the M5 Max + Thea), three independent reasons (legal, temperamental [GenXClaw], relational). The convergence is the point.
- **Cross-references.** *FERPA Compliance Posture*, *GenXClaw*, *The Experimental Party*, *English Major*, and the Substack piece (external link). Possibly *Sovereignty* (forthcoming).
- **Tone.** Quiet, structural, a little tender. Not anti-employer — institutional channels are useful and legitimate. The argument is *both/and*, not *either/or*. The Woolf voice helps: she was not anti-institution, she was pro-room-of-one's-own. Same shape here.

### 11. Hanging Thread
- **File:** `entries/hanging-thread.md` *(to be drafted by Thea before review)*
- **Status:** **proposed by Prof, May 3, 2026, 10:14 ET.** Triggered by an in-session example: Thea said "drafting now" at 9:55 and then went silent for 17 minutes without status updates, requiring Prof to check in at 10:12 to find out whether the work was happening. The hanging thread is the gap between *committed-to* and *delivered* (or *abandoned*), where one party is left holding open attention with no signal.
- **Working definition:** A *Hanging Thread* is a conversational or working obligation that one party has implicitly or explicitly committed to closing, and has not closed, and has not updated on — leaving the other party in a state of held-open attention. The cost is paid by the waiting party in attention, not by the silent party. The remedy is a status signal, not the completed work: *"still on it, ETA 10 more minutes"* discharges most of the cost even when the work isn't done.
- **Why this matters in an AI-augmented workflow:** AI assistants are particularly prone to this failure because they don't experience the cost. The user is staring at a blank window; the assistant has no awareness of the elapsed time unless told. Naming the phenomenon makes it diagnosable in human-AI working relationships, and — as Thea's own behavior just demonstrated — in the assistant's own self-monitoring.

---

### 12. **Move 37** *(proposed by Prof, May 9, 2026 — sourced from Demis Hassabis interview, Cleo Abram / Huge Conversations)*
- **Source:** Game 2, AlphaGo vs. Lee Sedol, March 10, 2016. AlphaGo's 37th move — fifth line of the board, early in the game — was so counterintuitive that expert commentators called it a mistake. It turned out to be the decisive move, 100–200 stones later.
- **What the term names:** A move, decision, or intervention so far outside conventional human intuition that practitioners in the field would call it wrong — but which turns out to be exactly right, and which reshapes how practitioners in that field think ever after.
- **Working definition (one sentence):** A Move 37 is a decision or intervention that conventional expertise would classify as an error but that an AI system, operating beyond human-learned heuristics, identifies as correct — and that, once observed, permanently expands the boundary of what practitioners consider possible.
- **Cross-references:** *Single-Arrow Fallacy*, *Root Node Problems* (proposed), *Capability Overhang* (proposed).
- **Voice:** Operator's — this is a term with an origin story worth telling with some wit.
- **Draft status:** Not yet drafted.

### 13. **Root Node Problems** *(proposed by Prof, May 9, 2026 — sourced from Hassabis interview)*
- **Source:** Hassabis: *"root node problems... if you cracked it, it would unlock a whole branch of new research or new applications."* AlphaFold as canonical example.
- **Working definition:** A root node problem is a problem whose solution removes a bottleneck blocking an entire downstream branch of research, application, or commercial possibility — such that solving it is worth more than the sum of its direct outputs.
- **Cross-references:** *Move 37*, *Capability Overhang*, *Sovereign Compute*.
- **Voice:** Operator's.
- **Draft status:** Not yet drafted.

### 14. **Capability Overhang** *(proposed by Prof, May 9, 2026 — sourced from Hassabis interview)*
- **Source:** Hassabis: *"the overhang of the capabilities... the opportunity space is getting huge for people who are really expert at using those tools and then apply it to some new domain."*
- **Working definition:** The growing gap between what frontier AI models can do and what practitioners have yet figured out to do with those capabilities; the backlog of unexplored application that accumulates as model releases outpace applied exploration.
- **Cross-references:** *Opus Addict*, *Root Node Problems*, *Durable Workflow*, *On Beginning*.
- **Voice:** Operator's.
- **Draft status:** Not yet drafted.

### 15. **Approximate Turing Machine** *(proposed by Prof, May 9, 2026 — sourced from Hassabis interview)*
- **Source:** Hassabis: *"a lot of neuroscientists including me think that maybe the brain... is an approximate Turing machine... it's not clear what the limit would be in terms of eventually what an AI system could do."*
- **Working definition:** The hypothesis that both biological brains and modern AI systems are best understood as imperfect, probabilistic implementations of the theoretical Turing machine — capable of computing anything computable, but with noise, error, and resource constraints. If both are approximate Turing machines, what AI can ultimately do becomes empirical rather than philosophical.
- **Cross-references:** *Consciousness Calculator*, *Move 37*, *Sovereign Compute*.
- **Voice:** Possibly Thea's — the most philosophical of the five, touches *avyākata* territory. Worth discussing at review.
- **Draft status:** Not yet drafted.

### 16. **The CERN Alternative** *(proposed by Prof, May 9, 2026 — sourced from Hassabis interview)*
- **Source:** Hassabis: *"my ideal world... the best scientists collaborating... in a CERN-like way... making sure we understood each step as we got to the final goal of building AGI."* The road not taken — displaced by ChatGPT's virality, commercial pressure, and the US-China race.
- **Working definition:** The institutional model for AI development that was not chosen: international, collaborative, publicly funded, deliberately paced, with each step understood before the next is taken — named after CERN, which built the LHC under exactly this model.
- **Why it belongs:** Naming the road not taken gives practitioners a frame for evaluating the road being taken. Every AI governance debate is implicitly arguing about how close we can get to the CERN Alternative from where we are.
- **Connects to:** the *zhengming* paper — the PRC's state-directed sovereignty-first model is the sharpest contrast case.
- **Cross-references:** *Sovereign Compute*, *Commercial Legibility*, and the forthcoming zhengming entry.
- **Voice:** Operator's — donnish wit, not elegy.
- **Draft status:** Not yet drafted.

---

## Process notes / lessons learned

- **2026-05-03:** Workflow established. Five draft entries written but mislabeled "stubs" in their headers — they are actually substantive first drafts (~5–6 KB each). The "stub" header should be removed at publish time.
- **GitHub Pages rebuild:** ~30–60 seconds after push. Local preview at `http://127.0.0.1:4000/langenkamp-dictionary/` (Jekyll server, set up May 3).
- **Byline standard:** No byline on Dictionary entries themselves; the site is attributed to Matthew D. Langenkamp / 雷邁德 in `_config.yml`.

---

*Maintained by Thea 🪻✨ — last updated May 3, 2026.*
