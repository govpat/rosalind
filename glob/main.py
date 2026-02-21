import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '_vendor_dh'))
from rosalind.bioinformatics_stronghold.glob import main as solve


if __name__ == '__main__':
    solve('rosalind_glob.txt')
