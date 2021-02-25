class Date:
	def __init__(self, date):
		Date.date = date

	@classmethod
	def convert_format(cls):
		cls.dd, cls.mm, cls.yy = map(int, cls.date.split('-'))

	@staticmethod
	def validate():
		assert 0 <= Date.dd <= 31,\
			f"incorrect day indicator! current value: {Date.dd}"

		assert 0 <= Date.mm <= 12,\
			f"incorrect month indicator! current value: {Date.mm}"


time = Date('12-03-1999')
Date.convert_format()
Date.validate()

time = Date('35-03-1999')
Date.convert_format()
Date.validate()
