list_example = []

while True:
	k = input('Please, enter a new list element; type \'q\' for exit: ')
	if k == 'q':
		break
	list_example.append(k)

print('unswapped list: ', list_example)
l_length = len(list_example)
for i in range(0,l_length,2):
	# we don't achive this threshold in case l_length%2 = 0
	if i == l_length-1:
		break
	list_example[i], list_example[i+1] = list_example[i+1], list_example[i]
print('swapped list: ', list_example)
