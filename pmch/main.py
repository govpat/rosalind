from math import factorial


def main():
    with open('rosalind_pmch.txt', 'r') as f:
        rna = ''.join(line.strip() for line in f if line and not line.startswith('>'))

    print(factorial(rna.count('A')) * factorial(rna.count('C')))


if __name__ == '__main__':
    main()
