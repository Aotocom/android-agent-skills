# Android Compose Accessibility Runnable Scenarios

## Happy path
- Goal: Add semantics and readable labels to the Compose OrbitTasks cards.
- Command: `cd examples/orbittasks-compose && ./gradlew :app:connectedDebugAndroidTest`

## Edge case
- Goal: Validate font scaling, contrast, and touch targets in narrow layouts.
- Command: `cd examples/orbittasks-compose && ./gradlew :app:assembleDebug`

## Failure recovery
- Goal: Differentiate accessibility requests from general UI validation or theme work.
- Command: `python3 scripts/eval_triggers.py --skill android-compose-accessibility`
