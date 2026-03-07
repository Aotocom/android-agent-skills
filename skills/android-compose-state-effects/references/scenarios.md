# Android Compose State Effects Runnable Scenarios

## Happy path
- Goal: Collect task state and snackbar events in Compose without duplicate launches.
- Command: `cd examples/orbittasks-compose && ./gradlew :app:testDebugUnitTest`

## Edge case
- Goal: Handle recomposition when permission state and sync state change together.
- Command: `cd examples/orbittasks-compose && ./gradlew :app:assembleDebug`

## Failure recovery
- Goal: Disambiguate state/effects work from generic Compose layout or state-management requests.
- Command: `python3 scripts/eval_triggers.py --skill android-compose-state-effects`
