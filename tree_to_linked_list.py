class TreeNode:
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None


def convert_to_ll(root):
    current = root
    while current.left:
        current = current.left
    tree_to_linkedlist(root)
    print_ll(current)

def tree_to_linkedlist(root):
    if root:
        left_child_node = tree_to_linkedlist(root.left)

        if left_child_node != None:
            root.left = left_child_node
            left_child_node.right = root

        right_child_node = tree_to_linkedlist(root.right)

        if right_child_node != None:
            root.right = right_child_node
            right_child_node.left = root

        return root

def print_ll(root):
    while root:
        print root.data,' ->',
        root = root.right

a = TreeNode(5)
b = TreeNode(7)
c = TreeNode(3)
e = TreeNode(2)

c.right = TreeNode(4)
c.left = e

a.right = b
a.left = c

convert_to_ll(a)
