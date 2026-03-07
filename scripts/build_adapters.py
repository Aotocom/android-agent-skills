#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from skill_lib import ensure_clean_dir, load_skills, render_agents_catalog, render_claude_agent, render_cursor_rule, repo_root


def build_codex(root: Path, skills: list[dict]) -> None:
    (root / 'AGENTS.md').write_text(render_agents_catalog(skills), encoding='utf-8')
    dist = root / 'dist' / 'codex'
    ensure_clean_dir(dist)
    (dist / 'AGENTS.md').write_text(render_agents_catalog(skills), encoding='utf-8')
    shutil.copytree(root / 'skills', dist / 'skills')


def build_claude(root: Path, skills: list[dict]) -> None:
    target = root / '.claude' / 'agents'
    ensure_clean_dir(target)
    for skill in skills:
        (target / f"{skill['slug']}.md").write_text(render_claude_agent(skill), encoding='utf-8')
    dist = root / 'dist' / 'claude'
    ensure_clean_dir(dist)
    shutil.copytree(root / '.claude', dist / '.claude')


def build_cursor(root: Path, skills: list[dict]) -> None:
    target = root / '.cursor' / 'rules'
    ensure_clean_dir(target)
    for skill in skills:
        (target / f"{skill['slug']}.mdc").write_text(render_cursor_rule(skill), encoding='utf-8')
    dist = root / 'dist' / 'cursor'
    ensure_clean_dir(dist)
    shutil.copytree(root / '.cursor', dist / '.cursor')


def main() -> int:
    parser = argparse.ArgumentParser(description='Generate agent-specific outputs from canonical skills.')
    parser.add_argument('--agent', choices=['codex', 'claude', 'cursor', 'all'], required=True)
    args = parser.parse_args()

    root = repo_root()
    skills = load_skills(root)
    if args.agent in {'codex', 'all'}:
        build_codex(root, skills)
    if args.agent in {'claude', 'all'}:
        build_claude(root, skills)
    if args.agent in {'cursor', 'all'}:
        build_cursor(root, skills)
    print(f'Generated adapters for {args.agent}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
