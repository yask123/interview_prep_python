# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def getSuccessor(self, A, B):
        current = A
        successor = None
        while True:
            if current.val == B:
                if current.right:
                    return self.get_min(A.right)
                else:
                    return successor
            elif current.val < B:
                current = current.right
            else:
                successor = current
                current = current.left

    def get_min(self, A):
        while A.left:
            A = A.left
        return A


a = TreeNode(2)
b = TreeNode(1)
c = TreeNode(3)

a.right = c
a.left = b

ans = Solution()
print ans.getSuccessor(a, 1).val
