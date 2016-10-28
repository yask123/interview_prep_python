class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

a  = Node('a')
b  = Node('b')
c  = Node('c')

a.right = c
a.left = b


def tree_to_list(root, prev_node, head_node, last_item_visited):
    if root == None:
        return None

    tree_to_list(root.left, prev_node, head_node, last_item_visited)

    if prev_node[0]:
        prev_node[0].right = root
        root.left = prev_node[0]
    else:
        head_node.append(root)

    last_item_visited.pop()
    last_item_visited.append(root)

    prev_node.pop()
    prev_node.append(root)

    tree_to_list(root.right, prev_node, head_node, last_item_visited)

current = b

head_node = []
last_item_visited = [None]

tree_to_list(a, [None], head_node, last_item_visited)

current = head_node[0]
last_item_visited[0].right = head_node[0]
head_node[0].prev = last_item_visited[0]

current = head_node[0]
