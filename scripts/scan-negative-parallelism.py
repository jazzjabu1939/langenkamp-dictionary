#!/usr/bin/env python3
"""
scan-negative-parallelism.py

Scans Langenkamp Dictionary entries for negative-parallelism constructions
("not just X, Y"; "not X but Y"; "It is not X. It is Y." etc.) and reports
per-entry counts and density (occurrences per 1000 words).

The catalogue distinguishes between AI-shaped (rhetorically "free") uses and
constructions that may be doing real work. Manual review is still required —
the scanner is a triage tool, not a judge.

Usage:
    python3 scripts/scan-negative-parallelism.py [--verbose] [--top N]
"""

from __future__ import annotations
import argparse
import re
from pathlib import Path
from collections import defaultdict

ENTRIES_DIR = Path(__file__).resolve().parent.parent / "entries"

# Patterns. Each is (label, regex). Designed to catch the family without
# triggering on every legitimate negative ("not yet", "do not", etc.).
PATTERNS = [
    # "not just X, [it's/this is/Y]"
    ("not_just_X_Y", re.compile(
        r"\bnot just\s+[^.,;:!?\n]{2,80}[,\u2014\-]\s*(?:it[' ]?s|this is|but|they are|but rather|but instead|\u2014)\b",
        re.IGNORECASE,
    )),
    # "not only X, [but/Y]"
    ("not_only_X_Y", re.compile(
        r"\bnot only\s+[^.,;:!?\n]{2,80}[,\u2014\-]\s*(?:but|it[' ]?s|this is|\u2014)\b",
        re.IGNORECASE,
    )),
    # "not merely/simply X, [but/Y]"
    ("not_merely_X_Y", re.compile(
        r"\bnot (?:merely|simply)\s+[^.,;:!?\n]{2,80}[,\u2014\-]\s*(?:but|it[' ]?s|this is|\u2014)\b",
        re.IGNORECASE,
    )),
    # ", not X but Y" or ", not X, Y" or ", not X \u2014 Y"
    ("comma_not_X_Y", re.compile(
        r",\s+not\s+[a-z][^.,;:!?\n]{2,60}\s+(?:but|\u2014|\-\-)\s+[a-z]",
        re.IGNORECASE,
    )),
    # "It is not X. It is Y." / "It is not X \u2014 it is Y" / "This is not X. It is Y."
    ("it_is_not_X_it_is_Y", re.compile(
        r"\b(?:it is|it[' ]?s|this is|that is)\s+not\s+[^.;:\n\u2014]{3,80}[.;\u2014]\s+(?:it is|it[' ]?s|this is|that is)\s+[a-z]",
        re.IGNORECASE,
    )),
    # "X is not Y. X is Z." (parallel anaphora)
    # Looser: subject not predicate. predicate. subject (same).
    # This one is risky; we'll keep it narrow to "The X is not...".
    ("the_X_is_not_then_is", re.compile(
        r"\bThe [a-z]+ is not\s+[^.;:\n]{3,60}\.\s+(?:It is|The [a-z]+ is)\b",
    )),
    # "not because X, but because Y"
    ("not_because_X_because_Y", re.compile(
        r"\bnot because\s+[^.,;:!?\n]{3,80},?\s*but because\b",
        re.IGNORECASE,
    )),
    # "from X to Y" parallels are different family; skip.
]

# Things that look like negative parallelism but aren't lazy-AI:
# - "not yet" alone
# - "is not a criticism" set up as anticipated misreading (still parallelism but earned)
# We won't filter these out automatically; we report and let humans decide.

def count_words(text: str) -> int:
    # Approximate word count; close enough for density.
    return len(re.findall(r"\b\w+\b", text))


def scan_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    # Strip front-matter and HTML comments to avoid false positives.
    text_body = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)
    text_body = re.sub(r"<!--.*?-->", "", text_body, flags=re.DOTALL)

    word_count = count_words(text_body)
    counts = defaultdict(int)
    examples = defaultdict(list)
    total = 0

    # Map of pattern_label -> list of (line_number, snippet)
    for label, regex in PATTERNS:
        for m in regex.finditer(text_body):
            counts[label] += 1
            total += 1
            # Find line number in original text
            start = m.start()
            # Compute line number by counting newlines up to start in text_body.
            line_no = text_body.count("\n", 0, start) + 1
            snippet = m.group(0).strip()
            if len(snippet) > 140:
                snippet = snippet[:137] + "..."
            examples[label].append((line_no, snippet))

    density = (total / word_count * 1000) if word_count else 0.0

    return {
        "path": path,
        "words": word_count,
        "total": total,
        "counts": dict(counts),
        "examples": dict(examples),
        "density": density,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--top", type=int, default=15,
                        help="Show the top N entries by density")
    parser.add_argument("--verbose", action="store_true",
                        help="Print example snippets for top entries")
    parser.add_argument("--min-words", type=int, default=200,
                        help="Skip entries with fewer than this many words "
                             "(short stubs distort density)")
    args = parser.parse_args()

    results = []
    for path in sorted(ENTRIES_DIR.glob("*.md")):
        if path.name == "index.md":
            continue
        r = scan_file(path)
        if r["words"] < args.min_words:
            continue
        results.append(r)

    # Totals
    grand_total = sum(r["total"] for r in results)
    grand_words = sum(r["words"] for r in results)
    grand_density = grand_total / grand_words * 1000 if grand_words else 0

    print(f"=== Langenkamp Dictionary: Negative-Parallelism Scan ===")
    print(f"Entries scanned: {len(results)} (min {args.min_words} words)")
    print(f"Total words:     {grand_words:,}")
    print(f"Total hits:      {grand_total}")
    print(f"Corpus density:  {grand_density:.2f} per 1000 words")
    print()

    print("--- By raw count (top of corpus offenders) ---")
    by_total = sorted(results, key=lambda r: r["total"], reverse=True)
    for r in by_total[:args.top]:
        print(f"  {r['total']:>3}  ({r['density']:>5.2f}/1k, {r['words']:>5}w)  {r['path'].name}")
    print()

    print("--- By density per 1000 words (style fingerprint) ---")
    by_density = sorted(results, key=lambda r: r["density"], reverse=True)
    for r in by_density[:args.top]:
        if r["total"] == 0:
            continue
        print(f"  {r['density']:>5.2f}/1k  ({r['total']:>2} in {r['words']:>5}w)  {r['path'].name}")
    print()

    print("--- Construction-family breakdown ---")
    family_totals = defaultdict(int)
    for r in results:
        for label, n in r["counts"].items():
            family_totals[label] += n
    for label, n in sorted(family_totals.items(), key=lambda kv: -kv[1]):
        print(f"  {n:>3}  {label}")
    print()

    if args.verbose:
        print("--- Examples from top density entries ---")
        for r in by_density[:5]:
            if r["total"] == 0:
                continue
            print(f"\n### {r['path'].name}  ({r['density']:.2f}/1k)")
            for label, items in r["examples"].items():
                for line_no, snippet in items[:3]:
                    print(f"  L{line_no:>4} [{label}]")
                    print(f"    {snippet}")


if __name__ == "__main__":
    main()
