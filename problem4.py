def is_palindrome(number):
	number_string = str(number)
	return number_string[::-1] == number_string


def get_palindrome(limit):
	x = limit
	largest_palindrome = 0
	while x > 99:
		y = limit
		while y > 99:
			print x, " * ", y, " = ", x * y
			if is_palindrome(x * y) and x * y > largest_palindrome:
				largest_palindrome =  x * y
			y = y - 1
		x = x - 1
	return largest_palindrome


print get_palindrome(999)