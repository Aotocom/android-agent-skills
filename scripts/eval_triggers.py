#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict

from skill_lib import load_skills, repo_root


def score(prompt: str, skill: dict) -> int:
    prompt_l = prompt.lower()
    total = 0
    for phrase in skill['metadata']['triggers']['include']:
        phrase_l = phrase.lower()
        if phrase_l in prompt_l:
            total += 8
        else:
            total += sum(1 for token in phrase_l.split() if token in prompt_l)
    for token in skill['slug'].split('-'):
        if token in prompt_l:
            total += 1
    for phrase in skill['metadata']['triggers']['exclude']:
        if phrase.lower() in prompt_l:
            total -= 4
    return total


def main() -> int:
    parser = argparse.ArgumentParser(description='Evaluate prompt-to-skill trigger precision.')
    parser.add_argument('--skill', help='Optional skill slug filter')
    parser.add_argument('--input', default='benchmarks/triggers.jsonl')
    args = parser.parse_args()

    root = repo_root()
    skills = load_skills(root)
    skill_map = {skill['slug']: skill for skill in skills}
    prompts = []
    with (root / args.input).open(encoding='utf-8') as handle:
        for line in handle:
            if not line.strip():
                continue
            payload = json.loads(line)
            if args.skill and payload['expected'] != args.skill:
                continue
            prompts.append(payload)
    if not prompts:
        print('No prompts to evaluate.')
        return 1

    hits = 0
    totals = Counter()
    correct = Counter()
    confusion = defaultdict(Counter)
    for payload in prompts:
        ranked = sorted(skill_map.values(), key=lambda skill: score(payload['prompt'], skill), reverse=True)
        predicted = ranked[0]['slug']
        expected = payload['expected']
        totals[expected] += 1
        if predicted == expected:
            hits += 1
            correct[expected] += 1
        else:
            confusion[expected][predicted] += 1

    accuracy = hits / len(prompts)
    print(f'Prompts: {len(prompts)}')
    print(f'Accuracy: {accuracy:.2%}')
    for slug in sorted(totals):
        recall = correct[slug] / totals[slug]
        print(f'- {slug}: recall={recall:.2%} ({correct[slug]}/{totals[slug]})')
        if confusion[slug]:
            common = ', '.join(f'{other}={count}' for other, count in confusion[slug].most_common(3))
            print(f'  confusion: {common}')

    artifact = {
        'prompts': len(prompts),
        'accuracy': accuracy,
        'recall': {slug: correct[slug] / totals[slug] for slug in totals},
        'confusion': {slug: dict(counter) for slug, counter in confusion.items()},
    }
    (root / 'benchmarks' / 'last_eval.json').write_text(json.dumps(artifact, indent=2, sort_keys=True), encoding='utf-8')
    return 0 if accuracy >= 0.90 else 1


if __name__ == '__main__':
    raise SystemExit(main())
