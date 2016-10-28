def coin_change(counts, current_index, target, count):

	if target == 0:

		return 1

	if current_index < 0:
		return 0

	if target < 0:
		return 0

	case_one = coin_change(counts, current_index, target - counts[current_index], count)
	case_two = coin_change(counts, current_index-1, target, count)

	return case_one + case_two

arr = [2,5,3,6]

print (coin_change(arr, len(arr)-1, 10, 0))
