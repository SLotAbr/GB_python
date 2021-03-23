with open('task-4-text-i.txt', 'r') as f_i,\
	 open('task-4-text-o.txt', 'w') as f_o:
	translate = ['Один','Два','Три','Четыре']

	i_lines = f_i.readlines()
	[f_o.write(
		' '.join([translate[i], *i_lines[i].split()[1:]]) + '\n'
		) for i in range(len(i_lines))]
