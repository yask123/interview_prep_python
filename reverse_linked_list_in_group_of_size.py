'''reverse node in groups of k'''

'''
Example:
Inputs:  1->2->3->4->5->6->7->8->NULL and k = 3
Output:  3->2->1->6->5->4->8->7->NULL.
'''


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


def reverse_in_group(head, k):

	if head == None:
		return

	prev = None
	current = head
	for _ in range(k):
		next_node = current.next
		current.next = prev
		prev = current
		current = next_node

	head.next = reverse_in_group(current, k)
	return prev


m_head = Node(0)
current = m_head
for i in range(1, 10):
	new_node = Node(i)
	current.next = new_node
	current = new_node


def print_nodes(head):
	while head:
		print head.data, '-->',
		head = head.next


m_head = reverse_in_group(m_head, 2)
print_nodes(m_head)
