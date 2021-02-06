s = 0
while True:
	string = input('Put your numbers or \"STOP\" symbol (q) here:\n')
	string = string.split()
	if string.count('q') != 0:
		string = string[:string.index('q')]
		s += sum(list(map(float, string)))
		print(f'The current sum of the numbers is: {s}\n')
		break
	else:
		s += sum(list(map(float, string)))
		print(f'The current sum of the numbers is: {s}\n')
