'''
Given a binary tree, flatten it to a linked list in-place.

Example :
Given


         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:

   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
Note that the left child of all nodes should be NULL.



		7
	2		 1
0      1 	     3

'''


def flatten(root):
    if root == None:
        return
    flatten(root.right)
    flatten(root.left)

    if flatten.prev:
        root.right = flatten.prev
    flatten.prev = root


flatten.prev = None

import sample_tree

root = sample_tree.a

flatten(root)

while root.right:
    print root.val
    root = root.right
