def display_data(name, second_name, year, location, email, phone):
	data = f'User_data:\nName: {name}\nSecond name: {second_name}\n'
	data += f'Date of birth: {year}\nLocation: {location}\n'
	data += f'Email: {email}\nPhone number: {phone}'
	print(data)


name = input('Please, enter your name: ')
second_name = input('Please, enter your second name: ')
year = input('Please, enter your date of birth: ')
location = input('Please, enter your location: ')
email = input('Please, enter your email: ')
phone = input('Please, enter your phone number: ')

display_data(name, second_name, year, location, email, phone) 