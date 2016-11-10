def bubble_sort(arr):
	# swap consecutive numbers if they are not in order

	for i in range(len(arr)):
		for j in range(0, len(arr) - i - 1):
			if arr[i] > arr[i + 1]:
				arr[i], arr[i + 1] = arr[i + 1], arr[i]


arr = [35, 675, 324, 12, 45, 76, 768, 546]

bubble_sort(arr)
print arr
