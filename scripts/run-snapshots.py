#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_DIR = ROOT / 'skills' / 'task-contract' / 'tests' / 'snapshots'
SNAPSHOT_README = SNAPSHOT_DIR / 'README.md'
SNAPSHOT_DOC = ROOT / 'docs' / 'snapshot-testing.md'

def main():
    issues = []

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
        for term in ['snapshot', 'v0.3.0', 'required sections']:
            if term not in text:
                issues.append('snapshot doc missing term: ' + term)

    if issues:
        for item in issues:
            print('FAIL: ' + item)
        print('Snapshot protocol validation failed: ' + str(len(issues)) + ' issue(s).')
        return 1

    print('Snapshot protocol validation passed.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
