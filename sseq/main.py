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
    s, t = parse_fasta('rosalind_sseq.txt')
    out = []
    j = 0
    for i, ch in enumerate(s):
        if j < len(t) and ch == t[j]:
            out.append(i + 1)
            j += 1
    print(' '.join(map(str, out)))


if __name__ == '__main__':
    main()
