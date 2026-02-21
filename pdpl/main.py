from collections import Counter


def max_key(counter):
    return max(k for k, v in counter.items() if v > 0)


def can_remove(counter, vals):
    c = Counter(vals)
    return all(counter[k] >= v for k, v in c.items())


def remove_vals(counter, vals):
    for v in vals:
        counter[v] -= 1


def add_vals(counter, vals):
    for v in vals:
        counter[v] += 1


def place(counter, X, width):
    if sum(counter.values()) == 0:
        return sorted(X)

    y = max_key(counter)
    for p in (y, width - y):
        if p in X:
            continue
        diffs = [abs(p - x) for x in X]
        if can_remove(counter, diffs):
            remove_vals(counter, diffs)
            X.add(p)
            ans = place(counter, X, width)
            if ans is not None:
                return ans
            X.remove(p)
            add_vals(counter, diffs)
    return None


def solve(distances):
    d = [x for x in distances if x > 0]
    if not d:
        return [0]
    width = max(d)
    counter = Counter(d)
    X = {0, width}
    counter[width] -= 1
    ans = place(counter, X, width)
    return ans if ans is not None else sorted(X)


def main():
    with open('rosalind_pdpl.txt', 'r') as f:
        distances = list(map(int, f.read().strip().split()))
    print(*solve(distances))


if __name__ == '__main__':
    main()
