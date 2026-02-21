from math import comb


def main():
    with open('rosalind_lia.txt', 'r') as f:
        k, n = map(int, f.read().strip().split())

    total = 2 ** k
    p = 0.25

    ans = 0.0
    for i in range(n, total + 1):
        ans += comb(total, i) * (p ** i) * ((1 - p) ** (total - i))

    print(f'{ans:.3f}')


if __name__ == '__main__':
    main()
