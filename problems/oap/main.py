import re
import parasail


def parse_fasta(path):
    seqs = []
    cur = []
    with open(path, 'r') as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            if line.startswith('>'):
                if cur:
                    seqs.append(''.join(cur))
                    cur = []
            else:
                cur.append(line)
    if cur:
        seqs.append(''.join(cur))
    return seqs


def parse_cigar(cigar_bytes):
    s = cigar_bytes.decode()
    return [(int(n), op) for n, op in re.findall(r'(\d+)([=XIDM])', s)]


def reconstruct(query, ref, ops):
    i = 0
    j = 0
    a1 = []
    a2 = []
    for n, op in ops:
        if op in ('=', 'X', 'M'):
            for _ in range(n):
                a1.append(query[i]); i += 1
                a2.append(ref[j]); j += 1
        elif op == 'I':
            for _ in range(n):
                a1.append(query[i]); i += 1
                a2.append('-')
        elif op == 'D':
            for _ in range(n):
                a1.append('-')
                a2.append(ref[j]); j += 1

    # Remove free-gap flanks for overlap output.
    while a2 and a2[0] == '-':
        a1.pop(0); a2.pop(0)
    while a1 and a1[-1] == '-':
        a1.pop(); a2.pop()

    return ''.join(a1), ''.join(a2)


def main():
    s1, s2 = parse_fasta('rosalind_oap.txt')
    matrix = parasail.matrix_create('ACGT', 1, -2)
    result = parasail.sg_qb_de_trace(s1, s2, 2, 2, matrix)
    ops = parse_cigar(result.cigar.decode)
    a1, a2 = reconstruct(s1, s2, ops)
    print(result.score)
    print(a1)
    print(a2)


if __name__ == '__main__':
    main()
