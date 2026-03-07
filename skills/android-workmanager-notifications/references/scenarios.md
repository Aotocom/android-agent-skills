# Android WorkManager Notifications Runnable Scenarios

## Happy path
- Goal: Schedule OrbitTasks reminders with unique work and actionable notifications.
- Command: `cd examples/orbittasks-compose && ./gradlew :app:testDebugUnitTest`

## Edge case
- Goal: Handle duplicate scheduling and denied notification capability in the XML fixture.
- Command: `cd examples/orbittasks-xml && ./gradlew :app:testDebugUnitTest`

## Failure recovery
- Goal: Disambiguate WorkManager requests from permission prompts and performance work.
- Command: `python3 scripts/eval_triggers.py --skill android-workmanager-notifications`
