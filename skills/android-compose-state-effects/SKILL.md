---
name: "android-compose-state-effects"
description: "Manage Compose state, remember APIs, side effects, snapshots, and lifecycle-aware collection without leaks or loops."
metadata:
  version: "0.1.0"
  category: "ui"
  tags: ["android", "compose", "state", "side-effects"]
  triggers:
    include: ["compose side effect problem", "remember vs derivedstateof", "collect flow in compose screen", "launchedeffect issue android", "compose state hoisting"]
    exclude: ["xml recycler issue", "apk alignment", "play console release"]
  owners: ["@android-agent-skills/maintainers"]
  test_targets: ["examples/orbittasks-compose", "examples/orbittasks-xml", "benchmarks/triggers.jsonl"]
---
# Android Compose State Effects

## When To Use
- Use this skill when the request is about: compose side effect problem, remember vs derivedstateof, collect flow in compose screen.
- Primary outcome: Manage Compose state, remember APIs, side effects, snapshots, and lifecycle-aware collection without leaks or loops.
- Handoff skills when the scope expands:
- `android-state-management`
- `android-compose-performance`

## Workflow
1. Identify whether the target surface is Compose, View system, or a mixed interoperability screen.
2. Select the lowest-friction UI pattern that satisfies responsiveness, accessibility, and performance needs.
3. Build the UI around stable state, explicit side effects, and reusable design tokens.
4. Exercise edge cases such as long text, font scaling, RTL, and narrow devices in the fixture apps.
5. Validate with unit, UI, and screenshot-friendly checks before handing off.

## Guardrails
- Optimize for stable state and predictable rendering before adding animation or abstraction.
- Respect accessibility semantics, contrast, focus order, and touch target guidance by default.
- Do not mix Compose and View system ownership without an explicit interoperability boundary.
- Prefer measured performance work over premature micro-optimizations.

## Anti-Patterns
- Embedding navigation or business logic directly in leaf UI components.
- Using fixed dimensions that break on localization or dynamic text.
- Ignoring semantics and announcing only visual changes.
- Porting XML patterns directly into Compose without adapting the mental model.

## Examples
### Happy path
- Scenario: Collect task state and snackbar events in Compose without duplicate launches.
- Command: `cd examples/orbittasks-compose && ./gradlew :app:testDebugUnitTest`

### Edge case
- Scenario: Handle recomposition when permission state and sync state change together.
- Command: `cd examples/orbittasks-compose && ./gradlew :app:assembleDebug`

### Failure recovery
- Scenario: Disambiguate state/effects work from generic Compose layout or state-management requests.
- Command: `python3 scripts/eval_triggers.py --skill android-compose-state-effects`

## Done Checklist
- The implementation path is explicit, minimal, and tied to the right Android surface.
- Relevant example commands and benchmark prompts have been exercised or updated.
- Handoffs to adjacent skills are documented when the request crosses boundaries.
- Official references cover the chosen pattern and the main migration or troubleshooting path.

## Official References
- [https://developer.android.com/develop/ui/compose/state](https://developer.android.com/develop/ui/compose/state)
- [https://developer.android.com/develop/ui/compose/side-effects](https://developer.android.com/develop/ui/compose/side-effects)
- [https://developer.android.com/reference/kotlin/androidx/lifecycle/compose/package-summary](https://developer.android.com/reference/kotlin/androidx/lifecycle/compose/package-summary)
- [https://developer.android.com/topic/architecture/ui-layer/state-production](https://developer.android.com/topic/architecture/ui-layer/state-production)
