---
name: "android-media-files-sharing"
description: "Use modern Android file, media, picker, FileProvider, and share-sheet APIs with minimal permissions."
metadata:
  version: "0.1.0"
  category: "data-platform"
  tags: ["android", "media", "files", "sharing"]
  triggers:
    include: ["android file sharing", "photo picker android app", "fileprovider setup android", "share pdf image android", "media attachment android flow"]
    exclude: ["room dao change", "compose performance", "gradle plugin error"]
  owners: ["@android-agent-skills/maintainers"]
  test_targets: ["examples/orbittasks-compose", "examples/orbittasks-xml", "benchmarks/triggers.jsonl"]
---
# Android Media Files Sharing

## When To Use
- Use this skill when the request is about: android file sharing, photo picker android app, fileprovider setup android.
- Primary outcome: Use modern Android file, media, picker, FileProvider, and share-sheet APIs with minimal permissions.
- Handoff skills when the scope expands:
- `android-permissions-activity-results`
- `android-security-best-practices`

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
- Scenario: Attach and share a task snapshot using the least-privilege API.
- Command: `cd examples/orbittasks-compose && ./gradlew :app:testDebugUnitTest`

### Edge case
- Scenario: Handle absent picker support or denied media capabilities in the XML fixture.
- Command: `cd examples/orbittasks-xml && ./gradlew :app:testDebugUnitTest`

### Failure recovery
- Scenario: Separate media/file flows from permission-only or networking-only requests.
- Command: `python3 scripts/eval_triggers.py --skill android-media-files-sharing`

## Done Checklist
- The implementation path is explicit, minimal, and tied to the right Android surface.
- Relevant example commands and benchmark prompts have been exercised or updated.
- Handoffs to adjacent skills are documented when the request crosses boundaries.
- Official references cover the chosen pattern and the main migration or troubleshooting path.

## Official References
- [https://developer.android.com/training/data-storage/shared/photopicker](https://developer.android.com/training/data-storage/shared/photopicker)
- [https://developer.android.com/training/secure-file-sharing/setup-sharing](https://developer.android.com/training/secure-file-sharing/setup-sharing)
- [https://developer.android.com/training/sharing/send](https://developer.android.com/training/sharing/send)
- [https://developer.android.com/topic/performance/graphics/picker](https://developer.android.com/topic/performance/graphics/picker)
