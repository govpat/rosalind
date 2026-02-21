from itertools import product


def main():
    with open('rosalind_lexf.txt', 'r') as f:
        alphabet = f.readline().strip().split()
        n = int(f.readline().strip())

    for tup in product(alphabet, repeat=n):
        print(''.join(tup))


if __name__ == '__main__':
    main()
