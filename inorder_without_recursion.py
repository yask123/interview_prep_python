""" Constructed binary tree is
            1
          /   \
         2     3
       /  \
      4    5   """


class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
	stack = [root]
	current = root

	while len(stack) > 0:
		print ([each.data for each in stack])
		while current != None and current.left:
			stack.append(current.left)
			current = current.left
		popped_element = stack.pop()
		print (popped_element.data)
		current = popped_element.right
		stack.append(current)



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inorder(root)
