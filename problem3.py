from math import sqrt


def is_prime(num):
	x = 2
	while x < num - 1:
		if num % x == 0:
			return False
		x = x + 1
	return True


def largest_prime_factor(num):
	divisor = num
	while divisor > 2:
		print divisor, " - ", num % divisor
		if num % divisor == 0 and is_prime(divisor):
			return divisor 
		divisor = divisor - 1
	return 0



if __name__ == '__main__':
	print largest_prime_factor(600851475143)


