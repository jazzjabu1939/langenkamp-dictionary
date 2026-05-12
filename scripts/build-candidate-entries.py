#!/usr/bin/env python3
"""
build-candidate-entries.py

Scan the Dictionary corpus + adjacent workspace materials, surface terms that
look like candidate entries but don't yet exist, and produce CANDIDATE_ENTRIES.md
as a triage document for Prof.

Three sources combined:
  1. Internal — capitalized noun phrases / italicized terms referenced in
     entries/*.md but with no corresponding entry file. These are the
     "promised links" — the highest-confidence tier.
  2. External — capitalized terms appearing in workspace materials adjacent
     to the Dictionary's editorial concerns (Koebler piece, Olang piece, Cherny
     transcript, Nate Jones piece, Hassabis interview transcripts).
  3. Curated — a hard-coded list of structural gaps Prof and Thea know about
     (AI labs, model brands, infrastructure pieces, etc.).

Each candidate is scored by:
  - count of internal references (how many existing entries mention it)
  - count of external references (how many workspace materials mention it)
  - kind: dictionary (load-bearing, voiced) or glossary (reference-card)
  - flags: PERSON, BRAND, MODEL, LAB, CONCEPT, TOOL, HARDWARE

Output: CANDIDATE_ENTRIES.md at the repo root, ready for triage.

Usage:
    python3 scripts/build-candidate-entries.py [--wide]
"""

from __future__ import annotations
import argparse
import json
import re
import sys
from collections import defaultdict, Counter
from dataclasses import dataclass, field, asdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ENTRIES_DIR = REPO_ROOT / "entries"
WORKSPACE = Path("/Users/Jazz/.openclaw/workspace")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# External materials we want to scan. Add or remove as needed.
EXTERNAL_SOURCES = [
    WORKSPACE / "Your AI Use Is Breaking My Brain.md",
    WORKSPACE / "Boris Cherny - Coding Solved.md",
    WORKSPACE / "Nate Jones May 11 2026.md",
    WORKSPACE / "Claude Mythos.md",
    WORKSPACE / "The Sincere Society.md",
]

