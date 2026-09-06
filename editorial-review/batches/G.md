# Batch G — Plain-Prose Review

**State:** approved and published

**Baseline:** `0335273`

**Branch:** `editorial/alphabetical-plain-prose-audit-g`

**Published corpus:** 14 entries

**Excluded current drafts:** none

## Ledger

| Entry | Review status | Change class | Notes |
|---|---|---|---|
| Gateway | reviewed | substantive revision | Corrected the loopback claim, narrowed failure and persistence claims, distinguished hosted assistants from operator-controlled gateways, removed machine-specific audit details, added metadata and an OpenClaw source, and repaired cross-links. |
| Gemini | reviewed | substantive revision | Replaced an incorrect Gemini 3 date and universal context-growth claim with a sourced family definition; separated the model family from the consumer product; removed a stale operator-model comparison; repaired formatting and cross-links. |
| Gemma | reviewed | substantive revision | Corrected the Gemma 4 architecture and release description, removed an obsolete claim about OpenAI open weights, scoped the local performance comparison as a dated operator observation, added official sources, and repaired cross-links. |
| GenXClaw | reviewed | substantive revision | Preserved the operator portrait and jokes while marking them as caricature rather than cohort psychology; removed unsupported statistics and diagnostic language; corrected the categorical FERPA claim; added metadata and repaired cross-links. |
| GLM | reviewed | light revision | Tightened the CAISI finding to the tested cyber domain, added direct research and NIST sources, normalised house spelling, and repaired cross-links. |
| Golden Age for Builders | reviewed | light revision | Marked the argument as a qualified Dictionary thesis, removed an unsupported 98-percent figure, reduced stock contrast, added explicit draft metadata, and repaired cross-links. |
| The Good Intentions Problem | reviewed | light revision | Preserved the definition and operator voice; repaired seven cross-links that rendered as relative `.md` URLs. |
| Google DeepMind | reviewed | substantive revision | Corrected formatting and the Nobel description, removed the unsupported claim that Hassabis named OpenClaw in the cited interview, clarified the institutional argument, added primary sources, and repaired cross-links. |
| GPT | reviewed | substantive revision | Replaced an overstated first-mover history and stale model list with a sourced account of the GPT lineage; distinguished the model family from ChatGPT and repaired cross-links. |
| GPTZero | reviewed | substantive revision | Removed an unsupported million-user claim, separated detector estimates from proof of authorship, scoped the non-native-writer bias finding to the tested detector class, added sources, and repaired cross-links. |
| Grep Architecture | reviewed | light revision | Qualified the context-cost and caching claims, added publication metadata, converted existing related terms to canonical links, and left two genuinely planned entries unlinked. |
| Grey Swans | reviewed | substantive revision | Acknowledged the established risk-management term, recast the convergence rule as a Dictionary extension and teaching heuristic, corrected the Apple succession chronology, disclosed the absence of a pre-event Dictionary forecast, added sources and metadata, and repaired cross-links. |
| Grid-share Shock | reviewed | light revision | Replaced a vague contested-percentage claim with IEA estimates, distinguished data-centre demand from AI demand, added the source, and repaired cross-links. |
| Grok Bot | reviewed | light revision | Replaced the “less interesting as” construction with a direct statement of editorial purpose and updated revision metadata. |

## Batch findings

- **14 entries reviewed:** 6 received light revisions and 8 received substantive revisions. Every G entry required at least one repair.
- The relative-link defect found in D through F affected thirteen G entries. All internal entry links now use canonical `/entries/<slug>/` paths; *Grok Bot* already did so.
- *GenXClaw* confused a deliberately comic portrait with unsupported cohort psychology and repeated the superseded claim that local processing is the only lawful FERPA architecture. The revision keeps the spare-bedroom voice while stating what is anecdote, caricature, and operational preference.
- *Grey Swans* previously presented an established risk term as though the Dictionary had coined it, then used an arbitrary two-of-three test as a classification rule. The revision distinguishes ordinary usage from the Dictionary's convergence extension and discloses that the Apple example was not forecast in the corpus before the announcement.
- *GPTZero* now treats detector output as a fallible signal rather than evidence of authorship. The cited 2023 study included GPTZero among seven tested detectors, but the revision does not project one experiment onto every later product version.
- *Gateway*, *Gemini*, *Gemma*, *Google DeepMind*, and *GPT* contained moving technical or institutional claims stated as timeless facts. They now carry primary or authoritative sources and explicit scope.
- The negative-parallelism scanner reports 97 hits across 160,155 words (0.61 per thousand). *GenXClaw* contains two deliberate constructions across roughly 2,015 words, below the review threshold.

## Representative changes

### GenXClaw: portrait rather than diagnosis

The original entry attributed self-reliance, contingency thinking, privacy instincts, and technology-mediated social substitution to a generation, supported one claim with an unsourced statistic, and called local Apple Silicon the only lawful architecture for student work. The revision identifies the entry as one operator's affectionate caricature, keeps its jokes and hardware texture, and separates lower disclosure risk from legal compliance.

### Grey Swans: extension rather than coinage

The revised entry begins with the established risk-management meaning: a foreseeable but unlikely high-impact event. The Dictionary's contribution is narrower—the proposal that single-arrow analysis can hide converging signals. Its three questions are now a heuristic, and the Apple case is labelled an after-the-fact illustration rather than evidence of a successful forecast.

### Model families: dated facts and stable definitions

The Gemini, Gemma, and GPT entries no longer rely on stale daily-model preferences or exhaustive release lists. They define durable family boundaries, distinguish models from products, source historical milestones, and label local benchmark observations as dated and configuration-dependent.

### Detection scores are not authorship evidence

The GPTZero entry now says what a detector can observe—statistical resemblance—and what it cannot observe—who wrote the text. It retains the fairness concern for non-native English writers while tying that concern to the conditions of the cited study.

## Rendered previews

The unpublished local build contains all fourteen reviewed pages under `_site/entries/`. The principal previews are:

- `_site/entries/gateway/index.html`
- `_site/entries/genxclaw/index.html`
- `_site/entries/gptzero/index.html`
- `_site/entries/grey-swans/index.html`
- `_site/entries/gemma/index.html`

All fourteen rendered pages were inspected for headings, literal `.md` URLs, and internal link targets. Every canonical entry target exists in the build.

## Publication record

Professor Langenkamp approved batch G on 6 September 2026. The reviewed content was integrated into `main` as `fd8ec59`. Batch H was authorised to begin after publication verification.
