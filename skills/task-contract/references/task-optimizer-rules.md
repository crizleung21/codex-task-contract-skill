# Task Optimizer Rules

The Task Optimizer rewrites vague requests into precise, bounded, outcome-first tasks.

## Optimized Task Template

```text
[Action verb] [object] to [outcome], using [context and constraints], so that [decision-use]. Output [format and depth], and consider the task complete when [acceptance criteria].
```

## Required Properties

An Optimized Task must:

1. Preserve the user's intent.
2. Use a clear action verb.
3. Identify the object of work.
4. Define the outcome.
5. Bound the scope.
6. Specify output format and depth.
7. Define acceptance criteria.
8. State decision-use when relevant.
9. Avoid unrelated expansion.
10. Surface unresolved choices as Decision Points.

## Action Verbs

Prefer specific verbs:

- create
- update
- review
- audit
- compare
- summarize
- validate
- refactor
- document
- package
- release-plan

Avoid vague verbs without an object, such as `improve` or `fix`, unless the Optimized Task defines what improvement or fix means.

## Scope Control

The Optimized Task must define:

- what is included;
- what is excluded;
- what files or areas are in scope when known;
- what level of detail is expected;
- what must not be changed without approval.

## Ambiguity Handling

Create Decision Points when ambiguity affects:

- architecture;
- public behavior;
- release scope;
- naming;
- data or file changes;
- repository structure;
- loop execution boundaries.

## Examples

Weak:

```text
Improve the repo.
```

Better:

```text
Audit the repository documentation, Skill source, plugin package, and test fixtures to identify release-blocking gaps. Output a prioritized checklist and proposed patch plan. Consider the task complete when P0 release blockers are identified with concrete fixes.
```

Weak:

```text
Keep working until done.
```

Better:

```text
Create a bounded Loop Contract for the task, defining the objective, observation method, adjustment strategy, validation method, stop condition, max iterations, and escalation trigger before execution.
```
