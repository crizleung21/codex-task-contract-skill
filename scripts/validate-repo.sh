#!/usr/bin/env bash
set -euo pipefail

required_files=(
  "README.md"
  "IMPLEMENTATION__PLAN.md"
  "skills/task-contract/SKILL.md"
  "plugin/codex-task-contract-skill/.codex-plugin/plugin.json"
  ".agents/plugins/marketplace.json"
  "docs/installation.md"
  "docs/usage.md"
  "docs/testing.md"
)

for file in "${required_files[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "Missing required file: $file"
    exit 1
  fi
done

grep -q "name: task-contract" skills/task-contract/SKILL.md

echo "Repository validation passed."
