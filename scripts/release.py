#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
from pathlib import Path

from skill_lib import list_skill_dirs, repo_root


def bump_stable(version: str) -> str:
    major, minor, patch = version.split('.')
    return f'{major}.{minor}.{int(patch) + 1}'


def bump_canary(version: str) -> str:
    if '-canary.' in version:
        base, suffix = version.split('-canary.')
        return f'{base}-canary.{int(suffix) + 1}'
    return f'{version}-canary.1'


def update_skill_versions(root: Path, version: str) -> None:
    pattern = re.compile(r'(^  version: ")[^"]+(")', re.MULTILINE)
    for skill_dir in list_skill_dirs(root):
        path = skill_dir / 'SKILL.md'
        text = path.read_text(encoding='utf-8')
        path.write_text(pattern.sub(rf'\g<1>{version}\2', text), encoding='utf-8')


def main() -> int:
    parser = argparse.ArgumentParser(description='Prepare release metadata and generated outputs.')
    parser.add_argument('--channel', choices=['stable', 'canary'], required=True)
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    root = repo_root()
    version_path = root / 'VERSION'
    current = version_path.read_text(encoding='utf-8').strip()
    next_version = bump_stable(current) if args.channel == 'stable' else bump_canary(current)
    if args.dry_run:
        print(next_version)
        return 0

    version_path.write_text(next_version + '\n', encoding='utf-8')
    update_skill_versions(root, next_version)
    subprocess.run(['python3', 'scripts/build_adapters.py', '--agent', 'all'], cwd=root, check=True)

    changelog_path = root / 'CHANGELOG.md'
    old = changelog_path.read_text(encoding='utf-8')
    header = f'## {next_version} - {dt.date.today().isoformat()}\n- Automated {args.channel} release preparation.\n\n'
    if old.startswith('# Changelog\n\n'):
        body = old[len('# Changelog\n\n') :]
    else:
        body = old
    changelog_path.write_text('# Changelog\n\n' + header + body, encoding='utf-8')
    print(next_version)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
