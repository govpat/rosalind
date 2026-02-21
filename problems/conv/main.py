from collections import Counter


def main():
    with open('rosalind_conv.txt', 'r') as f:
        s1 = list(map(float, f.readline().split()))
        s2 = list(map(float, f.readline().split()))

    diffs = [round(a - b, 5) for a in s1 for b in s2]
    c = Counter(diffs)
    x, m = max(c.items(), key=lambda kv: kv[1])
    print(m)
    print(abs(x))


if __name__ == '__main__':
    main()
