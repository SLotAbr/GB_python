class Cell:
	def __init__(self, number):
		self.number = number
	
	def make_order(self, columns):
		assert columns>0, 'input number must be > 0!'

		result = ['*'*columns for l in range(self.number // columns)]
		if (rest:=self.number % columns):
			result.append('*'*rest)

		return '\n'.join(result)

	def __add__(self, other):
		assert isinstance(other, Cell),\
			f'The type of second operand must be the Cell; {type(other)} found'

		return Cell(self.number + other.number)

	def __sub__(self, other):
		assert isinstance(other, Cell),\
			f'The type of second operand must be the Cell; {type(other)} found'

		assert (result:= self.number - other.number)>=0,\
			'incorrect subtraction: result can\'t be < 0!'

		return Cell(result)

	def __mul__(self, other):
		assert isinstance(other, Cell),\
			f'The type of second operand must be the Cell; {type(other)} found'

		return Cell(self.number * other.number)

	def __truediv__(self, other):
		assert isinstance(other, Cell),\
			f'The type of second operand must be the Cell; {type(other)} found'

		return Cell(self.number // other.number)


b_13 = Cell(13)
b_23 = Cell(2)
b_7 = Cell(19)

print((b_13 / b_23).number)
print(b_7.make_order(4))
