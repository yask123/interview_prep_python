class heap:
	def __init__(self):
		self.heap_list = [0]
		self.current_index = 0

	def push(self, value):
		self.current_index += 1
		self.heap_list.append(value)
		self.perc_up(self.current_index)

	def pop(self):
		if self.current_index > 0:
			popped_value = self.heap_list[1]
			self.heap_list[1] = self.heap_list[self.current_index]
			self.current_index -= 1
			self.heap_list.pop()
			self.perc_down(1)
			return popped_value

	def perc_up(self, index):
		if index/2 >= 1:
			if self.heap_list[index] > self.heap_list[index/2]:
				self.heap_list[index], self.heap_list[index/2] = self.heap_list[index/2], self.heap_list[index]
				self.perc_up(index/2)

	def perc_down(self, index):
		if index*2 <= self.current_index:
			left_child = index*2
			right_child = index*2+1

			max_child_index  = self.max_of_children(index, left_child, right_child)

			if max_child_index:
				self.heap_list[index], self.heap_list[max_child_index] = self.heap_list[max_child_index], self.heap_list[index]
				self.perc_down(max_child_index)

	def max_of_children(self, parent_index, left_child, right_child):
		if right_child > self.current_index:
			if self.heap_list[left_child] > self.heap_list[parent_index]:
				return right_child
			else:
				return None

		if self.heap_list[left_child] > self.heap_list[parent_index]:
			return left_child
		elif self.heap_list[right_child] > self.heap_list[parent_index]:
			return right_child
		return None

	def peek(self):
		print self.heap_list[1]

my_heap = heap()
my_heap.push(1)
my_heap.push(2)
my_heap.push(-10)
my_heap.push(100)
my_heap.push(120)
my_heap.pop()
my_heap.pop()
my_heap.pop()

my_heap.peek()

