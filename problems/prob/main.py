import math


def base_probs(gc):
    return {
        'A': (1 - gc) / 2,
        'T': (1 - gc) / 2,
        'C': gc / 2,
        'G': gc / 2,
    }


def log10_prob(s, gc):
    p = base_probs(gc)
    v = 0.0
    for ch in s:
        v += math.log10(p[ch])
    return v


def main():
    with open('rosalind_prob.txt', 'r') as f:
        s = f.readline().strip()
        gcs = list(map(float, f.readline().split()))
    vals = [f'{log10_prob(s, gc):.3f}' for gc in gcs]
    print(' '.join(vals))


if __name__ == '__main__':
    main()
