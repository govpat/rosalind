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


def longest_common_substring(strings):
    shortest = min(strings, key=len)
    others = [s for s in strings if s is not shortest]
    n = len(shortest)

    for length in range(n, 0, -1):
        hits = []
        for i in range(n - length + 1):
            candidate = shortest[i:i + length]
            if all(candidate in s for s in others):
                hits.append(candidate)
        if hits:
            return min(hits)
    return ''


def main():
    strings = parse_fasta('rosalind_lcsm.txt')
    print(longest_common_substring(strings))


if __name__ == '__main__':
    main()
