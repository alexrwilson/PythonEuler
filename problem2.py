def fibonacci (limit):
	last = 1
	current = 2
	total = 0
	while current < limit:
		if current % 2 == 0:
			total = total + current 
		temp = last
		last = current
		current = temp + last
	return total


if __name__ == '__main__':
	print fibonacci(4000000)



