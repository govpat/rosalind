import math


def main():
    with open('rosalind_indc.txt', 'r') as f:
        n = int(f.readline().strip())

    m = 2 * n
    ans = []
    for k in range(1, m + 1):
        p = 0.0
        for i in range(k, m + 1):
            p += math.comb(m, i) * (0.5 ** m)
        v = math.log10(p)
        if abs(v) < 5e-4:
            v = 0.0
        ans.append(f'{v:.3f}')
    print(' '.join(ans))


if __name__ == '__main__':
    main()
