from functools import reduce


def multiplication(x,y):
	return x * y


origin = [x for x in range(100, 1001) if x%2==0]
print(reduce(multiplication, origin))
