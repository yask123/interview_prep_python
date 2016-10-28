def is_balanced(root):
    if root == None:
        return 0,True

    left_sub_tree_height, left_balanced = is_balanced(root.left)
    right_sub_tree_height, right_balanced = is_balanced(root.right)

    current_height = max(left_sub_tree_height, right_sub_tree_height) + 1

    if abs(left_sub_tree_height - right_sub_tree_height) > 1:
        return current_height, False

    return (left_balanced and right_balanced), current_height
