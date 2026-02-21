def parse_set(line):
    s = line.strip()[1:-1].strip()
    if not s:
        return set()
    return set(map(int, s.split(', ')))


def fmt(s):
    if not s:
        return '{}'
    return '{' + ', '.join(map(str, sorted(s))) + '}'


def main():
    with open('rosalind_seto.txt', 'r') as f:
        n = int(f.readline().strip())
        a = parse_set(f.readline())
        b = parse_set(f.readline())

    u = set(range(1, n + 1))
    print(fmt(a | b))
    print(fmt(a & b))
    print(fmt(a - b))
    print(fmt(b - a))
    print(fmt(u - a))
    print(fmt(u - b))


if __name__ == '__main__':
    main()
