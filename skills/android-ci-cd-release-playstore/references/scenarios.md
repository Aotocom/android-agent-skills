# Android CI CD Release PlayStore Runnable Scenarios

## Happy path
- Goal: Validate the repo CI workflow, adapter generation, and version metadata flow.
- Command: `python3 scripts/validate_repo.py`

## Edge case
- Goal: Check canary and stable release script behavior before tagging.
- Command: `python3 scripts/release.py --channel canary --dry-run`

## Failure recovery
- Goal: Avoid routing pure build-logic or security work into release automation.
- Command: `python3 scripts/eval_triggers.py --skill android-ci-cd-release-playstore`
