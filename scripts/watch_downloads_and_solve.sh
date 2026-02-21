#!/usr/bin/env bash
set -euo pipefail

DOWNLOADS="/Users/sgp/Downloads"
ROOT="/Users/sgp/github/rosalind"
LOG="/tmp/rosalind_watch.log"

mkdir -p /tmp

echo "[$(date '+%Y-%m-%d %H:%M:%S')] watcher started" >> "$LOG"

while true; do
  shopt -s nullglob
  for in_file in "$DOWNLOADS"/rosalind_*.txt; do
    base="$(basename "$in_file")"
    id="${base#rosalind_}"
    id="${id%.txt}"

    prob_dir="$ROOT/$id"
    main_py="$prob_dir/main.py"
    local_in="$prob_dir/rosalind_${id}.txt"
    out_file="$DOWNLOADS/${id}_out.txt"

    if [[ ! -f "$main_py" ]]; then
      continue
    fi

    # Process when output is missing or input changed since last output
    if [[ ! -f "$out_file" || "$in_file" -nt "$out_file" ]]; then
      cp "$in_file" "$local_in"
      if (cd "$prob_dir" && python main.py > "$out_file" 2>/tmp/rosalind_watch_err.log); then
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] solved $id -> $out_file" >> "$LOG"
        osascript -e "display notification \"Generated $(basename "$out_file")\" with title \"Rosalind Solver\" subtitle \"$id solved\"" >/dev/null 2>&1 || true
        afplay /System/Library/Sounds/Glass.aiff >/dev/null 2>&1 || true
      else
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERROR $id (see /tmp/rosalind_watch_err.log)" >> "$LOG"
      fi
    fi
  done
  sleep 2
done
