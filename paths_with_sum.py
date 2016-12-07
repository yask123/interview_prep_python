'''
Paths with Sum: You are given a binary tree in which each node contains an integer value (which might be positive or negative).
Design an algorithm to count the number of paths that sum to a given value.
The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
'''


def path_with_sum(root, target):
    if root == None:
        return
    left_count = get_sum(root.left, target - root.val)
    right_count = get_sum(root.right, target - root.val)

    path_with_sum.count = left_count + right_count

    path_with_sum(root.left)
    path_with_sum(root.right)


path_with_sum.count = 0


def get_sum(root, target):
    if target == 0:
        return 1

    if root == None or target < 0:
        return 0

    a = get_sum(root.left, target - root.val)
    b = get_sum(root.right, target - root.val)

    return a + b
