# Batch H — Plain-Prose Review

**State:** approved and published

**Baseline:** `e300d45`

**Branch:** `editorial/alphabetical-plain-prose-audit-h`

**Published corpus:** 14 entries

**Excluded current drafts:** the companion concepts *Agentic Loop*, *Model–Harness Fit*, and *Verification* are untracked drafts on `main`; they remain unpublished and appear as plain-text draft references in *Harness*

## Ledger

| Entry | Review status | Change class | Notes |
|---|---|---|---|
| Heartbeat | reviewed | substantive revision | Updated the entry to OpenClaw's current system-owned automation architecture; removed a machine-specific policy excerpt and unsupported cost claims; clarified scheduling, context, delivery, and silence; added an official source and canonical links. |
| Hallucination | reviewed | light revision | Preserved the balanced definition and repaired four cross-links. |
| Hallucination Frequency Myth | reviewed | substantive revision | Replaced the sweeping claim that frequent fabrication is simply outdated with the narrower defect: treating one benchmark rate as a universal property of a model; clarified task dependence and evidence checking; repaired cross-links. |
| Harness | reviewed | substantive revision | Completed and source-checked the concurrent harness-engineering expansion; distinguished Big Model from Big Harness arguments; updated the OpenClaw example; tightened the management and governance analogies; canonicalised public cross-links while leaving three unpublished companion concepts as plain-text draft references. |
| Harness Hygiene | reviewed | light revision | Preserved the essay and its heartbeast joke; repaired six cross-links. |
| Heinlein Protagonist | reviewed | substantive revision | Identified the term explicitly as a Dictionary lens rather than a biographical diagnosis; corrected the TANSTAAFL attribution; qualified the postwar-stability thesis; tightened the summary and added the originating interview. |
| Hermes | reviewed | substantive revision | Replaced a stale Llama/Mistral-only family description and timeless local-model recommendation with the mixed-base Hermes 4 lineage; scoped hardware claims; added current model cards and canonical links. |
| Hill Climb | reviewed | substantive revision | Resolved duplication with *Hill Climbing* by defining this entry as operator shorthand for the formal search method; added a reciprocal link and repaired related links. |
| Hill Climbing | reviewed | light revision | Preserved the technical definition and added the reciprocal distinction from *Hill Climb*; repaired four cross-links. |
| Hugging Face | reviewed | substantive revision | Removed stale repository counts and the claim that the company is a neutral platform charging only for enterprise hosting and compute; distinguished Hub availability from open-source status; added official documentation and pricing sources; repaired links. |
| Human in the Loop | reviewed | light revision | Preserved the teaching definition and repaired four cross-links. |
| Human Judgment Layer | reviewed | light revision | Preserved the definition and examples and repaired seven cross-links. |
| Human Reserved | reviewed | light revision | Retained the current, sourced Gates essay and its educational extension; repaired six cross-links. |
| Hyperscaler | reviewed | substantive revision | Separated infrastructure operators from the labs that buy, partner for, or control hyperscale capacity; corrected and sourced the OpenAI, Anthropic, SpaceX, and xAI relationships; repaired cross-links. |

## Batch findings

- **14 entries reviewed:** 6 received light revisions and 8 received substantive revisions. All fourteen files are revised in this proposal.
- The relative-link defect found in D through G affected eleven H entries. All public-entry links in the fourteen changed files now use canonical `/entries/<slug>/` paths. Three unpublished companion concepts in *Harness* remain plain-text draft references and create no dead links.
- *Heartbeat* described an earlier runtime model and embedded local operating instructions in a public reference entry. It now reflects OpenClaw's automations-owned cadence, configurable session context, guarded timing, and current silence contract.
- *Hallucination Frequency Myth* previously replaced one crude generalisation with another. The revision makes the durable point that reliability varies with task, evidence, tools, prompt, model version, and evaluation.
- *Hermes* and *Hugging Face* contained time-sensitive ecosystem claims presented as stable facts. Both now explain what remains durable and point readers to sources that should be checked again as the ecosystem changes.
- The two hill entries now have distinct jobs: *Hill Climbing* defines the algorithm; *Hill Climb* names the operator's iterative habit.
- The negative-parallelism scanner reports 96 hits across 160,452 words (0.60 per thousand). *Heinlein Protagonist* contains two deliberate constructions across roughly 1,680 words, below the review threshold.
- *Harness* now incorporates the approved harness-engineering expansion without publishing or overwriting its three companion drafts on `main`.

## Representative changes

### Heartbeat: current architecture, public explanation

The revision replaces a local-machine policy excerpt and an unsourced 98-percent cost claim with the stable mechanism: a system-owned automation schedules an agent turn, runtime guards may defer it, and the response contract permits silence. It also distinguishes ambient monitoring from an independent named automation without pretending that session context is fixed.

### Hallucination: a rate is not a property label

The revised *Hallucination Frequency Myth* does not declare the problem solved or permanently frequent. It asks the more useful question: what task, benchmark, evidence path, and checking regime produced the reported rate?

### Two hills, two jobs

The older *Hill Climb* and newer *Hill Climbing* entries had become near-duplicates. The revision retains both without making readers guess: one is operator vocabulary and one is the formal search method.

### Ecosystem claims that can age

*Hermes*, *Hugging Face*, and *Hyperscaler* now distinguish durable definitions from current examples. Sources are attached to the moving institutional and model-family claims.

### Harness engineering: model and system

The completed *Harness* expansion treats model capability and harness quality as complementary levers. It gives the Big Model and Big Harness positions their strongest concise forms, then grounds the distinction in OpenClaw and ordinary management systems. Latent Space and OpenAI support the moving technical claims; unpublished companion concepts remain visibly labelled drafts rather than broken links.

## Rendered previews

The unpublished local build contains all fourteen reviewed pages under `_site/entries/`. The principal changed previews are:

- `_site/entries/heartbeat/index.html`
- `_site/entries/hallucination-frequency-myth/index.html`
- `_site/entries/harness/index.html`
- `_site/entries/heinlein-protagonist/index.html`
- `_site/entries/hermes/index.html`
- `_site/entries/hill-climb/index.html`
- `_site/entries/hugging-face/index.html`
- `_site/entries/hyperscaler/index.html`

All fourteen changed pages were inspected for headings, literal `.md` URLs, and internal link targets. Every canonical target exists in the build.

## Publication gate

Professor Langenkamp approved publication and completion of the held *Harness* expansion on 6 September 2026. Publication is complete only after the exact committed tree passes GitHub Pages deployment and live-page verification. Batch I remains locked pending separate authorization.
