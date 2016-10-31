class LinkedList:
	def __init__(self, head=None):
		self.head = head

	def reverse(self, current_node, prev=None):
		if current_node == None:
			self.head = prev
			return

		next_node = current_node.next
		current_node.next = prev
		self.reverse(next_node, current_node)

	def print_ll(self):
		current = self.head
		while current:
			print current.data,
			current = current.next


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c

ll = LinkedList(a)
ll.print_ll()
print ''
ll.reverse(a)
ll.print_ll()
