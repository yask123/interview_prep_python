def height_of_tree(root): #O(n)
	if root == None:
		return 0
	return height_of_tree(root.left) + 1 + height_of_tree(root.right)