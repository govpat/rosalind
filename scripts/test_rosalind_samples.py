#!/usr/bin/env python3
import html
import math
import os
import re
import subprocess
import sys
import urllib.request
from dataclasses import dataclass
from typing import Callable

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
IDS_FILE = os.path.join(ROOT, 'all_problem_ids.txt')


@dataclass
class Result:
    pid: str
    status: str
    detail: str = ''


def fetch_problem_html(pid: str) -> str:
    url = f'https://rosalind.info/problems/{pid}/'
    with urllib.request.urlopen(url, timeout=30) as resp:
        return resp.read().decode('utf-8', errors='replace')


def extract_sample_blocks(page: str):
    m_ds = re.search(r'<h2 id="sample-dataset">.*?</h2>\s*<div class="codehilite"><pre>(.*?)</pre>', page, re.S)
    m_out = re.search(r'<h2 id="sample-output">.*?</h2>\s*<div class="codehilite"><pre>(.*?)</pre>', page, re.S)
    if not m_ds or not m_out:
        return None, None
    dataset = html.unescape(re.sub(r'<[^>]+>', '', m_ds.group(1))).replace('\r\n', '\n').strip('\n') + '\n'
    expected = html.unescape(re.sub(r'<[^>]+>', '', m_out.group(1))).replace('\r\n', '\n').strip('\n')
    return dataset, expected


def is_float_token(x: str) -> bool:
    return re.fullmatch(r'[+-]?(?:\d+\.?\d*|\d*\.\d+)(?:[eE][+-]?\d+)?', x) is not None


def compare_float_tokens(a: str, b: str) -> bool:
    ta = a.strip().split()
    tb = b.strip().split()
    if len(ta) != len(tb):
        return False
    for x, y in zip(ta, tb):
        if x == y:
            continue
        if is_float_token(x) and is_float_token(y):
            fx = float(x)
            fy = float(y)
            if not math.isclose(fx, fy, rel_tol=1.1e-3, abs_tol=1.1e-3):
                return False
        else:
            return False
    return True


def parse_fasta(dataset: str):
    seqs = []
    cur = []
    for raw in dataset.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith('>'):
            if cur:
                seqs.append(''.join(cur))
                cur = []
        else:
            cur.append(line)
    if cur:
        seqs.append(''.join(cur))
    return seqs


def is_subsequence(s: str, t: str) -> bool:
    j = 0
    for ch in s:
        if j < len(t) and ch == t[j]:
            j += 1
    return j == len(t)


def validate_sseq(dataset: str, got: str) -> bool:
    seqs = parse_fasta(dataset)
    if len(seqs) != 2:
        return False
    s, t = seqs
    try:
        idx = [int(x) for x in got.split()]
    except ValueError:
        return False
    if len(idx) != len(t):
        return False
    if any(i < 1 or i > len(s) for i in idx):
        return False
    if any(idx[i] >= idx[i + 1] for i in range(len(idx) - 1)):
        return False
    return ''.join(s[i - 1] for i in idx) == t


def validate_lcsm(dataset: str, expected: str, got: str) -> bool:
    seqs = parse_fasta(dataset)
    if not seqs:
        return False
    cand = got.strip()
    if not cand:
        return False
    if not all(cand in s for s in seqs):
        return False
    return len(cand) == len(expected.strip())


def validate_lcsq(dataset: str, expected: str, got: str) -> bool:
    seqs = parse_fasta(dataset)
    if len(seqs) != 2:
        return False
    s, t = seqs
    g = got.strip()
    return is_subsequence(s, g) and is_subsequence(t, g) and len(g) == len(expected.strip())


def validate_long(dataset: str, expected: str, got: str) -> bool:
    reads = parse_fasta(dataset)
    g = got.strip()
    if not g:
        return False
    if not all(r in g for r in reads):
        return False
    return len(g) == len(expected.strip())


def normalized_lines(s: str):
    return [x.strip() for x in s.strip().splitlines() if x.strip()]


def validate_grph(expected: str, got: str) -> bool:
    return sorted(normalized_lines(expected)) == sorted(normalized_lines(got))


def validate_orf(expected: str, got: str) -> bool:
    return set(normalized_lines(expected)) == set(normalized_lines(got))


def validate_sign(expected: str, got: str) -> bool:
    e = normalized_lines(expected)
    g = normalized_lines(got)
    if not e or not g:
        return False
    if e[0] != g[0]:
        return False
    return sorted(e[1:]) == sorted(g[1:])


def parse_set_line(line: str):
    s = line.strip()
    if not (s.startswith('{') and s.endswith('}')):
        return None
    inner = s[1:-1].strip()
    if not inner:
        return set()
    try:
        return set(int(x.strip()) for x in inner.split(','))
    except ValueError:
        return None


