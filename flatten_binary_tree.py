class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class TreeNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def _flatten_tree(root):
	if root != None:
		new_node = Node(root.data)
		if _flatten_tree.prev:
			_flatten_tree.prev.next = new_node
		else:
			_flatten_tree.head = new_node
		_flatten_tree.prev = new_node

		_flatten_tree(root.left)
		_flatten_tree(root.right)


def flatten_tree(root):
	_flatten_tree.prev = None
	_flatten_tree.head = None
	_flatten_tree(root)
	return _flatten_tree.head


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)

a.right = b
a.left = c

result = flatten_tree(a)

while result:
	print result.data
	result = result.next
