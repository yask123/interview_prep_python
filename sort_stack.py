'''
Sort a stack #O(N^2) time and space (recursion stack)
1. Pop all elements from the stack
2. push elements in the stack such that elements remain sorted.
	* Pop all elements greater than the item to be pushed
	* push the item
	* push the remaining items that were popped earlier

'''


def sort_stack(stack):
	if len(stack) == 0:
		return
	popped_item = stack.pop()
	sort_stack(stack)
	push_in_sorted_position(stack, popped_item)


def push_in_sorted_position(stack, item):
	if len(stack) == 0 or stack[-1] < item:
		stack.append(item)
		return
	popped_item = stack.pop()
	push_in_sorted_position(stack, item)
	stack.append(popped_item)


stack = [87, 32, 345, 67754, 324, 21, 3435, 46232]

sort_stack(stack)

print stack
