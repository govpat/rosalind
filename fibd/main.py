def mortal_rabbits(n, m):
    ages = [0] * m
    ages[0] = 1

    for _ in range(1, n):
        newborn = sum(ages[1:])
        ages = [newborn] + ages[:-1]

    return sum(ages)


def main():
    with open('rosalind_fibd.txt', 'r') as f:
        n, m = map(int, f.read().strip().split())
    print(mortal_rabbits(n, m))


if __name__ == '__main__':
    main()
