#!/usr/bin/env bash
    set -euo pipefail

    cat <<'EOF'
    Skill: Android Compose State Effects
    Canonical path: skills/android-compose-state-effects
    Example commands:
    Happy path: cd examples/orbittasks-compose && ./gradlew :app:testDebugUnitTest
Edge case: cd examples/orbittasks-compose && ./gradlew :app:assembleDebug
Failure recovery: python3 scripts/eval_triggers.py --skill android-compose-state-effects
    EOF
