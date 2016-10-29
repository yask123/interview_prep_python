'''reverse node in groups of k'''


def reverse_ll(head, k):
	if head == None:
		return

	prev = None
	current = head

	for _ in range(k):
		next_node = current.next

		current.next = prev

		prev = current
		current = next_node

	head.next = reverse_ll(current, k)

	return prev


def print_ll(current):
	while current:
		print current.data, '-->',
		current = current.next


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

a = reverse_ll(a, 2)

print_ll(a)
