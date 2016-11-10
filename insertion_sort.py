def insertion_sort(arr):
	# The way you sort the cards

	for i in range(len(arr)):

		key = arr[i]

		j = i - 1
		while j >= 0 and arr[j] > key:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key


arr = [2543, 234, 34, 37, 453, 4553]

insertion_sort(arr)

print arr
