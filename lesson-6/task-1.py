class TrafficLight:
	def __init__(self):
		self.time, self.__color = 0, 'Red'

	def running(self):
		self.time+=1
		if self.time <= 7:
			self.__color = 'Red'
			print(f'Current color: {self.__color}')

		elif self.time <= 9:
			self.__color = 'Yellow'
			print(f'Current color: {self.__color}')

		elif self.time <= 15:
			self.__color = 'Green'
			print(f'Current color: {self.__color}')

		else:
			self.time = 0
			print(f'Current color: {self.__color}')


a = TrafficLight()
for i in range(30):
	print(i, end=' ')
	a.running()
