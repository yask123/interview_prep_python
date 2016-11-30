def k_largest_elements(root, result):
	if root == None:
		return

	k_largest_elements(root.right, result)

	if k_largest_elements.k > 0:
		result.append(root.val)

	k_largest_elements.k -= 1

	k_largest_elements(root.left, result)
