# Android Compose Performance Runnable Scenarios

## Happy path
- Goal: Profile the Compose task list for unnecessary recomposition hotspots.
- Command: `cd examples/orbittasks-compose && ./gradlew :app:testDebugUnitTest`

## Edge case
- Goal: Evaluate long lists, filter chips, and snackbar churn under repeated state changes.
- Command: `cd examples/orbittasks-compose && ./gradlew :app:assembleDebug`

## Failure recovery
- Goal: Separate performance requests from generic Compose or observability prompts.
- Command: `python3 scripts/eval_triggers.py --skill android-compose-performance`
