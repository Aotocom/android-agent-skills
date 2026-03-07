#!/usr/bin/env bash
    set -euo pipefail

    cat <<'EOF'
    Skill: Android CI CD Release PlayStore
    Canonical path: skills/android-ci-cd-release-playstore
    Example commands:
    Happy path: python3 scripts/validate_repo.py
Edge case: python3 scripts/release.py --channel canary --dry-run
Failure recovery: python3 scripts/eval_triggers.py --skill android-ci-cd-release-playstore
    EOF
