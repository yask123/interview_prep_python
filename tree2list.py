def tree_to_ll(root):
    if root == None:
        return

    tree_to_ll(root.left)

    if tree_to_ll.prev == None:
        tree_to_ll.head = root
    else:
        tree_to_ll.prev.right = root

    tree_to_ll.prev = root

    tree_to_ll(root.right)


def convert_tree_to_linked_list(root):
    tree_to_ll.prev = None
    tree_to_ll.head = None

    tree_to_ll(root)

    print_linked_list(tree_to_ll.head)


def print_linked_list(root):
    current = root
    while current:
        print current.val, '-->',
        current = current.right


class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.val = data


a = Node(5)
b = Node(1)
c = Node(8)

a.left = b

a.right = c

convert_tree_to_linked_list(a)
