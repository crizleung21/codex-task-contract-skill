#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Verify release config exists
test -f "$ROOT/config/release.json"
# Verify plugin manifest exists
test -f "$ROOT/plugin/codex-task-contract-skill/.codex-plugin/plugin.json"
# Verify packaged Skill exists
test -f "$ROOT/plugin/codex-task-contract-skill/skills/task-contract/SKILL.md"
# Verify local marketplace metadata exists
test -f "$ROOT/.agents/plugins/marketplace.json"

# Verify plugin sync
python3 "$ROOT/scripts/validate-plugin-sync.py"
# Verify release consistency
python3 "$ROOT/scripts/validate-release-consistency.py"

echo "Installation smoke test passed."
