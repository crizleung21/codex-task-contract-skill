#!/usr/bin/env bash
set -euo pipefail

if command -v markdownlint >/dev/null 2>&1; then
  markdownlint "**/*.md"
else
  echo "markdownlint is not installed; skipping markdown lint."
fi
