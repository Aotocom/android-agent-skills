# Android Permissions Activity Results Runnable Scenarios

## Happy path
- Goal: Request notification capability and handle the granted path cleanly.
- Command: `cd examples/orbittasks-compose && ./gradlew :app:testDebugUnitTest`

## Edge case
- Goal: Show denied and permanently denied permission states in the XML fixture.
- Command: `cd examples/orbittasks-xml && ./gradlew :app:testDebugUnitTest`

## Failure recovery
- Goal: Differentiate permission prompts from media-sharing and navigation requests.
- Command: `python3 scripts/eval_triggers.py --skill android-permissions-activity-results`
