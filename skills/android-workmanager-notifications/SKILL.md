---
name: "android-workmanager-notifications"
description: "Schedule reliable background work, reminders, and notification delivery with WorkManager and Android execution limits."
metadata:
  version: "0.1.0"
  category: "data-platform"
  tags: ["android", "workmanager", "notifications", "background-work"]
  triggers:
    include: ["android workmanager job", "background reminder notification android", "reliable retry workmanager", "periodic work android app", "notification scheduling android"]
    exclude: ["deeplink only", "compose modifier cleanup", "release track rollout"]
  owners: ["@android-agent-skills/maintainers"]
  test_targets: ["examples/orbittasks-compose", "examples/orbittasks-xml", "benchmarks/triggers.jsonl"]
---
# Android WorkManager Notifications

## When To Use
- Use this skill when the request is about: android workmanager job, background reminder notification android, reliable retry workmanager.
- Primary outcome: Schedule reliable background work, reminders, and notification delivery with WorkManager and Android execution limits.
- Handoff skills when the scope expands:
- `android-permissions-activity-results`
- `android-performance-observability`

## Workflow
1. Confirm the data source, persistence boundary, sync model, and device capability involved.
2. Model contracts explicitly before wiring network, storage, media, or background APIs.
3. Apply the recommended AndroidX or platform pattern with migration-safe defaults.
4. Validate offline, retry, and process death behavior against the sample apps and scenarios.
5. Escalate security, performance, or release risk to the linked supporting skills when needed.

## Guardrails
- Prefer typed models and explicit serializers over ad-hoc maps or bundles.
- Keep background work idempotent and cancellation-aware.
- Do not leak storage, media, or networking details into presentation code.
- Treat user data durability, privacy, and migration paths as part of the implementation.

## Anti-Patterns
- Blocking the main thread with disk or network calls.
- Treating retryable sync failures as terminal user-facing errors.
- Mixing cache models and wire models without a mapping layer.
- Requesting broad storage or notification capabilities when a narrower API exists.

## Examples
### Happy path
- Scenario: Schedule OrbitTasks reminders with unique work and actionable notifications.
- Command: `cd examples/orbittasks-compose && ./gradlew :app:testDebugUnitTest`

### Edge case
- Scenario: Handle duplicate scheduling and denied notification capability in the XML fixture.
- Command: `cd examples/orbittasks-xml && ./gradlew :app:testDebugUnitTest`

### Failure recovery
- Scenario: Disambiguate WorkManager requests from permission prompts and performance work.
- Command: `python3 scripts/eval_triggers.py --skill android-workmanager-notifications`

## Done Checklist
- The implementation path is explicit, minimal, and tied to the right Android surface.
- Relevant example commands and benchmark prompts have been exercised or updated.
- Handoffs to adjacent skills are documented when the request crosses boundaries.
- Official references cover the chosen pattern and the main migration or troubleshooting path.

## Official References
- [https://developer.android.com/topic/libraries/architecture/workmanager](https://developer.android.com/topic/libraries/architecture/workmanager)
- [https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started)
- [https://developer.android.com/develop/ui/views/notifications/build-notification](https://developer.android.com/develop/ui/views/notifications/build-notification)
- [https://developer.android.com/develop/background-work/background-tasks/optimize-battery](https://developer.android.com/develop/background-work/background-tasks/optimize-battery)
