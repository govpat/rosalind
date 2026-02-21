def parse_fasta(path):
    seqs = []
    cur = []
    with open(path, 'r') as f:
        for raw in f:
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


def edta(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    parent = [[None] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = i
        parent[i][0] = (i - 1, 0, 'D')
    for j in range(1, m + 1):
        dp[0][j] = j
        parent[0][j] = (0, j - 1, 'I')

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            cand = [
                (dp[i - 1][j] + 1, (i - 1, j, 'D')),
                (dp[i][j - 1] + 1, (i, j - 1, 'I')),
                (dp[i - 1][j - 1] + cost, (i - 1, j - 1, 'M')),
            ]
            best = min(cand, key=lambda x: x[0])
            dp[i][j] = best[0]
            parent[i][j] = best[1]

    a1, a2 = [], []
    i, j = n, m
    while i > 0 or j > 0:
        pi, pj, op = parent[i][j]
        if op == 'M':
            a1.append(s1[i - 1])
            a2.append(s2[j - 1])
        elif op == 'D':
            a1.append(s1[i - 1])
            a2.append('-')
        else:
            a1.append('-')
            a2.append(s2[j - 1])
        i, j = pi, pj

    return dp[n][m], ''.join(reversed(a1)), ''.join(reversed(a2))


def main():
    s1, s2 = parse_fasta('rosalind_edta.txt')
    d, a1, a2 = edta(s1, s2)
    print(d)
    print(a1)
    print(a2)


if __name__ == '__main__':
    main()