# Stoplist: capitalized words that are NOT entry candidates.
# Common English (sentence starts, place names, person names that are pure refs
# without sustained Dictionary engagement, etc.).
STOPLIST = {
    # Sentence-start common words
    "The", "This", "That", "And", "But", "Or", "It", "When", "Where", "What",
    "Why", "How", "Who", "These", "Those", "Their", "There", "If", "As",
    "For", "From", "With", "Without", "Within", "After", "Before", "By",
    "On", "In", "Of", "To", "At", "All", "Any", "Some", "Most", "Many",
    "Few", "Both", "Either", "Neither", "Each", "Every", "No", "Not", "So",
    "Yes", "Now", "Then", "Here", "Today", "Yesterday", "Tomorrow",
    "He", "She", "We", "You", "They", "My", "Your", "His", "Her", "Our", "Its",
    "Is", "Was", "Were", "Be", "Been", "Being", "Have", "Has", "Had",
    "Do", "Does", "Did", "Done", "Will", "Would", "Could", "Should", "May",
    "Might", "Must", "Can", "Shall", "Maybe", "Perhaps", "Even",
    "Only", "Just", "Also", "Still", "Already", "Yet", "Soon", "Later",
    "Very", "Quite", "Rather", "Much", "More", "Less", "Far", "Near",
    "Such", "Same", "Other", "Another", "Different", "New", "Old",
    "Good", "Bad", "Better", "Worse", "Best", "Worst",
    "Up", "Down", "Out", "Off", "Over", "Under", "Around", "Through",
    "While", "Until", "Unless", "Although", "Though", "Because", "Since",
    "Since", "During", "Through", "Throughout", "Across", "Against",
    "Long", "Short", "Big", "Small", "Large", "Little", "High", "Low",
    "Right", "Wrong", "True", "False", "Sure", "Certain", "Possible",
    "Real", "Honest", "Live", "Dead", "Alive", "Open", "Closed", "Free",
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday",
    "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December",
    "First", "Second", "Third", "Fourth", "Fifth", "Last", "Next",
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
    "Ten", "Eleven", "Twelve", "Hundred", "Thousand", "Million", "Billion",
    "Mr", "Mrs", "Ms", "Dr", "Prof", "Professor",
    "Inc", "LLC", "Ltd", "Corp", "Co",
    "USA", "US", "UK", "EU", "UN",
    # Words that look like proper nouns in code blocks
    "PDF", "URL", "HTTP", "HTTPS", "API", "CSV", "JSON", "XML", "HTML", "CSS",
    "TODO", "FIXME", "NOTE", "WARNING", "ERROR", "INFO", "DEBUG",
    # English major / academic register words
    "English", "American", "British", "European", "Asian", "African",
    "Chinese", "Japanese", "German", "French", "Italian", "Spanish",
    "Russian", "Indian", "Korean", "Vietnamese",
    # Common bare proper nouns inside our own corpus that won't become entries
    "Dictionary", "Substack", "GitHub", "Twitter", "LinkedIn", "Facebook",
    "Instagram", "YouTube", "Reddit", "Discord", "Slack", "Telegram",
    "WhatsApp", "Messenger", "Gmail", "Google", "Apple", "Microsoft",
    "Amazon", "Meta",  # ambiguous — could be company or generic; treat as no-entry by default
    "Dad", "Mom", "Mother", "Father", "Son", "Daughter", "Brother", "Sister",
    "AI", "LLM", "GPU", "CPU", "RAM", "SSD", "OS", "UI", "UX", "MCP", "A2A",
    "RAG",  # we have this
    # Words that surface as Title Case in headers but aren't entry candidates
    "Move", "Section", "Chapter", "Part", "Phase", "Step", "Item",
    "Notes", "Note", "See", "Sources", "Source", "References", "Bibliography",
    "Caption", "Hero", "Header", "Footer",
    "Live", "Draft", "Published", "Pending",
    "True", "False", "None", "Null",
    # Misc
    "Prof", "Thea", "Langenkamp", "Matthew",  # us; never our own entries
    "OpenClaw",  # explicitly REMOVED from stoplist below — we want it as a candidate
    # Dictionary-internal boilerplate that surfaces as caps phrases
    "Proposed May", "Approved", "Pending", "Cluster", "Commit",
    "AI Writing", "Zombie Internet", "Earned Parallelism",
    "Olang", "Olang Trap",  # The Olang' Trap exists
    "Lazy Median", "Lazy Median Hypothesis",
    "Sinceerly", "Sinceerly Stack",
    # Things we already have entries for in slight variants
    "Grey Swan", "Grey Swans",  # grey-swans.md
    "Dark Black Swan", "Dark Black Swans",  # dark-black-swans.md
    "Compliance Posture", "FERPA Compliance", "FERPA Compliance Posture",  # ferpa-compliance-posture.md
    "Sovereign Compute", "Sovereign Compute Calculator",  # both exist
    "Opus Addict", "Consciousness Calculator",  # exist
    "English Major", "GenXClaw", "Red Pill", "Lab Character", "Mediation",
    "Inverted Funnel", "Commercial Legibility", "Single Arrow Fallacy",
    "Sixfold Skyreading", "Capability Overhang", "Agentic Threshold",
    "Aunties", "Lowbeer", "Lowbeer Question", "Move", "Naming",
    "Closed Source", "Token Angst", "Experimental Party",
    "On Being", "On Beginning", "Dusty Laptop", "Sub-agent", "Ollama",
    "Cern Alternative", "CERN Alternative", "Convergence", "Descartes",
    "Approximate Turing", "Approximate Turing Machine",
    "Fine Tuning",  # fine-tuning.md
    "Mediation Gibson", "Mediation a la Gibson",
    "Incremental Construction", "Durable Workflow", "Quantum Effects",
    "Root Node", "Root Node Problems", "Space Cowboy", "Oracle Bones",
    "FERPA",  # subsumed
    # Common words that surface as bigrams from caps headers
    "See Also", "Move One", "Move Two", "Move Three", "Move Four",
    "Section One", "Section Two", "Phase One", "Phase Two",
    "Peak One", "Peak Two",
    "First Move", "Second Move", "Third Move", "Fourth Move",
    "Open Question", "Closed Question", "Worked Example",
    "Quick Reference", "Quick Note", "Small Note",
    "Hero Image", "Hero Quote", "Hero Line",
    "Big Call", "Single Arrow",
}
# Re-allow OpenClaw — we want it as a candidate even though it appears as identity
STOPLIST.discard("OpenClaw")

