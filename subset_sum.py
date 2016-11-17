arr = [1, 2, 3, 4]


def sub_set_sum(arr, current_index, target, ans):
	if target == 0:
		print (ans)
		return
	if target < 0:
		return
	if current_index < 0:
		return 

	sub_set_sum(arr, current_index, target-arr[current_index], ans + str(arr[current_index]))
	sub_set_sum(arr, current_index-1, target, ans)


sub_set_sum(arr, len(arr)-1, 5, '')