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

    def _insert_helper(self, root, key, val):

        if key > root.val:
            if root.right:
                self._insert_helper(root.right, key, val)
			else:
                root.right = Node(key, val)
		else:
            if root.left:
                self._insert_helper(root.left, key, val)
			else:
                root.left = Node(key, val)



	def delete(self, key):
		self._delete(key, self.root)

    def _delete(self, root, key):
        if key == root.val:

			if root.left == None:
                temp = root.right
				root = None
                return temp

            if root.right == None:
                temp = root.left
				root = None
                return temp

            inord_successor = self.get_min(root.right)
            root.val = inord_successor.val
            root.key = inord_successor.key
            self._delete(root, inord_successor.key)

        elif key > root.val:
            root.right = self._delete(root.right, key)
        else:
            root.left = self._delete(root.left, key)

    def get_min(self, root, key):
        while root.left:
            root = root.left
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
