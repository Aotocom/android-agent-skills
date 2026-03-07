# Android Local Persistence DataStore Runnable Scenarios

## Happy path
- Goal: Store reminder and filter preferences for OrbitTasks safely.
- Command: `cd examples/orbittasks-compose && ./gradlew :app:testDebugUnitTest`

## Edge case
- Goal: Migrate old preference keys without breaking the XML fixture.
- Command: `cd examples/orbittasks-xml && ./gradlew :app:testDebugUnitTest`

## Failure recovery
- Goal: Avoid mixing lightweight preference storage requests with Room persistence work.
- Command: `python3 scripts/eval_triggers.py --skill android-local-persistence-datastore`
