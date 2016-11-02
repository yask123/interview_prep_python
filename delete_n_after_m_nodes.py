def delete_m_after_n(head, m, n):
	if head != None:
		current = head
		for i in range(n - 1):
			current = current.next

		for i in range(m):
			current.next = current.next.next
		delete_m_after_n(current.next, m, n)


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


head = Node(1)
current = head
for i in range(2, 11):
	new_node = Node(i)
	current.next = new_node
	current = current.next


def print_list(head):
	while head:
		print head.data,
		head = head.next


print_list(head)

delete_m_after_n(head, 3, 2)

print '\n'
print_list(head)
