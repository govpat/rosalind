#!/usr/bin/env bash
set -euo pipefail

DOWNLOADS="/Users/sgp/Downloads"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

if [ "$#" -lt 1 ]; then
  if [ -f "$ROOT/all_problem_ids.txt" ]; then
    IDS=()
    while IFS= read -r line; do
      [ -n "$line" ] && IDS+=("$line")
    done < "$ROOT/all_problem_ids.txt"
  else
    echo "usage: $0 <problem_id> [problem_id ...]"
    exit 1
  fi
else
  IDS=("$@")
fi

for p in "${IDS[@]}"; do
  in_file="$DOWNLOADS/rosalind_${p}.txt"
  out_file="$DOWNLOADS/${p}_out.txt"
  prob_dir="$ROOT/$p"

  if [ ! -d "$prob_dir" ]; then
    echo "skip:$p (missing directory $prob_dir)"
    continue
  fi
  if [ ! -f "$in_file" ]; then
    echo "skip:$p (missing input $in_file)"
    continue
  fi

  cp "$in_file" "$prob_dir/rosalind_${p}.txt"
  (cd "$prob_dir" && python main.py) > "$out_file"
  echo "wrote:$out_file"
done
