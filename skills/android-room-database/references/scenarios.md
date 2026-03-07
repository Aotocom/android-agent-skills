# Android Room Database Runnable Scenarios

## Happy path
- Goal: Persist task items and reminder flags with schema-aware entities.
- Command: `cd examples/orbittasks-compose && ./gradlew :app:testDebugUnitTest`

## Edge case
- Goal: Recover from a failed schema change with an explicit migration path.
- Command: `python3 scripts/eval_triggers.py --skill android-room-database`

## Failure recovery
- Goal: Keep Room requests separate from DataStore, networking, and modernization prompts.
- Command: `cd examples/orbittasks-xml && ./gradlew :app:testDebugUnitTest`
