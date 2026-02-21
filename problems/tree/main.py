def main():
    with open('rosalind_tree.txt', 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    n = int(lines[0])
    edges = len(lines) - 1
    print(n - 1 - edges)


if __name__ == '__main__':
    main()
