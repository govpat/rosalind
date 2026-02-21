
def parse_fasta(path):
    labels = []
    seqs = []
    label = None
    curr = []
    with open(path, 'r') as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            if line.startswith('>'):
                if label is not None:
                    labels.append(label)
                    seqs.append(''.join(curr))
                label = line[1:]
                curr = []
            else:
                curr.append(line)
    if label is not None:
        labels.append(label)
        seqs.append(''.join(curr))
    return labels, seqs


def gc_content(seq):
    return 100.0 * (seq.count('G') + seq.count('C')) / len(seq)


def main():
    labels, seqs = parse_fasta('rosalind_gc.txt')
    best_i = max(range(len(seqs)), key=lambda i: gc_content(seqs[i]))
    print(labels[best_i])
    print(f'{gc_content(seqs[best_i]):.6f}')


if __name__ == '__main__':
    main()
