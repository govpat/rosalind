import math


def main():
    with open('rosalind_afrq.txt', 'r') as f:
        arr = list(map(float, f.readline().split()))

    out = []
    for q2 in arr:
        q = math.sqrt(q2)
        out.append(f'{(2 * q * (1 - q) + q2):.3f}')
    print(' '.join(out))


if __name__ == '__main__':
    main()
