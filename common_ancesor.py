'''
First Common Ancestor: Design an algorithm and write code to  nd the  rst common ancestor of two nodes in a binary tree.
Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.
'''


def fca(root, a, b):

    if root == None:
        return False

    if root.val == a or root.val == b:
        return root.val

    in_left = fca(root.left, a, b)
    in_right = fca(root.right, a, b)

    if in_left and in_right:
        return root.val

    if in_right:
        return in_right

    if in_left:
        return in_left

    return False


def first_common_ancesor(root, a, b):
    if is_present(root, a) and is_present(root, b):
        return fca(root, a, b)
    return False


def is_present(root, a):
    if root == None:
        return False

    if root.val == a:
        return True

    in_left = is_present(root.left)
    in_right = is_present(root.right)

    return in_left or in_right
