# Rosalind Solutions (Python)

This repository contains Python solutions for Rosalind bioinformatics problems, organized one problem per folder.

## Project Goals

- Keep each problem self-contained and runnable.
- Support quick local execution against downloaded Rosalind datasets.
- Validate behavior using sample-based functional tests.

## Repository Structure

- `/<problem_id>/main.py`  
  Solution entrypoint for that problem (for example `dna/main.py`, `ksim/main.py`, `laff/main.py`).
- `/<problem_id>/rosalind_<problem_id>.txt`  
  Dataset file used when running locally.
- `/<problem_id>/<problem_id>_out.txt`  
  Generated output for that dataset.
- `scripts/test_rosalind_samples.py`  
  Functional sample test runner across problems.
- `scripts/watch_downloads_and_solve.sh`  
  Optional watcher for processing newly downloaded datasets.
- `scripts/run_from_downloads.sh`  
  Helper to run one downloaded dataset by problem id.
- `_vendor_dh/`  
  Vendored helper implementations used by some problems.
- `problems.yaml`  
  Metadata index for each problem (`status`, `runtime`, `dependencies`, `last_validated`).

## Solved Coverage

The repo includes solution folders for the Rosalind list-view problem set and currently has 100+ runnable problem modules.

## How To Run A Problem

From the repository root:

```bash
cp ~/Downloads/rosalind_dna.txt dna/rosalind_dna.txt
cd dna
python main.py > dna_out.txt
```

General pattern:

1. Place dataset as `rosalind_<id>.txt` inside `<id>/`.
2. Run `python main.py` from that folder.
3. Save output to `<id>_out.txt`.

## Testing

Run sample functional tests:

```bash
python -u scripts/test_rosalind_samples.py
```

The script writes a summary report to `sample_test_report.txt`.

## Dependencies

Core solutions are Python-only, but some advanced problems use extra packages. Depending on the problem set you run, install:

- `numpy`
- `scipy`
- `biopython`
- `parasail`
- `dendropy`
- `tqdist` (for specific tree-distance tasks)

## Notes

- Most solutions are designed for file-based execution (`rosalind_<id>.txt`) rather than stdin piping.
- Keep datasets and outputs in the corresponding problem folder for reproducible reruns.

## Contribution Rules

- Keep one solution per folder as `/<id>/main.py`.
- Keep naming strict: input `rosalind_<id>.txt`, output `<id>_out.txt`.
- Prefer deterministic output formatting (no extra logs in stdout).
- If a problem is performance-sensitive, include the most efficient practical algorithm rather than brute force.
- Update `problems.yaml` when adding or materially changing a solution:
  - `status`: `implemented` or `dataset_run`
  - `runtime`: measured value or `null`
  - `dependencies`: external packages required by that problem
  - `last_validated`: date of latest verified run
