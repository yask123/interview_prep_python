'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Concept:
1. get m-1th node (m_prev)
2. design a reverse function which takes mth node and reversed next (n-m+1) nodes.
3. This function also returns the new head, new tail, and next node (same as old head).
4. connect m-1th node to the new head, new_tail to the next node and  you are done.
'''


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


def reverse(A, m, n):
	if A.next == None:
		return A
	m = m - 1
	n = n - 1

	# get m - 1 element
	current = A
	m_prev = None
	for _ in range(m):
		m_prev = current
		current = current.next
	if m_prev == None:
		new_head, new_tail, next_node = simple_reverse(A, (n - m + 1))
	else:
		new_head, new_tail, next_node = simple_reverse(m_prev.next, (n - m + 1))
	if m_prev == None:
		A = new_head
	else:
		m_prev.next = new_head
	new_tail.next = next_node

	return A


def simple_reverse(current, k):
	old_head = current
	prev = None
	for _ in range(k):
		next_node = current.next
		current.next = prev
		prev = current
		current = next_node
	return prev, old_head, current
