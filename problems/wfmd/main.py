from math import comb


def main():
    with open('rosalind_wfmd.txt', 'r') as f:
        N, m, g, k = map(int, f.readline().split())

    tot = 2 * N
    dist = [0.0] * (tot + 1)
    dist[tot - m] = 1.0

    for _ in range(g):
        nxt = [0.0] * (tot + 1)
        for r_prev, pr in enumerate(dist):
            if pr == 0.0:
                continue
            q = r_prev / tot
            for r in range(tot + 1):
                nxt[r] += pr * comb(tot, r) * (q ** r) * ((1 - q) ** (tot - r))
        dist = nxt

    print(f'{sum(dist[k:]):.3f}')


if __name__ == '__main__':
    main()
