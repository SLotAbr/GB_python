from tools import Printer, Scanner, Copier


class Store:
	def __init__(self, title):
		self.title = title
		self.container = []
		self.pick_tool = {'Printer':Printer, 'Scanner':Scanner, 'Copier':Copier}

	def search(self, object_type, description):
		# return [index_of_match]
		if (match:=[i for i in range(len(self.container)) 
			 if (object_type==self.container[i].title) & 
			   (description==self.container[i].unique_char)]):
			return match
		else:
			False

	def store_item(self, item_description):
		tool_type, number, characteristic = item_description

		# if match: increase number of selected items in the current store
		# else: make new cell for item
		if (match:=self.search(tool_type, characteristic)):
			self.container[match[0]].number += number
		else:
			self.container.append(self.pick_tool[tool_type](number, characteristic))

	def get_item(self, transfer_description):
		"""Returns data for method 'store_item' and update container"""
		tool_type, number, characteristic = transfer_description

		if (match:=self.search(tool_type, characteristic)):
			# Extract_element authomatically changes number in set
			if self.container[match[0]].extract_element(number):
				# Remove cell in current store, if new value is 0
				self.container.pop(match[0])
			# Return item
			return transfer_description
			
		else:
			print('The item was not found')

	@property
	def contain(self):
		"""Displays all items inside"""
		print('Items in:', self.title)
		print('{:>9}|{:>9}|{:>9}'.format('type','number','key char'))
		[print('{:>9}|{:>9}|{:>9}'.format(i.title, i.number, i.unique_char)) 
			for i in self.container]
		print()
