input_string = 'yaasskk iss niiiiiccccee'


def compress(input_string):
	current_frequency = 1

	for i in range(1, len(input_string)):
		if input_string[i] != input_string[i - 1]:
			print input_string[i - 1] + str(current_frequency),
			current_frequency = 1
		else:
			current_frequency += 1

	print input_string[len(input_string) - 1], current_frequency


compress(input_string)
