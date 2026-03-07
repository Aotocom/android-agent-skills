---
name: "android-modularization"
description: "Design Android repositories with feature, core, and build-logic modules that scale without cyclic dependencies."
metadata:
  version: "0.1.0"
  category: "foundations"
  tags: ["android", "modules", "gradle", "repository-design"]
  triggers:
    include: ["android module split", "feature modularization in android", "break cyclic module dependency", "android app into modules", "core ui data domain modules"]
    exclude: ["compose focus management", "room query tuning", "notification delivery only"]
  owners: ["@android-agent-skills/maintainers"]
  test_targets: ["examples/orbittasks-compose", "examples/orbittasks-xml", "benchmarks/triggers.jsonl"]
---
# Android Modularization

## When To Use
- Use this skill when the request is about: android module split, feature modularization in android, break cyclic module dependency.
- Primary outcome: Design Android repositories with feature, core, and build-logic modules that scale without cyclic dependencies.
- Handoff skills when the scope expands:
- `android-gradle-build-logic`
- `android-architecture-clean`

## Workflow
1. Map the request to the current Android stack, module boundaries, and minimum supported API level.
2. Inspect the existing implementation for implicit assumptions, duplicate helpers, and outdated patterns.
3. Apply the smallest change that improves correctness, readability, and long-term maintainability.
4. Validate the result against the relevant showcase app path and repo benchmarks.
5. Hand off adjacent work to the next specialized skill only after the core foundation is stable.

## Guardrails
- Prefer official Android and Kotlin guidance over custom local conventions when they conflict.
- Keep public APIs boring and explicit; avoid clever abstractions that hide Android lifecycle costs.
- Do not mix architectural cleanup with product behavior changes unless the request explicitly needs both.
- Document any compatibility constraints that will affect old modules or generated code.

## Anti-Patterns
- Sprinkling helpers across modules without a clear ownership boundary.
- Introducing framework-specific code into pure domain or data layers.
- Refactoring every adjacent file when only one contract needed to change.
- Leaving migration notes implied instead of writing them down.

## Examples
### Happy path
- Scenario: Review the fixture apps as app modules and map the next split into feature/core layers.
- Command: `cd examples/orbittasks-compose && ./gradlew :app:projects`

### Edge case
- Scenario: Keep shared XML resources and manifest placeholders from leaking across modules.
- Command: `cd examples/orbittasks-xml && ./gradlew :app:dependencies`

### Failure recovery
- Scenario: Differentiate modularization requests from architecture-clean and build-logic prompts.
- Command: `python3 scripts/eval_triggers.py --skill android-modularization`

## Done Checklist
- The implementation path is explicit, minimal, and tied to the right Android surface.
- Relevant example commands and benchmark prompts have been exercised or updated.
- Handoffs to adjacent skills are documented when the request crosses boundaries.
- Official references cover the chosen pattern and the main migration or troubleshooting path.

## Official References
- [https://developer.android.com/topic/modularization](https://developer.android.com/topic/modularization)
- [https://docs.gradle.org/current/userguide/multi_project_builds.html](https://docs.gradle.org/current/userguide/multi_project_builds.html)
- [https://developer.android.com/build/extend-agp](https://developer.android.com/build/extend-agp)
- [https://developer.android.com/build/migrate-to-kotlin-dsl](https://developer.android.com/build/migrate-to-kotlin-dsl)
