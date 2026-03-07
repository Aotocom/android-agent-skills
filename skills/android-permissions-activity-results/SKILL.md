---
name: "android-permissions-activity-results"
description: "Use modern permission requests, Activity Result APIs, and capability-gated UX in Android flows."
metadata:
  version: "0.1.0"
  category: "product"
  tags: ["android", "permissions", "activity-result", "capabilities"]
  triggers:
    include: ["android permission request flow", "activity result api android", "camera permission in android app", "photo picker or permission android", "permission denied recovery"]
    exclude: ["deeplink back stack only", "release signing only", "room transaction only"]
  owners: ["@android-agent-skills/maintainers"]
  test_targets: ["examples/orbittasks-compose", "examples/orbittasks-xml", "benchmarks/triggers.jsonl"]
---
# Android Permissions Activity Results

## When To Use
- Use this skill when the request is about: android permission request flow, activity result api android, camera permission in android app.
- Primary outcome: Use modern permission requests, Activity Result APIs, and capability-gated UX in Android flows.
- Handoff skills when the scope expands:
- `android-media-files-sharing`
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
- Scenario: Request notification capability and handle the granted path cleanly.
- Command: `cd examples/orbittasks-compose && ./gradlew :app:testDebugUnitTest`

### Edge case
- Scenario: Show denied and permanently denied permission states in the XML fixture.
- Command: `cd examples/orbittasks-xml && ./gradlew :app:testDebugUnitTest`

### Failure recovery
- Scenario: Differentiate permission prompts from media-sharing and navigation requests.
- Command: `python3 scripts/eval_triggers.py --skill android-permissions-activity-results`

## Done Checklist
- The implementation path is explicit, minimal, and tied to the right Android surface.
- Relevant example commands and benchmark prompts have been exercised or updated.
- Handoffs to adjacent skills are documented when the request crosses boundaries.
- Official references cover the chosen pattern and the main migration or troubleshooting path.

## Official References
- [https://developer.android.com/training/permissions/requesting](https://developer.android.com/training/permissions/requesting)
- [https://developer.android.com/training/basics/intents/result](https://developer.android.com/training/basics/intents/result)
- [https://developer.android.com/training/data-storage/shared/photopicker](https://developer.android.com/training/data-storage/shared/photopicker)
- [https://developer.android.com/privacy-and-security/minimize-permission-requests](https://developer.android.com/privacy-and-security/minimize-permission-requests)
