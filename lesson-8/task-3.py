class LetterElement(Exception):
	def __init__(self, txt):
		self.txt = txt


d_list = []
while True:
	try:
		d = input('Please, enter the digit:\n')
		if d.isdigit():
			d_list.append(float(d))
		elif d=='stop':
			break
		else:
			raise LetterElement('Incorrect element. Please, try again')

	except LetterElement as er:
		print(er)

print('Final list', d_list)