# Curated structural list — terms we KNOW we want to consider, with kind+flags
# pre-set. The script will merge their reference counts with the scan.
CURATED_LIST = [
    # ── AI Labs (mostly glossary unless we have sustained engagement)
    ("Anthropic",         "glossary", ["LAB"], "The lab behind Claude. We use their models daily; load-bearing in Sovereign Compute and Opus Addict."),
    ("OpenAI",            "glossary", ["LAB"], "The lab behind GPT/ChatGPT. Referenced often as the market comparator."),
    ("Google DeepMind",   "glossary", ["LAB"], "The lab behind Gemini. Hassabis as the CEO has been quoted on OpenClaw."),
    ("Meta AI",           "glossary", ["LAB"], "Llama models. The PRC's May 2026 block of the Manus acquisition is a structural data point."),
    ("xAI",               "glossary", ["LAB"], "Musk's lab. Grok. The xAI/Anthropic data center deal Willison covered May 7."),
    ("Mistral",           "glossary", ["LAB"], "French open-weights lab. Mistral models in the local-compute tier."),
    ("DeepSeek",          "glossary", ["LAB"], "Chinese open-weights lab. R1 reasoning models. Strategic significance for zhengming."),
    ("Hugging Face",      "glossary", ["TOOL", "LAB"], "Model hub / open-weights distribution platform. Referenced often in Sovereign Compute."),
    ("Nous Research",     "glossary", ["LAB"], "Open-weights fine-tuning lab. Hermes family of models."),
    # ── Specific models
    ("Claude",            "dictionary", ["MODEL"], "The Anthropic model family. Sufficiently load-bearing in our corpus to be its own dictionary entry."),
    ("Claude Opus",       "glossary", ["MODEL"], "The Opus tier. Already partially covered by Opus Addict but missing a clean reference page."),
    ("Claude Sonnet",     "glossary", ["MODEL"], "The Sonnet tier. Referenced often."),
    ("Claude Haiku",      "glossary", ["MODEL"], "The Haiku tier. The fast/cheap option."),
    ("GPT",               "glossary", ["MODEL"], "OpenAI's model family. Generic reference target."),
    ("Gemini",            "glossary", ["MODEL"], "Google's model family."),
    ("Llama",             "glossary", ["MODEL"], "Meta's open-weights family. Common local-compute target."),
    ("Qwen",              "glossary", ["MODEL"], "Alibaba's model family. Referenced in TOOLS.md / Sovereign Compute."),
    ("Gemma",             "glossary", ["MODEL"], "Google's open-weights family. The operator runs Gemma 4 26B/31B locally."),
    ("Hermes",            "glossary", ["MODEL"], "Nous Research's open-weights instruction-tuned family. Sovereign Compute reference."),
    # ── Tools / products
    ("OpenClaw",          "dictionary", ["TOOL"], "The platform the operator runs. Hassabis named-checked it May 2026. Load-bearing for the entire workspace."),
    ("Claude Code",       "dictionary", ["TOOL"], "Cherny's product. *Coding Solved* talk gives us the printing-press parallel. Load-bearing for any coding-related entry."),
    ("ChatGPT",           "glossary", ["TOOL"], "OpenAI's product. The default cultural-comparator for AI."),
    ("Cursor",            "glossary", ["TOOL"], "AI-first IDE. We don't run it but readers will ask how it fits."),
    ("Pangram Labs",      "glossary", ["TOOL"], "AI-detection firm. Already named in The Mamdani Misfire and The Olang' Trap. Worth its own reference page."),
    ("GPTZero",           "glossary", ["TOOL"], "AI-detection tool. Another player in the detection economy."),
    ("Originality.ai",    "glossary", ["TOOL"], "AI-detection / plagiarism tool. Used in academic settings."),
    ("Sinceerly",         "glossary", ["TOOL"], "Already covered in The Sinceerly Stack as the parent argument. A short reference page for the product itself, pointing at the parent entry."),
    ("Cline",             "glossary", ["TOOL"], "AI coding assistant. Open-source Claude Code alternative. Probably worth a stub."),
    ("Aider",             "glossary", ["TOOL"], "Git-aware AI pair programmer. Often referenced in the sovereign-compute discussion."),
    ("LM Studio",         "glossary", ["TOOL"], "Local-LLM runner for Mac. Sovereign Compute reference."),
    ("Ollama",            "dictionary", ["TOOL"], "Local-LLM runner. We have entries/ollama.md already — verify, and possibly expand."),
    # ── Concepts (mostly dictionary if load-bearing)
    ("RLHF",              "dictionary", ["CONCEPT"], "Reinforcement Learning from Human Feedback. Named in The Sincere Society as the canonical sycophancy mechanism. Load-bearing."),
    ("Constitutional AI", "dictionary", ["CONCEPT"], "Anthropic's training approach. Structurally relevant to cheng and Sincere Society's arguments."),
    ("Scaling Laws",      "glossary", ["CONCEPT"], "The empirical regularity that model capability tracks compute + data. Structural to capability-overhang."),
    ("Mixture of Experts","glossary", ["CONCEPT"], "MoE architecture. Already referenced in TOOLS.md re Qwen 3.6 routing. Worth a reference page."),
    ("Context Window",    "glossary", ["CONCEPT"], "The token-length a model can hold in attention. Structural to prefill and the model-as-substrate arguments."),
    ("Prompt Injection",  "dictionary", ["CONCEPT"], "Attack class. Load-bearing for any operator-running-agents discussion. Worth a real entry."),
    ("Jailbreak",         "glossary", ["CONCEPT"], "The practice of bypassing model safety filters. Glossary stub probably suffices."),
    ("Fine-Tuning",       "glossary", ["CONCEPT"], "Already exists as entries/fine-tuning.md. Verify."),
    ("Chain of Thought",  "glossary", ["CONCEPT"], "CoT reasoning prompts. Now subsumed by reasoning models but historically important."),
    ("Reasoning Model",   "dictionary", ["CONCEPT"], "The post-o1/post-R1 class. Cherny's '4.7 can hill-climb anything' moment is structurally significant. Dictionary-shaped."),
    ("Sycophancy",        "dictionary", ["CONCEPT"], "The Sincere Society's core diagnosis. Should have its own entry that hubs to the Substack essay."),
    ("Hill Climb",        "glossary", ["CONCEPT"], "Cherny's term from *Coding Solved*. Load-bearing little phrase."),
    # ── People (rare; only those we are engaging substantively)
    ("Ethan Mollick",     "dictionary", ["PERSON"], "Wharton, *One Useful Thing*. We've cited him often enough that a person-entry would be load-bearing."),
    ("Demis Hassabis",    "dictionary", ["PERSON"], "Hassabis named OpenClaw May 2026; lab-character entry already engages him. A standalone entry would consolidate."),
    ("Simon Willison",    "dictionary", ["PERSON"], "His link blog has been the surface-channel for several of our cluster entries. Worth a person-entry."),
    ("Jason Koebler",     "glossary", ["PERSON"], "404 Media. Coined Zombie Internet. Probably a glossary stub pointing at Zombie Internet rather than a full person entry."),
    ("Marcus Olang",      "glossary", ["PERSON"], "Author of the Olang' Trap source piece. Glossary stub with proper Dholuo apostrophe and link to the Olang' Trap entry."),
    ("Boris Cherny",      "glossary", ["PERSON"], "Creator of Claude Code. Coding Solved talk. Stub linking to AI Writing + Claude Code."),
    ("William Gibson",    "dictionary", ["PERSON"], "Foundational to Mediation (a la Gibson), Aunties, Lowbeer-Question. Person-entry would consolidate."),
    # ── Hardware
    ("M5 Max",            "glossary", ["HARDWARE"], "Apple Silicon. The operator's workstation. Sovereign Compute / GenXClaw substrate."),
    ("Mac Studio",        "glossary", ["HARDWARE"], "Apple Silicon. Sovereign-compute hardware target."),
    ("Apple Silicon",     "glossary", ["HARDWARE"], "M-series chips. The technical substrate of Sovereign Compute / FERPA Compliance Posture."),
    # ── Chinese AI / economy
    ("Manus",             "dictionary", ["CONCEPT"], "Chinese AI startup. PRC May 2026 acquisition block named in Commercial Legibility. Worth its own entry."),
    ("Moltbook",          "dictionary", ["CONCEPT"], "Coogan's Feb 2026 X post / Fast Company coverage. Named in Zombie Internet but undefined; needs a clean entry."),
    ("TBPN",              "glossary", ["TOOL"], "Tech-business-policy podcast (Coogan/Roberts). Brief glossary stub."),
    # ── Misc structural concepts that should exist
    ("Borrowed Brain",    "dictionary", ["CONCEPT"], "Sally / Sovereign-Assistant concept. Used in the morning's work but never named publicly."),
    ("Cooperative Writing","dictionary", ["CONCEPT"], "Named in AI Writing; load-bearing enough to graduate to its own entry over time. Mark as future-graduation candidate."),
    ("Cheng",             "dictionary", ["CONCEPT"], "誠. Already in Sincere Society but a Dictionary entry that *defines* the term and points at the essay would be useful."),
]


