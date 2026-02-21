def count_matchings(s, memo):
    if len(s) <= 3:
        return 1
    if s in memo:
        return memo[s]

    pairs = {('A', 'U'), ('U', 'A'), ('C', 'G'), ('G', 'C'), ('U', 'G'), ('G', 'U')}
    total = count_matchings(s[1:], memo)
    for i in range(4, len(s)):
        if (s[0], s[i]) in pairs:
            total += count_matchings(s[1:i], memo) * count_matchings(s[i + 1:], memo)

    memo[s] = total
    return total


def main():
    with open('rosalind_rnas.txt', 'r') as f:
        s = f.readline().strip()
    print(count_matchings(s, {}))


if __name__ == '__main__':
    main()
