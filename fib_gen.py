def fib():
	a = 0
	b = 1

	while True:
		yield a
		a, b = b, (a + b)


result = fib()

for i in range(6 - 1):
	next(result)

print next(result)
