def lex(num):
	# O(nlogn)
	digits = []
	for i in range(1, num):
		digits.append(str(i))
	digits.sort()
	digits = map(int, digits)  # O(n)
	return digits


print lex(20)
