def parse_fasta(path):
    out = []
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('>'):
                out.append(line)
    return ''.join(out)


def prefix_function(s):
    pi = [0] * len(s)
    j = 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi


def main():
    s = parse_fasta('rosalind_kmp.txt')
    print(' '.join(map(str, prefix_function(s))))


if __name__ == '__main__':
    main()
