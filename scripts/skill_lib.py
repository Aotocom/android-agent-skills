#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import shutil
from pathlib import Path
from typing import Any

REQUIRED_SECTIONS = [
    '## When To Use',
    '## Workflow',
    '## Guardrails',
    '## Anti-Patterns',
    '## Examples',
    '## Done Checklist',
    '## Official References',
]

CATEGORY_LABELS = {
    'foundations': 'Foundations',
    'product': 'Product Flows',
    'ui': 'UI Systems',
    'data-platform': 'Data And Platform',
    'quality-release': 'Quality And Delivery',
    'legacy-rescue': 'Legacy Rescue',
}


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def list_skill_dirs(root: Path | None = None) -> list[Path]:
    base = (root or repo_root()) / 'skills'
    return sorted(path for path in base.iterdir() if path.is_dir())


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if not value:
        return ''
    if value.startswith('[') or value.startswith('{'):
        return json.loads(value)
    if value.startswith('"') and value.endswith('"'):
        return json.loads(value)
    if value in {'true', 'false'}:
        return value == 'true'
    return value


def parse_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding='utf-8')
    if not text.startswith('---\n'):
        raise ValueError(f'{path} is missing YAML frontmatter')
    end = text.find('\n---\n', 4)
    if end == -1:
        raise ValueError(f'{path} frontmatter is malformed')
    frontmatter = text[4:end]
    body = text[end + 5 :]

    data: dict[str, Any] = {}
    stack: list[tuple[int, dict[str, Any]]] = [(-1, data)]
    for raw in frontmatter.splitlines():
        if not raw.strip():
            continue
        indent = len(raw) - len(raw.lstrip(' '))
        key, _, raw_value = raw.strip().partition(':')
        while stack and indent <= stack[-1][0]:
            stack.pop()
        current = stack[-1][1]
        if raw_value.strip() == '':
            current[key] = {}
            stack.append((indent, current[key]))
        else:
            current[key] = parse_scalar(raw_value)
    return data, body


def read_skill(skill_dir: Path) -> dict[str, Any]:
    metadata, body = parse_frontmatter(skill_dir / 'SKILL.md')
    metadata['body'] = body
    metadata['slug'] = skill_dir.name
    return metadata


def load_skills(root: Path | None = None) -> list[dict[str, Any]]:
    return [read_skill(skill_dir) for skill_dir in list_skill_dirs(root)]


def ensure_clean_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def count_reference_links(body: str) -> int:
    return len(re.findall(r'\[[^\]]+\]\(https?://', body))


def render_agents_catalog(skills: list[dict[str, Any]]) -> str:
    lines = [
        '# Android Agent Skills',
        '',
        'A discovery catalog for the canonical Android skills in this repository.',
        '',
        '## Install Surfaces',
        '- Codex / open standard: root `skills/` plus this `AGENTS.md` catalog.',
        '- Claude Code: generated `.claude/agents/` files.',
        '- Cursor: generated `.cursor/rules/` files.',
        '',
    ]
    for category in CATEGORY_LABELS:
        lines.append(f'## {CATEGORY_LABELS[category]}')
        for skill in [item for item in skills if item['metadata']['category'] == category]:
            lines.append(
                f"- `{skill['slug']}`: {skill['description']} Path: `skills/{skill['slug']}`"
            )
        lines.append('')
    return '\n'.join(lines).strip() + '\n'


def render_claude_agent(skill: dict[str, Any]) -> str:
    include = ', '.join(skill['metadata']['triggers']['include'][:3])
    return (
        '---\n'
        f"name: {skill['slug']}\n"
        f"description: {skill['description']}\n"
        '---\n\n'
        f"# {skill['slug']}\n\n"
        f"Use this subagent when the request is about {include}.\n\n"
        f"Canonical source: `skills/{skill['slug']}/SKILL.md`.\n"
    )


def render_cursor_rule(skill: dict[str, Any]) -> str:
    include = ', '.join(skill['metadata']['triggers']['include'][:3])
    return (
        '---\n'
        f"description: {skill['description']}\n"
        'alwaysApply: false\n'
        '---\n\n'
        f"# {skill['slug']}\n\n"
        f"Activate when the request is about {include}.\n"
        f"Read `skills/{skill['slug']}/SKILL.md` for the canonical workflow.\n"
    )
