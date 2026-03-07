# Android Modularization Runnable Scenarios

## Happy path
- Goal: Review the fixture apps as app modules and map the next split into feature/core layers.
- Command: `cd examples/orbittasks-compose && ./gradlew :app:projects`

## Edge case
- Goal: Keep shared XML resources and manifest placeholders from leaking across modules.
- Command: `cd examples/orbittasks-xml && ./gradlew :app:dependencies`

## Failure recovery
- Goal: Differentiate modularization requests from architecture-clean and build-logic prompts.
- Command: `python3 scripts/eval_triggers.py --skill android-modularization`
