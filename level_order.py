# coding=utf-8


'''
Given a binary tree, return the level order traversal of its nodes’ values. (ie, from left to right, level by level).
'''
from collections import deque

import sample_tree


def level_order(root):
    result = []

    queue = deque()
    queue.append((root, 0))

    while len(queue):
        popped_node, current_level = queue.popleft()
        if current_level + 1 > len(result):
            result.append([])
        result[current_level].append(popped_node.val)

        if popped_node.left:
            queue.append((popped_node.left, current_level + 1))
        if popped_node.right:
            queue.append((popped_node.right, current_level + 1))

    return result


print level_order(sample_tree.a)
