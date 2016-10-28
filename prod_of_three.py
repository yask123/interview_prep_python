
def prod_of_three(arr):
	pre_computed_arr = []
	temp_result = 1
	res = 1
	for i in range(-1,len(arr)-1): # O(N)
		if i == -1:
			pre_computed_arr.append(1)
		else:
			res *=arr[i]
			pre_computed_arr.append(res)
	res = 1
	temp_resul = 1
	for i in range(len(arr),0,-1): #O(N)
		if i == len(arr):
			pre_computed_arr[i-1] = 1 * pre_computed_arr[i-1]
		else:
			res *=arr[i]
			pre_computed_arr[i-1] = res * pre_computed_arr[i-1]

	return pre_computed_arr


arr = []
print (prod_of_three(arr))


'''
Space complexity = O(N)
Time Complexity = O(N)
'''
