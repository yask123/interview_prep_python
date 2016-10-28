class Node:
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next


def merge(first, second):
	prev = None

	while first or second:
		if first.data < second.data:
			new_node = Node(first.data)
			if prev:
				prev.next = new_node
			else:
				head = new_node
			first = first.next

		else:
			new_node = Node(second.data)
			if prev:
				prev.next = new_node
			else:
				head = new_node
			second = second.next

		prev = new_node

	if first:
		new_node.next= first
	elif second:
		new_node = second
	return head



