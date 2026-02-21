def rabbit_pairs(months, litter_size):
    if months <= 2:
        return 1

    a, b = 1, 1
    for _ in range(3, months + 1):
        a, b = b, b + litter_size * a
    return b


def main():
    with open('rosalind_fib.txt', 'r') as f:
        n, k = map(int, f.read().strip().split())

    print(rabbit_pairs(n, k))


if __name__ == '__main__':
    main()
