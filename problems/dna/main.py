def main():
    with open('rosalind_dna.txt', 'r') as f:
        s = f.read().strip()

    print(s.count('A'), s.count('C'), s.count('G'), s.count('T'))


if __name__ == '__main__':
    main()
