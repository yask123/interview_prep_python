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


# By divide and coquer O(nlogn)
def min_length(arr, k):
	return _min_length(arr, 0, len(arr) - 1, k)


def _min_length(arr, start_index, end_index, k):
	if start_index < end_index:
		mid = (start_index + end_index) // 2
		left_result = _min_length(arr, start_index, mid - 1, k)
		right_result = _min_length(arr, mid + 1, end_index, k)
		current_result = get_current_length(arr, start_index, end_index, k)

		return min(left_result, right_result, current_result)

	if arr[start_index] >= k:
		return 1
	else:
		return float('inf')


def get_current_length(arr, start_index, end_index, k):
	mid = (start_index + end_index) // 2

	left_index = mid
	right_index = mid
	current_sum = arr[mid]
	while left_index > start_index or right_index < end_index - 1:
		if current_sum >= k:
			return (right_index - left_index) + 1

		if arr[left_index - 1] > arr[right_index + 1] or right_index == end_index:
			current_sum += arr[left_index]
			left_index -= 1
		elif arr[right_index + 1] > arr[left_index - 1] or left_index == start_index:
			current_sum += arr[right_index]
			right_index += 1
		else:
			continue
	return float('inf')
