# Android Security Best Practices Patterns

## Selection Notes
- Category: `quality-release`
- Best fit when the request matches the trigger language in `SKILL.md` and the implementation focus is `Apply Android app security guidance around secrets, storage, network trust, exported components, and least privilege.`
- Reach for neighboring skills only after this skill has framed the main problem.

## Default Review Sequence
1. Scope the risk surface: correctness, security, performance, test depth, or release automation.
2. Pick the narrowest verification strategy that still catches the likely regressions.
3. Instrument the workflow so failures are actionable rather than just red.
4. Run the relevant checks on the showcase apps and packaging outputs.
5. Capture any residual risk with explicit follow-up work and owner skills.

## Handoff Shortlist
- `android-modernization-upgrade`
- `android-ci-cd-release-playstore`
