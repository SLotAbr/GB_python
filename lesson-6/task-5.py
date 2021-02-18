class Stationery:
	def __init__(self, title):
		self.title = title
		
	def draw(self):
		print("Запуск отрисовки.")


class Pen(Stationery):
	def draw(self):
		print('Use me for notes!')


class Pencil(Stationery):
	def draw(self):
		print('I can prepare a main lines in your picture!')


class Handle(Stationery):
	def draw(self):
		print('I can make notes too!')
		

tool1 = Pen('pen')
tool2 = Pencil('pencil')
tool3 = Handle('handle')

tool1.draw()
tool2.draw()
tool3.draw()
