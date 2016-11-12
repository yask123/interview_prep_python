def get_bit(n, i):
	''' returns true if the ith bit from left is 1 and false if 0
		Eg: get_bit(5,0) -> 1 and get_btt(5,1) -> 0
					'''
	# Left shift of 1 by i positions
	return n & (1 << i) != 0
