
def main():
	s = 'GAGCCTACTAACGGGAT'
	t = 'CATCGTAATGACGGCCT'

	f = open('rosalind_hamm.txt', 'r')
	lines = f.readlines()

	hamm = 0
	for i in range(len(lines[0])):
		if lines[0][i] != lines[1][i]:
			hamm += 1

	print(hamm)


if __name__ == '__main__':
	main()