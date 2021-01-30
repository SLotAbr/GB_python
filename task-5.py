revenue = float(input('Please, enter the firm\'s revenue measure:\n'))
cost = float(input('Please, enter the firm\'s cost measure:\n'))

if revenue < cost:
	print('Financial result: loss')
elif revenue > cost:
	print('Financial result: profit')
	profit = (revenue-cost)/revenue
	print('Profitability of revenue: {} (%)'.format(profit*100))
	n = int(input('Enter the number of employees:\n'))
	print('Profit per employee: {} (%)'.format(profit/n * 100))
