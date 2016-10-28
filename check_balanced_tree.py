def check_balanced_tree(root):

    if root == None:
        return 0

    left_sub_tree = check_balanced_tree(root.left)
    right_sub_tree = check_balanced_tree(root.right)

    if isinstance(left_sub_tree, int) and isinstance(right_sub_tree, int):

        if abs(left_sub_tree - right_sub_tree) > 1:
            return False

        return max(left_sub_tree, right_sub_tree) +1
    else:
        return False
