#!/usr/bin/env python3
from pathlib import Path
import hashlib
import sys

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / 'skills' / 'task-contract'
PACKAGED = ROOT / 'plugin' / 'codex-task-contract-skill' / 'skills' / 'task-contract'

IGNORED_NAMES = {
    '.DS_Store',
}

def fail(message, failures):
    failures.append(message)
    print('FAIL: ' + message)

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def collect_files(base):
    result = {}
    for path in base.rglob('*'):
        if not path.is_file():
            continue
        if path.name in IGNORED_NAMES:
            continue
        result[path.relative_to(base).as_posix()] = path
    return result

def main():
    failures = []

    if not CANONICAL.is_dir():
        fail('missing canonical Skill directory: ' + str(CANONICAL.relative_to(ROOT)), failures)
    if not PACKAGED.is_dir():
        fail('missing packaged Skill directory: ' + str(PACKAGED.relative_to(ROOT)), failures)

    if failures:
        print('Plugin sync validation failed: ' + str(len(failures)) + ' issue(s).')
        return 1

    canonical_files = collect_files(CANONICAL)
    packaged_files = collect_files(PACKAGED)

    canonical_set = set(canonical_files)
    packaged_set = set(packaged_files)

    for missing in sorted(canonical_set - packaged_set):
        fail('packaged Skill missing file: ' + missing, failures)

    for extra in sorted(packaged_set - canonical_set):
        fail('packaged Skill has extra file: ' + extra, failures)

    for relative in sorted(canonical_set & packaged_set):
        if digest(canonical_files[relative]) != digest(packaged_files[relative]):
            fail('packaged Skill drift: ' + relative, failures)

    if failures:
        print('Plugin sync validation failed: ' + str(len(failures)) + ' issue(s).')
        return 1

    print('Plugin sync validation passed.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