# ---------------------------------------------------------------------------
# Extraction
# ---------------------------------------------------------------------------

# Pattern A: italicized term in body text — *Foo Bar* or _Foo Bar_
ITALIC_PATTERN = re.compile(r"(?<![\\*_a-zA-Z0-9])\*([A-Z][A-Za-z0-9' \u2014\-]{2,40})\*(?![*_a-zA-Z])")

# Pattern B: capitalized 1–4 word phrase, not at sentence start
CAPS_PHRASE_PATTERN = re.compile(
    r"\b([A-Z][a-z]+(?:[ \-][A-Z][a-z]+){0,3})\b"
)

# Pattern C: explicit MarkDown link with non-existing target
LINK_PATTERN = re.compile(r"\[([^\]]+)\]\(([a-z][a-z\-]+\.md)\)")


def existing_entries() -> set:
    """The set of existing entry slugs (without .md), plus heuristic variants
    (singular/plural, common prefixes) so we don't propose entries that already exist."""
    if not ENTRIES_DIR.exists():
        return set()
    base = {p.stem for p in ENTRIES_DIR.glob("*.md") if p.stem != "index"}
    # Add singular/plural variants
    expanded = set(base)
    for slug in base:
        # Drop trailing 's' for plural→singular match
        if slug.endswith("s") and len(slug) > 3:
            expanded.add(slug[:-1])
        # Add trailing 's' for singular→plural match
        expanded.add(slug + "s")
        # Split on hyphens and add the last word; this catches
        # e.g. "fairbanks-tell" matching "the-fairbanks-tell" if we ever made it.
        # Also adds prefix variants.
        parts = slug.split("-")
        if len(parts) > 1:
            # Keep variants like "the-X" -> "X" so "Lowbeer" matches "lowbeer-question"
            expanded.add(parts[-1])
            expanded.add(parts[0])
            # And full minus leading "the"
            if parts[0] == "the":
                expanded.add("-".join(parts[1:]))
            # And "X-Y" -> "X" prefix
            expanded.add(parts[0] + "-" + parts[1] if len(parts) >= 2 else parts[0])
    return expanded