def validate_seto(expected: str, got: str) -> bool:
    e_lines = normalized_lines(expected)
    g_lines = normalized_lines(got)
    if len(e_lines) != 6 or len(g_lines) != 6:
        return False
    for e, g in zip(e_lines, g_lines):
        se = parse_set_line(e)
        sg = parse_set_line(g)
        if se is None or sg is None or se != sg:
            return False
    return True


def validate_prsm(dataset: str, got: str) -> bool:
    lines = [x.strip() for x in dataset.strip().splitlines() if x.strip()]
    if len(lines) < 3:
        return False
    n = int(lines[0])
    proteins = lines[1 : 1 + n]
    r = [float(x) for x in lines[1 + n :]]

    out = normalized_lines(got)
    if len(out) != 2:
        return False
    try:
        m_out = int(out[0])
    except ValueError:
        return False
    p_out = out[1]
    if p_out not in proteins:
        return False

    mass = {
        'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259, 'F': 147.06841,
        'G': 57.02146, 'H': 137.05891, 'I': 113.08406, 'K': 128.09496, 'L': 113.08406,
        'M': 131.04049, 'N': 114.04293, 'P': 97.05276, 'Q': 128.05858, 'R': 156.10111,
        'S': 87.03203, 'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333,
    }

    def spectrum(s):
        pref = [0.0]
        for ch in s:
            pref.append(round(pref[-1] + mass[ch], 5))
        total = pref[-1]
        out_spec = []
        for x in pref:
            out_spec.append(x)
            out_spec.append(round(total - x, 5))
        return out_spec

    def multiplicity(s):
        diffs = {}
        for a in spectrum(s):
            for b in r:
                d = round(a - b, 5)
                diffs[d] = diffs.get(d, 0) + 1
        return max(diffs.values()) if diffs else 0

    m_best = max(multiplicity(p) for p in proteins)
    if m_out != m_best:
        return False
    # Any protein achieving max multiplicity is acceptable.
    return True


def validate_line_set(expected: str, got: str) -> bool:
    return sorted(normalized_lines(expected)) == sorted(normalized_lines(got))


def revc(s: str) -> str:
    return s.translate(str.maketrans('ACGT', 'TGCA'))[::-1]


def rotations(s: str):
    return {s[i:] + s[:i] for i in range(len(s))}


def validate_pcov(dataset: str, got: str) -> bool:
    kmers = [x.strip() for x in dataset.splitlines() if x.strip()]
    g = got.strip()
    if not g or not kmers:
        return False
    circ = g + g
    return all(k in circ for k in kmers)


def validate_gasm(dataset: str, got: str) -> bool:
    reads = [x.strip() for x in dataset.splitlines() if x.strip()]
    g = got.strip()
    if not g or not reads:
        return False
    circ = g + g
    for r in reads:
        if r in circ or revc(r) in circ:
            continue
        return False
    return True


def validate_qrt(expected: str, got: str) -> bool:
    def canon(line: str):
        m = re.match(r'^\{([^}]*)\}\s+\{([^}]*)\}$', line.strip())
        if not m:
            return None
        a = tuple(sorted(x.strip() for x in m.group(1).split(',')))
        b = tuple(sorted(x.strip() for x in m.group(2).split(',')))
        return tuple(sorted((a, b)))

    e = [canon(x) for x in normalized_lines(expected)]
    g = [canon(x) for x in normalized_lines(got)]
    return None not in e and None not in g and sorted(e) == sorted(g)


def validate_loca_oap_sims(expected: str, got: str) -> bool:
    e = normalized_lines(expected)
    g = normalized_lines(got)
    if len(e) != 3 or len(g) != 3:
        return False
    if e[0] != g[0]:
        return False
    return len(g[1]) == len(g[2])


def validate_alph(expected: str, got: str) -> bool:
    e = normalized_lines(expected)
    g = normalized_lines(got)
    if not e or not g:
        return False
    if e[0] != g[0]:
        return False
    def parse(lines):
        out = {}
        i = 1
        while i + 1 < len(lines):
            if not lines[i].startswith('>'):
                return None
            out[lines[i][1:]] = lines[i + 1]
            i += 2
        return out
    pe = parse(e)
    pg = parse(g)
    if pe is None or pg is None:
        return False
    if set(pe.keys()) != set(pg.keys()):
        return False
    return all(len(pg[k]) == len(pe[k]) for k in pe)


def validate_cset(dataset: str, got: str) -> bool:
    rows = [x.strip() for x in dataset.splitlines() if x.strip()]
    out = normalized_lines(got)
    if not rows:
        return False
    return len(out) == len(rows) - 1 and all(x in rows for x in out)


