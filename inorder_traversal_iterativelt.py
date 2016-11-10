'''iterative inorder traversal, O(n) time & O(n) space '''
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

def inorder_iter(root):
    stack = [root]

    while len(stack) > 0:
        popped_node = stack.pop()
        print popped_node.value
        if popped_node.right:
            stack.append(popped_node.right)
        if popped_node.left:
            stack.append(popped_node.left)


def pre_order(root):
    stack = [root]
    current = root
    while len(stack) > 0:

        while current.left:
            stack.append(current.left)
            current = current.left
        popped_node = stack.pop()

        print popped_node.value

        if popped_node.right:
            current = popped_node.right
            stack.append(popped_node.right)


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

pre_order(root)
