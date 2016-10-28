class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def append(self, data):
        new_node = Node(data)

        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node

    def print_all(self):
        current = self.head

        while current:
            print (current.data, )
            current = current.next
    def get_last_node(self):
        current = self.head
        while current.next:
            current = current.next
        return current

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)

ll.print_all()
