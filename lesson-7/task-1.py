class Matrix:
	def __init__(self, data):
		assert isinstance(data, list),\
			'type of input data must be a list type!'

		self.data = data
		self.str_number = len(data)
		self.column_number = len(data[0])
		if len([x for x in data if len(x)!= self.column_number]):
			raise ValueError('incorrect number of columns!')

	def __str__(self):
		return '\n'.join([' '.join(map(str, j)) for j in self.data])

	def __add__(self, other):
		assert isinstance(other, Matrix),\
			'The type of second summand must be Matrix'
		assert self.str_number == other.str_number &\
			self.column_number == other.column_number,\
			'Matrices must have an equal shape'

		return Matrix([list(map(lambda x,y: x+y, 
				(x:=[u for u in self.data[s]]), 
				(y:=[v for v in other.data[s]]) 
				)) for s in range(self.str_number)])


a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[9,8,7],[6,5,4],[3,2,1]]

a_m = Matrix(a)
b_m = Matrix(b)
print(a_m + b_m)
