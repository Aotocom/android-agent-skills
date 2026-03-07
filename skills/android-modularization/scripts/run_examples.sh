#!/usr/bin/env bash
    set -euo pipefail

    cat <<'EOF'
    Skill: Android Modularization
    Canonical path: skills/android-modularization
    Example commands:
    Happy path: cd examples/orbittasks-compose && ./gradlew :app:projects
Edge case: cd examples/orbittasks-xml && ./gradlew :app:dependencies
Failure recovery: python3 scripts/eval_triggers.py --skill android-modularization
    EOF
