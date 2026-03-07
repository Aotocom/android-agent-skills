# Android Performance Observability Runnable Scenarios

## Happy path
- Goal: Use baseline checks and traces to profile the Compose fixture.
- Command: `python3 scripts/eval_triggers.py --skill android-performance-observability`

## Edge case
- Goal: Spot noisy XML view work and startup regressions under repeated launches.
- Command: `cd examples/orbittasks-xml && ./gradlew :app:assembleDebug`

## Failure recovery
- Goal: Keep observability requests distinct from Compose-only performance tuning.
- Command: `cd examples/orbittasks-compose && ./gradlew :app:assembleDebug`
