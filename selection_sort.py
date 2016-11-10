def selection_sort(arr):
	# Find the min number (arr[k]) from i+1 -> n-1, swap with arr[i]

	for i in range(len(arr)):
		min_no_index = i
		for j in range(i + 1, len(arr)):
			if arr[min_no_index] > arr[j]:
				min_no_index = j
		arr[min_no_index], arr[i] = arr[i], arr[min_no_index]


arr = [134, 34, 342, 32, 564, 324, 3424, 756, 768, 78, 3]

selection_sort(arr)
print arr
