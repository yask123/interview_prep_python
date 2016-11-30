def k_largest_elements(root, k, result):
	if root == None:
		return

	k_largest_elements(root.left, k, result)

	k_largest_elements.size -= 1
	if k_largest_elements.size < k:
		result.append(root.val)

	k_largest_elements(root.right, k, result)


def get_tree_size(root):
	if root == None:
		return 0
	return 1 + get_tree_size(root.left) + get_tree_size(root.right)


root = TreeNode()
k_largest_elements.size = get_tree_size(root)
