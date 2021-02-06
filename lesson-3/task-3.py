def my_func(n1, n2, n3):
	result = [n1, n2, n3]
	result.pop(result.index(min(result)))
	return sum(result)


print(my_func(3, 2, 4))
