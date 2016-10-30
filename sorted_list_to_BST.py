# https://www.interviewbit.com/problems/sorted-array-to-balanced-bst/
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	# @param A : tuple of integers
	# @return the root node in the tree
	def sortedArrayToBST(self, A):
		return self.array_to_bst(A, 0, len(A) - 1)

	def array_to_bst(self, arr, start_index, end_index):
		if start_index <= end_index:
			mid = (end_index + start_index) / 2
			tree_node = TreeNode(arr[mid])
			tree_node.left = self.array_to_bst(arr, start_index, mid - 1)
			tree_node.right = self.array_to_bst(arr, mid + 1, end_index)

			return tree_node


a = Solution()
A = [1, 2, 3]
a.sortedArrayToBST(A)
