class Stack:
	def __init__(self):
		stack = []
		max_stack = []

	def push(self,value):
		stack.append(value)
		if value > max_stack[-1] or len(stack) == 1:
			max_stack.append(value)
	def pop(self):
		if len(stack):
			popped_value = stack.pop()
			if popped_value == max_stack[-1]:
				max_stack.pop()

	def get_max(self):
		if len(max_stack) > 0:
			return max_stack[-1]
		else:
			return None

	def peek(self):
		return stack[-1]
