class Tool:
	def __init__(self, title, number):
		assert isinstance(title, str),\
			'Type of "Title" must be a str type'
		assert isinstance(number, int),\
			'Type of "number" must be a str type'

		self.title = title
		self.number = number

	def extract_element(self, number):
		"""Takes tools from current set"""
		assert self.number >= number,\
			'It\'s impossible to extract more than set contain!'

		self.number -= number
		return self.number==0


class Printer(Tool):
	def __init__(self, number, model):
		super(Printer, self).__init__('Printer', number)
		assert isinstance(model, str),\
			'Type of "Model" must be a str type'
		self.model = model

	@property
	def unique_char(self):
		return self.model

	def __add__(self, other):
		assert isinstance(other, Printer),\
			f'The type of second operand must be the Printer; {type(other)} found'
		assert self.model == other.model,\
			'It\'s impossible to add printers with different "model" mark'

		return Printer(self.number + other.number, self.model)

	def __sub__(self, other):
		assert isinstance(other, Printer),\
			f'The type of second operand must be the Printer; {type(other)} found'
		assert self.model == other.model,\
			'It\'s impossible to subtract printers with different "model" mark'
		assert (result:= self.number - other.number)>=0,\
			'Incorrect subtraction: result can\'t be < 0!'

		return Printer(result, self.model)


class Scanner(Tool):
	def __init__(self, number, resolution_capacity):
		super(Scanner, self).__init__('Scanner', number)
		assert isinstance(resolution_capacity, int),\
			'Type of "Resolution_capacity" must be a int type'
		self.resolution_capacity = resolution_capacity

	@property
	def unique_char(self):
		return self.resolution_capacity

	def __add__(self, other):
		assert isinstance(other, Scanner),\
			f'The type of second operand must be the Scanner; {type(other)} found'
		assert self.resolution_capacity == other.resolution_capacity,\
			'It\'s impossible to add printers with different "resolution_capacity" indicator'

		return Scanner(self.number + other.number, self.resolution_capacity)

	def __sub__(self, other):
		assert isinstance(other, Scanner),\
			f'The type of second operand must be the Scanner; {type(other)} found'
		assert self.resolution_capacity == other.resolution_capacity,\
			'It\'s impossible to subtract printers with different "resolution_capacity" indicator'
		assert (result:= self.number - other.number)>=0,\
			'Incorrect subtraction: result can\'t be < 0!'

		return Scanner(result, self.resolution_capacity)


class Copier(Tool):
	def __init__(self, number, w_type):
		super(Copier, self).__init__('Copier', number)
		assert isinstance(w_type, str),\
			'Type of "W_type" must be a str type'
		self.w_type = w_type

	@property
	def unique_char(self):
		return self.w_type

	def __add__(self, other):
		assert isinstance(other, Copier),\
			f'The type of second operand must be the Copier; {type(other)} found'
		assert self.w_type == other.w_type,\
			'It\'s impossible to add printers with different "w_type" mark'

		return Copier(self.number + other.number, self.w_type)

	def __sub__(self, other):
		assert isinstance(other, Copier),\
			f'The type of second operand must be the Copier; {type(other)} found'
		assert self.w_type == other.w_type,\
			'It\'s impossible to subtract printers with different "w_type" mark'
		assert (result:= self.number - other.number)>=0,\
			'Incorrect subtraction: result can\'t be < 0!'

		return Copier(result, self.w_type)
