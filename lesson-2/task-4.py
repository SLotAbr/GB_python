string = input('Please, input your string:\n')
data = string.split()
for i, word in enumerate(data):
	print(i, word[:10])
