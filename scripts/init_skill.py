#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from skill_lib import repo_root

SECTIONS = [
    '## When To Use\n- Describe the main trigger language here.\n',
    '## Workflow\n1. Inspect the request and current Android surface.\n2. Apply the recommended pattern.\n3. Validate with the listed targets.\n',
    '## Guardrails\n- Add do-not-break constraints.\n',
    '## Anti-Patterns\n- Add common mistakes to avoid.\n',
    '## Examples\n### Happy path\n- Scenario: ...\n- Command: `...`\n\n### Edge case\n- Scenario: ...\n- Command: `...`\n\n### Failure recovery\n- Scenario: ...\n- Command: `...`\n',
    '## Done Checklist\n- Define completion.\n',
    '## Official References\n- [Android Developers](https://developer.android.com/)\n',
]


def main() -> int:
    parser = argparse.ArgumentParser(description='Scaffold a new Android skill.')
    parser.add_argument('name')
    parser.add_argument('--description', required=True)
    parser.add_argument('--category', default='foundations')
    args = parser.parse_args()

    root = repo_root()
    skill_dir = root / 'skills' / args.name
    skill_dir.mkdir(parents=True, exist_ok=False)
    (skill_dir / 'agents').mkdir()
    (skill_dir / 'references').mkdir()
    (skill_dir / 'scripts').mkdir()

    frontmatter = '\n'.join(
        [
            '---',
            f'name: "{args.name}"',
            f'description: "{args.description}"',
            'metadata:',
            '  version: "0.1.0"',
            f'  category: "{args.category}"',
            '  tags: ' + json.dumps(['android']),
            '  triggers:',
            '    include: ' + json.dumps([args.description.lower()]),
            '    exclude: ' + json.dumps([]),
            '  owners: ' + json.dumps(['@android-agent-skills/maintainers']),
            '  test_targets: ' + json.dumps(['benchmarks/triggers.jsonl']),
            '---',
            '',
        ]
    )
    (skill_dir / 'SKILL.md').write_text(
        frontmatter + f'# {args.name}\n\n' + '\n'.join(SECTIONS),
        encoding='utf-8',
    )
    (skill_dir / 'agents' / 'openai.yaml').write_text(
        '\n'.join(
            [
                'interface:',
                f'  display_name: "{args.name.replace("-", " ").title()}"',
                f'  short_description: "{args.description}"',
                f'  default_prompt: "Use ${args.name} when the request is about {args.description}."',
                '',
            ]
        ),
        encoding='utf-8',
    )
    (skill_dir / 'references' / 'official-links.md').write_text('# Official Links\n', encoding='utf-8')
    (skill_dir / 'references' / 'patterns.md').write_text('# Patterns\n', encoding='utf-8')
    (skill_dir / 'references' / 'scenarios.md').write_text('# Scenarios\n', encoding='utf-8')
    script_path = skill_dir / 'scripts' / 'run_examples.sh'
    script_path.write_text('#!/usr/bin/env bash\nset -euo pipefail\necho "Add example commands here."\n', encoding='utf-8')
    script_path.chmod(0o755)
    print(f'Created {skill_dir}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
