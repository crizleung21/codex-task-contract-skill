#!/bin/bash
# Pre-commit hook for codex-task-contract-skill
echo "Running pre-commit repository validation gates..."

# Execute the validation scripts
bash scripts/sync-plugin-package.sh
if [ $? -ne 0 ]; then
  echo "ERROR: Plugin package sync failed."
  exit 1
fi

bash scripts/validate-repo.sh
if [ $? -ne 0 ]; then
  echo "ERROR: Repository validation failed."
  exit 1
fi

bash scripts/validate-loop-contract-fixtures.sh
if [ $? -ne 0 ]; then
  echo "ERROR: Loop fixture validation failed."
  exit 1
fi

python3 scripts/validate-schemas.py
if [ $? -ne 0 ]; then
  echo "ERROR: Schema validation failed."
  exit 1
fi

python3 scripts/validate-docs.py
if [ $? -ne 0 ]; then
  echo "ERROR: Documentation validation failed."
  exit 1
fi

python3 scripts/run-snapshots.py
if [ $? -ne 0 ]; then
  echo "ERROR: Snapshot protocol validation failed."
  exit 1
fi

python3 scripts/test-loop-runner.py
if [ $? -ne 0 ]; then
  echo "ERROR: Loop regression validation failed."
  exit 1
fi

python3 scripts/validate-release-consistency.py
if [ $? -ne 0 ]; then
  echo "ERROR: Release consistency validation failed."
  exit 1
fi

python3 scripts/validate-contract-semantics.py
if [ $? -ne 0 ]; then
  echo "ERROR: Semantic contract validation failed."
  exit 1
fi

bash scripts/smoke-test-installation.sh
if [ $? -ne 0 ]; then
  echo "ERROR: Installation smoke test failed."
  exit 1
fi

echo "All pre-commit checks passed successfully!"
exit 0
