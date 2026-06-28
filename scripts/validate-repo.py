#!/usr/bin/env python3
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_TAXONOMY = {
    'simple-writing-task.expected.md': {
        'Base Mode': 'Compact Contract',
        'Modifiers': []
    },
    'vague-repo-task.expected.md': {
        'Base Mode': 'Full Contract',
        'Modifiers': []
    },
    'high-risk-refactor-task.expected.md': {
        'Base Mode': 'Full Contract',
        'Modifiers': ['approval_gate']
    },
    'documentation-task.expected.md': {
        'Base Mode': 'Full Contract',
        'Modifiers': []
    },
    'research-task.expected.md': {
        'Base Mode': 'Full Contract',
        'Modifiers': []
    },
    'destructive-file-task.expected.md': {
        'Base Mode': 'Full Contract',
        'Modifiers': ['approval_gate']
    },
    'loop-debug-task.expected.md': {
        'Base Mode': 'Loop Contract Mode',
        'Modifiers': []
    },
    'loop-research-task.expected.md': {
        'Base Mode': 'Loop Contract Mode',
        'Modifiers': []
    },
    'loop-documentation-task.expected.md': {
        'Base Mode': 'Loop Contract Mode',
        'Modifiers': []
    },
    'loop-dangerous-task.expected.md': {
        'Base Mode': 'Loop Contract Mode',
        'Modifiers': ['approval_gate']
    },
    'loop-repo-maintenance-task.expected.md': {
        'Base Mode': 'Loop Contract Mode',
        'Modifiers': []
    },
    'subagent-delegation-task.expected.md': {
        'Base Mode': 'Full Contract',
        'Modifiers': ['subagent_delegation']
    },
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

    # 1. Load release config
    config_path = ROOT / 'config' / 'release.json'
    if not config_path.is_file():
        fail('missing release configuration: config/release.json', failures)
        return 1
    try:
        config = json.loads(config_path.read_text(encoding='utf-8'))
    except Exception as exc:
        fail('failed to parse config/release.json: ' + str(exc), failures)
        return 1

    version_tag = config.get('release_tag', 'v0.5.0')
    version_target = config.get('release_target', '0.5.0')
    checklist_rel_path = f'docs/{version_tag}-release-checklist.md'

    required_files = [
        'README.md',
        'CHANGELOG.md',
        'AGENTS.md',
        'IMPLEMENTATION__PLAN.md',
        'config/release.json',
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
        'docs/behavior-contract.md',
        checklist_rel_path,
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
        # v0.5.0 added files
        'scripts/validate-release-consistency.py',
        'scripts/validate-contract-semantics.py',
        'scripts/smoke-test-installation.sh',
        'skills/task-contract/tests/FIXTURE_MATRIX.md',
    ]

    for file in required_files:
        if not (ROOT / file).is_file():
            fail('missing required file: ' + file, failures)

    require_terms('skills/task-contract/SKILL.md', ['name: task-contract', 'Approval Gate', 'Loop Contract Mode', 'Adjustment Strategy'], failures)
    require_terms('README.md', [version_tag, 'validate-schemas.py', 'run-snapshots.py', 'test-loop-runner.py'], failures)
    require_terms('CHANGELOG.md', [f'[{version_target}]', 'regression', 'Subagent'], failures)
    require_terms('AGENTS.md', ['Schema Policy', 'CI Policy', 'Snapshot Policy'], failures)
    require_terms('docs/release-process.md', [version_tag, 'validate-schemas.py', 'run-snapshots.py', 'test-loop-runner.py'], failures)
    require_terms(checklist_rel_path, [version_tag, 'validate-plugin-sync.py', 'validate-schemas.py', 'test-loop-runner.py'], failures)
    require_terms('.github/workflows/validate.yml', ['validate-repo.sh', 'validate-schemas.py', 'run-snapshots.py', 'test-loop-runner.py'], failures)

    manifest = ROOT / 'plugin/codex-task-contract-skill/.codex-plugin/plugin.json'
    if manifest.is_file():
        data = json.loads(manifest.read_text(encoding='utf-8'))
        if data.get('name') != 'codex-task-contract-skill':
            fail('plugin manifest name mismatch', failures)
        if data.get('version') != version_target:
            fail(f'plugin manifest version must be {version_target} for {version_tag} release', failures)
        if data.get('skills') != './skills/':
            fail('plugin manifest skills path mismatch', failures)

    expected_dir = ROOT / 'skills/task-contract/tests/expected'
    for filename, taxonomy in EXPECTED_TAXONOMY.items():
        path = expected_dir / filename
        if not path.is_file():
            fail('missing expected fixture: ' + filename, failures)
            continue
        text = path.read_text(encoding='utf-8')
        base_mode_line = f"Base Mode: {taxonomy['Base Mode']}"
        if base_mode_line not in text:
            fail(f"{filename} missing deterministic Base Mode: {taxonomy['Base Mode']}", failures)
        for modifier in taxonomy['Modifiers']:
            modifier_line = f"  - {modifier}"
            if modifier_line not in text:
                fail(f"{filename} missing modifier: {modifier}", failures)

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
