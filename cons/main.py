ALPHABET = 'ACGT'


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


def main():
    seqs = parse_fasta('rosalind_cons.txt')
    m = len(seqs[0])
    profile = {base: [0] * m for base in ALPHABET}

    for s in seqs:
        for i, ch in enumerate(s):
            profile[ch][i] += 1

    consensus = []
    for i in range(m):
        consensus.append(max(ALPHABET, key=lambda b: profile[b][i]))

    print(''.join(consensus))
    for base in ALPHABET:
        print(f'{base}:', *profile[base])


if __name__ == '__main__':
    main()
