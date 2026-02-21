def main():
	f = open('rosalind_grph.txt', 'r')
	lines = f.readlines()

	names = []
	strings = []
	string = ''
	for line in lines:
		if line[0] == '>':
			names.append(line[1:].rstrip('\n'))
			strings.append(string)
			string = ''
		else:
			string += line.rstrip('\n')
	strings.append(string)
	strings = strings[1:]
	# print(names, strings) 

	f.close()
	f = open('out.txt', 'w')
	# writer = f.wr

	for i, string in enumerate(strings):
		for j, string2 in enumerate(strings):
			if i != j:
				if string[-3:] == string2[:3]:
					print(names[i], names[j]) 


if __name__ == '__main__':
	main()