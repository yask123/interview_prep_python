def longest_subarray(arr, k):
	start_index = 0
	end_index = 1
	current_sum = arr[0]
	longest_length = -float('inf')

	while end_index < len(arr):
		current_sum += arr[end_index]

		while current_sum > k and start_index < end_index:
			current_sum -= arr[start_index]
			start_index += 1

		if current_sum <= k:
			longest_length = max(longest_length, end_index - start_index + 1)
		end_index += 1
	return longest_length


arr = [100, 200, 0, 0, 4, 100, 90]

print longest_subarray(arr, 6)