def existing_entry_titles() -> dict[str, str]:
    """Map of {slug: title} from frontmatter, for nicer match-checking."""
    out = {}
    for p in ENTRIES_DIR.glob("*.md"):
        if p.stem == "index":
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        m = re.search(r'^title:\s*"([^"]+)"', text, re.MULTILINE)
        if m:
            out[p.stem] = m.group(1)
    return out


def slug_for_term(term: str) -> str:
    """Normalize a term to a slug-shape for de-duplication / matching."""
    s = term.lower()
    s = re.sub(r"[''\u2018\u2019]", "", s)        # strip apostrophes
    s = re.sub(r"[^a-z0-9\- ]", "", s)             # strip non-alpha
    s = re.sub(r"\s+", "-", s.strip())             # spaces -> dash
    s = re.sub(r"-+", "-", s)                      # collapse dashes
    return s


def scan_file(path: Path, source_label: str) -> dict[str, list[tuple[str, int]]]:
    """Return {term: [(source_label, line_no), ...]} of candidate terms from one file."""
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, FileNotFoundError):
        return {}
    # Strip frontmatter and HTML comments
    text = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    # Strip code blocks
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    # Strip inline code
    text = re.sub(r"`[^`]*`", "", text)

    hits: dict[str, list[tuple[str, int]]] = defaultdict(list)

    # Italic terms
    for m in ITALIC_PATTERN.finditer(text):
        term = m.group(1).strip().strip(" \u2014-")
        if len(term) < 3 or len(term) > 40:
            continue
        if term in STOPLIST:
            continue
        line_no = text.count("\n", 0, m.start()) + 1
        hits[term].append((source_label, line_no))

    # Caps phrases — only the multi-word ones (single-word too noisy at this stage)
    for m in CAPS_PHRASE_PATTERN.finditer(text):
        term = m.group(1).strip()
        if " " not in term and "-" not in term:
            continue  # skip bare single capitalized words for less noise
        if len(term) > 40:
            continue
        if term in STOPLIST:
            continue
        # Skip if first word is a stoplist sentence-starter (e.g. "When Anthropic")
        first = term.split()[0]
        if first in STOPLIST:
            term = " ".join(term.split()[1:])
            if len(term) < 3:
                continue
        line_no = text.count("\n", 0, m.start()) + 1
        hits[term].append((source_label, line_no))

    return hits


