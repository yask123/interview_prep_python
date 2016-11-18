'''
serialization and deserizalization of a Binary tree.
The data is stored as a list [root val, left child val, right child val]
Similar to the way Heap is constructed using list
i -> root
2*i + 1-> left child
2*i + 2-> right child

'''


def serialize(root, result):
	if root == None:
		return
	if root.left:
		result.append(root.left.val)
	else:
		result.append(None)
	if root.right:
		result.append(root.right.val)
	else:
		result.append(None)

	serialize(root.left, result)
	serialize(root.right, result)


def deserialize(result, index):
	if index < len(result):
		if result[index] == None:
			return None
		root = TreeNode(result[index])
		root.left = deserialize(result, 2 * index + 1)
		root.right = deserialize(result, 2 * index + 2)
		return root


def inorder(root):
	if root:
		inorder(root.left)
		print root.val
		inorder(root.right)


class TreeNode:
	def __init__(self, data):
		self.val = data
		self.left = None
		self.right = None


a = TreeNode(2)
b = TreeNode(1)
c = TreeNode(3)

a.right = c
a.left = b

d = TreeNode(5)
c.right = d
result = [a.val]

serialize(a, result)
print result

new_root = deserialize(result, 0)

inorder(new_root)
