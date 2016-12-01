'''
Concept:
At each ith position you can either have ( or )
for valid entry, you can have ( only if open count is less than n
and ) if opening count is more than closing count.
'''


def generate(n, pos, open, close, result):
	if close == n:
		print result
		return
	else:
		if open < n:
			b = result[:]
			b[pos] = '('
			generate(n, pos + 1, open + 1, close, b)

		if open > close:
			b = result[:]

			b[pos] = ')'
			generate(n, pos + 1, open, close + 1, b)


generate(4, 0, 0, 0, [0] * 8)
