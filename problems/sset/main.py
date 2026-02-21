MOD = 1_000_000


def main():
    with open('rosalind_sset.txt', 'r') as f:
        n = int(f.readline().strip())
    print(pow(2, n, MOD))


if __name__ == '__main__':
    main()
