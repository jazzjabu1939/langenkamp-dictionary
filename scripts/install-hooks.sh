#!/usr/bin/env bash
# install-hooks.sh — installs git hooks that protect the Dictionary.
# Idempotent: safe to re-run.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HOOK_DIR="$REPO_ROOT/.git/hooks"
PRE_COMMIT="$HOOK_DIR/pre-commit"

mkdir -p "$HOOK_DIR"

cat > "$PRE_COMMIT" <<'HOOK'
#!/usr/bin/env bash
# Auto-installed by scripts/install-hooks.sh
# Blocks commits with unclassified entries or an unhealthy entries index.

set -e
REPO_ROOT="$(git rev-parse --show-toplevel)"
"$REPO_ROOT/scripts/check-entry-kinds.sh"
"$REPO_ROOT/scripts/check-index.sh"
HOOK

chmod +x "$PRE_COMMIT"
echo "✅ pre-commit hook installed at $PRE_COMMIT"
echo "   Runs entry-kind and index checks before every commit."
