# list version
# season=[]
# for i in range(1,13):
# 	if (i <= 2) or (i == 12):
# 		season.append('Winter')
# 	elif (3 <= i <= 5):
# 		season.append('Spring')
# 	elif (6 <= i <= 8):
# 		season.append('Summer')
# 	elif (9 <= i <= 11):
# 		season.append('Autumn')

# m = int(input('Please, enter a month number: '))
# print('season of current month: ', season[m-1])

# dict version
season = {}
for i in range(1,13):
	if (i <= 2) or (i == 12):
		season.update([(i,'Winter')])
	elif (3 <= i <= 5):
		season.update([(i,'Spring')])
	elif (6 <= i <= 8):
		season.update([(i,'Summer')])
	elif (9 <= i <= 11):
		season.update([(i,'Autumn')])

m = int(input('Please, enter a month number: '))
print('season of current month: ', season[m])
