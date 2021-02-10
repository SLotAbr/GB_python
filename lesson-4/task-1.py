from sys import argv


hours, hourly_rate, premium = map(float, argv[1:])
salary = (hours * hourly_rate) + premium
print(salary)
