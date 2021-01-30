a = float(input('Please, enter the \"a\" value:\n'))
b = float(input('Please, enter the \"b\" value:\n'))
day = 1

while a < b:
	a*= 1.1
	day+= 1
print('Day number: ', day)