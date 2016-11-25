'''
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
'''


def min_subarray(arr, k):
	i = 0
	j = 0
	min_length = float('inf')
	current_sum = 0
	while j < len(arr):
		current_sum += arr[j]

		j += 1
		while current_sum - arr[i] >= k:
			current_sum = current_sum - arr[i]
			i += 1
		if current_sum >= k:
			min_length = min(j - i, min_length)
	return min_length


arr = [2, 3, 1, 2, 4, 3]
s = 7

print min_subarray(arr, s)
