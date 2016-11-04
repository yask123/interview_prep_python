def shortest_substring_with_unique_chars(user_string):
	char_set = set()

	start_index = 0
	end_index = 1

	char_set.add(user_string[start_index])
	max_length = 1

	while end_index < len(user_string):
		char_set.add(user_string[end_index])

		if end_index - start_index + 1 > len(char_set):
			start_index = end_index
			end_index += 1
			continue

		max_length = max(max_length, end_index - start_index + 1)

		end_index += 1

	return max_length


print shortest_substring_with_unique_chars('helpp')
