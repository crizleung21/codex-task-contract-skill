# Loop Observation Methods

This reference defines acceptable observation methods for stable Loop Contract Mode.

## Observation Matrix

| Loop Type | Observation Method | Acceptable Evidence | Not Acceptable |
|---|---|---|---|
| Simple loop | Checklist or direct output review. | Checklist result, visible output comparison. | Vague claim that it is better. |
| Coding/debug loop | Test, lint, build, log, or diff review. | Command output, failing test, passing test, changed file summary. | Claiming validation without evidence. |
| Research loop | Source review and coverage check. | Citations, source coverage, contradiction check. | Unsupported summary. |
| Documentation loop | Coverage and consistency review. | Missing-section list, link or path consistency, table coverage. | Subjective quality only. |
| Repo maintenance loop | File map, script output, checklist, or diff review. | Changed files, validation output, release checklist result. | Broad statement that repo is clean. |
| High-impact loop | Inspection only unless approved. | Impact analysis, decision point, approval request. | Unapproved execution. |

## Observation Rules

1. Observation must be visible to the user.
2. Observation must be tied to acceptance criteria.
3. Observation must occur after one bounded iteration unit.
4. Observation must not be invented.
5. Observation may be a limitation statement when validation cannot be performed.

## Evidence Summary Format

```md
Observation: [what was checked]
Evidence: [test output, citation, diff summary, checklist result, or limitation]
Impact: [what this means for the loop]
```
