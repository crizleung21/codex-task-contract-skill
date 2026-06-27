#!/usr/bin/env python3
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

def main():
    issues = []

    # Load release configuration
    config_path = ROOT / 'config' / 'release.json'
    if not config_path.is_file():
        issues.append('missing release configuration: config/release.json')
        print('FAIL: missing release configuration: config/release.json')
        return 1
    try:
        config = json.loads(config_path.read_text(encoding='utf-8'))
    except Exception as exc:
        issues.append('failed to parse config/release.json: ' + str(exc))
        print('FAIL: failed to parse config/release.json')
        return 1

    version_tag = config.get('release_tag', 'v0.4.0')
    checklist_rel_path = f'docs/{version_tag}-release-checklist.md'

    required_docs = [
        'README.md',
        'CHANGELOG.md',
        'AGENTS.md',
        'docs/testing.md',
        'docs/release-process.md',
        'docs/roadmap.md',
        'docs/validator-design.md',
        'docs/schema-design.md',
        'docs/snapshot-testing.md',
        'docs/ci.md',
        'docs/behavior-contract.md',
        checklist_rel_path,
    ]

    for rel in required_docs:
        path = ROOT / rel
        if not path.is_file():
            issues.append('missing docs file: ' + rel)
            continue
        text = path.read_text(encoding='utf-8')
        if text.count('\n# ') > 0:
            issues.append('extra H1 heading in: ' + rel)
        if not text.startswith('# '):
            issues.append('missing H1 heading in: ' + rel)

    # Validate active checklist
    checklist_path = ROOT / checklist_rel_path
    if checklist_path.is_file():
        text = checklist_path.read_text(encoding='utf-8')
        for term in [version_tag, 'validate-repo.sh', 'validate-plugin-sync.py', 'validate-schemas.py']:
            if term not in text:
                issues.append(f'release checklist missing term: {term}')

    # Validate release target consistency (detect stale references to v0.3.0 as current release gates in active files)
    active_gate_docs = [
        'README.md',
        'AGENTS.md',
        'docs/release-process.md',
        'docs/testing.md',
    ]
    for rel in active_gate_docs:
        path = ROOT / rel
        if path.is_file():
            content = path.read_text(encoding='utf-8')
            if 'v0.3.0 release gate' in content.lower() or 'v0.3.0 release check' in content.lower():
                issues.append(f'{rel} refers to v0.3.0 as the current release gate')

    if issues:
        for item in issues:
            print('FAIL: ' + item)
        print('Documentation validation failed: ' + str(len(issues)) + ' issue(s).')
        return 1

    print('Documentation validation passed.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
