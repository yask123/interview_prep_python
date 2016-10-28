max_node_sum = 0
def find_special_node(root):
	global max_node_sum

	if root == None:
		return 0

	left_subtree_sum = find_special_node(root.left)
	right_subtree_sum = find_special_node(root.right)

	current_node_sum = root.val + left_subtree_sum + right_subtree_sum

	max_node_sum = max(current_node_sum, max_node_sum)

	return current_node_sum

def are_tree_same(roota, rootb):
	if roota == None and rootb == None:
		return True

	if roota == None and rootb != None or rootb == None and roota!= None:
		return False

	if roota.val == rootb.val:
		return (are_tree_same(roota.left, rootb.left) and are_tree_same(roota.right, rootb.right))
	else:
		return False

def count_nodes_greater_than_root(root, tree_root):

	if root == None:
		return 0

	left_count = count_nodes_greater_than_root(root.left, tree_root)
	right_count = count_nodes_greater_than_root(root.right, tree_root)

	if root.val > tree_root.val:
		return 1 + left_count + right_count
	else:
		return left_count + right_count


def get_height(root):
	if root == None:
		return 0

	left_subtree_height = get_height(root.left)
	right_subtree_height = get_height(root.right)

	return 1 + max(left_subtree_height, right_subtree_height)

def node_with_largest_data(root):
	if root == None:
		return None

	largest_data_left = node_with_largest_data(root.left)
	largest_data_right = node_with_largest_data(root.right)

	return max(max(largest_data_left, largest_data_right), root.val)
