#!/usr/bin/env bash
# check-entry-kinds.sh — requires every tracked, published entry to declare its editorial form.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

problems=0
checked=0

while IFS= read -r file; do
  [[ "$file" == "entries/index.md" ]] && continue

  frontmatter=$(awk '/^---$/{c++; next} c==1{print} c==2{exit}' "$file")
  if grep -qE '^published:[[:space:]]*false([[:space:]]*)$' <<<"$frontmatter"; then
    continue
  fi

  checked=$((checked + 1))
  kind=$(sed -nE 's/^kind:[[:space:]]*([^[:space:]#]+).*$/\1/p' <<<"$frontmatter" | head -n 1)

  case "$kind" in
    glossary|reference|essay) ;;
    "")
      echo "ERROR: $file has no explicit kind (glossary, reference, or essay)" >&2
      problems=1
      ;;
    *)
      echo "ERROR: $file has invalid kind: $kind" >&2
      problems=1
      ;;
  esac
done < <(git ls-files 'entries/*.md' | sort)

if [[ $problems -ne 0 ]]; then
  exit 1
fi

echo "Entry kinds are explicit and valid ($checked published entries checked)"
