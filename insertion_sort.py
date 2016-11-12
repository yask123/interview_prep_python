def insertion_sort(arr):
	# The way you sort the cards

	for i in range(1, len(arr)):
		j = i - 1
		key = arr[i]

		while j >= 0 and key < arr[j]:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key


arr = [2543, 234, 34, 37, 453, 4553]

insertion_sort(arr)

print arr
