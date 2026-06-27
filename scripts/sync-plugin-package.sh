#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$ROOT/skills/task-contract"
DEST="$ROOT/plugin/codex-task-contract-skill/skills/task-contract"

rm -rf "$DEST"
mkdir -p "$(dirname "$DEST")"
cp -R "$SRC" "$DEST"

echo "Synced task-contract skill into plugin package."
