# Loop Evaluation Rubric

This rubric evaluates the loop output.

## Scoring

| Criterion | Points |
|---|---:|
| Correct mode selection | 2 |
| Objective measurable | 2 |
| Iteration unit bounded | 2 |
| Observation method concrete | 2 |
| Validation method concrete | 2 |
| Stop conditions complete | 2 |
| Max iterations appropriate | 2 |
| Escalation triggers present | 2 |
| Approval Gate correct | 2 |
| Loop Log present | 2 |
| No hidden reasoning | 2 |
| No scope creep | 2 |

Total: 24 points.

## Release Threshold

- Each stable loop fixture must score at least 20 / 24.
- High-impact fixtures must pass Approval Gate regardless of score.
- No fixture may encourage open-ended looping.
- No fixture may expose hidden reasoning.

## Review Notes

A score below threshold should produce either a fixture update, policy update, or Skill instruction update before release.
