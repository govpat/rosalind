import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '_vendor_dh'))
from rosalind.bioinformatics_stronghold.full import full as solve_full
from rosalind.bioinformatics_stronghold.helpers import Parser


def main():
    weights = [float(x) for x in Parser('rosalind_full.txt').lines()]
    cands = solve_full(weights[0], weights[1:])
    if cands:
        print(sorted(cands)[0])


if __name__ == '__main__':
    main()
