def factorial(number):
	return reduce(lambda x, y: x * y, range(1, number + 1))

def sum_digits(number):
	return reduce(lambda x, y: int(x) + int(y), iter(str(number)))



if __name__ == '__main__':
	print sum_digits(factorial(100))