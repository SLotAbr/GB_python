with open('task-3-text.txt', 'r') as f:
	lines = f.readlines()
	f_lenght, mean = len(lines), 0
	print('Employees with salary < 20k: \n')
	# lines = [lines[i].split() for i in range(f_lenght)]
	# [print(*lines[i], sep=' ') 
	#  for i in range(f_lenght) if float(lines[i][1]) < 20]
	# [(mean:= mean+ float(lines[i][1])) for i in range(f_lenght)]

	for i in range(f_lenght):
		lines[i] = lines[i].split()
		lines[i][1] = float(lines[i][1])
		mean += lines[i][1]

		if lines[i][1] < 20:
			print(*lines[i], sep=' ')
		
	print(f'Mean salary: {round(mean/f_lenght, 4)}')
	