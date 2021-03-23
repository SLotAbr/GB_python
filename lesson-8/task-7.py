class Complex_number:
	def __init__(self, a, i):
		self.a = a
		self.i = i

	def __add__(self, other):
		return Complex_number(self.a+other.a, self.i+other.i)

	def __mul__(self, other):
		return Complex_number(self.a*other.a - self.i*other.i, 
							  self.i*other.a + self.a*other.i)

	def __str__(self):
		return f'{self.a} + ({self.i})i'

q = Complex_number(2, -5)
w = Complex_number(6, 3)

print((q+w) * q)
print(q * w)
