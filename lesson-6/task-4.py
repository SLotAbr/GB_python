class Car:
	def __init__(self, speed, color, name, is_police):
		self.speed = float(speed)
		self.color = color
		self.name = name
		self.is_police = is_police

	def go(self):
		print(f'The {self.name} now is in motion')

	def stop(self):
		print(f'The {self.name} has stopped')

	def turn(self, direction):
		print(f'Direction of moving has been changed. Current value: {direction}')
	
	def show_speed(self):
		print(f'Current speed of {self.name} is {self.speed}')


class TownCar(Car):
	def show_speed(self):
		print(f'Current speed of {self.name} is {self.speed}')
		if self.speed > 60:
			print(f'The maximum allowable speed was exceeded! ({self.speed} > 60)')


class WorkCar(Car):
	def show_speed(self):
		print(f'Current speed of {self.name} is {self.speed}')
		if self.speed > 40:
			print(f'The maximum allowable speed was exceeded! ({self.speed} > 40)')


class SportCar(Car):
	pass


class PoliceCar(Car):
	pass


# speed, color, name, is_police
pl_car = PoliceCar(70, 'Blue', 'Justice', True)
tw_car = TownCar(57, 'Green', 'Element', False)
wk_car = WorkCar(52, 'Grey', 'Bee', False)

tw_car.go()
tw_car.show_speed()
tw_car.turn('West')
tw_car.speed = 75
tw_car.show_speed()
print()
pl_car.go()
pl_car.show_speed()
tw_car.speed = 95
tw_car.show_speed()
print()
pl_car.speed = 100
pl_car.show_speed()

tw_car.turn('North')
tw_car.stop()
pl_car.stop()
