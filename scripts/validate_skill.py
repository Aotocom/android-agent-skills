#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from skill_lib import REQUIRED_SECTIONS, count_reference_links, read_skill

REQUIRED_DIRS = ['agents', 'references', 'scripts']
REQUIRED_FILES = ['SKILL.md', 'agents/openai.yaml']
MODERNIZATION_REF_FILES = [
    'references/agp-upgrade-notes.md',
    'references/kotlin-compatibility.md',
    'references/androidx-migration.md',
    'references/gradle-compatibility.md',
    'references/sdk-behavior-changes.md',
    'references/jetpack-release-notes.md',
    'references/deprecated-replacements.md',
    'references/upgrade-matrix.md',
    'references/issue-signature-catalog.md',
]
MODERNIZATION_SCRIPT_FILES = [
    'scripts/scan_project.py',
    'scripts/build_compat_matrix.py',
    'scripts/generate_remediation_checklist.py',
    'scripts/apply_safe_upgrades.py',
    'scripts/check_16kb_alignment.py',
]


def validate(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    for rel in REQUIRED_DIRS:
        if not (skill_dir / rel).is_dir():
            errors.append(f'missing directory: {rel}')
    for rel in REQUIRED_FILES:
        if not (skill_dir / rel).exists():
            errors.append(f'missing file: {rel}')
    if errors:
        return errors

    skill = read_skill(skill_dir)
    for key in ['name', 'description', 'metadata']:
        if key not in skill:
            errors.append(f'missing frontmatter key: {key}')
    metadata = skill.get('metadata', {})
    for key in ['version', 'category', 'tags', 'triggers', 'owners', 'test_targets']:
        if key not in metadata:
            errors.append(f'missing metadata key: {key}')
    triggers = metadata.get('triggers', {})
    for key in ['include', 'exclude']:
        if key not in triggers:
            errors.append(f'missing trigger key: {key}')

    body = skill.get('body', '')
    for section in REQUIRED_SECTIONS:
        if section not in body:
            errors.append(f'missing section: {section}')
    if body.count('### Happy path') != 1 or body.count('### Edge case') != 1 or body.count('### Failure recovery') != 1:
        errors.append('examples section must contain Happy path, Edge case, and Failure recovery headings exactly once')
    if count_reference_links(body) < 4:
        errors.append('skill must include at least 4 official reference links')

    if skill_dir.name == 'android-modernization-upgrade':
        for rel in MODERNIZATION_REF_FILES + MODERNIZATION_SCRIPT_FILES:
            if not (skill_dir / rel).exists():
                errors.append(f'missing modernization asset: {rel}')
        body_l = body.lower()
        if '16 kb alignment' not in body_l:
            errors.append('modernization skill must mention 16 KB alignment')
        if 'purpose:' not in body_l:
            errors.append('modernization skill must document purpose explicitly')
        if 'responsibilities' not in body_l:
            errors.append('modernization skill must document responsibilities explicitly')
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description='Validate a single skill directory.')
    parser.add_argument('path', type=Path)
    args = parser.parse_args()
    errors = validate(args.path)
    if errors:
        for error in errors:
            print(f'ERROR: {args.path}: {error}')
        return 1
    print(f'PASS: {args.path}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
