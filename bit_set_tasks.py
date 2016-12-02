def get_bit(n, i):
	''' returns true if the ith bit from left is 1 and false if 0
		Eg: get_bit(5,0) -> 1 and get_btt(5,1) -> 0
					'''
	# Left shift of 1 by i positions
	return n & (1 << i) != 0


def set_bit(n, i):
	'''
	Sets the ith bit of n (from left) to 1
	4 -> 100 -> set_bit(4,0) -> 101 -> 5
	'''
	return n | 1 << i


def clear_bit(n, i):
	'''
	Clears the ith bit from the left.
	4 -> 100 clear_bit(4,2) -> 000 -> 0
	5 -> 101 clear_bit(5,2) -> 001 -> 1
	'''
	mask = ~(1 << i)
	return n & mask


def convert_base(number, base):
	result = []
	while number > 0:
		result.append(number % base)
		number = number / base
	result.reverse()
	return result


print convert_base(123, 16)
