'''
Concept:
At each ith position you can either have ( or )
for valid entry, you can have ( only if open count is less than n
and ) if opening count is more than closing count.
'''

n = 10

arr = [0] * n


def generate(arr, pos, open, close):
    if close == n / 2:
        print arr
		return

    if pos >= n:
        return

    if open < n / 2:
        arr = arr[:]
        arr[pos] = '('
        generate(arr, pos + 1, open + 1, close)
    if open > close:
        arr = arr[:]
        arr[pos] = ')'
        generate(arr, pos + 1, open, close + 1)


generate(arr, 0, 0, 0)
