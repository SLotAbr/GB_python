with open('task-2-text.txt', 'r') as f:
	lines = f.readlines()
	f_lenght = len(lines)
	print(f'Number of lines: {f_lenght}\nNumber of words per every line:')
	for i in range(f_lenght):
		print(f'line {i+1}: {len(lines[i].split())} word/s')
