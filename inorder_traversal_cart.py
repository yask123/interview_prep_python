'''
Given an inorder traversal of a cartesian tree, construct the tree.

 Cartesian tree : is a heap ordered binary tree, where the root is greater than all the elements in the subtree.
 Note: You may assume that duplicates do not exist in the tree.
Example :

Input : [1 2 3]

Return :
          3
         /
        2
       /
      1
'''


class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def build_tree(A):
    if len(A):
        max_index = A.index(max(A))
        root_node = TreeNode(A[max_index])

        root_node.left = build_tree(A[:max_index])
        root_node.right = build_tree(A[max_index + 1:])

        return root_node


def pre_order(root):
    if root:
        print root.val,
        pre_order(root.left)
        pre_order(root.right)


def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print root.val,


root = build_tree([2, 1, 3])

pre_order(root)
print ''
post_order(root)
