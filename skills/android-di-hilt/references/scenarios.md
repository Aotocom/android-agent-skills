# Android DI Hilt Runnable Scenarios

## Happy path
- Goal: Inject OrbitTasks repositories and dispatchers with clear Hilt scopes.
- Command: `cd examples/orbittasks-compose && ./gradlew :app:testDebugUnitTest`

## Edge case
- Goal: Swap fake dependencies in the XML fixture for deterministic tests.
- Command: `cd examples/orbittasks-xml && ./gradlew :app:testDebugUnitTest`

## Failure recovery
- Goal: Catch DI-specific prompts before they drift into architecture-clean or networking.
- Command: `python3 scripts/eval_triggers.py --skill android-di-hilt`
