def reverse_complement(dna):
    c = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(c[b] for b in reversed(dna))


def parse_fasta(path):
    seq = []
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('>'):
                seq.append(line)
    return ''.join(seq)


def main():
    s = parse_fasta('rosalind_revp.txt')
    n = len(s)
    for i in range(n):
        for l in range(4, 13):
            if i + l <= n:
                t = s[i:i + l]
                if t == reverse_complement(t):
                    print(i + 1, l)


if __name__ == '__main__':
    main()
