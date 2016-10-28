class My_LRU:
	def __init__(self, capacity):
		self.queue = []
		self.max_capacity = capacity
		self.current_capacity =0 

	def insert(self, key, val):
		if self.current_capacity < max_capacity:
			self.current_capacity += 1
		else:
			self.remove_least_recent()

		self.queue.append((key,val))

	def get(self, key):
		for i in range(len(self.queue)):
			if self.queue[i][0] == key:
				removed_item = self.queue.pop(i)
				insert_

				return self.queue[i][1]
