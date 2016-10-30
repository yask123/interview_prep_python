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
