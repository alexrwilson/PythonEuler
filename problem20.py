def factorial(number):
	return reduce(lambda x, y: x * y, range(1, number + 1))

def sum_digits(number):
	return reduce(lambda x, y: int(x) + int(y), iter(str(number)))


def sum_factorial_digits(number):
	return sum_digits(factorial(number))


if __name__ == '__main__':
	print sum_factorial_digits(100)