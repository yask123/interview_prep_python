class Node:
	def __init__(self, data, next = None, prev = None):
		self.data = data
		self.next = next
		self.prev = prev

class DoubleLL:
	def __init__(self):
		self.head = None


class LRU:
	def __init__(self, max_capacity = 10):
		self.doubly_ll = DoubleLL()
		self.max_capacity = max_capacity
		self.current_capacity = 0
		self.node_map = {}

	def get(self, key):
		node = self.node_map[key]
		if node:
			self.remove_node(node)
			self.doubly_ll.append_left(node)
		return -1

	def set(self,value, key):
		if self.current_capacity >= self.max_capacity:
			self.doubly_ll.pop_right()
		if key in self.node_map:
			self.remove_node(self.node_map[key])

		new_node = Node((key,val))
		self.doubly_ll.append_left(new_node)
		self.node_map[key] = new_node
