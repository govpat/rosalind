def main():
    with open('rosalind_iev.txt', 'r') as f:
        counts = list(map(int, f.read().strip().split()))

    probs_dom = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]
    expected = sum(2 * counts[i] * probs_dom[i] for i in range(6))
    print(expected)


if __name__ == '__main__':
    main()
