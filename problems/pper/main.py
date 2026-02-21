MOD = 1_000_000


def main():
    with open('rosalind_pper.txt', 'r') as f:
        n, k = map(int, f.read().strip().split())

    ans = 1
    for x in range(n - k + 1, n + 1):
        ans = (ans * x) % MOD
    print(ans)


if __name__ == '__main__':
    main()
