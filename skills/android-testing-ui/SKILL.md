---
name: "android-testing-ui"
description: "Validate Android UI behavior with Compose UI tests, Espresso-style checks, accessibility assertions, and state coverage."
metadata:
  version: "0.1.0"
  category: "quality-release"
  tags: ["android", "testing", "ui-tests", "instrumentation"]
  triggers:
    include: ["android ui test", "compose ui test screen", "espresso validation android", "instrumentation test android flow", "accessibility assertions android ui"]
    exclude: ["gradle version conflict", "room dao only", "release version tag"]
  owners: ["@android-agent-skills/maintainers"]
  test_targets: ["examples/orbittasks-compose", "examples/orbittasks-xml", "benchmarks/triggers.jsonl"]
---
# Android Testing UI

## When To Use
- Use this skill when the request is about: android ui test, compose ui test screen, espresso validation android.
- Primary outcome: Validate Android UI behavior with Compose UI tests, Espresso-style checks, accessibility assertions, and state coverage.
- Handoff skills when the scope expands:
- `android-compose-accessibility`
- `android-ui-states-validation`

## Workflow
1. Scope the risk surface: correctness, security, performance, test depth, or release automation.
2. Pick the narrowest verification strategy that still catches the likely regressions.
3. Instrument the workflow so failures are actionable rather than just red.
4. Run the relevant checks on the showcase apps and packaging outputs.
5. Capture any residual risk with explicit follow-up work and owner skills.

## Guardrails
- Prefer reproducible checks in CI over one-off local heroics.
- Fail with a precise remediation path instead of a vague quality gate.
- Keep secrets, signing material, and production credentials out of examples and fixtures.
- Treat performance and security work as engineering tasks with evidence, not folklore.

## Anti-Patterns
- Adding more tests without increasing signal.
- Shipping benchmarks or security scans that no one can reproduce.
- Hard-coding release credentials into build logic.
- Using synthetic metrics with no user-impact interpretation.

## Examples
### Happy path
- Scenario: Run Compose UI assertions for the task board and action flows.
- Command: `cd examples/orbittasks-compose && ./gradlew :app:connectedDebugAndroidTest`

### Edge case
- Scenario: Validate XML screen behavior under configuration and content edge cases.
- Command: `cd examples/orbittasks-xml && ./gradlew :app:connectedDebugAndroidTest`

### Failure recovery
- Scenario: Separate UI-testing requests from UI-state reviews or accessibility-only prompts.
- Command: `python3 scripts/eval_triggers.py --skill android-testing-ui`

## Done Checklist
- The implementation path is explicit, minimal, and tied to the right Android surface.
- Relevant example commands and benchmark prompts have been exercised or updated.
- Handoffs to adjacent skills are documented when the request crosses boundaries.
- Official references cover the chosen pattern and the main migration or troubleshooting path.

## Official References
- [https://developer.android.com/training/testing/espresso](https://developer.android.com/training/testing/espresso)
- [https://developer.android.com/develop/ui/compose/testing](https://developer.android.com/develop/ui/compose/testing)
- [https://developer.android.com/guide/topics/ui/accessibility/testing](https://developer.android.com/guide/topics/ui/accessibility/testing)
- [https://developer.android.com/training/testing/instrumented-tests](https://developer.android.com/training/testing/instrumented-tests)
