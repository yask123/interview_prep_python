"""
Input:
1 - 2 - 3 - 4
    |
    7 -  8 - 10 - 12
    |    |    |
    9    16   11
    |    |
    14   17 - 18 - 19 - 20
    |                    |
    15 - 23             21
         |
         24

Output:
Linked List to be flattened to
1 - 2 - 7 - 9 - 14 - 15 - 23 - 24 - 8
 - 16 - 17 - 18 - 19 - 20 - 21 - 10 -
11 - 12 - 3 - 4
"""


def flatted_linked_list(head):
    if head == None:
        return
    flatted_linked_list.last_node = head
    next_node = head.next

    if head.down:
        head.next = flatted_linked_list(head.down)

    if next_node:
        flatted_linked_list.last_node.next = flatted_linked_list(next_node)

    return head


def print_list(head):
    while head:
        print head.data, '-->',
        head = head.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.down = None


a = Node(1)
a.next = Node(2)
a.next.down = Node(7)
a.next.down.next = Node(8)
a.next.down.down = Node(9)

a.next.next = Node(3)

new_head = flatted_linked_list(a)
print_list(new_head)
