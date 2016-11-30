import sample_tree


def path(root, sum):
	if sum < 0 or root == None:
		return False

	if root.left == None and root.right == None and sum - root.val == 0:
		return True

	if path(root.left, sum - root.val) or path(root.right, sum - root.val):
		return True
	return False


'''
		7
	2		 1
0      1 	     3
'''

print path(sample_tree.a, 11)
