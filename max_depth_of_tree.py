def max_depth(root):
    if root == None:
        return 0

    left_subtree_depth = max_depth(root.left)
    right_subtree_depth = max_depth(root.right)

    return max(left_subtree_depth, right_subtree_depth) +1
