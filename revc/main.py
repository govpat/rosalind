def reverse_complement(dna):
    comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(comp[b] for b in reversed(dna))


def main():
    with open('rosalind_revc.txt', 'r') as f:
        s = f.read().strip()

    print(reverse_complement(s))


if __name__ == '__main__':
    main()
