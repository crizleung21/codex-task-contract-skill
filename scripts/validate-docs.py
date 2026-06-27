#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_DOCS = [
    'README.md',
    'CHANGELOG.md',
    'AGENTS.md',
    'IMPLEMENTATION__PLAN.md',
    'docs/testing.md',
    'docs/release-process.md',
    'docs/roadmap.md',
    'docs/validator-design.md',
    'docs/schema-design.md',
    'docs/snapshot-testing.md',
    'docs/ci.md',
    'docs/v0.3.0-release-checklist.md',
]

def main():
    issues = []
    for rel in REQUIRED_DOCS:
        path = ROOT / rel
        if not path.is_file():
            issues.append('missing docs file: ' + rel)
            continue
        text = path.read_text(encoding='utf-8')
        if text.count('\n# ') > 0:
            issues.append('extra H1 heading in: ' + rel)
        if not text.startswith('# '):
            issues.append('missing H1 heading in: ' + rel)

    checklist = ROOT / 'docs' / 'v0.3.0-release-checklist.md'
    if checklist.is_file():
        text = checklist.read_text(encoding='utf-8')
        for term in ['v0.3.0', 'validate-repo.sh', 'validate-plugin-sync.py', 'validate-schemas.py']:
            if term not in text:
                issues.append('release checklist missing term: ' + term)

    if issues:
        for item in issues:
            print('FAIL: ' + item)
        print('Documentation validation failed: ' + str(len(issues)) + ' issue(s).')
        return 1

    print('Documentation validation passed.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
