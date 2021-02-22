from abc import ABC, abstractmethod


class Clothes(ABC):
	def __init__(self, title):
		self.title = title

	@abstractmethod
	def cloth_consumption(self):
		pass


class Coat(Clothes):
	def __init__(self, title, V):
		super(Coat, self).__init__(title)
		self.V = V

	@property
	def cloth_consumption(self):
		return self.V/6.5 + 0.5


class Suit(Clothes):
	def __init__(self, title, H):
		super(Suit, self).__init__(title)
		self.H = H

	@property
	def cloth_consumption(self):
		return 2 * self.H + 0.3


object_1 = Suit('clear weather', 56)
object_2 = Suit('new deal', 183)

print('Cloth required: ',object_1.cloth_consumption + object_2.cloth_consumption)
