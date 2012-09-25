def get_sum(limit):
	sum = 0
	for x in range(1,limit):
		if x % 3 == 0 or x % 5 == 0:
			sum = sum + x
	return sum


if __name__ == '__main__':
	print get_sum(1000)