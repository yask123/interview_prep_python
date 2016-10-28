def get_common_ancesor(root, a, b):
    if root == None:
        return None
    
    if root == a or root == b:
        return root
    
    is_in_left_subtree = get_common_ancesor(root.left, a, b)
    is_in_right_subtree = get_common_ancesor(root.right, a, b)

    if is_in_left_subtree and is_in_right_subtree:
        return root 
    
    if is_in_left_subtree:
        return is_in_left_subtree
    elif is_in_right_subtree:
        return is_in_right_subtree
    
    return None
a = 1
b = 1
c = a*b