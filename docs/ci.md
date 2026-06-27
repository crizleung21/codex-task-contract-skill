# CI

Status: v0.4.0 CI guide.

The CI workflow must mirror the local release validation sequence as closely as possible.

## Workflow

```text
.github/workflows/validate.yml
```

The workflow runs on:
- push;
- pull request;
- workflow dispatch.

## CI Steps

The workflow should run:

```bash
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
bash scripts/validate-loop-contract-fixtures.sh
python3 scripts/validate-schemas.py
python3 scripts/validate-docs.py
python3 scripts/run-snapshots.py
python3 scripts/test-loop-runner.py
```

## Local Parity

Before release, run the same commands locally from the repository root.

```bash
bash scripts/sync-plugin-package.sh
bash scripts/validate-repo.sh
bash scripts/validate-loop-contract-fixtures.sh
python3 scripts/validate-schemas.py
python3 scripts/validate-docs.py
python3 scripts/run-snapshots.py
python3 scripts/test-loop-runner.py
git status
```

## Network Boundary

v0.4.0 validation should use committed repository files only. Validation should not require network access.

## Release Gate

A v0.4.0 tag should not be created until the latest CI run is green and local validation has passed after plugin package sync.
