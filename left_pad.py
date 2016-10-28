def left_pad(inp, n, k=' '):
	no_of_extra_space = n - len(inp)
	for i in range(no_of_extra_space):
		inp = k +inp
	return inp

print (left_pad('yask', 11))