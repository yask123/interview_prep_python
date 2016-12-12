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

