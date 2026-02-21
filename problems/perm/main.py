from itertools import permutations
from math import factorial


def main():
    with open('rosalind_perm.txt', 'r') as f:
        n = int(f.read().strip())

    nums = list(range(1, n + 1))
    print(factorial(n))
    for p in permutations(nums):
        print(' '.join(map(str, p)))


if __name__ == '__main__':
    main()
