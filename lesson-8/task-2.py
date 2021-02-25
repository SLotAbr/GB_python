class ZeroDevErr(Exception):
	def __init__(self, txt):
		self.txt = txt

try:
	d = int(input('Please, enter the digit:\n'))
	if d == 0:
		raise ZeroDevErr('Please, choose another math system or don\'t use 0 under division')
	print(200/d)
except ZeroDevErr as er:
	print(er)
