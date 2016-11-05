# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param A : root node of tree
	# @param val1 : integer
	# @param val2 : integer
	# @return an integera
	left_exist = False
	right_exist = False
	def lca(self, A, val1, val2):
		result = self._lca(A, val1, val2)
		if Solution.left_exist and Solution.right_exist:
			return result
		return -1

	def _lca(self, A, val1, val2):
		if A == None:
			return -1

		if A.val == val1:
			Solution.left_exist = True
			return A.val
		if A.val == val2:
			Solution.right_exist = True
			return A.val

		in_left_subtree = self._lca(A.left, val1, val2)

		in_right_subtree = self._lca(A.right, val1, val2)

		if in_left_subtree != -1 and in_right_subtree != -1:
			return A.val

		if in_left_subtree != -1:
			return in_left_subtree

		if in_right_subtree != -1:
			return in_right_subtree

		return -1
