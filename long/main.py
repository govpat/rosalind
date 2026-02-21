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


def overlap(a, b):
    max_k = min(len(a), len(b))
    min_k = max(len(a) // 2 + 1, 1)
    for k in range(max_k, min_k - 1, -1):
        if a[-k:] == b[:k]:
            return k
    return 0


def main():
    reads = parse_fasta('rosalind_long.txt')
    n = len(reads)

    out = [-1] * n
    inc = [-1] * n
    ov = [0] * n

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            k = overlap(reads[i], reads[j])
            if k > ov[i]:
                ov[i] = k
                out[i] = j
            if k > 0:
                inc[j] = i

    start = next(i for i in range(n) if inc[i] == -1)

    ans = reads[start]
    cur = start
    while out[cur] != -1:
        nxt = out[cur]
        k = overlap(reads[cur], reads[nxt])
        ans += reads[nxt][k:]
        cur = nxt

    print(ans)


if __name__ == '__main__':
    main()
