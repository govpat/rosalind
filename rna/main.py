def main():
    with open('rosalind_rna.txt', 'r') as f:
        s = f.read().strip()

    print(s.replace('T', 'U'))


if __name__ == '__main__':
    main()
