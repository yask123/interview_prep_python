# O(n) time
def is_sum_tree(root):
	if root == None:
		return 0

	left_subtree_sum = is_sum_tree(root.left)
	right_subtree_sum = is_sum_tree(root.right)

	if left_subtree_sum == -1 or right_subtree_sum == -1:
		return -1

	if root.left == None and root.right == None:
		return root.val
	if left_subtree_sum + right_subtree_sum != root.val:
		return - 1

	return root.val + left_subtree_sum + right_subtree_sum


class Node:
	def __init__(self, data):
		self.right = None
		self.left = None
		self.val = data


root = Node(26)
root.left = Node(10)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(6)

root.right.right = Node(3)

print is_sum_tree(root)
