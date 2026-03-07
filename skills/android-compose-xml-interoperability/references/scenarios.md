# Android Compose XML Interoperability Runnable Scenarios

## Happy path
- Goal: Embed a Compose task summary inside the XML fixture without ownership confusion.
- Command: `cd examples/orbittasks-xml && ./gradlew :app:assembleDebug`

## Edge case
- Goal: Host a View-based screen from a Compose entry point during phased migration.
- Command: `cd examples/orbittasks-compose && ./gradlew :app:assembleDebug`

## Failure recovery
- Goal: Separate interoperability prompts from pure View or pure Compose requests.
- Command: `python3 scripts/eval_triggers.py --skill android-compose-xml-interoperability`
