from itertools import count
from sys import argv


for d in count(int(argv[1])):
	if d > 10:
		break
	else:
		print(d)
