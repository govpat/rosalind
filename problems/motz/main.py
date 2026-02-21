MOD = 1_000_000


def parse_fasta(path):
    seq = []
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('>'):
                seq.append(line)
    return ''.join(seq)


def motz(s, memo):
    if len(s) <= 1:
        return 1
    if s in memo:
        return memo[s]

    total = motz(s[1:], memo)
    pairs = {('A', 'U'), ('U', 'A'), ('C', 'G'), ('G', 'C')}
    for k in range(1, len(s)):
        if (s[0], s[k]) in pairs:
            total += motz(s[1:k], memo) * motz(s[k + 1:], memo)
    memo[s] = total % MOD
    return memo[s]


def main():
    s = parse_fasta('rosalind_motz.txt')
    print(motz(s, {}))


if __name__ == '__main__':
    main()
