'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5 and x = 3,
return
1

'''
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

	def partition(self,root,x):
		original_last = self.get_last(self,root)
		current = root
		current_last = original_last
		prev = None

		while current != original_last:
			# Delete the current node
			current >= x:

			current = current.next
		if current >= x:

	def delete_and_append_to_last(self,val):

			if prev:
				prev.next = current.next
			else:
				self.head = current.next
			# Add this node to the last
			current_last.next = current
			current.next = None
			current_last = current