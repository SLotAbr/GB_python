rate = [7, 5, 3, 3, 2]
k = int(input('Please, enter a new rate element:\n'))
print('The old version:\n', rate)

if k > rate[0]:
	rate.insert(0, k)
else:
	l_length = len(rate)
	for i in range(l_length):
		if k > rate[i]:
			rate.insert(i, k)
			break
		if i == l_length-1:
			rate.insert(i+1, k)

print('The new version:\n', rate)
