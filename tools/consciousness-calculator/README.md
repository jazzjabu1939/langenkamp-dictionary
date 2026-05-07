# Consciousness Calculator — Prototype README

**Location:** `tools/consciousness-calculator-draft/index.html`  
**Status:** Draft — not yet promoted to `/tools/consciousness-calculator/`  
**Do not commit or push without Prof and Thea review.**

---

## What this is

A single-file, vanilla HTML/CSS/JS interactive tool that makes visible the economic trade between a user's consciousness and "free" closed-tier AI services. Conceptually anchored to the Dictionary entry at https://langenkamp.io/entries/consciousness-calculator/.

No build system, no framework, no external network requests after page load (Google Fonts is the only external resource; remove the `<link>` tag to go fully offline). Zero telemetry.

---

## Assumptions baked into the calculation

### Base CPM (US, programmatic, intent-adjacent context)

| Service | Base CPM | Rationale |
|---|---|---|
| ChatGPT Free | $15 | Search-intent-adjacent; OpenAI has discussed ad-supported tiers publicly; estimate is midpoint of search CPM range ($10–$20) |
| ChatGPT Plus | $0 | Paid plan; no ad model currently active |
| Gemini Free | $12 | Google's programmatic infrastructure is the most mature; estimate slightly below ChatGPT Free because conversational integration is less mature than Search |
| Meta AI | $20 | Meta has the highest-value consumer programmatic targeting in the world; behavioral profile depth is the ceiling case |
| Other free AI | $8 | Conservative estimate for an emerging platform without a mature ad stack |

CPM figures are informed by publicly available industry ranges (Google DV360 benchmarks, Meta Business Help Center rate card commentary, Forrester/eMarketer estimates 2023–2025). They are proxies, not audited data.

### Intent-shaping multiplier: 3×

Applied uniformly across services. Rationale: a search engine observes intent after the fact ("I was just searching for X"). An AI assistant shapes intent prospectively ("I'm going to suggest you do Y next"). This premium is real in advertiser willingness-to-pay; 3× is the conservative midpoint of the 2×–5× range cited in the spec. Source: analyst commentary on conversational AI advertising premiums.

### Stickiness multiplier: 1× to 50×

Continuous exponential curve: `stickiness_multiplier = 50^(slider_value/100)`. This gives:
- 0 (oil filter) → 1×
- 33 → ~3.7×
- 50 → ~7.1×
- 66 → ~14×
- 100 (anti-depressant) → 50×

The 50× ceiling is defensible: pharma DTC CPMs run $40–$80 in passive display; the additional intent-shaping premium for an AI that has just read emotional vulnerability as a market signal could easily double or triple that. The 50× figure represents the multiplier *above the base CPM* of the service, not an absolute CPM.

### Income bracket multipliers: 1×, 1.5×, 2.2×, 3×

Standard programmatic segmentation. High-income audiences (top 10%) are 2–3× more valuable per impression than median. Figures are consistent with publicly available CPM segmentation commentary.

### Impressions per hour: 6

Estimated at roughly one query-response pair per 10 minutes of active use. This is conservative — some sessions run faster. Each pair represents one "placement opportunity" in the ad model.

### Price escalator: 12% per year

Based on YouTube Premium trajectory: $12.99 (2018) → $13.99 (2021) → $18.99 (2023) → $22.99 (2024+), approximately 15%/year. OpenAI's own trajectory (ChatGPT Plus $20/mo since 2023; rate increases widely expected) suggests the same arc. 12% is the conservative end; used here to avoid overstating the forward case.

### Extraction growth: 10% per year (in forward projection)

The projection assumes platform usage normalizes upward as AI becomes ambient — i.e., the same user will likely spend *more* time in AI assistants over time, not less. 10%/year growth in extraction is conservative.

---

## Decisions made where the spec was silent

1. **Single-file HTML** — spec left it open (one file or split). Single file was chosen for simplicity; the JS and CSS are easily extractable if needed.

2. **Google Fonts link included** — spec said "system fonts are fine for the prototype." The Fonts link was included anyway so the design register matches the Dictionary immediately. Remove one `<link>` tag to go fully offline.

3. **"No ads currently" handling** — for services that don't run ads yet (ChatGPT, Gemini), the tool shows a notice explaining the figures represent *latent value* and *potential* extraction. This is more honest than silently zeroing or silently calculating.

4. **ChatGPT Plus zeroed** — since Plus is a paid, no-ad plan, `base_CPM = 0`. The tool will show $0 extracted and a gap in the user's favor (overcompensating relative to the *data* dimension, though not necessarily relative to their threshold). This is the correct outcome — the paid plan is Plan A (honest rental).

5. **Extraction growth in projection** — the spec described price escalation for subscriptions; I also added a 10%/year growth factor on the extraction side, because the underlying dynamic is that *both* the subscription price and the behavioral value being extracted will grow over time. This is documented in the "How we computed this" section.

6. **No "share" buttons, no CTA** — spec was explicit; honored fully.

7. **The `threshold` default is $1,000/mo** — Prof's anchor figure from the spec.

---

## Open questions for Prof and Thea before promotion

1. **CPM figures** — Should we cite specific sources inline (with footnotes or a table), or keep them in the "How we computed this" block as-is? More citation would be more rigorous but breaks the visual flow.

2. **ChatGPT Plus behavior** — Currently shows $0 extracted and a "you are overcompensating" gap (because subscription cost + threshold > $0). Is this the right framing, or should it be reframed as "honest rental — no mispricing gap to report"?

3. **The stickiness slider labels** — The four labels ("Oil filter", "New car", "Rx drug", "Anti-depressant") are spaced evenly across the visual track but the underlying multiplier curve is exponential. Should the labels be positioned at their *actual* positions on the curve (roughly 0%, 40%, 70%, 100%) rather than evenly spaced?

4. **Mobile layout** — Tested visually; inputs stack above outputs on narrow screens. Is this acceptable for the prototype, or should we refine?

5. **The "latent value" framing for non-ad services** — The notice saying "this service doesn't currently run ads, but here's the latent value" is philosophically correct but may confuse some readers. Alternative: hide the calculation entirely for non-ad services and just show a note. Prof's call.

6. **Tone of "How we computed this" section** — currently fairly dry/technical. Should it be warmed into the operator's voice (donnish wit, light humor)?
