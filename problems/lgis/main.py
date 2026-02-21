def reconstruct(seq, prev, end_idx):
    out = []
    i = end_idx
    while i != -1:
        out.append(seq[i])
        i = prev[i]
    return list(reversed(out))


def lis(seq):
    n = len(seq)
    dp = [1] * n
    prev = [-1] * n
    best = 0

    for i in range(n):
        for j in range(i):
            if seq[j] < seq[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
        if dp[i] > dp[best]:
            best = i

    return reconstruct(seq, prev, best)


def lds(seq):
    n = len(seq)
    dp = [1] * n
    prev = [-1] * n
    best = 0

    for i in range(n):
        for j in range(i):
            if seq[j] > seq[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
        if dp[i] > dp[best]:
            best = i

    return reconstruct(seq, prev, best)


def main():
    with open('rosalind_lgis.txt', 'r') as f:
        _ = int(f.readline().strip())
        perm = list(map(int, f.readline().strip().split()))

    print(' '.join(map(str, lis(perm))))
    print(' '.join(map(str, lds(perm))))


if __name__ == '__main__':
    main()
