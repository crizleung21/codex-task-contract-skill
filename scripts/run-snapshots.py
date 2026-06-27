#!/usr/bin/env python3
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_DIR = ROOT / 'skills' / 'task-contract' / 'tests' / 'snapshots'
SNAPSHOT_README = SNAPSHOT_DIR / 'README.md'
SNAPSHOT_DOC = ROOT / 'docs' / 'snapshot-testing.md'
FIXTURE_DIR = ROOT / 'skills' / 'task-contract' / 'tests' / 'fixtures'

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

    if not SNAPSHOT_DIR.is_dir():
        issues.append('missing snapshot directory')
    if not SNAPSHOT_README.is_file():
        issues.append('missing snapshot README')
    if not SNAPSHOT_DOC.is_file():
        issues.append('missing docs/snapshot-testing.md')

    if SNAPSHOT_README.is_file():
        text = SNAPSHOT_README.read_text(encoding='utf-8')
        for term in ['expected mode', 'required sections', 'approval requirements']:
            if term not in text:
                issues.append('snapshot README missing term: ' + term)

    if SNAPSHOT_DOC.is_file():
        text = SNAPSHOT_DOC.read_text(encoding='utf-8')
        for term in ['snapshot', version_tag, 'required sections']:
            if term not in text:
                issues.append(f'snapshot doc missing term: {term}')

    # Validate snapshot file coverage and contents
    if FIXTURE_DIR.is_dir() and SNAPSHOT_DIR.is_dir():
        fixtures = [f for f in FIXTURE_DIR.glob('*.md')]
        for fixture in fixtures:
            snapshot_name = fixture.name.replace('.md', '.snapshot.md')
            snapshot_path = SNAPSHOT_DIR / snapshot_name
            if not snapshot_path.is_file():
                issues.append(f'missing snapshot file for fixture: {fixture.name} -> {snapshot_name}')
            else:
                # Validate snapshot contents
                content = snapshot_path.read_text(encoding='utf-8')
                required_headers = [
                    '# Snapshot:',
                    '## Expected Mode',
                    '## Required Sections',
                    '## Required Fields',
                    '## Required Checks',
                    '## Approval Requirements',
                    '## Forbidden Patterns',
                    '## Reviewer Notes'
                ]
                for header in required_headers:
                    if header not in content:
                        issues.append(f'{snapshot_name}: missing required section "{header}"')
                
                # Check for empty sections or placeholder values
                placeholders = ['...', '[placeholder]', 'TBD', 'TODO']
                for placeholder in placeholders:
                    if placeholder in content:
                        issues.append(f'{snapshot_name}: contains placeholder value "{placeholder}"')

    if issues:
        for item in issues:
            print('FAIL: ' + item)
        print('Snapshot protocol validation failed: ' + str(len(issues)) + ' issue(s).')
        return 1

    print('Snapshot protocol validation passed.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