def find_promised_links() -> set[str]:
    """Find [foo](foo.md) references where foo.md doesn't exist."""
    promised = set()
    existing = existing_entries()
    for p in ENTRIES_DIR.glob("*.md"):
        if p.stem == "index":
            continue
        text = p.read_text(encoding="utf-8")
        for m in LINK_PATTERN.finditer(text):
            target = m.group(2)[:-3]  # strip .md
            if target not in existing:
                promised.add((m.group(1), target))
    return promised


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

@dataclass
class Candidate:
    term: str
    slug: str
    kind: str = "?"           # "dictionary" | "glossary" | "?"
    flags: list = field(default_factory=list)
    notes: str = ""
    internal_count: int = 0
    external_count: int = 0
    sample_sources: list = field(default_factory=list)
    is_promised_link: bool = False

    @property
    def total(self) -> int:
        return self.internal_count + self.external_count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--wide", action="store_true",
                        help="Also include single-word caps phrases (noisy)")
    args = parser.parse_args()

    existing_slugs = existing_entries()
    existing_titles = existing_entry_titles()

    # Pass 1: internal scan
    print("=== Pass 1: Internal scan of entries/*.md ===", file=sys.stderr)
    internal_hits: dict[str, list[tuple[str, int]]] = defaultdict(list)
    for entry in sorted(ENTRIES_DIR.glob("*.md")):
        if entry.stem == "index":
            continue
        for term, occurrences in scan_file(entry, entry.stem).items():
            internal_hits[term].extend(occurrences)
    print(f"  {len(internal_hits)} unique caps/italic terms in {len(list(ENTRIES_DIR.glob('*.md'))) - 1} entries",
          file=sys.stderr)

    # Pass 2: external scan
    print("=== Pass 2: External scan of workspace materials ===", file=sys.stderr)
    external_hits: dict[str, list[tuple[str, int]]] = defaultdict(list)
    for src in EXTERNAL_SOURCES:
        if not src.exists():
            print(f"  SKIP (not found): {src}", file=sys.stderr)
            continue
        label = src.stem[:40]
        for term, occurrences in scan_file(src, label).items():
            external_hits[term].extend(occurrences)
        print(f"  scanned: {src.name}", file=sys.stderr)

    # Pass 3: promised links
    print("=== Pass 3: Promised-link scan ===", file=sys.stderr)
    promised = find_promised_links()
    promised_slugs = {p[1] for p in promised}
    print(f"  {len(promised)} promised links to non-existent files", file=sys.stderr)

    # Merge
    candidates: dict[str, Candidate] = {}

    # From curated list
    for term, kind, flags, notes in CURATED_LIST:
        slug = slug_for_term(term)
        if slug in existing_slugs:
            continue
        c = Candidate(term=term, slug=slug, kind=kind, flags=list(flags), notes=notes)
        candidates[slug] = c

    # From internal scan
    for term, occurrences in internal_hits.items():
        slug = slug_for_term(term)
        if slug in existing_slugs:
            continue
        if slug not in candidates:
            c = Candidate(term=term, slug=slug)
            candidates[slug] = c
        candidates[slug].internal_count += len(occurrences)
        # Record up to 3 sample source-paths
        for src, line in occurrences[:3]:
            if len(candidates[slug].sample_sources) < 3:
                candidates[slug].sample_sources.append(f"{src}.md:{line}")

    # From external scan
    for term, occurrences in external_hits.items():
        slug = slug_for_term(term)
        if slug in existing_slugs:
            continue
        if slug not in candidates:
            c = Candidate(term=term, slug=slug)
            candidates[slug] = c
        candidates[slug].external_count += len(occurrences)

    # Promised links
    for display, slug in promised:
        if slug in existing_slugs:
            continue
        if slug not in candidates:
            c = Candidate(term=display, slug=slug)
            candidates[slug] = c
        candidates[slug].is_promised_link = True

    # Filter: keep candidates with internal_count >= 2 OR external_count >= 2
    # OR is_promised_link OR is in curated list (kind != "?")
    filtered = []
    for c in candidates.values():
        if c.kind != "?":  # curated
            filtered.append(c)
        elif c.is_promised_link:
            filtered.append(c)
        elif c.internal_count >= 2 or c.external_count >= 3:
            filtered.append(c)
        elif args.wide and (c.internal_count >= 1 or c.external_count >= 1):
            filtered.append(c)

    # Heuristic: assign kind for uncurated candidates
    for c in filtered:
        if c.kind != "?":
            continue
        # Default: glossary unless heavily internally referenced
        if c.internal_count >= 4:
            c.kind = "dictionary"
            c.notes = f"Highly referenced internally ({c.internal_count}x). Consider dictionary-shape."
        elif c.is_promised_link:
            c.kind = "glossary"  # promised stub
            c.notes = "Promised-link in existing entry — the corpus has already committed to this term."
        else:
            c.kind = "glossary"
            c.notes = "Inferred from scan. Review for relevance."

    # Sort: dictionary first by total references, then glossary by total
    filtered.sort(key=lambda c: (c.kind != "dictionary", -c.total, c.term.lower()))

    # Write CANDIDATE_ENTRIES.md
    out_path = REPO_ROOT / "CANDIDATE_ENTRIES.md"
    write_output(filtered, out_path, args)
    print(f"\nWrote {out_path}", file=sys.stderr)
    print(f"Total candidates: {len(filtered)}", file=sys.stderr)
    dict_n = sum(1 for c in filtered if c.kind == "dictionary")
    gloss_n = sum(1 for c in filtered if c.kind == "glossary")
    print(f"  dictionary-shape: {dict_n}", file=sys.stderr)
    print(f"  glossary-shape:   {gloss_n}", file=sys.stderr)


