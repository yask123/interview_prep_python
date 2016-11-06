'''
While Queen Elizabeth has a limited number of types of cake, she has an unlimited supply of each type.

Each type of cake has a weight and a value, stored in a tuple with two indices:

An integer representing the weight of the cake in kilograms
An integer representing the monetary value of the cake in British pounds
'''


def max_profit(cakes, current_index, target_weight):
	if target_weight == 0:
		return 0

	if current_index < 0:
		return 0

	if cakes[current_index][0] > target_weight:
		return max_profit(cakes, current_index - 1, target_weight)

	a = cakes[current_index][1] + (cakes, current_index, target_weight - cakes[current_index][0])
	b = max_profit(cakes, current_index - 1, target_weight)

	return max(a, b)
