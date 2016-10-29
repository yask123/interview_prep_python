def is_balance(root):
	if root == None:
		return 0, True

	left_subtree_height, is_left_balaced = is_balance(root.left)
	right_subtree_height, is_right_balanced = is_balance(root.right)

	current_height = max(left_subtree_height, right_subtree_height) + 1

	return current_height, (
	is_left_balaced and is_right_balanced and abs(left_subtree_height - right_subtree_height) < 1)


class Node:
	def __init__(self, data=None):
		self.data = data
		self.left = None
		self.right = None


a = Node(2)
b = Node(3)
c = Node(1)

c.right = Node(5)

a.right = b
a.left = c

print is_balance(a)
