P = {
    ('AA', 'AA'): (1.0, 0.0, 0.0),
    ('AA', 'Aa'): (0.5, 0.5, 0.0),
    ('AA', 'aa'): (0.0, 1.0, 0.0),
    ('Aa', 'AA'): (0.5, 0.5, 0.0),
    ('Aa', 'Aa'): (0.25, 0.5, 0.25),
    ('Aa', 'aa'): (0.0, 0.5, 0.5),
    ('aa', 'AA'): (0.0, 1.0, 0.0),
    ('aa', 'Aa'): (0.0, 0.5, 0.5),
    ('aa', 'aa'): (0.0, 0.0, 1.0),
}


def cross(a, b):
    out = {'AA': 0.0, 'Aa': 0.0, 'aa': 0.0}
    for ga, pa in a.items():
        for gb, pb in b.items():
            c = P[(ga, gb)]
            out['AA'] += pa * pb * c[0]
            out['Aa'] += pa * pb * c[1]
            out['aa'] += pa * pb * c[2]
    return out


def parse(expr):
    i = 0

    def rec():
        nonlocal i
        if expr.startswith('AA', i):
            i += 2
            return {'AA': 1.0, 'Aa': 0.0, 'aa': 0.0}
        if expr.startswith('Aa', i):
            i += 2
            return {'AA': 0.0, 'Aa': 1.0, 'aa': 0.0}
        if expr.startswith('aa', i):
            i += 2
            return {'AA': 0.0, 'Aa': 0.0, 'aa': 1.0}
        if expr[i] == '(':
            i += 1
            left = rec()
            i += 1  # comma
            right = rec()
            i += 1  # )
            return cross(left, right)
        raise ValueError('bad pedigree')

    return rec()


def main():
    with open('rosalind_mend.txt', 'r') as f:
        s = f.readline().strip().rstrip(';')
    p = parse(s)
    print(f"{p['AA']:.3f} {p['Aa']:.3f} {p['aa']:.3f}")


if __name__ == '__main__':
    main()
