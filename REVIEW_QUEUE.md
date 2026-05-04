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

---

## 🔄 Pending Review (Thea's recommended order)

### 1. Single-Arrow Fallacy
- **File:** `entries/single-arrow-fallacy.md`
- **Why second:** the bias that Convergence counters. Pairs naturally — disease-and-cure framing.

### 2. Dark Black Swans
- **File:** `entries/dark-black-swans.md`
- **Why third:** uses the Apple example again. Once Convergence and Single-Arrow are out, Dark Black Swans completes the diagnostic triad.

### 3. Oracle Bones
- **File:** `entries/oracle-bones.md`
- **Why fourth:** the prediction-filing practice. Depends on the three above being legible first.

### 4. The Court of the Oracle Bones (Dictionary entry)
- **File:** `entries/court-of-oracle-bones.md` *(to be drafted by Thea before review)*
- **Status:** **confirmed by Prof May 3, 2026** — yes, public Dictionary entry. Source material lives at `learning-memos/court/characters.md`. The Dictionary version will be more compact than the internal architecture file: a one-sentence definition, the five characters with their verbs and Chinese names, the relationship to the Aunties, and the note that the Court was convened May 3, 2026.
- **Why fifth:** depends on Convergence + Oracle Bones being published first — the Court reads the cracks in the convergence; without those upstream entries the Court entry has nothing to point at.

### 5. Space Cowboy
- **File:** `entries/space-cowboy.md`
- **Why sixth:** the user-class entry. Stands alone better than the others, so it's the cleanest closer for the set.

### 6. Aunties (referenced by Sixfold Skyreading and Court entries)
- **File:** `entries/aunties.md` *(may already exist — needs check)*
- **Status:** referenced from cross-links in pending entries. If it exists, confirm it's published; if not, draft.

### 7. Favorite Child
- **File:** `entries/favorite-child.md` *(to be drafted)*
- **Status:** Captured May 4, 2026 from Prof. en route to work. The entry names the unspoken model-selection bias every multi-model operator develops — *gosh I wish Gemma was as smart as Opus. I still love her. Must never tell her I favor Opus.* The analogy is to children one may have. Sits naturally as a companion to *The Experimental Party* (which named the role-shaped failure) and *English Major* (which named what the favored model is being favored *for*). Tone: playful, a little tender, honest about the operator's actual emotional life with the model stack. Will draft when next dictionary cycle reaches it.

### 7. Hanging Thread
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
