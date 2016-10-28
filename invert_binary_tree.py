def invert_tree(root):
	if root == None:
		return

	left_child = invert_tree(root.left)
	right_child = invert_tree(root.right)

	root.left = right_child
	root.right = left_child

	return root
