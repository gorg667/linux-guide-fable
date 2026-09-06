#!/usr/bin/env bash
# Concatenate all chapter files into guide/FULL_GUIDE.md
set -euo pipefail
cd "$(dirname "$0")/.."
out=guide/FULL_GUIDE.md
{
  echo "# Choosing a Linux Distribution for Software Engineering, CS Study, and Daily Life"
  echo
  echo "_Generated $(date -u +%Y-%m-%d) from individual chapter files. See README.md for the table of contents._"
  echo
  for f in guide/[0-9][0-9]-*.md guide/[A-Z]-*.md; do
    [ -f "$f" ] || continue
    echo
    echo "---"
    echo
    cat "$f"
    echo
  done
} > "$out"
wc -w guide/*.md | tail -1
echo "Wrote $out"
