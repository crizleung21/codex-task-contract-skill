# Loop Escalation Rules

%s

## Mandatory Triggers

Escalate when:

1. multiple valid directions exist;
2. required credentials or permissions are missing;
3. validation cannot be performed;
4. broad restructuring is needed;
5. the loop would exceed the iteration cap;
6. the same failure repeats twice;
7. public behavior, release metadata, security posture, dependencies, or destructive actions may change;
8. continuing would require assumptions that change the outcome.

## Optional Triggers

Escalate when:

- the user asked for speed but quality would materially suffer;
- the requested output conflicts with documented repo policy;
- evidence is contradictory;
- the next iteration would be low confidence.

## Approval Gate Wording

```md
## Approval Gate

This loop requires approval before execution because [reason].

Blocked action: [action]
Recommended safe default: [default]
Reply template: Approved: [bounded scope]
```

## Examples

- `Approved: inspect only; do not edit files.`
- `Approved: edit files under docs/ only.`
- `Approved: run one more iteration; do not change release metadata.`
