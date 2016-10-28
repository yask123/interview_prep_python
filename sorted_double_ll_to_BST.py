def double_dd_to_tree(current, start_index, end_index):
	if start_index <= end_index:
		middle = get_middle(current, start_index, end_index)

		middle.right = double_dd_to_tree(current, start_index, middle - 1)
		middle.left = double_dd_to_tree(current, middle + 1, end_index)

	return middle


def get_middle(head, start_index, end_index):
	for i in range(start_index - end_index):
		head = head.next
	return head
