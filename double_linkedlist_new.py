
class Node:
    def __init__(self,data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def append(self,data):
        new_node = Node(data)
        if self.front:
            self.front.next = new_node
            new_node.prev = self.front
            self.front = new_node
        else:
            self.front = new_node
            self.rear = new_node

    def append_left(self,data):
        new_node = Node(data)
        if self.rear:
            new_node.next = self.rear
            self.rear.prev = new_node
            self.rear = new_node

        else:
            self.front = new_node
            self.rear = new_node

    def pop_left(self):
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.next
            self.rear.prev = None

    def pop(self):
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.prev
            self.front.next = None

    def print_all(self):
        current = self.rear

        while current:
            print current.data,
            current = current.next

a.print_all()
