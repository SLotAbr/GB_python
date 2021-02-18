class Worker:
	def __init__(self, name, surname, position, wage, bonus):
		self.name = name
		self.surname = surname
		self.position = position
		self._income = {"wage": float(wage), "bonus": float(bonus)}


class Position(Worker):
	def get_full_name(self):
		return f'{self.name} {self.surname}'

	def get_total_income(self):
		return self._income['wage'] + self._income['bonus']


person1 = Position('Harry', 'Quary', 'developer', 105, 10)
person2 = Position('John', 'Labat', 'manager', 80, 25)

data = [(prs.name, prs.surname, prs.position, prs._income['wage'], 
			prs._income['bonus']) for prs in [person1, person2]]

[print(d) for d in [' '.join(map(str, data[i])) for i in range(len(data))] ]
print(person1.get_total_income())
print(person2.get_full_name())
