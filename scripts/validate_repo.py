#!/usr/bin/env python3
from __future__ import annotations

import json

from skill_lib import load_skills, render_agents_catalog, render_claude_agent, render_cursor_rule, repo_root
from validate_skill import validate

EXPECTED_COUNT = 29
REQUIRED_FIXTURES = [
    'examples/orbittasks-compose',
    'examples/orbittasks-xml',
    'examples/fixtures/legacy-support-app',
    'examples/fixtures/legacy-mismatch-app',
    'examples/fixtures/native-misaligned-app',
]


def main() -> int:
    root = repo_root()
    skills = load_skills(root)
    errors: list[str] = []

    if len(skills) != EXPECTED_COUNT:
        errors.append(f'expected {EXPECTED_COUNT} skills, found {len(skills)}')
    for skill in skills:
        skill_dir = root / 'skills' / skill['slug']
        errors.extend(f'{skill_dir}: {issue}' for issue in validate(skill_dir))

    expected_catalog = render_agents_catalog(skills)
    agents_path = root / 'AGENTS.md'
    if not agents_path.exists() or agents_path.read_text(encoding='utf-8') != expected_catalog:
        errors.append('AGENTS.md is missing or out of date; run python3 scripts/build_adapters.py --agent codex')

    claude_dir = root / '.claude' / 'agents'
    for skill in skills:
        path = claude_dir / f"{skill['slug']}.md"
        if not path.exists() or path.read_text(encoding='utf-8') != render_claude_agent(skill):
            errors.append(f'Claude adapter drift: {path}')

    cursor_dir = root / '.cursor' / 'rules'
    for skill in skills:
        path = cursor_dir / f"{skill['slug']}.mdc"
        if not path.exists() or path.read_text(encoding='utf-8') != render_cursor_rule(skill):
            errors.append(f'Cursor adapter drift: {path}')

    prompt_counts: dict[str, int] = {}
    prompts_path = root / 'benchmarks' / 'triggers.jsonl'
    if not prompts_path.exists():
        errors.append('missing benchmark prompt corpus')
    else:
        for line in prompts_path.read_text(encoding='utf-8').splitlines():
            if not line.strip():
                continue
            payload = json.loads(line)
            prompt_counts[payload['expected']] = prompt_counts.get(payload['expected'], 0) + 1
        for skill in skills:
            if prompt_counts.get(skill['slug'], 0) < 10:
                errors.append(f'benchmark corpus has fewer than 10 prompts for {skill["slug"]}')

    for rel in REQUIRED_FIXTURES:
        if not (root / rel).exists():
            errors.append(f'missing example fixture: {rel}')

    if errors:
        for error in errors:
            print(f'ERROR: {error}')
        return 1
    print('PASS: repository validation')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
