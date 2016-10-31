val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)


def knapsack(values, weights, target, current_index):
	if current_index < 0:
		return 0
	if target == 0:
		return 0

	if weights[current_index] > target:
		knapsack(values, weights, target, current_index - 1)

	with_current_value = values[current_index] + knapsack(values, weights, target - weights[current_index],
	                                                      current_index - 1)
	without_current_value = knapsack(values, weights, target, current_index - 1)

	return max(with_current_value, without_current_value)


print knapsack(val, wt, W, n - 1)
