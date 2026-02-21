def main():
    with open('rosalind_iprb.txt', 'r') as f:
        k, m, n = map(int, f.read().strip().split())

    total = k + m + n
    recessive = 0.0

    # aa x aa
    recessive += (n / total) * ((n - 1) / (total - 1))
    # aa x Aa
    recessive += (n / total) * (m / (total - 1)) * 0.5
    # Aa x aa
    recessive += (m / total) * (n / (total - 1)) * 0.5
    # Aa x Aa
    recessive += (m / total) * ((m - 1) / (total - 1)) * 0.25

    print(f'{1 - recessive:.5f}')


if __name__ == '__main__':
    main()
