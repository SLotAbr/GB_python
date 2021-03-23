with open('file.txt', 'w') as f:
	while True:
		i = input()
		if i != '':
			f.writelines(i+'\n')
		else:
			break
