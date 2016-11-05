class Node:
	def __init__(self, start_time, end_time):
		self.key = start_time
		self.end_time = end_time
		self.max_end_time = end_time
		self.left = None
		self.right = None


class IntervalTree:
	def __init__(self):
		self.root = Node()

	def insert_interval(self, interval):
		self._insert_interval(self.root, interval[0], interval[1])

	def _insert_interval(self, root, start_time, end_time):
		if root == None:
			return
		if root.max_end_time < end_time:
			root.max_end_time = end_time

		if start_time > root.key:
			if root.right == None:
				root.right = Node(start_time, end_time)
			else:
				self._insert_interval(root.right, start_time, end_time)
		else:
			if root.left == None:
				root.left = Node(start_time, end_time)
			else:
				self._insert_interval(root.left, start_time, end_time)

	def find_merged_interval(self, interval):
		start_time = interval[0]
		end_time = interval[1]
