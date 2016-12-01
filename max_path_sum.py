import sample_tree


def max_path(root):
	if root == None:
		return 0

	left_subtree = max_path(root.left)
	right_subtree = max_path(root.right)

	get_current_max_sum.max = 0
	get_current_max_sum(root.left, 0)
	current_left = get_current_max_sum.max

	get_current_max_sum.max = 0
	get_current_max_sum(root.right, 0)
	current_right = get_current_max_sum.max

	return max(left_subtree, right_subtree, (current_right + current_left + root.val))


def get_current_max_sum(root, current_sum):
	if root == None:
		return

	if get_current_max_sum.max < current_sum + root.val:
		get_current_max_sum.max = current_sum + root.val

	get_current_max_sum(root.left, current_sum + root.val)
	get_current_max_sum(root.right, current_sum + root.val)


print max_path(sample_tree.a)
