MOD = 1_000_000


def parse_fasta(path):
    seq = []
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('>'):
                seq.append(line)
    return ''.join(seq)


def cat_count(s, memo):
    if len(s) <= 1:
        return 1
    if s in memo:
        return memo[s]

    total = 0
    pairs = {('A', 'U'), ('U', 'A'), ('C', 'G'), ('G', 'C')}
    for k in range(1, len(s), 2):
        if (s[0], s[k]) not in pairs:
            continue
        left = s[1:k]
        right = s[k + 1:]
        if left.count('A') != left.count('U') or left.count('C') != left.count('G'):
            continue
        total = (total + cat_count(left, memo) * cat_count(right, memo)) % MOD

    memo[s] = total
    return total


def main():
    s = parse_fasta('rosalind_cat.txt')
    print(cat_count(s, {}))


if __name__ == '__main__':
    main()
