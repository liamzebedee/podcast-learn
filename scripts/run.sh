#!/usr/bin/env bash
set -euo pipefail

{
  cat src/PROMPT.md
  echo
  echo "$1"
} | claude --dangerously-skip-permissions