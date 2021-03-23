def my_func(x, y):
	m = x
	for i in range(-y-1):
		x *= m
	return 1/x


print(my_func(20, -5))
