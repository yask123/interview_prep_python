
def get_successor(root, node):
    kth_node = search_node(root, node)

    if kth_node.right:
        return get_min_node(kth_node.right)
    else:
        ancestor = node.parent
        child = node
        while (ancestor != None and child == ancestor.right):
            child = ancestor
            ancestor = child.parent
        return ancestor
