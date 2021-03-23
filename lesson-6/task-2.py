from functools import reduce


class Road:
	def __init__(self, length, width):
		self._length = length
		self._width = width
	
	def calculate_mass(self, local_mass, corpulence):
		return reduce(lambda x,y: x*y, 
			list(map(int, [self._length, self._width, local_mass, corpulence]))
					)


north_road = Road(20, 5000)
print(f'{north_road.calculate_mass(25, 5)/1000} (Т)')
