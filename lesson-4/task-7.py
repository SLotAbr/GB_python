from sys import argv


def fact(n):
	d = 1
	for i in range(n):
		d*= i+1
		yield d


for el in fact(int(argv[1])):
	print(el)
