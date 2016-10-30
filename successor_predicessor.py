def successor_and_precicessor(root, key, succ, pred):
	if root == None:
		return None, None

	if root.key == key:
		if root.left != None:
			pred = get_min(root.left)
		if root.right != None:
			succ = get_min(root.right)

		return pred, succ.key

	if key < root.key:
		return successor_and_precicessor(root.left, key, root.key, pred)
	else:
		return successor_and_precicessor(root.right, key, succ, root.key)


def get_min(root):
	while root.left:
		root = root.left
	return root


# A BST node
class Node:
	# Constructor to create a new node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


def insert(node, key):
	if node is None:
		return Node(key)

	if key < node.key:
		node.left = insert(node.left, key)

	else:
		node.right = insert(node.right, key)

	return node


root = None
root = insert(root, 50)
insert(root, 30);
insert(root, 40);
insert(root, 70);
insert(root, 80);

print successor_and_precicessor(root, 70, None, None)
