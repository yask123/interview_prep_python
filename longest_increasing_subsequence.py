def lic(arr):
	lic_arr = [1] * len(arr)

	for i in range(1, len(arr)):
		for j in range(0, i):
			if arr[j] < arr[i]:
				lic_arr[i] = max(lic_arr[i], 1 + lic_arr[j])
	return max(lic_arr)


arr = [10, 22, 9, 33, 21, 50, 41, 60]

print lic(arr)
