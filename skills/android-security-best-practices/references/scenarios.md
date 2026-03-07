# Android Security Best Practices Runnable Scenarios

## Happy path
- Goal: Review the showcase apps for least-privilege sharing, notification, and storage usage.
- Command: `python3 scripts/eval_triggers.py --skill android-security-best-practices`

## Edge case
- Goal: Catch insecure defaults while migrating old manifest and network config settings.
- Command: `cd examples/orbittasks-compose && ./gradlew :app:assembleDebug`

## Failure recovery
- Goal: Separate security work from modernization or release automation requests.
- Command: `cd examples/orbittasks-xml && ./gradlew :app:assembleDebug`
