class Node:
	def __init__(self, key, value=None):
		self.key = key
		self.value = value
		self.left = None
		self.right = None


class BST:
	def __init__(self, root=None):
		self.root = root

	def insert(self, key, val=None):
		if self.root == None:
			self.root = Node(key, val)
		else:
			self._insert_helper(self.root, key, val)

	def _insert_helper(self, current_node, key, val):
		if key > current_node.key:
			if current_node.right == None:
				current_node.right = Node(key, val)
			else:
				self._insert_helper(current_node.right, key, val)
		else:
			if current_node.left == None:
				current_node.left = Node(key, val)
			else:
				self._insert_helper(current_node.left, key, val)

	def delete(self, key):
		self._delete(key, self.root)

	def _delete(self, key, root):
		if root == None:
			return

		if key > root.val:
			root.right = self._delete(key, root.right)

		elif key < root.val:
			root.left = self._delete(key, root.left)
		else:
			if root.left == None:
				right_child = root.right
				root = None
				return right_child
			elif root.right == None:
				left_child = root.left
				root = None
				return left_child
			else:
				inorder_successor = self.get_min_value(root.right)
				root.val = inorder_successor.val
				self.right = self._delete(inorder_successor)

		return root







	def print_tree(self):
		self.print_tree_inorder(self.root)

	def print_tree_inorder(self, current_node):
		if current_node == None:
			return
		self.print_tree_inorder(current_node.left)
		print current_node.key
		self.print_tree_inorder(current_node.right)


my_bst = BST()
my_bst.insert(1)
my_bst.insert(2)
my_bst.insert(-10)
my_bst.insert(-7)

my_bst.print_tree()
