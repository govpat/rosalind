MOD = 1_000_000

CODON_COUNT = {
    'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'C': 2, 'W': 1,
    'P': 4, 'H': 2, 'Q': 2, 'R': 6, 'I': 3, 'M': 1,
    'T': 4, 'N': 2, 'K': 2, 'V': 4, 'A': 4, 'D': 2,
    'E': 2, 'G': 4,
}


def main():
    with open('rosalind_mrna.txt', 'r') as f:
        protein = f.read().strip()

    ans = 3
    for aa in protein:
        ans = (ans * CODON_COUNT[aa]) % MOD

    print(ans)


if __name__ == '__main__':
    main()
