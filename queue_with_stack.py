class Stack_Queue:
    def __init__(self):
        self.first_stack  = []
        self.second_stack = []

    def push(self, val):
        self.first_stack.append(val)

    def pop(self):
        if len(self.second_stack) == 0:
            while len(self.first_stack) > 0:
                popped_element = self.first_stack.pop()
                self.second_stack.append(popped_element)
        popped_element = self.second_stack.pop()
        return popped_element


a = Stack_Queue()
a.push(1)
a.push(2)
a.push(3)
print (a.pop())
print (a.pop())
print (a.pop())
a.push(100)
print (a.pop())
