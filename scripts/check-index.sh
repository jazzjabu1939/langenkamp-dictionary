#!/usr/bin/env bash
# check-index.sh — verifies that entries/index.md lists every entry file on disk.
#
# Run before commit/push, or in CI. Exits non-zero on drift, prints what is
# missing or stale.
#
# Why this exists: the alphabetical "All Entries" list at /entries/ is hand-
# maintained. New entries got published as files but forgotten in the index
# (May 5, 2026 incident: On Beginning + Mediation a la Gibson both missing).
# This script makes drift impossible to ship silently.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ENTRIES_DIR="$REPO_ROOT/entries"
INDEX_FILE="$ENTRIES_DIR/index.md"

if [[ ! -f "$INDEX_FILE" ]]; then
  echo "ERROR: $INDEX_FILE not found" >&2
  exit 2
fi

# If index.md uses Liquid templating to auto-generate the listing from
# site.pages, drift is structurally impossible — every entry file is
# read at build time. In that case, the hand-written check below does
# not apply. Detect the template pattern and exit clean.
if grep -q 'site.pages | where_exp' "$INDEX_FILE"; then
  count=$(ls "$ENTRIES_DIR"/*.md | grep -v '/index.md$' | wc -l | tr -d ' ')
  echo "✅ entries/index.md uses Liquid auto-generation ($count entries on disk; all included automatically)"
  exit 0
fi

# Entries on disk: every *.md in entries/ except index.md itself
disk_entries=$(ls "$ENTRIES_DIR"/*.md \
  | xargs -I{} basename {} .md \
  | grep -v '^index$' \
  | sort)

# Entries listed in index.md: extract slugs from markdown links like (slug.md)
indexed_entries=$(grep -oE '\(([a-z0-9-]+)\.md\)' "$INDEX_FILE" \
  | sed 's/[()]//g; s/\.md//g' \
  | sort \
  | uniq)

# Diff
missing_from_index=$(comm -23 <(echo "$disk_entries") <(echo "$indexed_entries"))
stale_in_index=$(comm -13 <(echo "$disk_entries") <(echo "$indexed_entries"))

problems=0

if [[ -n "$missing_from_index" ]]; then
  echo "❌ Entries on disk but NOT in entries/index.md:"
  echo "$missing_from_index" | sed 's/^/   - /'
  problems=1
fi

if [[ -n "$stale_in_index" ]]; then
  echo "❌ Entries linked in index.md but NOT on disk:"
  echo "$stale_in_index" | sed 's/^/   - /'
  problems=1
fi

# topics.md is editorial (entries are grouped by theme, not all listed in a single
# A–Z list), so missing entries there are a *warning*, not a hard failure. We still
# surface them so they are not invisible.
TOPICS_FILE="$REPO_ROOT/topics.md"
if [[ -f "$TOPICS_FILE" ]]; then
  topics_entries=$(grep -oE '\(entries/([a-z0-9-]+)\.md\)' "$TOPICS_FILE" \
    | sed 's|(entries/||; s|\.md)||' \
    | sort -u)
  missing_from_topics=$(comm -23 <(echo "$disk_entries") <(echo "$topics_entries"))
  if [[ -n "$missing_from_topics" ]]; then
    echo "⚠️  Entries on disk but NOT in topics.md (warning, editorial decision):"
    echo "$missing_from_topics" | sed 's/^/   - /'
    echo ""
  fi
fi

if [[ $problems -eq 0 ]]; then
  count=$(echo "$disk_entries" | wc -l | tr -d ' ')
  echo "✅ entries/index.md is in sync ($count entries)"
  exit 0
fi

echo ""
echo "Fix: edit entries/index.md to match the entry files on disk."
exit 1
