import random


with open('task-5-text.txt', 'w') as f:
	digits = [random.randint(0, 10) for i in range(5)]
	d_sum = sum(digits)
	digits = ' '.join(map(str, digits))
	print(f'Numbers in file: {digits}\nTheir sum: {d_sum}')
	f.write(digits)
