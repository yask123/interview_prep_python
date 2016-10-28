def inorderPredicessor(root, k , ans = -inf):
	if root == None:
		return ans
	if root.data <= k and root.data > ans:
		ans = root.data

	if k < root.data:
		inorderPredicessor(root.left,k,ans)
	else:
		inorderPredicessor(root.right,k,ans)

