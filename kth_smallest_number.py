def kth_smallest(root, k):
	_kth_smallest.count = k
	_kth_smallest.result = None
	_kth_smallest(root)
	return _kth_smallest.result


def _kth_smallest(root):
	if root == None:
		return

	_kth_smallest(root.left)
	_kth_smallest.count -= 1
	if _kth_smallest.count == 0:
		_kth_smallest.result = root.data
	_kth_smallest(root.right)


class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


a = Node(2)
b = Node(3)
c = Node(4)

b.right = c
b.left = a

print kth_smallest(b, 3)
