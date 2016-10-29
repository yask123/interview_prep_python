import deque


class LRU:
	def __init__(self, capacity=10):
		self.lru_deque = deque.Deque()
		self.MAX_CAPACITY = capacity
		self.current_capacity = 0
		self.node_map = {}

	def get(self, key):
		if key in self.node_map:
			return self.node_map[key]
		else:
			return -1

	def set(self, key, val):
		if key in self.node_map:
			current_node = self.node_map[key]
			current_node.prev.next = current_node.next
			current_node.val = val
			self.lru_deque.append_left(current_node)
		else:
			if self.current_capacity == self.MAX_CAPACITY:
				self.lru_deque.pop()

			current_node = self.lru_deque.append_left(key, val)
			self.node_map[key] = current_node
