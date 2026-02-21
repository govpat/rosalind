from __future__ import print_function
import re


def main():
	# string = 'GATATATGCATATACTT'
	# sub = 'ATAT'

	f = open('rosalind_subs.txt', 'r')
	lines = f.readlines()
	sub = lines[1].replace('\n', '')
	string = lines[0].replace('\n', '')

	positions = [m.start() + 1 for m in re.finditer('(?=' + sub + ')', string)]

	print(*positions, sep = ' ')






if __name__ == '__main__':
	main()