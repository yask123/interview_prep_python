from binarytree import tree, bst, heap, pprint

my_tree = tree(height=2, balanced=True)

def get_predicessor(root, val, predicessor):
    if root == None:
        return None
    if val > root.value:
        return get_predicessor(root.left, val, predicessor)

    if root.value == val:
        if root.right != None:
            predicessor[0] = get_min_node(root.value)

        return predicessor[0]
    else:
        predicessor[0] = root.value
        return get_predicessor(root.right, val, predicessor)

def get_min_node(root):
    current = root
    while current.left:
        current = current.left
    return current.value

pprint (my_tree)
print get_predicessor(my_tree, 2, [1])
