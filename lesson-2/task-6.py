store = []
measures = [0, 0, 0, 0]
description = ['title','price','number','measurement unit']

while True:
	answer = input('\nDo you want add an extra element? y/n\n')

	if answer == 'n':
		break
	elif answer == 'y':
		l = len(store)
		measures[0] = input('Please, enter title of a product: ')
		measures[1] = input('Please, enter price of a product: ')
		measures[2] = input('Please, enter number of a product: ')
		measures[3] = input('Please, enter measurement unit of a product: ')

		store.append((l+1, dict([
			(description[0], measures[0]),
			(description[1], measures[1]),
			(description[2], measures[2]),
			(description[3], measures[3])
			])
		))

data = dict()
for i in range(len(measures)):
	measures[i] = set()
	for l in range(len(store)):
		measures[i].add(store[l][1][description[i]])
	data.update([(description[i], list(measures[i]))])

print(data)
