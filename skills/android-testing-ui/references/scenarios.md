# Android Testing UI Runnable Scenarios

## Happy path
- Goal: Run Compose UI assertions for the task board and action flows.
- Command: `cd examples/orbittasks-compose && ./gradlew :app:connectedDebugAndroidTest`

## Edge case
- Goal: Validate XML screen behavior under configuration and content edge cases.
- Command: `cd examples/orbittasks-xml && ./gradlew :app:connectedDebugAndroidTest`

## Failure recovery
- Goal: Separate UI-testing requests from UI-state reviews or accessibility-only prompts.
- Command: `python3 scripts/eval_triggers.py --skill android-testing-ui`
