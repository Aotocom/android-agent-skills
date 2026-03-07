#!/usr/bin/env bash
    set -euo pipefail

    cat <<'EOF'
    Skill: Android Compose XML Interoperability
    Canonical path: skills/android-compose-xml-interoperability
    Example commands:
    Happy path: cd examples/orbittasks-xml && ./gradlew :app:assembleDebug
Edge case: cd examples/orbittasks-compose && ./gradlew :app:assembleDebug
Failure recovery: python3 scripts/eval_triggers.py --skill android-compose-xml-interoperability
    EOF
