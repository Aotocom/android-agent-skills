---
name: "android-performance-observability"
description: "Measure startup, rendering, memory, jank, vitals, logs, and crash signals for Android apps with actionable traces."
metadata:
  version: "0.1.0"
  category: "quality-release"
  tags: ["android", "performance", "observability", "profiling"]
  triggers:
    include: ["android performance profiling", "baseline profile or macrobenchmark", "app startup issue android", "observability for android app", "trace jank crash android"]
    exclude: ["permission request only", "retrofit dto change only", "fragment transaction only"]
  owners: ["@android-agent-skills/maintainers"]
  test_targets: ["examples/orbittasks-compose", "examples/orbittasks-xml", "benchmarks/triggers.jsonl"]
---
# Android Performance Observability

## When To Use
- Use this skill when the request is about: android performance profiling, baseline profile or macrobenchmark, app startup issue android.
- Primary outcome: Measure startup, rendering, memory, jank, vitals, logs, and crash signals for Android apps with actionable traces.
- Handoff skills when the scope expands:
- `android-compose-performance`
- `android-ci-cd-release-playstore`

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
- Scenario: Use baseline checks and traces to profile the Compose fixture.
- Command: `python3 scripts/eval_triggers.py --skill android-performance-observability`

### Edge case
- Scenario: Spot noisy XML view work and startup regressions under repeated launches.
- Command: `cd examples/orbittasks-xml && ./gradlew :app:assembleDebug`

### Failure recovery
- Scenario: Keep observability requests distinct from Compose-only performance tuning.
- Command: `cd examples/orbittasks-compose && ./gradlew :app:assembleDebug`

## Done Checklist
- The implementation path is explicit, minimal, and tied to the right Android surface.
- Relevant example commands and benchmark prompts have been exercised or updated.
- Handoffs to adjacent skills are documented when the request crosses boundaries.
- Official references cover the chosen pattern and the main migration or troubleshooting path.

## Official References
- [https://developer.android.com/studio/profile/overview](https://developer.android.com/studio/profile/overview)
- [https://developer.android.com/topic/performance/vitals](https://developer.android.com/topic/performance/vitals)
- [https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)
- [https://developer.android.com/topic/performance/baselineprofiles/overview](https://developer.android.com/topic/performance/baselineprofiles/overview)
