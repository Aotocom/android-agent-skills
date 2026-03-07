#!/usr/bin/env bash
    set -euo pipefail

    AGENT="codex"
    SCOPE="user"
    SKILL="all"

    while [[ $# -gt 0 ]]; do
      case "$1" in
        --agent)
          AGENT="$2"
          shift 2
          ;;
        --scope)
          SCOPE="$2"
          shift 2
          ;;
        --skill)
          SKILL="$2"
          shift 2
          ;;
        *)
          echo "Unknown argument: $1" >&2
          exit 1
          ;;
      esac
    done

    ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
    python3 "$ROOT/scripts/build_adapters.py" --agent all >/dev/null

    copy_skill() {
      local src="$1"
      local dest="$2"
      mkdir -p "$dest"
      rsync -a --delete "$src" "$dest/"
    }

    case "$AGENT" in
      codex)
        TARGET="${CODEX_HOME:-$HOME/.codex}/skills"
        if [[ "$SCOPE" == "project" ]]; then
          TARGET="$PWD/skills"
        fi
        mkdir -p "$TARGET"
        if [[ "$SKILL" == "all" ]]; then
          rsync -a "$ROOT/skills/" "$TARGET/"
        else
          rsync -a "$ROOT/skills/$SKILL" "$TARGET/"
        fi
        cp "$ROOT/AGENTS.md" "$(dirname "$TARGET")/AGENTS.md" 2>/dev/null || true
        ;;
      claude)
        TARGET="$HOME/.claude/agents"
        if [[ "$SCOPE" == "project" ]]; then
          TARGET="$PWD/.claude/agents"
        fi
        mkdir -p "$TARGET"
        if [[ "$SKILL" == "all" ]]; then
          rsync -a "$ROOT/.claude/agents/" "$TARGET/"
        else
          rsync -a "$ROOT/.claude/agents/$SKILL.md" "$TARGET/"
        fi
        ;;
      cursor)
        TARGET="$PWD/.cursor/rules"
        if [[ "$SCOPE" == "user" ]]; then
          TARGET="$HOME/.cursor/rules"
        fi
        mkdir -p "$TARGET"
        if [[ "$SKILL" == "all" ]]; then
          rsync -a "$ROOT/.cursor/rules/" "$TARGET/"
        else
          rsync -a "$ROOT/.cursor/rules/$SKILL.mdc" "$TARGET/"
        fi
        ;;
      *)
        echo "Unsupported agent: $AGENT" >&2
        exit 1
        ;;
    esac

    echo "Installed $SKILL for $AGENT ($SCOPE)"
