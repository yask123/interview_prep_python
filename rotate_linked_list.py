# Rotate linked list https://www.interviewbit.com/problems/rotate-list/
'''
Concept: New head will be N - K th element. Set prev of (n-k)th to None and set the tail of linked list to prev head
O(n)
'''


def rotate(self, A, B):
	total_length = self.get_length(A)
	prev_head = A
	B = B % total_length
	prev = None
	for _ in range(total_length - B):
		prev = A
		A = A.next
	if prev != None and A != None:
		prev.next = None
		head = A

		while A.next != None:
			A = A.next
		A.next = prev_head

		return head
	else:
		return prev_head
