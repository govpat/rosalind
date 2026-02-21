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


def is_transition(a, b):
    return (a, b) in {('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')}


def main():
    s1, s2 = parse_fasta('rosalind_tran.txt')
    ts = 0
    tv = 0
    for a, b in zip(s1, s2):
        if a == b:
            continue
        if is_transition(a, b):
            ts += 1
        else:
            tv += 1
    print(f'{ts / tv:.11f}')


if __name__ == '__main__':
    main()
