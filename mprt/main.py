import re
from urllib.request import urlopen
from urllib.error import HTTPError


def fetch_fasta_sequence(protein_id):
    accession = protein_id.split('_')[0]
    urls = [
        f'https://rest.uniprot.org/uniprotkb/{accession}.fasta',
        f'https://www.uniprot.org/uniprot/{accession}.fasta',
    ]

    for url in urls:
        try:
            with urlopen(url) as resp:
                data = resp.read().decode('utf-8')
            lines = [line.strip() for line in data.splitlines() if line and not line.startswith('>')]
            return ''.join(lines)
        except HTTPError:
            continue

    raise ValueError(f'Could not fetch FASTA for {protein_id}')


def motif_positions(sequence):
    pattern = re.compile(r'(?=(N[^P][ST][^P]))')
    return [m.start() + 1 for m in pattern.finditer(sequence)]


def main():
    with open('rosalind_mprt.txt', 'r') as f:
        ids = [line.strip() for line in f if line.strip()]

    for protein_id in ids:
        seq = fetch_fasta_sequence(protein_id)
        positions = motif_positions(seq)
        if positions:
            print(protein_id)
            print(' '.join(map(str, positions)))


if __name__ == '__main__':
    main()
