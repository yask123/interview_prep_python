# Merge two arrays on O(m + n) time and O(1) space, assuming one of the array has enough space to accomodate
# elements of both array.

def merge(A, B, m, n):
	b_index = n - 1
	a_index = m - 1
	k = m + n - 1

	while a_index >= 0 and b_index >= 0:
		if A[a_index] > B[b_index]:
			A[k] = A[a_index]
			k -= 1
			a_index -= 1
		else:
			A[k] = B[b_index]
			k -= 1
			b_index -= 1

	while b_index >= 0:
		A[k] = B[b_index]
		b_index -= 1


A = [4, 7, 9, 0, 0, 0]
B = [1, 5, 6]

merge(A, B, 3, 3)

print A
