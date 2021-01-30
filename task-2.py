def proper_display(digit):
	string = str(digit)
	if len(string)==1:
		return '0'+string
	else:
		return string


n = int(input('Please, enter the number of seconds:\n'))
hh, mm, ss = n // 3600, (n // 60) % 60, n % 60
hh, mm, ss = proper_display(hh), proper_display(mm), proper_display(ss)
print('{}:{}:{}'.format(hh, mm, ss))
