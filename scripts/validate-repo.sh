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
  "skills/task-contract/references/loop-contract-policy.md"
  "skills/task-contract/references/loop-observation-methods.md"
  "skills/task-contract/references/loop-stop-conditions.md"
  "skills/task-contract/references/loop-escalation-rules.md"
  "skills/task-contract/references/loop-evaluation-rubric.md"
)

for file in "${required_files[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "Missing required file: $file"
    exit 1
  fi
done

grep -q "name: task-contract" skills/task-contract/SKILL.md

if [[ -f scripts/validate-loop-contract-fixtures.py ]]; then
  python3 scripts/validate-loop-contract-fixtures.py
fi

echo "Repository validation passed."
