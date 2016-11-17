'''
subset sum problem, top-down aproach.
Target sum = T
Length of array = N

Optimized time complexity after memoization : O(T*N) (Brought down from exponential)
Space : O(T*N)
'''

arr = [1, 2, 3, 4]


def subset_sum(arr, index, target, current_result, cache={}):
	if index not in cache:
		cache[index] = {}
	if target in cache[index]:
		return cache[index][target]

	if target == 0:
		return current_result
	if target < 0 or index < 0:
		return False

	a = subset_sum(arr, index - 1, target - arr[index], current_result + str(arr[index]), cache)
	b = subset_sum(arr, index - 1, target, current_result, cache)

	if a:
		cache[index][target] = a
		return cache[index][target]

	if b:
		cache[index][target] = b
		return cache[index][target]


print subset_sum(arr, len(arr) - 1, 5, '')
