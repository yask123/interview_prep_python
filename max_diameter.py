def max_diameter(root):
	if root == None:
		return 0

	left_subtree_depth, left_max_diameter = max_diameter(root.left)
	right_subtree_depth, right_max_diameter = max_diameter(root.right)

	current_diameter = left_max_diameter + 1 + right_max_diameter

	current_depth = 1 + max(left_subtree_depth, right_subtree_depth)

	return current_depth, max(current_diameter, left_max_diameter, right_max_diameter)
