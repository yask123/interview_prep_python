def kth_form_last(node,k):
	if node == None:
		return 0

	temp = kth_form_last(node.next,k)
	if type(temp) is int:
		ans = 1 + kth_form_last(node.next,k)
		if ans == k :
			return node
	else:
		return temp 