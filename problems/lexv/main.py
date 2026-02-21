def main():
    with open('rosalind_lexv.txt', 'r') as f:
        alphabet = f.readline().strip().split()
        n = int(f.readline().strip())

    def dfs(prefix, depth):
        if prefix:
            print(prefix)
        if depth == n:
            return
        for ch in alphabet:
            dfs(prefix + ch, depth + 1)

    dfs('', 0)


if __name__ == '__main__':
    main()
