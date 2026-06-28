#!/usr/bin/env python3
import json
import sys
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

def main():
    failures = []

    # 1. Load release config
    config_path = ROOT / 'config' / 'release.json'
    if not config_path.is_file():
        print("FAIL: missing release configuration: config/release.json")
        return 1
    try:
        config = json.loads(config_path.read_text(encoding='utf-8'))
    except Exception as exc:
        print("FAIL: failed to parse config/release.json: " + str(exc))
        return 1

    version_tag = config.get('release_tag')  # e.g., "v0.5.0"
    version_target = config.get('release_target')  # e.g., "0.5.0"
    schema_version = config.get('schema_version')  # e.g., "0.5.0-draft"
    
    if not version_tag or not version_target or not schema_version:
        print("FAIL: config/release.json missing release_tag, release_target, or schema_version")
        return 1

    # 2. Check plugin manifest version
    manifest_path = ROOT / 'plugin' / 'codex-task-contract-skill' / '.codex-plugin' / 'plugin.json'
    if not manifest_path.is_file():
        failures.append(f"missing plugin manifest: {manifest_path.relative_to(ROOT)}")
    else:
        try:
            manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
            manifest_version = manifest.get('version')
            if manifest_version != version_target:
                failures.append(f"plugin.json version ({manifest_version}) does not match release target ({version_target})")
        except Exception as exc:
            failures.append(f"failed to parse plugin.json: {exc}")

    # 3. Check schema version defaults
    schema_dir = ROOT / 'schemas'
    if not schema_dir.is_dir():
        failures.append("missing schemas directory")
    else:
        for schema_path in schema_dir.glob('*.schema.json'):
            try:
                schema = json.loads(schema_path.read_text(encoding='utf-8'))
                default_ver = schema.get('properties', {}).get('schema_version', {}).get('default')
                if default_ver != schema_version:
                    failures.append(f"{schema_path.name}: schema_version default ({default_ver}) does not match expected ({schema_version})")
            except Exception as exc:
                failures.append(f"failed to parse {schema_path.name}: {exc}")

    # 4. Check active release checklist existence
    active_checklist_path = ROOT / 'docs' / f"{version_tag}-release-checklist.md"
    if not active_checklist_path.is_file():
        failures.append(f"missing active release checklist: {active_checklist_path.relative_to(ROOT)}")

    # 5. Check for stale release checks or release gate references to previous versions (v0.4.0, etc.)
    # in active docs and scripts (excluding CHANGELOG.md, docs/roadmap.md, archive directories)
    stale_patterns = [
        re.compile(r'v0\.4\.0\s+(?:release check|release gate|Release Gates|Release Check)', re.IGNORECASE),
        re.compile(r'v0\.3\.0\s+(?:release check|release gate|Release Gates|Release Check)', re.IGNORECASE),
    ]

    exclude_files = {
        'CHANGELOG.md',
        'docs/roadmap.md',
    }

    def should_scan(path):
        rel_posix = path.relative_to(ROOT).as_posix()
        if rel_posix in exclude_files:
            return False
        if 'docs/archive/' in rel_posix:
            return False
        if '.git/' in rel_posix:
            return False
        if 'node_modules/' in rel_posix:
            return False
        if 'brain/' in rel_posix or '.agents/' in rel_posix:
            return False
        return path.suffix in ('.md', '.py', '.sh', '.json', '.yml')

    for path in ROOT.rglob('*'):
        if path.is_file() and should_scan(path):
            try:
                content = path.read_text(encoding='utf-8')
                for pattern in stale_patterns:
                    if pattern.search(content):
                        failures.append(f"{path.relative_to(ROOT)} contains stale release gate/check reference: {pattern.pattern}")
            except Exception as exc:
                pass  # Ignore unreadable files

    # 6. Check that workflows and files contain references to the new validation tasks
    # (specifically validate-release-consistency.py, validate-contract-semantics.py, smoke-test-installation.sh)
    required_validations = [
        'validate-release-consistency.py',
        'validate-contract-semantics.py',
        'smoke-test-installation.sh'
    ]
    
    ci_workflow_path = ROOT / '.github/workflows/validate.yml'
    if ci_workflow_path.is_file():
        ci_content = ci_workflow_path.read_text(encoding='utf-8')
        for v in required_validations:
            if v not in ci_content:
                failures.append(f"CI workflow validate.yml is missing check for {v}")

    # Output results
    if failures:
        print(f"Release consistency validation failed: {len(failures)} issue(s).")
        for fail_msg in failures:
            print(f"FAIL: {fail_msg}")
        return 1

    print("Release consistency validation passed.")
    return 0

if __name__ == '__main__':
    sys.exit(main())
