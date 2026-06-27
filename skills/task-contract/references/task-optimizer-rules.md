# Task Optimizer Rules

The Task Optimizer rewrites vague requests into precise, bounded, outcome-first tasks.

## Optimized Task Template

```text
[Action verb] [object] to [outcome], using [context and constraints], so that [decision-use]. Output [format and depth], and consider the task complete when [acceptance criteria].
```

## Requirements

1. Preserve the user's intent.
2. Define a clear action.
3. Identify the object of work.
4. Bound the scope.
5. Specify the output format.
6. Define completion criteria.
7. Avoid expanding the task beyond the user's request.

## Ambiguity Handling

When resolving ambiguity would change intent, produce numbered Decision Points instead of silently choosing.
