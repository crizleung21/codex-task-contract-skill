#!/usr/bin/env python3
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / 'schemas'

REQUIRED_SCHEMAS = [
    'task-contract.schema.json',
    'loop-contract.schema.json',
    'expected-output.schema.json',
    'plugin-local-invariants.schema.json',
]

REQUIRED_TOP_LEVEL_FIELDS = [
    '$schema',
    'title',
    'type',
    'properties',
]

def fail(message, failures):
    failures.append(message)
    print('FAIL: ' + message)

def validate_schema(path, failures):
    try:
        data = json.loads(path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as exc:
        fail(str(path.relative_to(ROOT)) + ' is not valid JSON: ' + str(exc), failures)
        return

    for field in REQUIRED_TOP_LEVEL_FIELDS:
        if field not in data:
            fail(str(path.relative_to(ROOT)) + ' missing top-level field: ' + field, failures)

    if data.get('type') != 'object':
        fail(str(path.relative_to(ROOT)) + ' must use top-level type object', failures)

    if 'required' not in data or not isinstance(data.get('required'), list) or not data.get('required'):
        fail(str(path.relative_to(ROOT)) + ' must define non-empty required fields', failures)

    description = data.get('description', '')
    if 'draft' not in description.lower():
        fail(str(path.relative_to(ROOT)) + ' description must state draft status', failures)

def main():
    failures = []

    if not SCHEMA_DIR.is_dir():
        fail('missing schemas directory', failures)
    else:
        for filename in REQUIRED_SCHEMAS:
            path = SCHEMA_DIR / filename
            if not path.is_file():
                fail('missing schema file: schemas/' + filename, failures)
            else:
                validate_schema(path, failures)

    if failures:
        print('Schema validation failed: ' + str(len(failures)) + ' issue(s).')
        return 1

    print('Schema validation passed.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
