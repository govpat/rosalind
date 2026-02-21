import re
import sys


def get_seeds(pattern, text, k):
    seed_size = len(pattern) // (k + 1)
    for p0 in range(0, len(pattern) - seed_size + 1, seed_size):
        p1 = p0 + seed_size
        seed = pattern[p0:p1]
        for m in re.finditer(rf"(?=({seed}))", text):
            t0 = m.span()[0]
            t1 = t0 + seed_size
            yield (p0, p1), (t0, t1)


def process_seed(seed, k, pattern, text):
    def bounded_prefix_dist(full_pat, text_prefix, max_edits):
        """Distances edit(full_pat, text_prefix[:j]) for j near len(full_pat) within band."""
        m = len(full_pat)
        n = len(text_prefix)
        inf = max_edits + 1

        prev = [inf] * (n + 1)
        upto = min(n, max_edits)
        for j in range(upto + 1):
            prev[j] = j

        for i in range(1, m + 1):
            lo = max(0, i - max_edits)
            hi = min(n, i + max_edits)
            cur = [inf] * (n + 1)
            if lo == 0:
                cur[0] = i
            pi = full_pat[i - 1]
            row_best = inf
            start_j = max(1, lo)
            for j in range(start_j, hi + 1):
                cost = 0 if pi == text_prefix[j - 1] else 1
                a = prev[j] + 1
                b = cur[j - 1] + 1
                c = prev[j - 1] + cost
                v = a if a < b else b
                if c < v:
                    v = c
                cur[j] = v
                if v < row_best:
                    row_best = v
            if row_best > max_edits:
                return {}
            prev = cur

        lo = max(0, m - max_edits)
        hi = min(n, m + max_edits)
        out = {}
        for j in range(lo, hi + 1):
            if prev[j] <= max_edits:
                out[j] = prev[j]
        return out

    (p0, p1), (t0, t1) = seed
    seed_len = p1 - p0
    left_pat = pattern[:p0]
    right_pat = pattern[p1:]

    left_max = len(left_pat) + k
    left_text = text[max(0, t0 - left_max) : t0]
    left_d = bounded_prefix_dist(left_pat[::-1], left_text[::-1], k)
    if not left_d:
        return set()

    right_text = text[t1 : t1 + len(right_pat) + k]
    right_d = bounded_prefix_dist(right_pat, right_text, k)
    if not right_d:
        return set()

    hits = set()
    # j_left is number of chars consumed before seed, ending exactly at t0.
    for j_left, c_left in left_d.items():
        start0 = t0 - j_left
        for j_right, c_right in right_d.items():
            if c_left + c_right <= k:
                hits.add((start0 + 1, j_left + seed_len + j_right))
    return hits


def main(path="rosalind_ksim.txt"):
    sys.setrecursionlimit(10000)
    k_str, pattern, text = open(path).read().splitlines()
    k = int(k_str)

    seeds = list(get_seeds(pattern, text, k))
    print(f"found {len(seeds)} seeds", file=sys.stderr)

    all_hits = set()
    for idx, seed in enumerate(seeds, 1):
        if idx % 10 == 0:
            print(".", end="", file=sys.stderr, flush=True)
        all_hits.update(process_seed(seed, k, pattern, text))
    print("", file=sys.stderr)

    for pos, ln in sorted(all_hits):
        print(pos, ln)


if __name__ == "__main__":
    main()
