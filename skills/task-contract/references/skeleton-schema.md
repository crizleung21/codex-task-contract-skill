# Auto-Skeleton Schema

## Required Fields

| Field | Description |
|---|---|
| Role | The role Codex should adopt. |
| Raw Task | The user's request summarized without distortion. |
| Optimized Task | A precise, bounded, outcome-first rewrite. |
| Object | The target of work: repo, file, document, feature, question, or workflow. |
| Context | Relevant background and implied state. |
| Constraints | Requirements, exclusions, and boundaries. |
| Output | Expected deliverable shape. |
| Acceptance | How completion will be judged. |

## Rules

- Infer obvious fields.
- Mark unclear fields as `Need choice`.
- Do not invent facts.
- Preserve user intent.
- Keep compact contracts concise.
- Expand only when task complexity justifies it.

## Loop Extensions

Loop Contract Mode adds loop objective, loop type, iteration unit, observation method, repair strategy, validation method, stop condition, max iterations, escalation trigger, and risk gate.
