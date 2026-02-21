def parse_fasta(path):
    seqs = []
    curr = []
    with open(path, 'r') as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            if line.startswith('>'):
                if curr:
                    seqs.append(''.join(curr))
                    curr = []
            else:
                curr.append(line)
    if curr:
        seqs.append(''.join(curr))
    return seqs


def lcs(s, t):
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    i, j = m, n
    out = []
    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]:
            out.append(s[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(out))


def main():
    s, t = parse_fasta('rosalind_lcsq.txt')
    print(lcs(s, t))


if __name__ == '__main__':
    main()
