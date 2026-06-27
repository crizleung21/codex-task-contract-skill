#!/bin/bash
# Install Git hooks for codex-task-contract-skill

HOOK_SOURCE="scripts/pre-commit-hook.sh"
HOOK_TARGET=".git/hooks/pre-commit"

if [ ! -d ".git" ]; then
  echo "ERROR: .git directory not found. Please run this script from the repository root."
  exit 1
fi

echo "Installing pre-commit hook..."
cp "$HOOK_SOURCE" "$HOOK_TARGET"
chmod +x "$HOOK_TARGET"

echo "Git pre-commit hook installed successfully at $HOOK_TARGET"
