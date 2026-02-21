def neighbors(p):
    n = len(p)
    out = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            out.append(p[:i] + tuple(reversed(p[i:j + 1])) + p[j + 1:])
    return out


def distance(a, b):
    if a == b:
        return 0
    front = {a}
    back = {b}
    seen_f = {a}
    seen_b = {b}
    d = 0
    while front and back:
        d += 1
        if len(front) <= len(back):
            nxt = set()
            for x in front:
                for y in neighbors(x):
                    if y in seen_f:
                        continue
                    if y in back:
                        return d
                    seen_f.add(y)
                    nxt.add(y)
            front = nxt
        else:
            nxt = set()
            for x in back:
                for y in neighbors(x):
                    if y in seen_b:
                        continue
                    if y in front:
                        return d
                    seen_b.add(y)
                    nxt.add(y)
            back = nxt
    return -1


def main():
    with open('rosalind_rear.txt', 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    ans = []
    for i in range(0, len(lines), 2):
        a = tuple(lines[i].split())
        b = tuple(lines[i + 1].split())
        ans.append(str(distance(a, b)))
    print(' '.join(ans))


if __name__ == '__main__':
    main()
