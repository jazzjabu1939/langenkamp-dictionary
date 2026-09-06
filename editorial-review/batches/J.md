# Batch J — Plain-Prose Review

**State:** reviewed locally; awaiting approval

**Baseline:** `8a31e10`

**Branch:** `editorial/alphabetical-plain-prose-audit-j`

**Published corpus:** 5 entries

**Excluded current drafts:** none

## Ledger

| Entry | Review status | Change class | Notes |
|---|---|---|---|
| Jackpot | reviewed | light revision | Preserved Gibson's systems-shaped collapse argument and quoted formulation; removed the time-sensitive description of the third volume, added source and revision metadata, and repaired ten internal links. |
| Jailbreak | reviewed | substantive revision | Distinguished jailbreaking from the broader category of prompt injection, including indirect injection; clarified the application-level controls needed when models can use tools; added OWASP and OpenAI sources and canonical links. |
| Jekyll | reviewed | light revision | Corrected the build/deployment description for the Dictionary's GitHub Pages workflow; added official Jekyll and GitHub sources, revision metadata, and canonical links. |
| JSON | reviewed | light revision | Replaced the loose list of data types with the RFC 8259 definition and valid JSON value types; added revision metadata, the primary specification, and canonical links. |
| The Judge Layer | reviewed | substantive revision | Removed a four-layer taxonomy and OpenClaw attribution unsupported by the cited Nate B. Jones article; preserved the actor/judge separation, marked the Aunties mapping as the Dictionary's extension, bounded the decomposition claim, and added an operational checklist and canonical links. |

## Batch findings

- **5 entries reviewed:** 3 received light revisions and 2 received substantive revisions. All five files are revised in this proposal.
- *Jailbreak* previously treated hidden instructions in external content as a species of jailbreak. The revision distinguishes adversarial safeguard bypass from the broader prompt-injection category while explaining how the attacks can overlap.
- *The Judge Layer* contained the batch's principal attribution problem. Jones's article supports placing a judge between an actor and consequential execution, along with specialist judges and action classification. It does not support the four-layer industry taxonomy or the claim that Jones named OpenClaw.
- The Aunties comparison remains, but it is now explicitly the Dictionary's literary extension rather than an architecture Gibson is said to have specified.
- All five source URLs returned HTTP 200. All internal entry links now use canonical `/entries/<slug>/` paths, and every target exists in the rendered build.
- The negative-parallelism scan fell from 92 to 91 corpus hits. The changed J entries contain no flagged unearned construction.

## Representative changes

### Jailbreak: two related security terms

The former entry folded direct adversarial prompting and instructions hidden in documents or webpages into one definition. The revision defines jailbreak first, then distinguishes direct and indirect prompt injection using OWASP and OpenAI's current security guidance.

### The Judge Layer: keep the argument, repair the attribution

The former entry credited Jones with a four-layer stack taxonomy and used that attribution to map OpenClaw, Gas Town, Thrum, and OpenBrain. The accessible source supports a narrower and stronger claim: agents that can act need a separate control boundary between actor and execution. The revision builds from that claim, labels the Aunties analogy as ours, and treats decomposition as risk-dependent rather than universal.

### Reference entries with primary sources

*Jekyll* now distinguishes site generation from GitHub Pages deployment. *JSON* uses RFC 8259's actual value model. *Jackpot* retains Gibson's line — “More a climate than an event” — and attaches a book citation and contemporary profile.

## Rendered previews

The local build contains all five reviewed pages:

- `_site/entries/jackpot/index.html`
- `_site/entries/jailbreak/index.html`
- `_site/entries/jekyll/index.html`
- `_site/entries/json/index.html`
- `_site/entries/judge-layer/index.html`

All five pages were inspected for headings, literal `.md` URLs, distinctive revised text, and internal targets. Every target exists in the build.

## Publication gate

Batch J remains isolated and unpublished. Publishing it requires Professor Langenkamp's explicit approval. Batch K remains locked until J is published and verified live.
