import tqdist


def main():
    with open('rosalind_qrtd.txt', 'r') as f:
        _ = f.readline()
        t1 = f.readline().strip()
        t2 = f.readline().strip()

    stats = tqdist.quartet_distance(t1, t2)
    dquart = stats[2]
    print(int(round(dquart * 2)))


if __name__ == '__main__':
    main()
