#Finding the predicessor and successor of the current node in a Binary Search Tree

def find_pred_and_succ(root, node, successor, predicessor):
    if root == None:
        return None
    if node.val == root.val:
        if root.right:
            successor = find_min(root.right)
        if root.left:
            predicessor = find_max(root.left)
            return successor, predicessor
    if node.val > root.val:
        successor = root
        return find_pred_and_succ(root.left, node, successor, predicessor)
    else:
        predicessor = root
        return find_pred_and_succ(root.right, node, successor, predicessor)
