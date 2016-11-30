arr = [4, 5, 9, 11]


def greater_than_k(arr, k):
	i = 0
	j = len(arr) - 1

	while i <= j:
		mid = (i + j) / 2

		if mid == 0 and arr[mid] > k:
			return mid

		if mid != 0 and arr[mid - 1] <= k and arr[mid] > k:
			return mid

		if arr[mid] > k:
			j = mid - 1
		else:
			i = mid + 1
	return -1


print greater_than_k(arr, 90)
