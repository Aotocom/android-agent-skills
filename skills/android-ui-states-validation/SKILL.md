---
name: "android-ui-states-validation"
description: "Review Android UI flows for empty, loading, error, offline, and edge-case behavior before release."
metadata:
  version: "0.1.0"
  category: "product"
  tags: ["android", "ui", "validation", "edge-cases"]
  triggers:
    include: ["validate android ui states", "check loading empty error flow android", "edge cases in android screen", "android screen regression review", "state coverage before release"]
    exclude: ["macrobenchmark only", "dependency alignment only", "hilt graph only"]
  owners: ["@android-agent-skills/maintainers"]
  test_targets: ["examples/orbittasks-compose", "examples/orbittasks-xml", "benchmarks/triggers.jsonl"]
---
# Android UI States Validation

## When To Use
- Use this skill when the request is about: validate android ui states, check loading empty error flow android, edge cases in android screen.
- Primary outcome: Review Android UI flows for empty, loading, error, offline, and edge-case behavior before release.
- Handoff skills when the scope expands:
- `android-compose-accessibility`
- `android-testing-ui`

## Workflow
1. Confirm the user-visible journey, target device behavior, and failure states that matter.
2. Identify the owning screens, activities, destinations, and state holders for the flow.
3. Implement the flow with explicit loading, success, empty, and error handling.
4. Validate accessibility, configuration changes, and back-stack behavior in the showcase apps.
5. Escalate data, architecture, or release concerns to the specialized skills called out in the handoff notes.

## Guardrails
- Treat loading, empty, error, offline, and permission-denied states as first-class UI states.
- Do not hide navigation or permission side effects inside reusable UI components.
- Prefer lifecycle-aware APIs over manual callback chains.
- Keep deep links, intents, and permission prompts testable and observable.

## Anti-Patterns
- Assuming the happy path is enough for product flows.
- Hard-coding request codes or route strings in multiple places.
- Triggering navigation directly from repositories or network layers.
- Shipping flows without recovery UI for denied permissions or broken state.

## Examples
### Happy path
- Scenario: Validate OrbitTasks loading, content, and success confirmation states.
- Command: `cd examples/orbittasks-compose && ./gradlew :app:connectedDebugAndroidTest`

### Edge case
- Scenario: Exercise long content, empty lists, and sync failures in the XML fixture.
- Command: `cd examples/orbittasks-xml && ./gradlew :app:connectedDebugAndroidTest`

### Failure recovery
- Scenario: Avoid misrouting UI validation work to accessibility or testing-only skills.
- Command: `python3 scripts/eval_triggers.py --skill android-ui-states-validation`

## Done Checklist
- The implementation path is explicit, minimal, and tied to the right Android surface.
- Relevant example commands and benchmark prompts have been exercised or updated.
- Handoffs to adjacent skills are documented when the request crosses boundaries.
- Official references cover the chosen pattern and the main migration or troubleshooting path.

## Official References
- [https://developer.android.com/topic/architecture/ui-layer](https://developer.android.com/topic/architecture/ui-layer)
- [https://developer.android.com/guide/topics/resources/runtime-changes](https://developer.android.com/guide/topics/resources/runtime-changes)
- [https://developer.android.com/guide/practices/ui_guidelines](https://developer.android.com/guide/practices/ui_guidelines)
- [https://developer.android.com/guide/topics/ui/accessibility/apps](https://developer.android.com/guide/topics/ui/accessibility/apps)
