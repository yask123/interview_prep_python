class Stack_Min:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self,val):
        if len(self.min_stack) == 0 or self.min_stack[-1] > val:
            self.min_stack.append(val)
        self.stack.append(val)

    def pop(self):
        if len(self.stack):
            popped_element = self.stack.pop()
            if popped_element == self.min_stack[-1]:
                self.min_stack.pop()

    def get_min(self):
        print self.min_stack[-1]
