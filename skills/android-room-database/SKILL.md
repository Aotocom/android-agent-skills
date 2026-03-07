---
name: "android-room-database"
description: "Model Room entities, DAOs, transactions, migrations, schema exports, and test-safe local persistence."
metadata:
  version: "0.1.0"
  category: "data-platform"
  tags: ["android", "room", "database", "migrations"]
  triggers:
    include: ["room database android", "dao query migration android", "room schema export", "transaction issue room", "android local database cleanup"]
    exclude: ["deeplink back stack", "compose semantics", "play rollout"]
  owners: ["@android-agent-skills/maintainers"]
  test_targets: ["examples/orbittasks-compose", "examples/orbittasks-xml", "benchmarks/triggers.jsonl"]
---
# Android Room Database

## When To Use
- Use this skill when the request is about: room database android, dao query migration android, room schema export.
- Primary outcome: Model Room entities, DAOs, transactions, migrations, schema exports, and test-safe local persistence.
- Handoff skills when the scope expands:
- `android-local-persistence-datastore`
- `android-testing-unit`

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
- Scenario: Persist task items and reminder flags with schema-aware entities.
- Command: `cd examples/orbittasks-compose && ./gradlew :app:testDebugUnitTest`

### Edge case
- Scenario: Recover from a failed schema change with an explicit migration path.
- Command: `python3 scripts/eval_triggers.py --skill android-room-database`

### Failure recovery
- Scenario: Keep Room requests separate from DataStore, networking, and modernization prompts.
- Command: `cd examples/orbittasks-xml && ./gradlew :app:testDebugUnitTest`

## Done Checklist
- The implementation path is explicit, minimal, and tied to the right Android surface.
- Relevant example commands and benchmark prompts have been exercised or updated.
- Handoffs to adjacent skills are documented when the request crosses boundaries.
- Official references cover the chosen pattern and the main migration or troubleshooting path.

## Official References
- [https://developer.android.com/training/data-storage/room](https://developer.android.com/training/data-storage/room)
- [https://developer.android.com/training/data-storage/room/migrating-db-versions](https://developer.android.com/training/data-storage/room/migrating-db-versions)
- [https://developer.android.com/training/data-storage/room/accessing-data](https://developer.android.com/training/data-storage/room/accessing-data)
- [https://developer.android.com/topic/performance/sqlite-performance-best-practices](https://developer.android.com/topic/performance/sqlite-performance-best-practices)
