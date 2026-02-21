CODON_TABLE = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
    'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
}


def reverse_complement(dna):
    comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(comp[b] for b in reversed(dna))


def translate_frame(rna, frame):
    protein = []
    for i in range(frame, len(rna) - 2, 3):
        aa = CODON_TABLE[rna[i:i + 3]]
        protein.append('*' if aa == 'Stop' else aa)
    return ''.join(protein)


def proteins_from_rna(rna):
    proteins = set()
    for frame in range(3):
        prot = translate_frame(rna, frame)
        for i, aa in enumerate(prot):
            if aa != 'M':
                continue
            j = i
            while j < len(prot) and prot[j] != '*':
                j += 1
            if j < len(prot):
                proteins.add(prot[i:j])
    return proteins


def parse_fasta(path):
    with open(path, 'r') as f:
        return ''.join(line.strip() for line in f if line and not line.startswith('>'))


def main():
    dna = parse_fasta('rosalind_orf.txt')
    rna1 = dna.replace('T', 'U')
    rna2 = reverse_complement(dna).replace('T', 'U')

    proteins = proteins_from_rna(rna1) | proteins_from_rna(rna2)
    for p in proteins:
        print(p)


if __name__ == '__main__':
    main()
