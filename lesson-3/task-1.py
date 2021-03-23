def devide(y, x):
	try:
		return y/x
	except ZeroDivisionError:
		print('You enter incorrect number: your second number must not be zero.')


n1 = float(input('Please, enter a first number: '))
n2 = float(input('Please, enter a second number: '))

print(devide(n1, n2) or 'Please, try again')
