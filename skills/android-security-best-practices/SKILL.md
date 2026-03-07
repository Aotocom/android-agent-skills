---
name: "android-security-best-practices"
description: "Apply Android app security guidance around secrets, storage, network trust, exported components, and least privilege."
metadata:
  version: "0.1.0"
  category: "quality-release"
  tags: ["android", "security", "privacy", "hardening"]
  triggers:
    include: ["android security review", "secret handling android app", "exported component security android", "network security config android", "hardening android project"]
    exclude: ["compose animation only", "room index tuning", "play listing copy"]
  owners: ["@android-agent-skills/maintainers"]
  test_targets: ["examples/orbittasks-compose", "examples/orbittasks-xml", "benchmarks/triggers.jsonl"]
---
# Android Security Best Practices

## When To Use
- Use this skill when the request is about: android security review, secret handling android app, exported component security android.
- Primary outcome: Apply Android app security guidance around secrets, storage, network trust, exported components, and least privilege.
- Handoff skills when the scope expands:
- `android-modernization-upgrade`
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
- Scenario: Review the showcase apps for least-privilege sharing, notification, and storage usage.
- Command: `python3 scripts/eval_triggers.py --skill android-security-best-practices`

### Edge case
- Scenario: Catch insecure defaults while migrating old manifest and network config settings.
- Command: `cd examples/orbittasks-compose && ./gradlew :app:assembleDebug`

### Failure recovery
- Scenario: Separate security work from modernization or release automation requests.
- Command: `cd examples/orbittasks-xml && ./gradlew :app:assembleDebug`

## Done Checklist
- The implementation path is explicit, minimal, and tied to the right Android surface.
- Relevant example commands and benchmark prompts have been exercised or updated.
- Handoffs to adjacent skills are documented when the request crosses boundaries.
- Official references cover the chosen pattern and the main migration or troubleshooting path.

## Official References
- [https://developer.android.com/privacy-and-security/security-best-practices](https://developer.android.com/privacy-and-security/security-best-practices)
- [https://developer.android.com/privacy-and-security/risks/unsafe-exported-components](https://developer.android.com/privacy-and-security/risks/unsafe-exported-components)
- [https://developer.android.com/privacy-and-security/security-config](https://developer.android.com/privacy-and-security/security-config)
- [https://developer.android.com/privacy-and-security/minimize-permission-requests](https://developer.android.com/privacy-and-security/minimize-permission-requests)