def validate_chbp(dataset: str, got: str) -> bool:
    lines = [x.strip() for x in dataset.splitlines() if x.strip()]
    taxa = set(lines[0].split()) if lines else set()
    g = got.strip()
    return all(t in g for t in taxa)


def validate_eubt(dataset: str, expected: str, got: str) -> bool:
    taxa = set(dataset.split())
    g = normalized_lines(got)
    e = normalized_lines(expected)
    if len(g) != len(e):
        return False
    return all(all(t in line for t in taxa) for line in g)


SPECIAL: dict[str, Callable[[str, str, str], bool]] = {
    'sseq': lambda ds, exp, got: validate_sseq(ds, got),
    'lcsm': validate_lcsm,
    'lcsq': validate_lcsq,
    'long': validate_long,
    'grph': lambda ds, exp, got: validate_grph(exp, got),
    'orf': lambda ds, exp, got: validate_orf(exp, got),
    'sign': lambda ds, exp, got: validate_sign(exp, got),
    'seto': lambda ds, exp, got: validate_seto(exp, got),
    'prsm': lambda ds, exp, got: validate_prsm(ds, got),
    'grep': lambda ds, exp, got: validate_line_set(exp, got),
    'rsub': lambda ds, exp, got: validate_line_set(exp, got),
    'suff': lambda ds, exp, got: validate_line_set(exp, got),
    'qrt': lambda ds, exp, got: validate_qrt(exp, got),
    'pcov': lambda ds, exp, got: validate_pcov(ds, got),
    'gasm': lambda ds, exp, got: validate_gasm(ds, got),
    'loca': lambda ds, exp, got: validate_loca_oap_sims(exp, got),
    'oap': lambda ds, exp, got: validate_loca_oap_sims(exp, got),
    'sims': lambda ds, exp, got: validate_loca_oap_sims(exp, got),
    'alph': lambda ds, exp, got: validate_alph(exp, got),
    'cset': lambda ds, exp, got: validate_cset(ds, got),
    'chbp': lambda ds, exp, got: validate_chbp(ds, got),
    'eubt': lambda ds, exp, got: validate_eubt(ds, exp, got),
}


def evaluate(pid: str, dataset: str, expected: str, got: str) -> bool:
    exp = expected.strip()
    out = got.strip()
    if exp == out:
        return True
    if compare_float_tokens(exp, out):
        return True
    if pid in SPECIAL:
        return SPECIAL[pid](dataset, exp, out)
    return False


def run_one(pid: str) -> Result:
    pdir = os.path.join(ROOT, pid)
    main_py = os.path.join(pdir, 'main.py')
    input_file = os.path.join(pdir, f'rosalind_{pid}.txt')

    if not os.path.isfile(main_py):
        return Result(pid, 'missing', 'main.py missing')

    try:
        page = fetch_problem_html(pid)
    except Exception as e:
        return Result(pid, 'error', f'fetch failed: {e}')

    dataset, expected = extract_sample_blocks(page)
    if dataset is None:
        return Result(pid, 'skip', 'no sample blocks')

    with open(input_file, 'w') as f:
        f.write(dataset)

    try:
        proc = subprocess.run([sys.executable, 'main.py'], cwd=pdir, capture_output=True, text=True, timeout=30)
    except subprocess.TimeoutExpired:
        return Result(pid, 'fail', 'timeout >30s')

    if proc.returncode != 0:
        err = (proc.stderr or proc.stdout).strip()
        return Result(pid, 'fail', f'runtime error: {err[:400]}')

    out = proc.stdout
    if evaluate(pid, dataset, expected, out):
        return Result(pid, 'pass')

    brief = (
        'output mismatch\n'
        + 'expected:\n' + expected[:250] + ('...' if len(expected) > 250 else '') + '\n'
        + 'got:\n' + out[:250] + ('...' if len(out) > 250 else '')
    )
    return Result(pid, 'fail', brief)


def main():
    with open(IDS_FILE, 'r') as f:
        ids = [x.strip() for x in f if x.strip()]

    results: list[Result] = []
    for i, pid in enumerate(ids, start=1):
        r = run_one(pid)
        results.append(r)
        print(f'[{i:03d}/{len(ids):03d}] {pid}: {r.status}')

    out_path = os.path.join(ROOT, 'sample_test_report.txt')
    with open(out_path, 'w') as f:
        for r in results:
            f.write(f'{r.pid}\t{r.status}\t{r.detail}\n')

    summary = {}
    for r in results:
        summary[r.status] = summary.get(r.status, 0) + 1

    print('\nSummary:')
    for k in sorted(summary):
        print(f'{k}: {summary[k]}')
    print(f'report: {out_path}')

    if summary.get('fail', 0) > 0 or summary.get('missing', 0) > 0 or summary.get('error', 0) > 0:
        sys.exit(1)


if __name__ == '__main__':
    main()
