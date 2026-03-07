#!/usr/bin/env bash
    set -euo pipefail

    cat <<'EOF'
    Skill: Android Media Files Sharing
    Canonical path: skills/android-media-files-sharing
    Example commands:
    Happy path: cd examples/orbittasks-compose && ./gradlew :app:testDebugUnitTest
Edge case: cd examples/orbittasks-xml && ./gradlew :app:testDebugUnitTest
Failure recovery: python3 scripts/eval_triggers.py --skill android-media-files-sharing
    EOF
