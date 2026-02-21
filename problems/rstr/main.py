def main():
    with open('rosalind_rstr.txt', 'r') as f:
        n, x = f.readline().split()
        n = int(n)
        x = float(x)
        s = f.readline().strip()

    at = s.count('A') + s.count('T')
    gc = s.count('G') + s.count('C')
    p = (x / 2) ** gc * ((1 - x) / 2) ** at
    print(f'{1 - (1 - p) ** n:.3f}')


if __name__ == '__main__':
    main()
