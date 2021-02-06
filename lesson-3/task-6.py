def int_func(word):
	return word.title()


# input data
string = 'you shall know a word by the company it keeps'

output = ' '.join(list(map(int_func, string.split())))
print(output)
