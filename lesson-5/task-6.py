import re


with open('task-6-text.txt', 'r') as f:
	lines = f.readlines()
	f_lenght, d_output = len(lines), {}
	lines = [lines[i].split(':') for i in range(f_lenght)]
	d_output.update(
		[(lines[i][0], sum(map(int, re.findall(r'\d+', lines[i][1]))))
		for i in range(f_lenght)]
		)
	print(d_output)
