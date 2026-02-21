from itertools import permutations, product
from math import factorial


def main():
    with open('rosalind_sign.txt', 'r') as f:
        n = int(f.read().strip())

    nums = list(range(1, n + 1))
    print((2 ** n) * factorial(n))

    for perm in permutations(nums):
        for signs in product((-1, 1), repeat=n):
            print(' '.join(str(signs[i] * perm[i]) for i in range(n)))


if __name__ == '__main__':
    main()
