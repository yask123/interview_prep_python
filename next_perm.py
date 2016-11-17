def next_perm(number):
	i = len(number) - 1
	while i >= 1:
		if number[i - 1] < number[i]:
			next_greater_number_index = get_next_greater_number(number, i - 1)

			number[i - 1], number[next_greater_number_index] = number[next_greater_number_index], number[i - 1]

			right_sub_array = sorted(number[i:])
			return number[:i] + right_sub_array
		i -= 1

	return sorted(number)


def get_next_greater_number(number, index):
	next_greater_num_index = float('inf')

	for i in range(index + 1, len(number)):
		if number[i] > number[index] and number[i] < next_greater_num_index:
			next_greater_num_index = i
	return next_greater_num_index


print next_perm([3, 1, 2])
