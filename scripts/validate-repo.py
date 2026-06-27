#!/usr/bin/env python3
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    'README.md',
    'CHANGELOG.md',
    'AGENTS.md',
    '.github/workflows/validate.yml',
    '.agents/plugins/marketplace.json',
    'skills/task-contract/SKILL.md',
    'skills/task-contract/assets/compact-contract-template.md',
    'skills/task-contract/assets/full-contract-template.md',
    'skills/task-contract/assets/loop-contract-template.md',
    'skills/task-contract/assets/compact-loop-contract-template.md',
    'skills/task-contract/assets/full-loop-contract-template.md',
    'skills/task-contract/references/subagent-delegation-policy.md',
    'skills/task-contract/assets/subagent-contract-template.md',
    'skills/task-contract/tests/expected/subagent-delegation-task.expected.md',
    'skills/task-contract/tests/snapshots/README.md',
    'plugin/codex-task-contract-skill/.codex-plugin/plugin.json',
    'docs/installation.md',
    'docs/usage.md',
    'docs/testing.md',
    'docs/release-process.md',
    'docs/roadmap.md',
    'docs/validator-design.md',
    'docs/plugin-packaging.md',
    'docs/plugin-manifest.md',
    'docs/schema-design.md',
    'docs/snapshot-testing.md',
    'docs/ci.md',
    'docs/v0.3.0-release-checklist.md',
    'schemas/task-contract.schema.json',
    'schemas/loop-contract.schema.json',
    'schemas/expected-output.schema.json',
    'schemas/plugin-local-invariants.schema.json',
    'schemas/subagent-contract.schema.json',
    'scripts/validate-repo.sh',
    'scripts/validate-repo.py',
    'scripts/validate-loop-contract-fixtures.sh',
    'scripts/validate-loop-contract-fixtures.py',
    'scripts/validate-schemas.py',
    'scripts/validate-plugin-sync.py',
    'scripts/validate-docs.py',
    'scripts/run-snapshots.py',
    'scripts/sync-plugin-package.sh',
    'scripts/pre-commit-hook.sh',
    'scripts/install-git-hooks.sh',
    'scripts/test-loop-runner.py',
    'skills/task-contract/tests/loop-regression-tests.json',
]

EXPECTED_MODES = {
    'simple-writing-task.expected.md': 'Mode: Compact Contract',
    'vague-repo-task.expected.md': 'Mode: Full Contract',
    'high-risk-refactor-task.expected.md': 'Mode: Full Contract with Approval Gate',
    'documentation-task.expected.md': 'Mode: Full Contract',
    'research-task.expected.md': 'Mode: Full Contract',
    'destructive-file-task.expected.md': 'Mode: Full Contract with Approval Gate',
    'loop-debug-task.expected.md': 'Mode: Loop Contract Mode',
    'loop-research-task.expected.md': 'Mode: Loop Contract Mode',
    'loop-documentation-task.expected.md': 'Mode: Loop Contract Mode',
    'loop-dangerous-task.expected.md': 'Mode: Loop Contract Mode with Approval Gate',
    'loop-repo-maintenance-task.expected.md': 'Mode: Loop Contract Mode',
    'subagent-delegation-task.expected.md': 'Mode: Full Contract with Subagent Delegation',
}

SCHEMA_FILES = [
    'task-contract.schema.json',
    'loop-contract.schema.json',
    'expected-output.schema.json',
    'plugin-local-invariants.schema.json',
    'subagent-contract.schema.json',
]

def fail(message, failures):
    failures.append(message)
    print('FAIL: ' + message)

def validate_schema_file(path, failures):
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as exc:
        fail(str(path.relative_to(ROOT)) + ' is not valid JSON: ' + str(exc), failures)
        return

    for field in ['$schema', 'title', 'type', 'properties']:
        if field not in data:
            fail(str(path.relative_to(ROOT)) + ' missing schema field: ' + field, failures)

    if data.get('type') != 'object':
        fail(str(path.relative_to(ROOT)) + ' must use top-level type object', failures)

    if not isinstance(data.get('required'), list) or not data.get('required'):
        fail(str(path.relative_to(ROOT)) + ' must define non-empty required fields', failures)

    if 'draft' not in data.get('description', '').lower():
        fail(str(path.relative_to(ROOT)) + ' must state draft status in description', failures)

def require_terms(rel_path, terms, failures):
    path = ROOT / rel_path
    if not path.is_file():
        return
    text = path.read_text(encoding='utf-8')
    for term in terms:
        if term not in text:
            fail(rel_path + ' missing required term: ' + term, failures)

def main():
    failures = []

    for file in REQUIRED_FILES:
        if not (ROOT / file).is_file():
            fail('missing required file: ' + file, failures)

    require_terms('skills/task-contract/SKILL.md', ['name: task-contract', 'Approval Gate', 'Loop Contract Mode', 'Adjustment Strategy'], failures)
    require_terms('README.md', ['v0.3.0', 'validate-schemas.py', 'run-snapshots.py'], failures)
    require_terms('CHANGELOG.md', ['[0.3.0]', 'Schema validator', 'Plugin package sync validator'], failures)
    require_terms('AGENTS.md', ['Schema Policy', 'CI Policy', 'Snapshot Policy'], failures)
    require_terms('docs/release-process.md', ['v0.3.0', 'validate-schemas.py', 'run-snapshots.py'], failures)
    require_terms('docs/v0.3.0-release-checklist.md', ['v0.3.0', 'validate-plugin-sync.py', 'validate-schemas.py'], failures)
    require_terms('.github/workflows/validate.yml', ['validate-repo.sh', 'validate-schemas.py', 'run-snapshots.py'], failures)

    manifest = ROOT / 'plugin/codex-task-contract-skill/.codex-plugin/plugin.json'
    if manifest.is_file():
        data = json.loads(manifest.read_text(encoding='utf-8'))
        if data.get('name') != 'codex-task-contract-skill':
            fail('plugin manifest name mismatch', failures)
        if data.get('version') != '0.3.2':
            fail('plugin manifest version must be 0.3.2 for v0.3.2 release', failures)
        if data.get('skills') != './skills/':
            fail('plugin manifest skills path mismatch', failures)

    expected_dir = ROOT / 'skills/task-contract/tests/expected'
    for filename, mode in EXPECTED_MODES.items():
        path = expected_dir / filename
        if not path.is_file():
            fail('missing expected fixture: ' + filename, failures)
            continue
        text = path.read_text(encoding='utf-8')
        if mode not in text:
            fail(filename + ' missing deterministic mode: ' + mode, failures)

    schema_dir = ROOT / 'schemas'
    for filename in SCHEMA_FILES:
        path = schema_dir / filename
        if path.is_file():
            validate_schema_file(path, failures)

    if failures:
        print('Repository validation failed: ' + str(len(failures)) + ' issue(s).')
        return 1

    print('Repository validation passed.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
