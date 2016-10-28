'''iterative inorder traversal, O(n) time & O(n) space '''
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

def inorder_iter(root):

    stack = [root]
    current = root

    while len(stack) > 0:
        if current:
            while current.left:
                stack.append(current.left)
                current = current.left
        popped_node = stack.pop()
        current = None
        if popped_node:
            print popped_node.value
            current = popped_node.right
            stack.append(current)

# Driver program to test above function

""" Constructed binary tree is
            1
          /   \
         2     3
       /  \
      4    5   """

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inorder_iter(root)
