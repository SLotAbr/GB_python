from itertools import cycle
from sys import argv


seq, c = 'Is it true?', 0
for s in cycle(seq):
	if c > int(argv[1]):
		break
	else:
		print(s)
		c+= 1
