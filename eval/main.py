from decimal import Decimal, ROUND_HALF_UP


def q3(x):
    return str(Decimal(str(x)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))


def main():
    with open('rosalind_eval.txt', 'r') as f:
        n = int(f.readline().strip())
        s = f.readline().strip()
        arr = list(map(float, f.readline().split()))

    at = s.count('A') + s.count('T')
    gc = s.count('G') + s.count('C')
    out = []
    for x in arr:
        p = ((1 - x) / 2) ** at * (x / 2) ** gc
        out.append(q3(p * (n - len(s) + 1)))
    print(' '.join(out))


if __name__ == '__main__':
    main()
