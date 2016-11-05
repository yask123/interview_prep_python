def to_postfix(input_expression):
	input_expression = input_expression.split(' ')
	result = []
	stack = []
	for each in input_expression:
		if is_operand(each):
			result.append(each)
		else:
			if len(stack):
				while len(stack) > 0 and (rank_of(stack[-1])) > rank_of(each):
					result.append(stack.pop())
				stack.append(each)
			else:
				stack.append(each)
	while len(stack):
		result.append(stack.pop())
	return result


def is_operand(each):
	if ord(each) >= ord('0') and ord(each) <= ord('9'):
		return True
	return False


def rank_of(operarator):
	ops_ranks = {'+': 1, '-': 1, '*': 2, '/': 2}
	return ops_ranks[operarator]


expression = '2 * 3 + 4'

print to_postfix(expression)
