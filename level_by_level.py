from collections import deque

def level_by_level(root):
    current_level = deque([root])
    next_level = deque()
    result = []
    level = 0
    while len(current_level) > 0:
        popped_node = deque.pop()
        result[level].append(popped_node)

        if popped_node.right:
            next_level.appendleft(popped_node.right)
        if popped_node.left:
            next_level.appendleft(popped_node.left)
        if len(current_level) == 0:
            current_level.extendleft(next_level)
            level += 1
            result.append([])
    return result



def level_by_depth(root, current_level, result):
    if root == None:
        return
    if root.left:
        if len(result)-1 <= current_level+1:
            result.append([])
    level_by_depth(root.left, current_level+1, result)

    #Visit
    result[current_level].append(root)

    if root.right:
        if len(result)-1 <= current_level+1:
            result.append([])
    level_by_depth(root.right, current_level+1, result)
