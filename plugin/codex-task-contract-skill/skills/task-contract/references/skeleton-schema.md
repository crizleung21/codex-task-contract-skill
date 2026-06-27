# Auto-Skeleton Schema

The Auto-Skeleton is the first visible section produced by the Skill. It turns an incoming request into a compact task frame.

## Required Fields

| Field | Description | Fill Rule |
|---|---|---|
| Role | The role Codex should adopt. | Infer from task type. |
| Raw Task | The user's request summarized without distortion. | Preserve intent and key wording. |
| Optimized Task | A precise, bounded, outcome-first rewrite. | Use Task Optimizer rules. |
| Object | The target of work. | File, repo, codebase, document, feature, question, or workflow. |
| Context | Relevant background and implied state. | Use known context only. |
| Constraints | Requirements, exclusions, risks, and boundaries. | Include explicit and obvious constraints. |
| Output | Expected deliverable shape. | Define format and depth. |
| Acceptance | How completion will be judged. | Define observable pass conditions. |

## Field Quality Rules

- Use `Need choice` when the field cannot be resolved safely.
- Do not hide major uncertainty inside assumptions.
- Do not convert a vague goal into a broader project unless the user asked for it.
- Keep compact mode short.
- Use full mode when unclear choices affect output.

## Loop Extensions

When Loop Contract Mode is selected, extend the skeleton with:

| Field | Description |
|---|---|
| Loop Objective | Final goal of the loop. |
| Loop Type | Simple, coding/debug, research, documentation, repo maintenance, or high-impact. |
| Iteration Unit | Smallest useful action per cycle. |
| Observation Method | What will be checked after each cycle. |
| Adjustment Strategy | How the next action changes based on evidence. |
| Validation Method | How completion is verified. |
| Stop Condition | Success or safe stop condition. |
| Max Iterations | Maximum cycles before stop or escalation. |
| Escalation Trigger | Condition that requires user input. |
| Approval Gate | Whether execution may proceed. |

## Acceptance Field Examples

Good acceptance criteria are observable:

- Documentation covers installation, usage, and validation.
- A fixture output includes Auto-Skeleton and Output Contract.
- A loop contract includes objective, observation method, stop condition, and max iterations.

Avoid vague acceptance such as `looks good`, `better`, or `complete` without a concrete check.
