def main():
    with open('rosalind_inod.txt', 'r') as f:
        n = int(f.readline().strip())
    print(n - 2)


if __name__ == '__main__':
    main()
