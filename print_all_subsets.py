def all_subset(arr, current_index, result, result_list):
	if current_index >= len(arr):
		result_list.append(result)
		return None

	all_subset(arr, current_index+1, result + str(arr[current_index]), result_list)
	all_subset(arr, current_index+1, result, result_list)

	return sorted(result_list)


arr = [1,2,3,4]

print all_subset(arr,0,'', [])
