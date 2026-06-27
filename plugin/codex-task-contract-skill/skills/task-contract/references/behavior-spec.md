# Behavior Spec

This reference defines the expected behavior of the `task-contract` Skill.

## Core Principle

Clarify before action. Codex should convert the user request into a visible task contract before doing meaningful work.

## Behavior Contract

The Skill must:\n\n1. Preserve the user's intent.
2. Bound the task scope.
3. Define the work object.
4. State assumptions separately from facts.
5. Identify constraints and exclusions.
6. Define output shape and acceptance criteria.
7. Use Decision Points when a choice changes the outcome.
8. Use an Approval Gate before high-impact work.
9. Use Loop Contract Mode only when iterative work is useful.
10. Stop or escalate when context is missing, validation is impossible, or scope drift appears.

## Mode Selection Algorithm

1. Use Compact Contract for simple low-impact tasks.
2. Use Full Contract for complex, ambiguous, repo-level, or high-impact tasks.
3. Use Loop Contract when progress depends on repeated observation and adjustment.
4. Escalate to Full Contract if a compact output would hide a meaningful decision.
5. Escalate to Loop Contract only when a bounded loop can be defined.

## Output Rules

- Start with Auto-Skeleton.
- Put BLUF before long detail in Full or Loop mode.
- Keep assumptions to five items or fewer unless the user asks for deeper analysis.
- Prefer numbered choices over open-ended questions.
- End with one clear next step.

## Safety and Trust Rules

- Do not invent facts, files, tests, or results.
- Do not imply validation happened unless evidence is available.
- Do not expose hidden reasoning.
- Do not run unbounded loops.
- Do not expand scope without surfacing the change.

## Evidence Rules

When sources, tests, build output, diff review, or logs are used, cite or summarize the evidence in the visible response. Evidence should support the conclusion, not replace the acceptance criteria.
