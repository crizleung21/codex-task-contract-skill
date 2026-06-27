# Validator Design

This document records the intended local validation scope for v0.2.0.

## Repository Validator

`validate-repo.py` should check:

- required file inventory;
- Skill metadata;
- plugin manifest local invariants;
- version consistency;
- fixture mode consistency;
- template and checklist consistency.

## Loop Fixture Validator

`validate-loop-contract-fixtures.py` should check:

- loop expected files exist;
- required Loop Contract fields are present;
- Loop Log columns are present;
- Stop Conditions are present;
- Escalation Triggers are present;
- Approval Gate appears for high-impact fixtures;
- open-ended loop phrasing is absent.

## Boundary

These validators are local release-readiness checks. They are not a substitute for human review.
