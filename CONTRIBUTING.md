# Contributing

Thanks for contributing to `android-agent-skills`.

This repository is meant to grow, and good expansion is part of the goal. If you find a clearer structure, a better authoring pattern, a stronger validation rule, or a more useful way to package skills, propose it. Improvements to the system are welcome. The bar is simple: the repo should stay easier to use, easier to maintain, and fully green in CI.

## Expectations
- Every skill should meet the same structure, trigger quality, benchmark, and official reference bar as the rest of the catalog.
- Canonical edits belong in `skills/<skill-name>/`. Generated adapters must not be edited by hand.
- Keep pull requests focused. One skill family, one tooling area, or one repository system change per PR is the right size.
- If you add a new skill, expand an existing one, or change repository structure, all validation and generation steps must still pass.
- If you believe there is a better way to organize the repo, show the improvement in code and keep the authoring experience clear for the next contributor.

## Local workflow
```bash
python3 scripts/init_skill.py my-skill --description "What it does" --category foundations
python3 scripts/validate_repo.py
python3 scripts/build_adapters.py --agent all
python3 scripts/eval_triggers.py
```

## Growing the catalog
- New skills should solve real Android work, not just create more surface area.
- Match the depth of the existing catalog. A new skill should be as useful as the skills already in the repo, not thinner.
- Prefer improving shared structure and tooling when it helps future skills land faster and more consistently.
- If your change introduces a better pattern, document it in the canonical source so future contributors can follow it.

## Review requirements
- CI must pass.
- CODEOWNERS review is required for canonical skills and release tooling.
- Public behavior changes must update `CHANGELOG.md` and, when relevant, the skill version metadata.
