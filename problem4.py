def is_palindrome(number):
	number_string = str(number)
	return number_string[::-1] == number_string


def get_palindrome(limit):
	x = limit
	largest_palindrome = 0
	while x > 1:
		y = limit
		while y > 1:
			print x, " * ", y, " = ", x * y
			if is_palindrome(x * y) and x * y > largest_palindrome:
				largest_palindrome =  x * y
			y = y - 1
		x = x - 1
	return largest_palindrome

if __name__ == '__main__':
	print get_palindrome(999)