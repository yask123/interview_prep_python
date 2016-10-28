'''
Input : A : [4, 5, 2, 10]
Return :    [-1, 4, -1, 2]

'''

def next_smaller_no(arr):
	stack = []
	result = []
	for each in arr:
		if len(stack) == 0:
			result.append(-1)
			stack.append(each)
		elif each > stack[-1]:
			result.append(stack[-1])
		elif each < stack[-1]:
			result.append(-1)
			stack.append(each)
	return result

print (next_smaller_no( [4, 5, 2, 10]))