def write_output(candidates: list[Candidate], out_path: Path, args) -> None:
    from datetime import datetime
    now = datetime.now().strftime("%Y-%m-%d %H:%M %Z").strip()

    lines = []
    lines.append("# Candidate Entries — Triage Document")
    lines.append("")
    lines.append(f"*Auto-generated by `scripts/build-candidate-entries.py` on {now}. "
                 f"Not linked from the public site. This file is a working triage document for "
                 f"Prof. Langenkamp to pick the next entries to draft.*")
    lines.append("")
    lines.append("## How to use this file")
    lines.append("")
    lines.append("Each candidate has been scored by:")
    lines.append("")
    lines.append("- **Internal references** (`int`): how many existing entries already mention the term")
    lines.append("- **External references** (`ext`): how many workspace materials (Koebler, Cherny, etc.) mention it")
    lines.append("- **🔗 Promised**: an existing entry contains a Markdown link to a non-existent `.md` file with this slug")
    lines.append("- **Kind**: 📖 `dictionary` (full essay-shape) or 📇 `glossary` (reference-card stub)")
    lines.append("- **Flags**: PERSON / BRAND / MODEL / LAB / CONCEPT / TOOL / HARDWARE")
    lines.append("")
    lines.append("**Triage workflow**: read down each section, mark candidates you want to tackle with `[x]` and "
                 "those to skip with `[-]`. Bring the marked list back to Thea to start drafting.")
    lines.append("")
    lines.append("To regenerate: `python3 scripts/build-candidate-entries.py` (add `--wide` for a noisier scan).")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Section 1: dictionary candidates
    dict_cands = [c for c in candidates if c.kind == "dictionary"]
    lines.append(f"## 📖 Dictionary candidates ({len(dict_cands)})")
    lines.append("")
    lines.append("Substantive essays. 1,500–3,000 words. Voice, footnotes, See-also block, load-bearing thesis.")
    lines.append("")
    for c in dict_cands:
        lines.append(format_candidate(c))
    lines.append("")
    lines.append("---")
    lines.append("")

    # Section 2: glossary candidates
    gloss_cands = [c for c in candidates if c.kind == "glossary"]
    lines.append(f"## 📇 Glossary candidates ({len(gloss_cands)})")
    lines.append("")
    lines.append("Reference cards. 100–250 words. One paragraph defining the thing, one paragraph naming where "
                 "in the Dictionary it shows up. See-also of 2–4 links.")
    lines.append("")
    for c in gloss_cands:
        lines.append(format_candidate(c))
    lines.append("")
    lines.append("---")
    lines.append("")

    # Footer
    lines.append(f"*{len(candidates)} candidates total. Generated by `scripts/build-candidate-entries.py`. "
                 f"Sources scanned: {len(EXTERNAL_SOURCES)} external + {len(list(ENTRIES_DIR.glob('*.md'))) - 1} internal entries.*")

    out_path.write_text("\n".join(lines), encoding="utf-8")


def format_candidate(c: Candidate) -> str:
    flag_str = " ".join(f"`{f}`" for f in c.flags) if c.flags else ""
    promised = " 🔗 *promised*" if c.is_promised_link else ""
    lines = [
        f"### [ ] **{c.term}**  ({c.kind})  {flag_str}{promised}",
        "",
        f"`int:{c.internal_count}  ext:{c.external_count}  slug:`{c.slug}`",
        "",
    ]
    if c.notes:
        lines.append(f"- {c.notes}")
    if c.sample_sources:
        lines.append(f"- Sample internal references: {', '.join(c.sample_sources)}")
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
