def find_freq(arr, k):
	lower_index = get_lower_index(arr, k)
	higher_index = get_higher_index(arr, k)

	return (higher_index - lower_index + 1)


def get_lower_index(arr, k):
	start_index = 0
	end_index = len(arr) - 1
	ans = -1
	while start_index <= end_index:
		mid = (start_index + end_index) / 2

		if arr[mid] >= k:
			end_index = mid - 1
			ans = mid

		else:
			start_index = mid + 1

	return ans


def get_higher_index(arr, k):
	start_index = 0
	end_index = len(arr) - 1

	ans = -1

	while start_index <= end_index:
		mid = (start_index + end_index) / 2

		if arr[mid] <= k:
			ans = mid
			start_index = mid + 1
		else:
			end_index = mid - 1
	return ans


arr = [1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4]

print get_higher_index(arr, 10)
