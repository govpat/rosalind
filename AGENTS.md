# AGENTS Workflow (Rosalind Repo)

## Objective

Run Rosalind problem solutions locally, generate outputs, and keep datasets/outputs organized per problem folder.

## Standard File Conventions

- Problem folder: `/Users/sgp/github/rosalind/<id>/`
- Input dataset filename: `rosalind_<id>.txt`
- Solution entrypoint: `main.py`
- Output filename: `<id>_out.txt`

## Core Execution Workflow

1. Identify problem id `<id>` from dataset filename.
2. Copy dataset into matching folder:
   - `cp ~/Downloads/rosalind_<id>.txt /Users/sgp/github/rosalind/<id>/rosalind_<id>.txt`
3. Run solution from the problem folder:
   - `cd /Users/sgp/github/rosalind/<id> && python main.py > <id>_out.txt`
4. If output is requested in Downloads:
   - `cp <id>_out.txt ~/Downloads/<id>_out.txt`
5. Final organization rule:
   - Move both `rosalind_<id>.txt` and `<id>_out.txt` into `/Users/sgp/github/rosalind/<id>/`.

## Batch Move Workflow (Downloads -> Repo)

For files in `~/Downloads`:

- `rosalind_*.txt` -> move to matching `/Users/sgp/github/rosalind/<id>/`
- `*_out.txt` -> move to matching `/Users/sgp/github/rosalind/<id>/`

Skip files that do not map to an existing problem folder.

## Functional Testing

Run repository sample tests:

- `python -u /Users/sgp/github/rosalind/scripts/test_rosalind_samples.py`

Report path:

- `/Users/sgp/github/rosalind/sample_test_report.txt`

## Performance / Failure Handling

If a solver is slow or times out:

1. Validate correctness on small/brute-forceable cases.
2. Refactor to a more efficient algorithm.
3. Re-run full dataset and confirm output is non-empty.
4. Re-test sample behavior if available.

## Monitoring Notes

- Watcher script (optional): `/Users/sgp/github/rosalind/scripts/watch_downloads_and_solve.sh`
- If asked to stop monitoring, kill watcher processes before file moves to prevent regenerated outputs during cleanup.
