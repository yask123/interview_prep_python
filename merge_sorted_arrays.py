# Merge two arrays on O(m + n) time and O(1) space, assuming one of the array has enough space to accomodate
# elements of both array.



def merge(A, B):
	a_index = 0
	b_index = 0
	temp = []
	while a_index <= len(A) - 1 and b_index <= len(B) - 1:
		if A[a_index] < B[b_index]:
			temp.append(A[a_index])
			a_index += 1
		else:
			temp.append(B[b_index])
			b_index += 1

	temp.extend(A[a_index: len(A)])
	temp.extend(B[b_index: len(B)])

	return temp


A = [4, 7, 9]
B = [1]

print merge(A, B)
