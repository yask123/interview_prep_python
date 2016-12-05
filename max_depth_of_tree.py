'''

Given a binary tree, find its maximum depth.

The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node.

 NOTE : The path has to end on a leaf node.
Example :

         1
        /
       2
max depth = 2.

'''


def max_depth(root):
    if root == None:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))


import sample_tree

print max_depth(sample_tree.a)
