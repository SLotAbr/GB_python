n = input('Please, enter a digit:\n')
digit_length, i, max_d = len(n), 0, -1

while i < digit_length:
	if int(n[i]) > max_d:
		max_d = int(n[i])
	i+= 1
print(max_d)
