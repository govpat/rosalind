from math import comb

MOD = 1_000_000


def main():
    with open('rosalind_aspc.txt', 'r') as f:
        n, m = map(int, f.readline().split())
    ans = sum(comb(n, k) for k in range(m, n + 1)) % MOD
    print(ans)


if __name__ == '__main__':
    main()
